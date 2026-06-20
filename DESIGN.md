# Design system

> **Not a UI project.** dustjacket is a Claude Code skill — Markdown and prompts, no frontend, no
> rendered interface. The conventional design-system sections (color palette, typography, components,
> breakpoints) do not apply, so frontend/UI reviews (`/review-frontend-health`) are N/A here.

## Stack

- Claude Code skill: `SKILL.md` + reference files (`references/`), helper scripts (`scripts/`).
- Output format: GitHub-Flavored Markdown (the READMEs the skill produces).
- No runtime UI, no styling layer, no component library.

## Output style system

dustjacket's real "design system" is the set of conventions for the **READMEs it produces**, not an
app UI. Those conventions are documented and version-controlled here:

- [docs/research.md](docs/research.md) — per-repo-type house styles, signature devices, and the
  cross-type rules (the output style system).
- [docs/design.md](docs/design.md) — the anti-slop ruleset, voice modes, and asset conventions.

## Anti-patterns (do NOT do these)

These govern dustjacket's output, enforced by the anti-slop ruleset (#5):

- Empty self-adjectives (comprehensive, powerful, robust, seamless) — the specs are the adjectives.
- Filler verbs (leverage, utilize, empower, delve), throat-clearing openers, bold-everything.
- Emoji sprinkled through prose — emoji are structural (headings/bullets) or absent, never decorative.
- Scattered badge walls — badges cluster with unified styling.
- Inventing any feature, command, or benchmark not supported by the repo.
