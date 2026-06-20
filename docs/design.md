# README skill — design notes

Working doc. Captures scope, voice modes, and rules as we extract them from the README research.
Developer-local; not committed.

## One-liner

A skill that takes a repo and produces (or repairs) a README in the *house style* of its repo
type, in a chosen voice, without fabricating anything — and can run as a check, not just a writer.

## Three operating modes

The "prettyfier" framing is really three jobs. Keep them separate.

1. **generate** — greenfield. No README, or a stub. Build from repo signals + asked-for gaps.
2. **prettify** — the common case. A README exists; restructure and restyle it to the house
   style without inventing facts. Preserve every real claim; flag missing sections rather than
   filling them with marketing.
3. **check** — read-only. Report drift and style violations, exit non-zero. This is the CI gate
   (see below). No file writes.

Same ruleset underneath; different output contract (write / write-with-diff / report-only).

## Repo-type detection

Style is earned differently per type (confirmed by research), so detect first, then ask to confirm.

| Type | Signals | House style |
|---|---|---|
| **CLI** | `bin` in package.json, `[project.scripts]`, `cmd/` + cobra, single binary | logo-as-title or prose-authority; badge trio (CI/version/packaging); demo GIF or screenshot; `<details>` per-OS install; tables that teach the command language; honest "why not" section |
| **library / SDK** | published package, no entrypoint binary, `src/` + API surface | code-first within ~10 lines; minimal visuals; API section; comparison/"why" tables; install one-liner |
| **framework** | monorepo, plugin ecosystem, `packages/` | banner + tagline; per-package version-badge directory table; docs/community/sponsors |
| **product / app** | Dockerfile + frontend, hosted offering | hero (theme-aware `<picture>`), curated badge cluster, product screenshot, sponsors/community/follow rows |
| **content / awesome** | mostly lists, `awesome-*`, tutorial repo | navigation *is* the product: TOC, anchor links, emoji legend/key, grouped categories, back-to-top |

Fallback: ask. Detection is a default, not a gate.

## Voice modes

Voice is orthogonal to repo type — a library can be terse or friendly. Default to **technical-writer**.

- **technical-writer** (default) — the non-LLMy voice. Direct, specific, no hype. ripgrep / requests /
  Flask register. Numbers attached to nouns. Honest caveats welcome. This is the anti-slop voice; see
  ruleset below. Maps closely to the user's own writing-style guide in CLAUDE.md.
- **product** — benefit-first but still concrete. starship / Supabase register. Allowed: a hero line, a
  short feature-benefit list. Still banned: empty self-adjectives.
- **friendly-OSS** — warm, contributor-inviting. bat / Astro register. "New contributors welcome,"
  light, but not salesy.
- **reference-manual** — exhaustive, table-heavy, trusts the reader. fzf register. For tools whose
  README is the docs.

Open question: integrate with the installed **voice-suite** (`voice-profile`) so "my voice" becomes a
mode that pulls the user's harvested style. Strong fit — the user already has a voice profile system.

## The anti-slop ruleset (the "non-LLMy" core)

This is the highest-value part and applies in *every* mode and voice. The default AI README voice is
recognizable; strip its tells.

**Ban (rewrite on sight):**
- Empty self-adjectives: comprehensive, powerful, robust, seamless, cutting-edge, blazing (unless
  there's a benchmark behind it), elegant, beautiful (unless it's a UI screenshot doing the work).
- Filler verbs: leverage, utilize, facilitate, empower, unlock, supercharge, delve, dive into.
- Throat-clearing: "In today's fast-paced world," "Whether you're a beginner or a pro," "Look no
  further," "In conclusion."
- Bold-everything and emoji-on-every-bullet. Emoji are structural or absent, never decoration
  (research: zero-emoji and systematic-heading-emoji both work; sprinkled-through-prose never appears
  in great READMEs).
- Vague quantifiers: "various," "a number of," "several powerful features." Replace with a count or cut.
- The triad-of-three rhythm and the em-dash-summary tic when overused.

**Require:**
- A real one-line description (the one near-universal mandatory element).
- A License section (the other near-universal mandatory element).
- Numbers/names/versions on claims, or cut the claim.
- Alt text on every image; descriptive link text (accessibility + correctness).
- Code examples that are real and runnable, not pseudo-snippets.

**Never:** invent a feature, benchmark, install command, or roadmap item that isn't supported by the
repo. If a section is empty, flag it (`> TODO: no LICENSE found — add one`) rather than writing fiction.
This is the line between prettify and fabricate, and it's non-negotiable.

## Drift / CI gate (`check` mode)

The user's idea: a gate that fails when the README no longer matches reality. Split by what's
deterministic vs. what needs the model.

**Deterministic (cheap, run first):**
- Broken links — internal anchors, relative file paths, image paths, external URLs (liveness).
- TOC ↔ headings out of sync (if a manual TOC exists).
- Metadata mismatch — README title/description/license vs. package.json / pyproject / Cargo.toml.
- Stale badge URLs (404), wrong package name in install command.
- Code fences with declared languages that don't parse.

