# House styles by repo type

Signature devices, default voice, and emoji/visual stance per type — extracted from a verbatim
analysis of exemplar READMEs (see `docs/research.md` for the full corpus). Apply the section that
matches the detected type. The cross-type rules at the bottom hold for every type.

> **Layout is owned by the format, not the type.** Section ordering and length come from the chosen
> format (`references/formats.md`); this file supplies the *devices and assets* each type can show
> (a CLI's demo GIF, a product's hero, a content repo's index). Where a per-type "skeleton" below and
> the format disagree on ordering, the format wins. Repo type only sets the *default* format
> (`references/repo-types.md`).

---

## CLI / terminal tools

*Exemplars: bat, starship, gum, ripgrep, fzf.*

- **Header:** centered block — logo (often *replacing* the H1), badge trio, one-line tagline,
  `•`/`·` anchor nav. Or, deliberately, prose-authority: a descriptive paragraph before the badges
  (ripgrep). Avoid the muddy middle (bare title + one screenshot + link-outs).
- **Skeleton:** hero → highlights/features → installation → usage/examples → configuration →
  contributing → license.
- **Signature devices:** prove it *in the terminal* — demo GIF (VHS), screenshots, or benchmark
  tables; `<details>` to collapse per-OS install matrices; GitHub callouts (`> [!NOTE]`); tables that
  teach the command language; an honest "why not use this" section.
- **Default voice:** `technical-writer` (or `reference-manual` for tools whose README is the docs).
- **Emoji:** zero, or systematic heading emoji — never sprinkled in prose.

## Library / SDK

*Exemplars: zod, requests, pydantic, typer, got.*

- **Header:** identity strip then get out of the way — plain H1 + tagline, or centered logo + tagline,
  one badge row (version/install/CI).
- **Skeleton:** what-is-it → install → **usage (code, fast)** → API → contributing → license.
- **Signature devices:** **code is the hero and comes within the first screenful**, framed by exactly
  one sentence so it reads as proof; show the payoff inline (a REPL transcript with real return values,
  or output comments showing the transformation); number-bearing feature bullets; comparison tables
  only when positioning against rivals. Minimal visuals — there's nothing to screenshot.
- **Default voice:** `technical-writer`.
- **Emoji:** none to sparse. The README is a doorway — link out to full docs.

## Framework

*Exemplars: Astro, Svelte.*

- **Header:** banner image + centered tagline + badge cluster (the banner is the brand mark).
- **Skeleton:** banner → what/why → install → docs → contributing → packages directory → sponsors.
- **Signature devices:** a monorepo directory table with inline per-package version badges (a
  self-updating release dashboard); theme-aware `<picture>` header; docs/community/sponsors sections.
- **Default voice:** `friendly-OSS` (warm, contributor-inviting) or `product`.
- **Emoji:** sparse.

## Product / app

*Exemplars: Excalidraw, Supabase, Appwrite, Next.js.*

- **Header:** the header is a **hero, not a title** — an image (banner/logo) stands in for the H1,
  then a centered nav row and a curated badge cluster.
- **Skeleton:** hero → features → quick start / deploy → docs → community → sponsors → license.
- **Signature devices:** theme-aware images (`<picture>` or `#gh-light-mode-only`); a product
  screenshot (and occasional GIF in `<kbd>`); curated badge clusters with *unified* styling; tables
  doing structural marketing (capability matrix, one-click-deploy grid); community/commerce sections.
- **Default voice:** `product`.
- **Emoji:** sparse and structural (bullet icons, table dividers) — never through prose.

## Content / awesome / educational

*Exemplars: public-apis, coding-interview-university, system-design-primer, awesome, project-based-learning.*

The defining problem is **navigation across hundreds of lines.**

- **Header:** optional centered banner/logo → ≤3 sentences of what-and-why → **TOC** → body. The faster
  the reader reaches the TOC, the better.
- **Signature devices:** a TOC whose nesting tracks content depth; back-to-top links after every
  section once the doc is long (`**[⬆ back to top](#...)**`); parallel fixed-shape entries
  (`[Name](url) - one line.`) or fixed-column tables; `<details>` to collapse noisy metadata; nest
  multi-part series under an unlinked parent.
- **Default voice:** `reference-manual` (terse) — or a short human hook (a one-paragraph testimonial),
  never middling throat-clearing.
- **Emoji:** austere; functional markers only (e.g., the `⬆` back-to-top arrow).

## Plugin / skill (Claude Code & agent plugins)

*Exemplars: the jacquardlabs marketplace plugins (jaqal, gg, voice-suite).*

dustjacket's own type, and the common target for agent-skill authors. It behaves like a small,
install-and-use library README — the value is what the plugin *does for the agent*, not an API.

- **Header:** plain H1 + one-line description, optional small badge (license). No hero needed.
- **Skeleton:** title → one-liner → what it does → **install** (`/plugin marketplace add …` then
  `/plugin install …`) → the commands/skills/agents it provides (a table) → how it works →
  contributing → license.
- **Signature devices:** a table listing each command/skill with its trigger and one-line job; a short
  "what it does" list of real capabilities; install as copy-paste slash commands.
- **Default voice:** `technical-writer`.
- **Emoji:** off or sparse. No screenshots, no API code blocks — show the commands instead.

---

## Cross-type rules (true everywhere)

1. **One real one-line description**, immediately under the title. Mandatory.
2. **A License section.** Mandatory.
3. **Show, don't tell** — but the proof medium is type-specific: code (library), terminal GIF/benchmark
   (CLI), screenshot (product), table (content/framework).
4. **The README is a doorway** — front-load value, link out for depth; brevity is a feature.
5. **Emoji are structural or absent, never decorative prose.**
6. **Badges cluster and unify** — a curated set with coherent styling, never a scattered wall.
7. **Theme-aware images** are the highest-leverage polish device when visuals apply at all.
8. **Write for the newcomer deciding whether to use this**, not for yourself.
