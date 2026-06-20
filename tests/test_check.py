"""Tests for the dustjacket README drift checker."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import dustjacket_check as dc  # noqa: E402


# --- pure helpers --------------------------------------------------------------


def test_slugify_heading():
    assert dc.slugify_heading("Hello, World!") == "hello-world"
    assert dc.slugify_heading("Quick Start") == "quick-start"
    assert dc.slugify_heading("API & SDK") == "api-sdk"  # runs of whitespace collapse


def test_headings_and_links_and_images():
    md = "# Title\n\n## Install\n\n[docs](#install) [ext](https://x.io) [file](./a.md)\n\n![alt](img.png)"
    assert dc.headings(md) == ["title", "install"]
    targets = [t for _, t, _ in dc.links(md)]
    assert targets == ["#install", "https://x.io", "./a.md"]  # image excluded from links()
    assert dc.images(md) == [("alt", "img.png", 7)]


def test_first_paragraph_skips_badges_and_headings():
    md = "# Title\n\n[![CI](https://img.shields.io/x.svg)](https://ci)\n\nThe real one-liner.\n"
    assert dc.first_paragraph(md) == "The real one-liner."


def test_first_paragraph_skips_badge_with_query_params():
    # shields badges carry ?query=params — the old char-class regex let these through
    md = "# T\n\n[![v](https://img.shields.io/crates/v/bat.svg?colorB=319e8c)](https://x)\n\nReal desc.\n"
    assert dc.first_paragraph(md) == "Real desc."


# --- checks --------------------------------------------------------------------


def test_missing_license_is_error():
    findings = dc.check_required_sections("# T\n\nA tool.\n\n## Usage\n")
    assert any(f.check == "license" and f.severity == "error" for f in findings)


def test_present_license_passes():
    findings = dc.check_required_sections("# T\n\nA tool.\n\n## License\n\nMIT\n")
    assert not any(f.check == "license" for f in findings)


def test_broken_anchor_is_error():
    md = "# Title\n\n[jump](#nope)\n\n## Real\n"
    findings = dc.check_anchors(md)
    assert len(findings) == 1 and findings[0].severity == "error"


def test_valid_anchor_passes():
    md = "# Title\n\n[jump](#real)\n\n## Real\n"
    assert dc.check_anchors(md) == []


def test_missing_local_file_is_error(tmp_path: Path):
    (tmp_path / "exists.md").write_text("x")
    md = "[here](exists.md) [gone](missing.md)"
    findings = dc.check_local_paths(md, tmp_path)
    assert len(findings) == 1 and "missing.md" in findings[0].message


def test_image_missing_alt_and_missing_file(tmp_path: Path):
    md = "![](logo.png)"
    findings = dc.check_images(md, tmp_path)
    checks = {f.check for f in findings}
    assert "alt-text" in checks and "image-path" in checks


def test_metadata_mismatch_warns(tmp_path: Path):
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nname = "realname"\nlicense = { text = "MIT" }\n'
    )
    md = "# wrongname\n\nA tool.\n\n## License\n\nApache\n"
    findings = dc.check_metadata(md, tmp_path)
    assert any("name" in f.message for f in findings)
    assert any("license" in f.message.lower() for f in findings)


def test_metadata_match_passes(tmp_path: Path):
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nname = "tool"\nlicense = { text = "MIT" }\n'
    )
    md = "# tool\n\nA tool.\n\n## License\n\nMIT\n"
    assert dc.check_metadata(md, tmp_path) == []


# --- shell ---------------------------------------------------------------------


def test_run_and_exit_code(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text("# tool\n\nA tool.\n\n[bad](#nowhere)\n")  # no license + broken anchor
    findings = dc.run_checks(readme, tmp_path, with_urls=False)
    assert dc.max_severity(findings) == dc.SEVERITIES.index("error")
    # threshold error -> exit 1
    assert dc.main([str(readme), "--repo-root", str(tmp_path)]) == 1


def test_clean_readme_exits_zero(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text("# tool\n\nA tool that does one thing.\n\n## License\n\nMIT\n")
    assert dc.main([str(readme), "--repo-root", str(tmp_path)]) == 0


def test_run_checks_orders_errors_first(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text("# tool\n\n![](x.png)\n\n[bad](#no)\n")  # warning (alt) + error (anchor), no license
    findings = dc.run_checks(readme, tmp_path, with_urls=False)
    assert findings[0].severity == "error"  # errors sort ahead of warnings
