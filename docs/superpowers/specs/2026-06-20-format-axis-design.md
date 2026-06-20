# Format axis — design spec

Date: 2026-06-20 · Status: approved (brainstorm), pending spec review · Target: M5

## Problem

dustjacket has two things a user might mean by "style," but only one produces dramatically different
output, and it isn't selectable as such:

- **Repo type** drives layout today (structure, emoji stance, devices), but it's auto-detected, not
  chosen — a user can't say "give me the onboarding-tutorial layout for my library."
- **Voice** is only tone (terse ↔ warm ↔ marketing). Four voices on the same one-liner look nearly
  identical, which is what surfaced the gap.

Users expect to pick a *fundamentally different presentation*: emoji or not, reference manual vs.
onboarding tutorial vs. marketing landing. That axis must be first-class and selectable.

## Solution: a selectable Format axis

Add **Format** as the primary, layout-level axis, independent of **Voice** (tone). Format sets
structure, emoji default, length, and which devices appear. Repo type supplies the *default* format;
the user can override.

### The two axes

| Axis | Controls | Options | Default |
|------|----------|---------|---------|
| **Format** (new, primary) | structure, emoji default, length, devices | minimal, standard, reference, tutorial, landing | from repo type |
| **Voice** (existing, secondary) | tone only | technical-writer, product, friendly-OSS, reference-manual | from format |

Fine-grained overrides a format pre-sets but the user can flip individually: **emoji on/off**, TOC,
usage-vs-install order, badge level (these already exist in `references/toggles.md`).

### The five formats

| Format | Structure | Emoji default | Length | Default voice |
|--------|-----------|---------------|--------|---------------|
| **minimal** | title, one-line description, install, usage, license | none | shortest | technical-writer |
| **standard** | consensus skeleton: + description, contributing | none | lean | technical-writer |
| **reference** | TOC, option/API tables, exhaustive sections, back-to-top | none | long | reference-manual |
| **tutorial** | getting-started first, step-by-step, narrative, example-heavy | light, structural only | medium-long | friendly-OSS |
| **landing** | hero image, badge cluster, feature grid, screenshots, benefit-first | structural | medium | product |

Each format is a bundle of toggle settings plus a section ordering and a device set. `minimal` and
`standard` differ only in completeness; the opinionated three (`reference`, `tutorial`, `landing`) are
the dramatic layouts.

### Repo type → default format

| Repo type | Default format | Rationale |
|-----------|----------------|-----------|
| library | standard | code-first, lean doorway; `reference` on request for API-heavy libs |
| CLI | standard (+ demo) | install-heavy with a demo; `landing` if product-positioned |
| framework | landing | banner, package ecosystem, community |
| product / app | landing | hero, screenshots, community/commerce |
| content / awesome | reference | the README is an index — TOC, back-to-top, fixed-shape entries |
| plugin / skill | standard | install + capability table |
| profile | tutorial-ish (personal) | personal page; its own light structure (no project skeleton) |

Override always wins: "make my library a tutorial" applies `tutorial` even though type = library.

### Emoji

Independent on/off override. Defaults from the format (landing/tutorial = some structural; the rest =
none). **Emoji are never in prose, in any format** — the anti-slop ruleset still governs. The override
only changes structural emoji (headings/bullets/markers).

### Voice relationship

Voice stays orthogonal and tone-only. Each format implies a default voice (table above); the user can
pair any voice with any format ("landing format, technical-writer voice"). Voice never changes
structure, emoji, or length — only register. All voices and formats obey anti-slop + no-fabrication.

### Selection logic & precedence

For both Format and Voice: **explicit user choice > repo-type default**. dustjacket states what it
picked and why ("Using **landing** format (default for a product repo) with **product** voice — say the
word to switch to e.g. `reference`/`minimal`"). Low detection confidence → confirm with the user.

## How it surfaces

- **SKILL.md** — the prettify/generate workflow gains a step between type-detection and the rewrite:
  *choose the format* (default from type, honor an explicit request, state the choice), then *choose the
  voice*.
- **Command** — `/dustjacket [path] [format] [voice]` (both optional, order-independent by keyword).
- **New `references/formats.md`** — the five presets: each one's section ordering, emoji default, length
  target, device set, and default voice. The single source of truth for layout.
- **`references/repo-types.md`** — add the default-format column (table above).
- **`references/toggles.md`** — note that a format sets the toggle bundle; emoji/TOC/usage-order/badges
  remain individual overrides on top.
- **`references/voice-modes.md`** — clarify voice = tone only, orthogonal to format.
- **`references/house-styles.md`** — refocus on type-specific *devices/assets* (what a CLI vs product
  can show); the *layout* now lives in formats.md. Keep cross-type rules.

## README payoff (the visible fix)

Replace the near-identical voice samples with a **format showcase**: the same small project rendered in
each format so the layouts are obviously different — `minimal` (5 lines) vs `reference` (TOC + tables)
vs `tutorial` (steps + light emoji) vs `landing` (hero + badges + feature grid). A short note keeps
voice as the secondary axis. This directly answers "the samples all look the same."

## Testing

- Unit: `references/formats.md` presets are internally consistent (each names ordering, emoji default,
  length, default voice).
- Behavioral fixture (the key one): run a fresh agent on one repo twice — once `--format reference`,
  once `--format landing` — and assert the outputs are *structurally* different (one has a hero +
  badges + emoji, the other has a TOC + tables + no emoji), and both still pass anti-slop +
  no-fabrication. This is the proof the axis does what the voice axis couldn't.
- Regression: `dustjacket_check.py` still passes on the showcase README (em-dash, links, sections).

## Scope & decomposition (M5)

1. `references/formats.md` — the five presets (the core).
2. Repo-type → default-format mapping in `repo-types.md`; refocus `house-styles.md` on devices.
3. SKILL.md + `/dustjacket` wiring: format selection step + arg, precedence, stated choice.
4. Emoji-as-independent-override (formats.md + toggles.md).
5. voice-modes.md clarified to tone-only.
6. README format showcase (replaces the voice samples).
7. Behavioral fixture test: two formats on one repo are fundamentally different.

## Unchanged

No-fabrication line, anti-slop ruleset (incl. the em-dash check from #26), repo-type detection, check
mode, generate mode. Format is an added selection layer; every format obeys the existing discipline.

## Dependencies / ordering

PR #26 (em-dash enforcement) should merge first; M5's README showcase supersedes #26's voice-sample
section, so building M5 on merged main avoids a tangled stack.
