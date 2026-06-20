# Format presets

Format is the primary, layout-level axis. It sets structure, emoji default, length, and which devices
appear. Repo type supplies the default format; an explicit user choice overrides it. Voice stays
orthogonal: it controls tone only, never structure (see `references/voice-modes.md`).

## Format table

| Format | Structure | Emoji default | Length | Default voice |
|--------|-----------|---------------|--------|---------------|
| minimal | title, one-line description, install, usage, license | none | shortest | technical-writer |
| standard | consensus skeleton + description, contributing | none | lean | technical-writer |
| reference | TOC, option/API tables, exhaustive sections, back-to-top | none | long | reference-manual |
| tutorial | getting-started first, step-by-step, narrative, example-heavy | light, structural | medium-long | friendly-OSS |
| landing | hero image, badge cluster, feature grid, screenshots, benefit-first | structural | medium | product |

Every format obeys `references/anti-slop.md` and the no-fabrication rules in
`references/fabrication.md`. Emoji are never in prose in any format; defaults above apply only to
structural positions (headings, bullets, section markers).

## Selection rule

1. Look up the repo type's default format in `references/repo-types.md`.
2. If the user named a format, use it regardless of type.
3. State the choice: "Using **\<format\>** format (default for a \<type\> repo) — say the word to switch
   to e.g. `reference`/`minimal`."
4. Low detection confidence: confirm with the user before applying.

The same precedence applies to voice: **explicit user choice > repo-type default**.

## minimal

**Use when:** the user wants the smallest honest README (scripts, small utilities, personal tools).

**Ordered sections:**
1. Title
2. One-line description
3. Install
4. Usage
5. License

**Devices:** none. No badges, no images, no TOC. Emit only what exists in the repo. Every section
must be real or flagged as a TODO — nothing fabricated.

## standard

**Use when:** the default for most libraries, CLIs, and plugins — a complete doorway without being long.

**Ordered sections:**
1. Title + one-line description
2. Install
3. Usage
4. Configuration (if applicable)
5. API / commands (if applicable)
6. Contributing
7. License

**Devices:** curated badge cluster (CI, version, packaging) from `references/helpers.md`; GitHub alert
callouts (`> [!NOTE]`) for important caveats; collapsible `<details>` for per-OS install matrices.
No hero image, no TOC unless the doc grows long.

## reference

**Use when:** the README is the docs — tools, CLIs, content repos, or API-heavy libraries where the
reader needs exhaustive detail.

**Ordered sections:**
1. Title + one-line description
2. Table of contents
3. Install
4. Usage
5. Options / API tables (one table per command or module)
6. Configuration
7. Examples
8. Contributing
9. License

**Devices:** TOC with GitHub-style anchors and back-to-top links after each section (from
`references/helpers.md`); option/API tables — one per command or exported symbol; collapsible
`<details>` for verbose flag lists or install matrices; GitHub alert callouts for requirements and
warnings. No hero image, no structural emoji.

## tutorial

**Use when:** the goal is onboarding — the reader needs to succeed at a task end-to-end, not look
up a flag.

**Ordered sections:**
1. Title + one-line description
2. Getting started (prerequisites, install)
3. Step-by-step walkthrough (numbered, narrative)
4. Example output or result
5. Next steps
6. Contributing
7. License

**Devices:** light structural emoji on numbered steps and callout labels (never in prose); GitHub
alert callouts (`> [!NOTE]`, `> [!TIP]`) for prerequisite and "what just happened" notes; terminal
GIF or screenshot via VHS tape (from `references/assets.md`) if the repo has a demo command; real
runnable code in every step with actual output shown. No hero image, no badge cluster, no TOC.

## landing

**Use when:** the repo is a product, framework, or community project whose README must sell before
it explains.

**Ordered sections:**
1. Hero image (theme-aware `<picture>`)
2. One-line tagline
3. Badge cluster
4. Features / benefit grid
5. Screenshots or demo
6. Quick start / install
7. Documentation link
8. Community / sponsors
9. License

**Devices:** theme-aware header image (`<picture>` with light/dark variants) from
`references/helpers.md`; curated badge cluster (CI, version, packaging, community); feature grid
as a markdown table or aligned bullets with one concrete claim per row; screenshots via the capture
script from `references/assets.md` (scaffold if missing); structural emoji as section markers and
table icons. No manual TOC (GitHub auto-generates one); prose is badge-free and emoji-free.

## License

See [LICENSE](../../../LICENSE) (MIT).
