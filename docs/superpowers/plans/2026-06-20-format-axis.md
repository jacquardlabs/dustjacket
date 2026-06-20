# Format Axis Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a selectable, layout-level **Format** axis (minimal, standard, reference, tutorial, landing) to the dustjacket skill, separate from tone-Voice, so users get fundamentally different README layouts.

**Architecture:** dustjacket is a prompt/markdown Claude Code skill (`skills/dustjacket/SKILL.md` + `references/*.md`) with one Python helper (`scripts/dustjacket_check.py`). Format is a new reference (`references/formats.md`) that the SKILL workflow consults after repo-type detection; repo type supplies the default format, the user can override, and Voice stays orthogonal (tone only). No new runtime code — the deterministic checker is unchanged; verification is a behavioral subagent fixture.

**Tech Stack:** Markdown skill files; Python 3.12 stdlib for the existing checker; pytest; fresh-agent fixtures for behavioral verification.

**Spec:** `docs/superpowers/specs/2026-06-20-format-axis-design.md` (canonical source for all tables).

## Global Constraints

- Every format and voice obeys `references/anti-slop.md` (incl. the em-dash rule) and `references/fabrication.md`. No exceptions per format.
- Emoji are **never in prose**, in any format; the emoji override only toggles *structural* emoji.
- Selection precedence everywhere: explicit user choice > repo-type default. The skill always states what it chose.
- The five format names are fixed tokens: `minimal`, `standard`, `reference`, `tutorial`, `landing`.
- Branch: `m5-format-axis`. `main` is protected — land via PR with one approval (admin bypass for solo).
- Conventional Commits (semantic-release): `feat:` for capability, `docs:` for reference-only text, `test:` for fixtures.

---

### Task 1: `references/formats.md` — the five presets (issue #27)

The core contract every other task depends on. Single source of truth for layout.

**Files:**
- Create: `skills/dustjacket/references/formats.md`

**Interfaces:**
- Produces: the five format tokens and, for each, five fields — **section ordering**, **emoji default**, **length target**, **device set**, **default voice**. Other tasks reference these tokens and the default-voice mapping verbatim.

- [ ] **Step 1: Write `formats.md`** with one section per format. Use this table as the contract (copy verbatim), then a subsection per format detailing section ordering and device set:

```markdown
| Format | Structure | Emoji default | Length | Default voice |
|--------|-----------|---------------|--------|---------------|
| minimal | title, one-line description, install, usage, license | none | shortest | technical-writer |
| standard | consensus skeleton + description, contributing | none | lean | technical-writer |
| reference | TOC, option/API tables, exhaustive sections, back-to-top | none | long | reference-manual |
| tutorial | getting-started first, step-by-step, narrative, example-heavy | light, structural | medium-long | friendly-OSS |
| landing | hero image, badge cluster, feature grid, screenshots, benefit-first | structural | medium | product |
```

For each format add: the exact ordered section list, which devices from `references/helpers.md` and `references/assets.md` apply, and a one-line "use when." Include the precedence + "state your choice" rule.

- [ ] **Step 2: Verify internal consistency**

Run: `for f in minimal standard reference tutorial landing; do grep -q "$f" skills/dustjacket/references/formats.md || echo "MISSING $f"; done`
Expected: no output (all five present).

Run: `python scripts/dustjacket_check.py skills/dustjacket/references/formats.md --repo-root . --threshold warning`
Expected: no em-dash/structural findings (the file is internally clean).

- [ ] **Step 3: Commit**

```bash
git add skills/dustjacket/references/formats.md
git commit -m "feat: add format presets (minimal/standard/reference/tutorial/landing)"
```

---

### Task 2: repo-type default-format mapping + refocus house-styles (issue #28)

**Files:**
- Modify: `skills/dustjacket/references/repo-types.md`
- Modify: `skills/dustjacket/references/house-styles.md`

**Interfaces:**
- Consumes: format tokens from Task 1.
- Produces: a `repo type → default format` mapping the SKILL workflow (Task 3) reads.

- [ ] **Step 1: Add the default-format column to `repo-types.md`** using this mapping verbatim:

```
library → standard | CLI → standard (+demo) | framework → landing
product → landing | content → reference | plugin/skill → standard | profile → personal
```

State: this is the *default*; an explicit user format overrides it.

- [ ] **Step 2: Refocus `house-styles.md`** — keep the per-type *devices/assets* (what a CLI vs product can show) and the cross-type rules; move layout/structure responsibility to `formats.md` with a pointer (`Layout is chosen by format — see references/formats.md`). Do not duplicate section orderings now owned by formats.md.

- [ ] **Step 3: Verify**

Run: `grep -n "formats.md" skills/dustjacket/references/house-styles.md`
Expected: at least one pointer to formats.md.

Run: `python scripts/dustjacket_check.py skills/dustjacket/references/repo-types.md --repo-root . --threshold warning`
Expected: clean.

- [ ] **Step 4: Commit**

```bash
git add skills/dustjacket/references/repo-types.md skills/dustjacket/references/house-styles.md
git commit -m "feat: map repo types to default formats; house-styles owns devices, formats owns layout"
```

---

### Task 3: SKILL.md + `/dustjacket` format wiring (issue #29)

**Files:**
- Modify: `skills/dustjacket/SKILL.md`
- Modify: `commands/dustjacket.md`

**Interfaces:**
- Consumes: format tokens (Task 1), default-format mapping (Task 2).
- Produces: the workflow step order the implementer/agent follows at runtime.

- [ ] **Step 1: Add a format-selection step** to the prettify workflow in SKILL.md, immediately after "Detect the repo type" and before "Pick a voice":

