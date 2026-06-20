# dustjacket

A Claude Code skill that restyles a repository's README to a chosen format and voice, without
fabricating anything.

> **Status:** all three modes are implemented: prettify, check, and generate.

## What it does

A dust jacket sells and summarizes a book, and a README does the same for a repo. Most are either
generic AI boilerplate or an afterthought. dustjacket fixes a README to read like the *great* READMEs in
its category, drawing on a corpus of verbatim-analyzed exemplars across six repo types.

- **Detects the repo type** (CLI, library, framework, product, content, or plugin/skill) and picks a
  sensible default format.
- **Chooses a format** (the layout axis): minimal, standard, reference, tutorial, or landing. This sets
  structure, length, and emoji. Override the default anytime.
- **Picks a voice** (the tone axis): technical-writer, product, friendly-OSS, or reference-manual.
- **Strips the AI tells.** An anti-slop ruleset removes empty self-adjectives, filler verbs, and
  throat-clearing, and requires numbers, real code, and alt text.
- **Never fabricates.** Missing sections become flagged TODOs, not invented marketing.

## Formats

Format is the layout axis: it changes structure, length, and emoji, not just wording. Pick one, or let
dustjacket default from the repo type and override when you want a different presentation.

| Format | Opens with | Emoji | Length | Best for |
|--------|------------|-------|--------|----------|
| `minimal` | title + one-liner | none | shortest | scripts, small utilities |
| `standard` | title + install | none | lean | most libraries, CLIs, plugins |
| `reference` | a table of contents | none | long | tools whose README is the docs |
| `tutorial` | "Getting started" | light, structural | medium-long | onboarding-focused projects |
| `landing` | a hero image | structural | medium | products, frameworks |

The same project (`tokenbucket`, a rate limiter) in each format. Voice is layered on top and changes
wording only, never the layout.

<details>
<summary><code>minimal</code></summary>

```markdown
# tokenbucket

A token-bucket rate limiter for Python.

## Install

    pip install tokenbucket

## Usage

    from tokenbucket import TokenBucket
    bucket = TokenBucket(rate=10, capacity=50)
    bucket.take()  # True if a token was available

## License

MIT
```
</details>

<details>
<summary><code>standard</code></summary>

```markdown
# tokenbucket

A token-bucket rate limiter for Python. Zero dependencies, Python 3.9+.

## Install

    pip install tokenbucket

## Usage

    from tokenbucket import TokenBucket
    bucket = TokenBucket(rate=10, capacity=50)
    if bucket.take():
        ...  # allowed

## API

`TokenBucket(rate, capacity)` and `take(n=1) -> bool`.

## Contributing

See CONTRIBUTING.md.

## License

MIT
```
</details>

<details>
<summary><code>reference</code></summary>

```markdown
# tokenbucket

Token-bucket rate limiter for Python.

## Contents
- [Install](#install)
- [Usage](#usage)
- [API](#api)

## API

### take(n=1) -> bool

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| n     | int  | 1       | Tokens to consume |

Returns True if n tokens were available and consumed, else False.

**[⬆ back to top](#contents)**

## License

MIT
```
</details>

<details>
<summary><code>tutorial</code></summary>

```markdown
# tokenbucket

Rate-limit a function in three steps.

## ✦ Getting started

1. Install it:

        pip install tokenbucket

2. Create a bucket: 10 tokens/sec, burst of 50.

        bucket = TokenBucket(rate=10, capacity=50)

3. Gate each call:

        if bucket.take():
            handle(request)

## License

MIT
```
</details>

<details>
<summary><code>landing</code></summary>

```markdown
<p align="center"><img src="docs/assets/logo.png" alt="tokenbucket logo"></p>

# tokenbucket

Rate-limit any call to a steady rate, with bursts.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](#license)

## ✦ Why tokenbucket

| | |
|---|---|
| **Zero dependencies** | Pure stdlib. |
| **Monotonic clock** | Clock changes never corrupt the bucket. |

## ⚡ Quick start

    pip install tokenbucket

## License

MIT
```
</details>

## Install

```
/plugin marketplace add jacquardlabs/marketplace
/plugin install dustjacket@jacquardlabs-marketplace
```

## Usage

| Provides | Trigger | Job |
|----------|---------|-----|
| `/dustjacket [path] [format] [voice]` | you run it | Prettify a README; optional path, format, and voice |
| `dustjacket` skill | a request to clean up, rewrite, or review a README | Runs the prettify workflow automatically |

The skill detects the repo type, chooses a format, picks a voice, restructures to that format, strips
the AI tells, flags gaps as TODOs, and shows a diff for approval before writing.

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
