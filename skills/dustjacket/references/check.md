# Check mode (drift gate)

Read-only. Reports where the README no longer matches reality and exits non-zero when findings meet a
threshold. **check never writes** — it only reports.

Two layers, cheapest first. Run the deterministic script; only if it passes, spend tokens on the
model-assisted layer.

## Layer 1 — deterministic (the script)

`scripts/dustjacket_check.py` (stdlib, no deps) covers what a regex/filesystem check settles for sure:

```
python scripts/dustjacket_check.py README.md --repo-root .
python scripts/dustjacket_check.py README.md --check-urls   # also HEAD external URLs (network)
python scripts/dustjacket_check.py README.md --json         # machine-readable
```

Checks: missing one-line description (warning) and License (error); broken in-page anchors (error);
links to local files that don't exist (error); images missing or missing alt text (error/warning);
README title/license vs. the package manifest (warning); external URL liveness (opt-in). Exit is
non-zero once any finding reaches `--threshold` (default `error`).

## Layer 2 — model-assisted (gated behind layer 1 passing)

What only reading the code can settle. Run these as the skill, citing the README claim **and** the
contradicting code location for each finding:

- **Removed CLI flags/commands** — every flag the README documents still exists in `--help` or the arg
  parser.
- **Gone API** — every public symbol the README shows is still exported.
- **Install mismatch** — the documented install matches the actual package name / entry point.
- **Stale examples** — code samples still run (`references/verify-code.md`); flag any that don't.

Report format: severity-ranked, each finding naming the README line and the code file/symbol that
contradicts it. Like layer 1, **report only — never edit** in check mode (that's prettify's job).

## Output contract

- Print the deterministic report, then the model-assisted findings, merged and severity-ranked.
- Exit non-zero if anything reaches the threshold (CI gate).
- Never modify any file. If the user wants fixes, they run prettify.