**Model-assisted (gated behind the cheap checks passing):**
- Documented CLI commands / flags that no longer exist in `--help` or the arg parser.
- Public API in the README that's gone from the exported surface.
- Install instructions that don't match the actual package manager / entry point.
- Anti-slop violations as warnings (style drift, not just factual drift).

Output: severity-ranked report, non-zero exit on `error`-level. Ships as a pre-commit hook and/or a
GitHub Action. Note: GitHub auto-generates a TOC now, so flag manual TOCs as *optional/redundant*
rather than required.

## Mechanical helpers the skill should offer

Low-risk, high-leverage generators (no fabrication risk):
- Theme-aware `<picture>` light/dark header block (the single most-stolen device in product/framework
  READMEs).
- Curated badge cluster (shields.io URLs) — unified style, not a wall. CI + version + packaging trio
  as the floor.
- TOC generation + "back to top" links (content repos).
- `<details>` collapsing for combinatorial install matrices (the canonical CLI pattern).
- GitHub alert callouts (`> [!NOTE]` / `[!WARNING]`) — modern replacement for bold "Note:".

## Asset coaching & scaffolding

The research's highest-leverage devices — theme-aware screenshots, demo GIFs, REPL transcripts — are
exactly the things the skill *must not fabricate*. So split assets three ways by what the skill can
honestly do:

**A. Scaffold (generate as text — zero fabrication risk):**
- **Terminal GIFs via VHS** (charmbracelet/vhs). A `.tape` file is just a declarative script
  (`Type "..."`, `Enter`, `Sleep 2s`, `Set FontSize`, `Output demo.gif`). The skill writes the `.tape`
  from the repo's real commands; the user runs `vhs demo.tape` to render. This is the gum pattern, and
  it's reproducible + version-controllable. Offer per-command tapes (gum style) or one hero tape.
- **App screenshots via a capture script** — write a Playwright/Puppeteer script that navigates the
  real app and screenshots the hero flow in *both* color schemes (`prefers-color-scheme`). The user
  runs it; output is real pixels, not a mockup.
- **Diagrams via Mermaid** — renders natively on GitHub, theme-aware automatically, no binary asset to
  store. The no-tooling option for architecture/flow diagrams (system-design-primer used static images;
  Mermaid removes the maintenance).
- **The `<picture>` light/dark markup** and curated badge cluster, once the asset files exist.

**B. Coach (needs the user's environment/eyes — checklist, never fake):**
- **Screenshots:** *what* to capture (the hero flow, not a settings panel), aspect/resolution (Appwrite's
  1920×1080 hero), light+dark pair, where to store (`.github/assets/`), and required alt text.
- **GIFs:** keep them short, show one task end-to-end (gum rhythm), frame in `<kbd>` for a keycap border
  (Supabase). asciinema (`asciinema rec` → `agg` to GIF) as the alternative to VHS for live sessions.
- A pre-flight checklist so the produced asset matches the house style for the repo type.

**C. Verify (runnable — capture real output, never hand-wave):**
- **Code samples / REPL transcripts:** pull examples from the repo's `tests/`/`examples/` rather than
  invent, then *run them* and paste the actual output. requests' REPL with real `200`/dict returns and
  pydantic's `#>` coercion comments work *because the output is true*. The skill should execute the
  snippet and embed verified output, flagging any example it couldn't run rather than faking the result.

Principle: scaffold the scriptable, coach the visual, verify the runnable. Asset gaps the skill can't
fill become flagged TODOs (`> TODO: add a light/dark hero screenshot — capture script written to
scripts/shot.ts`), consistent with the fabrication line.

## Contested choices → toggles with defaults

From the meta-resource research (standard-readme, art-of-readme, makeareadme, Best-README-Template):

| Choice | Default | Notes |
|---|---|---|
| Badges | small honest set (CI/version/packaging) | never a wall |
| Emoji | off | no canonical source endorses or bans; folklore only |
| TOC | off for short docs | GitHub auto-generates; on for content repos |
| Usage vs. install order | install-first | flip to usage-first for "show value fast" libraries |
| Visuals (screenshot/GIF) | on for product/CLI, off for library | library has no UI to show |
| Length | lean; link out to docs/ | art-of-readme: "brevity is a feature" |

Consensus skeleton (always-on spine): **title → one-line description → longer description → install →
usage → contributing → license.** License + one-liner are the only two non-negotiables.

## Open questions

1. Scope v1: all three modes, or ship **prettify** first and add **check** later?
2. Is the CI gate part of this skill or a sibling skill it calls?
3. Integrate voice-suite as a "my voice" mode, or keep voice modes self-contained?
4. Output for prettify: overwrite README.md (with backup), or always show a diff for approval first?
5. Profile READMEs (`username/username`) — in scope as a special type, or out for v1?