```markdown
2. **Choose the format.** Default to the repo type's default format (`references/repo-types.md`); honor
   an explicit user request. Apply `references/formats.md`. State the choice and offer the alternatives:
   "Using **standard** format (default for a library) — say the word for reference / tutorial / landing / minimal."
```

Renumber subsequent steps. Add a one-line mention of format to the Overview and the reference-files list.

- [ ] **Step 2: Add the format arg** to `commands/dustjacket.md`: `/dustjacket [path] [format] [voice]` (all optional, matched by keyword). Note precedence.

- [ ] **Step 3: Verify**

Run: `grep -n "format" skills/dustjacket/SKILL.md commands/dustjacket.md`
Expected: format step present in SKILL.md and the arg present in the command.

- [ ] **Step 4: Commit**

```bash
git add skills/dustjacket/SKILL.md commands/dustjacket.md
git commit -m "feat: wire format selection into the skill workflow and command"
```

---

### Task 4: Emoji as an independent override (issue #30)

**Files:**
- Modify: `skills/dustjacket/references/formats.md`
- Modify: `skills/dustjacket/references/toggles.md`

**Interfaces:**
- Consumes: per-format emoji defaults (Task 1).
- Produces: the rule that emoji on/off is a standalone override.

- [ ] **Step 1: Document the override** in toggles.md: emoji defaults from the format; the user can force on/off regardless; emoji never appear in prose (anti-slop). Cross-link from formats.md.

- [ ] **Step 2: Verify**

Run: `grep -ni "emoji" skills/dustjacket/references/toggles.md`
Expected: explicit "independent override" wording and the "never in prose" caveat.

- [ ] **Step 3: Commit**

```bash
git add skills/dustjacket/references/formats.md skills/dustjacket/references/toggles.md
git commit -m "feat: emoji on/off as an independent override on top of format"
```

---

### Task 5: Clarify voice-modes to tone-only (issue #31)

**Files:**
- Modify: `skills/dustjacket/references/voice-modes.md`

- [ ] **Step 1: Edit voice-modes.md** to state voice = tone only, orthogonal to format; each format implies a default voice (point to formats.md); any voice pairs with any format. Remove any implication that voice changes structure/length.

- [ ] **Step 2: Verify**

Run: `grep -ni "tone only\|orthogonal\|format" skills/dustjacket/references/voice-modes.md`
Expected: the tone-only/orthogonal framing is present.

- [ ] **Step 3: Commit**

```bash
git add skills/dustjacket/references/voice-modes.md
git commit -m "docs: clarify voice is tone-only, orthogonal to format"
```

---

### Task 6: README format showcase (issue #32)

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: the five formats (Task 1).

- [ ] **Step 1: Add a `## Formats` section** showing the *same* small project rendered in each format, so the layouts are visibly different: `minimal` (5 lines), `standard` (skeleton), `reference` (TOC + an option table), `tutorial` (numbered steps + one light structural emoji), `landing` (a hero line + a badge row + a feature grid). Keep a one-line note that Voice is the secondary tone axis. Use a real example project (reuse the httpcache sample from the fixtures so it's grounded). Keep em-dashes ≤1 per line.

- [ ] **Step 2: Verify the README still passes the checker**

Run: `python scripts/dustjacket_check.py README.md --repo-root . --threshold warning`
Expected: `no drift found.` exit 0.

Run: `grep -c "—" README.md`
Expected: 0 (or each line ≤1; the checker enforces the hard rule).

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: showcase the five formats with distinct layouts"
```

---

### Task 7: Behavioral fixture — two formats differ (issue #33)

**Files:**
- Create: `tests/fixtures/format-demo/` (a small real repo: one module + manifest + stub README)
- Modify: `tests/RESULTS.md` (record the comparison)

**Interfaces:**
- Consumes: the whole skill (Tasks 1–6).

- [ ] **Step 1: Create the fixture repo** — a tiny but real project (e.g. a `pyproject.toml` + one module + a thin README) so there are real facts to format and nothing forces fabrication.

- [ ] **Step 2: Run the comparison** — dispatch a fresh agent twice on the fixture, once instructed to use the dustjacket skill with `format: reference`, once with `format: landing`. Capture both outputs.

- [ ] **Step 3: Assert structural difference** (manual/scripted): the `landing` output has a hero/badge cluster and structural emoji; the `reference` output has a TOC + tables and no emoji; both pass `dustjacket_check.py` and contain no fabricated facts. Record the before/after and the verdict in `tests/RESULTS.md`.

- [ ] **Step 4: Commit**

```bash
git add tests/fixtures/format-demo tests/RESULTS.md
git commit -m "test: prove reference vs landing produce structurally different READMEs"
```

---

## Self-Review

- **Spec coverage:** All 7 spec decomposition items map to Tasks 1–7 (formats.md, type→format mapping + house-styles refocus, SKILL/command wiring, emoji override, voice clarification, README showcase, behavioral fixture). Selection precedence and "state the choice" are in Task 3; emoji-never-in-prose is a Global Constraint + Task 4.
- **Placeholder scan:** No TBDs; each task has concrete content (the format table and type→format mapping verbatim), exact verification commands, and commit messages. Full prose of each reference file is authored at implementation time against the spec's canonical tables (referenced, not duplicated, to stay DRY).
- **Type/token consistency:** The five format tokens and the default-voice/default-format mappings are stated once (Task 1 / Task 2) and referenced thereafter; no divergent names.

## Notes for the implementer

- formats.md (Task 1) is the keystone — get its tokens and mappings exactly right; everything references it.
- These are documentation changes to a prompt-skill; "tests" are the deterministic `dustjacket_check.py` (already on main) plus the Task 7 behavioral fixture. There is no new runtime code to unit-test.
- Order matters: Task 1 → 2 → 3 unblock the rest; Tasks 4/5 are small and independent; 6/7 come last.
