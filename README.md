# dustjacket

A Claude Code skill that restyles, generates, and drift-checks READMEs in their repo type's house
style and a chosen voice — without fabricating anything.

> **Status:** early development. The design is set ([docs/design.md](docs/design.md)); implementation
> is tracked in [milestone-driven issues](https://github.com/jacquardlabs/dustjacket/milestones).
> v1 ships **prettify** mode first, then layers **check** and **generate**.

## What it does

A dust jacket sells and summarizes a book. A README does the same for a repo — and most are either
generic AI boilerplate or an afterthought. dustjacket fixes an existing README (or writes a new one)
to match how *great* READMEs in its category actually read, drawing on a corpus of verbatim-analyzed
exemplars across five repo types.

- **Detects the repo type** — CLI, library, framework, product, or content — and applies that type's
  house style (a library leads with code; a product leads with a theme-aware hero; a content repo leads
  with navigation).
- **Strips the AI tells** — an anti-slop ruleset that removes empty self-adjectives, filler verbs, and
  throat-clearing, and requires numbers, real code, and alt text.
- **Picks a voice** — technical-writer (default), product, friendly-OSS, or reference-manual.
- **Never fabricates** — missing sections become flagged TODOs, not invented marketing. Code samples
  are run and their real output captured; visual assets are scaffolded (VHS tapes, capture scripts,
  Mermaid) or coached, never faked.

## Modes

| Mode | Job | Milestone |
|---|---|---|
| `prettify` | Restyle an existing README to the house style and chosen voice | v1 |
| `check` | Read-only drift gate — fails CI when the README no longer matches reality | layered |
| `generate` | Build a README from repo signals, interviewing for gaps | layered |

## Documentation

- [docs/design.md](docs/design.md) — modes, voice modes, the anti-slop ruleset, the drift gate, asset
  coaching, and the contested-choice toggles.
- [docs/research.md](docs/research.md) — the exemplars and extracted rules per repo type that the skill
  draws on.

## License

[MIT](LICENSE).
