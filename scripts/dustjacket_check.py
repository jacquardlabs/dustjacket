#!/usr/bin/env python3
"""dustjacket check — deterministic README drift checks.

Read-only. Reports findings ranked by severity and exits non-zero when any finding
meets or exceeds the threshold (default: error). Stdlib only.

Usage:
    python scripts/dustjacket_check.py [README] [--repo-root DIR]
        [--threshold error|warning] [--check-urls] [--json]

Model-assisted checks (removed CLI flags, gone API) layer on top — see
skills/dustjacket/references/check.md.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
import urllib.error
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path

SEVERITIES = ("info", "warning", "error")


@dataclass(frozen=True)
class Finding:
    severity: str
    check: str
    message: str
    line: int = 0


# --- functional core: pure helpers over README text ----------------------------


def slugify_heading(text: str) -> str:
    """GitHub-style heading anchor slug."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s+", "-", s)


def headings(md: str) -> list[str]:
    return [
        slugify_heading(m.group(2))
        for m in re.finditer(r"^(#{1,6})\s+(.*?)\s*#*$", md, re.MULTILINE)
    ]


def links(md: str) -> list[tuple[str, str, int]]:
    """(text, target, line) for every [text](target), skipping images."""
    out: list[tuple[str, str, int]] = []
    for m in re.finditer(r"(?<!\!)\[([^\]]*)\]\(([^)]+)\)", md):
        line = md.count("\n", 0, m.start()) + 1
        out.append((m.group(1), m.group(2).strip(), line))
    return out


def images(md: str) -> list[tuple[str, str, int]]:
    """(alt, target, line) for every ![alt](target)."""
    out: list[tuple[str, str, int]] = []
    for m in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", md):
        line = md.count("\n", 0, m.start()) + 1
        out.append((m.group(1), m.group(2).strip(), line))
    return out


def first_paragraph(md: str) -> str:
    """The first non-heading, non-blank, non-badge line — the one-line description."""
    for raw in md.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("![") or line.startswith(">"):
            continue
        if re.fullmatch(r"[\[\]!()\s|/:.\w-]*", line) and "http" in line and "](" in line:
            continue  # a badge-only line
        return line
    return ""


def has_section(md: str, name: str) -> bool:
    return any(name.lower() in h for h in headings(md))


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:"))


def is_anchor(target: str) -> bool:
    return target.startswith("#")


# --- checks: each returns a list of Findings -----------------------------------


def check_required_sections(md: str) -> list[Finding]:
    out: list[Finding] = []
    if not first_paragraph(md):
        out.append(Finding("warning", "description", "No one-line description under the title."))
    if not has_section(md, "license"):
        out.append(Finding("error", "license", "No License section found."))
    return out


def check_anchors(md: str) -> list[Finding]:
    valid = set(headings(md))
    out: list[Finding] = []
    for _text, target, line in links(md):
        if is_anchor(target) and target[1:] not in valid:
            out.append(Finding("error", "anchor", f"Broken anchor link: {target}", line))
    return out


def check_local_paths(md: str, root: Path) -> list[Finding]:
    out: list[Finding] = []
    for _text, target, line in links(md):
        if is_external(target) or is_anchor(target):
            continue
        path = target.split("#", 1)[0]
        if path and not (root / path).exists():
            out.append(Finding("error", "link-path", f"Linked file not found: {path}", line))
    return out


def check_images(md: str, root: Path) -> list[Finding]:
    out: list[Finding] = []
    for alt, target, line in images(md):
        if not alt.strip():
            out.append(Finding("warning", "alt-text", f"Image missing alt text: {target}", line))
        if not is_external(target):
            path = target.split("#", 1)[0]
            if path and not (root / path).exists():
                out.append(Finding("error", "image-path", f"Image not found: {path}", line))
    return out


def check_metadata(md: str, root: Path) -> list[Finding]:
    """README title/license vs the package manifest."""
    out: list[Finding] = []
    name, license_ = _manifest_meta(root)
    if name:
        title = next((h for h in headings(md)), "")
        if title and name.lower() not in title and title not in name.lower():
            out.append(
                Finding("warning", "metadata", f"README title '{title}' != package name '{name}'.")
            )
    if license_ and has_section(md, "license"):
        if license_.lower() not in md.lower():
            out.append(
                Finding("warning", "metadata", f"Manifest license '{license_}' not mentioned in README.")
            )
    return out


def _manifest_meta(root: Path) -> tuple[str, str]:
    """(name, license) from pyproject.toml or package.json, best-effort."""
    py = root / "pyproject.toml"
    if py.exists():
        data = tomllib.loads(py.read_text())
        proj = data.get("project", {})
        lic = proj.get("license")
        lic = lic.get("text", "") if isinstance(lic, dict) else (lic or "")
        return proj.get("name", ""), lic
    pkg = root / "package.json"
    if pkg.exists():
        data = json.loads(pkg.read_text())
        return data.get("name", ""), data.get("license", "")
    return "", ""


def check_urls(md: str, timeout: float = 5.0) -> list[Finding]:
    """Opt-in: HEAD each external URL. Network — off by default."""
    out: list[Finding] = []
    seen: set[str] = set()
    for _text, target, line in links(md) + [(a, t, l) for a, t, l in images(md)]:
        if not target.startswith(("http://", "https://")) or target in seen:
            continue
        seen.add(target)
        try:
            req = urllib.request.Request(target, method="HEAD")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                if resp.status >= 400:
                    out.append(Finding("warning", "url", f"{resp.status} for {target}", line))
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError, OSError) as e:
            out.append(Finding("warning", "url", f"Unreachable: {target} ({e})", line))
    return out


# --- imperative shell ----------------------------------------------------------


def run_checks(readme: Path, root: Path, with_urls: bool) -> list[Finding]:
    md = readme.read_text()
    findings: list[Finding] = []
    findings += check_required_sections(md)
    findings += check_anchors(md)
    findings += check_local_paths(md, root)
    findings += check_images(md, root)
    findings += check_metadata(md, root)
    if with_urls:
        findings += check_urls(md)
    order = {s: i for i, s in enumerate(reversed(SEVERITIES))}
    return sorted(findings, key=lambda f: (order[f.severity], f.line))


def max_severity(findings: list[Finding]) -> int:
    return max((SEVERITIES.index(f.severity) for f in findings), default=-1)


def render(findings: list[Finding]) -> str:
    if not findings:
        return "dustjacket check: no drift found."
    lines = [f"dustjacket check: {len(findings)} finding(s)\n"]
    for f in findings:
        loc = f":{f.line}" if f.line else ""
        lines.append(f"  [{f.severity:<7}] {f.check}{loc}: {f.message}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="dustjacket README drift check")
    ap.add_argument("readme", nargs="?", default="README.md")
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--threshold", choices=("warning", "error"), default="error")
    ap.add_argument("--check-urls", action="store_true", help="HEAD external URLs (network)")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args(argv)

    readme = Path(args.readme)
    if not readme.exists():
        print(f"dustjacket check: README not found: {readme}", file=sys.stderr)
        return 2

    findings = run_checks(readme, Path(args.repo_root), args.check_urls)
    if args.as_json:
        print(json.dumps([asdict(f) for f in findings], indent=2))
    else:
        print(render(findings))

    return 1 if max_severity(findings) >= SEVERITIES.index(args.threshold) else 0


if __name__ == "__main__":
    raise SystemExit(main())
