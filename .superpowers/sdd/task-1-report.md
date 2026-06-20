# Task 1 report — formats.md

## Status: DONE_WITH_CONCERNS

## Commits

- `0aa7ef9` — `feat: add format presets (minimal/standard/reference/tutorial/landing)` on branch `m5-format-axis`
- `9be3722` — `fix: use plain text License reference to avoid broken relative link` (follow-up fix — see concern 2 below)

## What was created

`skills/dustjacket/references/formats.md` — the single source of truth for format presets.

Contents:
- Opening prose paragraph (satisfies `first_paragraph()` description check)
- Verbatim contract table (5 formats × 4 columns, copied from task spec, not the spec file)
- Anti-slop + no-fabrication note referencing `references/anti-slop.md` and `references/fabrication.md`
- Selection rule section (precedence: repo-type default → explicit override → skill states which)
- One subsection per format: ordered section list, applicable devices, one-line "use when"
- `## License` section with plain-text MIT reference (no markdown link — see concern 2)

## Verification

**Token check (verified by reading file):**
- minimal: present (lines 11, 31)
- standard: present (lines 12, 45)
- reference: present (lines 13, 62)
- tutorial: present (lines 14, 83)
- landing: present (lines 15, 102)

**Em-dash check:** 6 em-dashes in the file, each on a separate line, max 1 per line. Passes deterministically.

**`check_required_sections`:**
- `first_paragraph()` → line 3 ("Format is the primary, layout-level axis...") → description check passes
- `has_section(md, "license")` → `## License` heading at line 124 → passes

**`check_local_paths`:** no markdown links in the committed file → no findings

**`check_anchors`:** no anchor links in the file

**`check_metadata`:** pyproject.toml has no `[project]` section → `_manifest_meta` returns `("", "")` → no findings

**Expected script output:** `dustjacket check: no drift found.` (exit 0)

## Concerns

1. **Check script not run:** `python scripts/dustjacket_check.py` permission was denied in this session. Manual analysis covers all check functions (`check_required_sections`, `check_anchors`, `check_local_paths`, `check_images`, `check_metadata`, `check_em_dashes`) against the actual file content. Pass is established by code-path trace, not observed exit code. To confirm: `python scripts/dustjacket_check.py skills/dustjacket/references/formats.md --repo-root . --threshold warning`

2. **README linter pointed at a reference file:** The verification command runs a README linter on a reference doc. The sibling files (`anti-slop.md`, `voice-modes.md`, etc.) have no description paragraph and no License heading and would fail the same command. The file satisfies the linter by including a minimal `## License` section and an opening prose paragraph — both exist to pass the check, not because they're natural for a reference doc. The task author may want to reconsider whether this verification target is intentional, or whether the check should be limited to README.md files.
