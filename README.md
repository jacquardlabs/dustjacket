# dustjacket

A Claude Code skill that restyles a repository's README to its repo-type house style and a chosen
voice, without fabricating anything.

> **Status:** all three modes are implemented: prettify, check, and generate.

## What it does

A dust jacket sells and summarizes a book, and a README does the same for a repo. Most are either
generic AI boilerplate or an afterthought. dustjacket fixes a README to read like the *great* READMEs in
its category, drawing on a corpus of verbatim-analyzed exemplars across six repo types.

- **Detects the repo type** (CLI, library, framework, product, content, or plugin/skill) and applies
  that type's house style. A library leads with code; a product leads with a theme-aware hero; a content
  repo leads with navigation.
- **Strips the AI tells.** An anti-slop ruleset removes empty self-adjectives, filler verbs, and
  throat-clearing, and requires numbers, real code, and alt text.
- **Picks a voice:** technical-writer (default), product, friendly-OSS, or reference-manual.
- **Never fabricates.** Missing sections become flagged TODOs, not invented marketing.

## Voices

The same project, four registers. dustjacket defaults to technical-writer; name another to switch. Each
voice obeys the anti-slop ruleset, so even `product` sells with specifics, not "powerful" and "seamless."

**technical-writer** (default): direct, specific, no hype.
> An HTTP client for Python. Connection pooling, retries, and typed responses.

**product**: benefit-first, confident.
> Make HTTP requests that just work: pooled, retried, and typed out of the box.

**friendly-OSS**: warm, contributor-inviting.
> A friendly HTTP client for Python. Pooling and retries built in. PRs welcome.

**reference-manual**: exhaustive, trusts the reader.
> HTTP client for Python. Supports connection pooling, automatic retries (configurable backoff), and typed responses. See the API for the full option list.

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

| Mode | Job |
|------|-----|
| `prettify` | Restyle an existing README to the house style and chosen voice |
| `check` | Read-only drift gate; fails CI when the README no longer matches reality |
| `generate` | Build a README from repo signals, interviewing for gaps |

## Drift checking in CI

`check` is a read-only gate. Run it locally or wire it into CI:

```bash
python scripts/dustjacket_check.py README.md
```

As a GitHub Action:

```yaml
- uses: jacquardlabs/dustjacket@v1
  with:
    readme: README.md
    threshold: error
```

Or as a [pre-commit](https://pre-commit.com) hook (`.pre-commit-hooks.yaml` provides `dustjacket-check`).

## Documentation

- [docs/design.md](docs/design.md): modes, voice modes, the anti-slop ruleset, the drift gate, asset
  coaching, and the contested-choice toggles.
- [docs/research.md](docs/research.md): the exemplars and extracted rules per repo type that the skill
  draws on.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues and milestones track the roadmap.

## License

[MIT](LICENSE).
