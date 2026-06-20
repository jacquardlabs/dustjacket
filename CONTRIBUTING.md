# Contributing to dustjacket

Thanks for your interest in improving dustjacket. Here's how to contribute.

dustjacket is in early development. The design is set ([docs/design.md](docs/design.md)) and the work
is tracked as [milestone-driven issues](https://github.com/jacquardlabs/dustjacket/milestones) — start
there to see what's planned and what's open.

## Reporting issues

Open an issue for bugs, unclear documentation, or suggestions. Include:

- What you expected to happen
- What actually happened
- Which mode was involved (prettify / check / generate)
- Your Claude Code version (`claude --version`)

## Proposing changes

1. **Open an issue first** for anything beyond a typo fix — or comment on the existing milestone issue.
   Describe what you want to change and why. This saves everyone time if it doesn't fit the direction.
2. **Fork and branch** from `main`. `main` is protected: changes land via pull request with one
   approval, squash-merged.
3. **Make your changes.** Follow the patterns in existing files and the conventions in
   [docs/design.md](docs/design.md) and [docs/research.md](docs/research.md).
4. **Open a PR** against `main` with a clear description of what changed and why.

## Commit messages

Releases are automated with [python-semantic-release](https://python-semantic-release.readthedocs.io)
from [Conventional Commits](https://www.conventionalcommits.org). Use the standard prefixes:

- `feat:` — a new capability (minor version bump)
- `fix:` — a bug fix (patch bump)
- `docs:`, `chore:`, `refactor:`, `test:` — no release
- `feat!:` / `fix!:` or a `BREAKING CHANGE:` footer — major bump (disabled while pre-1.0)

The version in `.claude-plugin/plugin.json` and the GitHub release are computed from commit history —
don't bump versions by hand.

## What makes a good contribution

- **Improvements to the rules** — sharper anti-slop detection, better house-style fidelity, new voice
  modes (see [docs/research.md](docs/research.md))
- **Bug fixes** — behavior that doesn't match the docs
- **Test corpora** — slop → clean pairs, fabrication-bait cases, drift fixtures
- **Documentation** — clearer examples, better onboarding

## The non-negotiable

dustjacket never fabricates. Any contribution that lets the skill invent a feature, command, benchmark,
or fact not supported by the target repo will be rejected. Missing information becomes a flagged TODO,
never invented prose.
