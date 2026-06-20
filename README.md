# dustjacket

A Claude Code skill that restyles a repository's README to its repo-type house style and a chosen
voice — without fabricating anything.

> **Status:** prettify mode is implemented (M0 + M1). `check` (drift gate) and `generate` are planned
> — see the [milestones](https://github.com/jacquardlabs/dustjacket/milestones).

## What it does

A dust jacket sells and summarizes a book. A README does the same for a repo — and most are either
generic AI boilerplate or an afterthought. dustjacket fixes a README to read like the *great* READMEs in
its category, drawing on a corpus of verbatim-analyzed exemplars across six repo types.

- **Detects the repo type** — CLI, library, framework, product, content, or plugin/skill — and applies
  that type's house style (a library leads with code; a product leads with a theme-aware hero; a content
  repo leads with navigation).
- **Strips the AI tells** — an anti-slop ruleset that removes empty self-adjectives, filler verbs, and
  throat-clearing, and requires numbers, real code, and alt text.
- **Picks a voice** — technical-writer (default), product, friendly-OSS, or reference-manual.
- **Never fabricates** — missing sections become flagged TODOs, not invented marketing.

## Install

```
/plugin marketplace add jacquardlabs/marketplace
/plugin install dustjacket@jacquardlabs-marketplace
```

## Usage

| Provides | Trigger | Job |
|----------|---------|-----|
| `/dustjacket [path] [voice]` | you run it | Prettify a README; optional path and voice |
| `dustjacket` skill | a request to clean up, rewrite, or review a README | Runs the prettify workflow automatically |

The skill detects the repo type, picks a voice, restructures to the house style, strips the AI tells,
flags gaps as TODOs, and shows a diff for approval before writing.

## Modes

| Mode | Job | Status |
|------|-----|--------|
| `prettify` | Restyle an existing README to the house style and chosen voice | available |
| `check` | Read-only drift gate — fails CI when the README no longer matches reality | planned (M3) |
| `generate` | Build a README from repo signals, interviewing for gaps | planned (M4) |

## Documentation

- [docs/design.md](docs/design.md) — modes, voice modes, the anti-slop ruleset, the drift gate, asset
  coaching, and the contested-choice toggles.
- [docs/research.md](docs/research.md) — the exemplars and extracted rules per repo type that the skill
  draws on.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues and milestones track the roadmap.

## License

[MIT](LICENSE).
