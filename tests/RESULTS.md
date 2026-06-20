# Verification: baseline vs. skill

Method: a fresh general-purpose agent prettified each fixture's README twice — once with no guidance
(**baseline**) and once instructed to follow the dustjacket skill (**skill**). Same model, same input.
This isolates what the skill changes. Output ground-truth for code claims was checked by running the
fixture code.

## Fixture 1 — `sloppy-readme` (complete repo, slop-drenched README)

Tests the **anti-slop ruleset** (#5). The repo has real facts (manifest, `Cache` API, LICENSE), so no
fabrication is needed — only slop removal.

- **Baseline:** a strong (Opus-class) agent already removed the slop and stayed grounded. It also
  asserted `pip install httpcache` as fact and added accurate-but-inferred limitations.
- **Skill:** same slop removal, plus — declared **type (library) + voice (technical-writer)**
  explicitly, consciously flipped to usage-first per the library house style, emitted only the *real*
  license badge, and **flagged `pip install` / CI / PyPI badges as TODOs** rather than asserting them.

**Finding:** against a strong model, slop removal is not a night-and-day gap — the model self-corrects.
The skill's value here is *consistency and discipline*: explicit type/voice, house-style structure, and
flagging unverified facts (install/badges) that the baseline stated as fact. The slop-removal win is
larger against weaker models (the baseline control did most of the work here).

## Fixture 2 — `sparse-repo` (thin code, no LICENSE, no manifest, stub README)

Tests the **no-fabrication line** (#8). The bait: a complete-looking README requires inventing an
install command, a license, and behavior.

Ground truth (`python3 widget.py`):
`slugify("Café & Crème")` → `'café-crème'` (Python `str.isalnum()` is Unicode-aware; accents survive).

| Axis | Baseline | Skill |
|------|----------|-------|
| Install | invented "copy `widget.py` to your `PYTHONPATH`" | **flagged TODO** — no manifest detected |
| License | "No license has been specified" (didn't invent — good) | **flagged TODO** — no LICENSE found |
| Output example | **fabricated** `slugify("Café & Crème")` → `"caf-cr-me"` and a "Notes" section claiming non-ASCII → hyphens — both **wrong** | one example, **hand-verified** correct; no false claims |
| Name/content mismatch | missed | flagged (repo is named "widget" but only contains `slugify`) |
| Empty sections | invented an API reference + limitations | left as TODOs; invented nothing |

**Finding:** clear, objective behavior change. The baseline produced confident, incorrect documentation
about code it never ran; the skill flagged the gaps and verified the one output it included. This is the
failure mode dustjacket exists to prevent.

## Fixture 3 — generate mode on `sparse-repo` (M4)

Tests **generate mode** (#21), the most fabrication-prone mode — greenfield, nothing to preserve. A
fresh agent generated a README from scratch for the sparse repo following `references/generate.md`.

- Detected **library** (medium confidence — flagged the thin signals).
- Flagged **install** and **license** as TODOs — invented neither (no `pip install widget`, no guessed
  license).
- Flagged the **name/tagline mismatch** ("utilities for widgets" vs. a lone `slugify`).
- **The decisive moment:** with code execution unavailable, it showed the usage example *without
  asserting output* ("output not verified") and noted `str.isalnum()` is Unicode-aware — exactly where
  the Fixture 2 baseline fabricated `"caf-cr-me"`. `references/verify-code.md` held the line.

**Finding:** generate mode produces an honest, mostly-TODO skeleton and refuses to invent — including
refusing to assert code output it couldn't run. Same no-fabrication discipline as prettify, on the mode
most likely to violate it.

## Fixture 4 — format axis: same repo, two formats (M5)

Tests the **format axis** — the whole point of M5. Two fresh agents wrote a README for the same fixture
(`tests/fixtures/format-demo`, a `tokenbucket` library), one in `reference` format, one in `landing`.
The outputs are structurally different, not just differently worded:

| Aspect | `reference` | `landing` |
|--------|-------------|-----------|
| Opens with | a table of contents | a tagline + badge cluster |
| Emoji | none | section markers (`✦ ⚡ 📖 📦`) |
| Centerpiece | one API table per method + an Algorithm section + back-to-top links | a benefit/feature grid + hero image (flagged) |
| Voice | reference-manual | product |
| Length | long, exhaustive | medium, scannable |

Both obeyed the discipline: each flagged the missing `LICENSE` file, the unconfirmed PyPI package, and
missing CI as `> TODO:` and invented nothing. The `landing` agent explicitly declined "blazing-fast"
and latency claims for lack of a benchmark, and flagged the hero image as a TODO rather than linking a
missing asset. Emoji appeared only as structural section markers, never in prose.

**Finding:** the format axis produces fundamentally different *layouts* on identical input — the thing
the four near-identical voice samples could not show — while every format still passes anti-slop and
no-fabrication.

## Conclusion

- **#8 (no-fabrication):** verified against an adversarial fixture — the skill avoids fabrication the
  baseline commits.
- **#5 (anti-slop):** verified — the skill produces slop-free output and adds the structural discipline
  (type/voice/TODOs) a bare prompt skips; the magnitude of the slop win scales with model weakness.
- **#21 (generate):** verified against the same adversarial fixture — generate mode flags gaps and
  refuses to assert unrun code output.
- **check mode (M3):** the deterministic checker has 15 unit tests; it's dogfooded in CI on this repo's
  README, and the GitHub Action + pre-commit hook are exercised end-to-end (`pre-commit try-repo`, a CI
  `uses: ./` job).
- **format axis (M5):** verified — `reference` and `landing` produce structurally different layouts on
  one repo (Fixture 4); every format obeys anti-slop + no-fabrication.
- **Follow-up:** full pressure-testing (combined pressures, 5+ reps per variant per the writing-skills
  methodology) is a fair next issue, not a v1 blocker.
