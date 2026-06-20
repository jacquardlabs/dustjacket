# Mechanical helpers

Markup generators with zero fabrication risk — they restyle real content or wrap real assets. Apply
them within the toggles (`references/toggles.md`). Never reference an asset that doesn't exist; if a
device needs an image the repo lacks, flag it as a TODO (asset *creation* is a later milestone).

## Theme-aware header image

The highest-leverage device when the repo has a logo/banner. Light/dark via `<picture>`:

```html
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/logo-dark.svg">
    <img alt="<project> — <one-line>" src="docs/assets/logo-light.svg" width="420">
  </picture>
</p>
```

Only emit this if the image files exist (or the user confirms they will). Otherwise:
`> TODO: add a light/dark header image at docs/assets/.`

## Curated badge cluster

A small, unified set — never a wall. Floor: CI, version, packaging. Keep one style across all badges.

```markdown
[![CI](https://github.com/<org>/<repo>/actions/workflows/ci.yml/badge.svg)](…)
[![npm](https://img.shields.io/npm/v/<pkg>.svg)](…)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
```

Only include a badge whose URL actually resolves for this repo. Don't invent a CI badge if there's no
CI workflow.

## Collapsible `<details>` (install matrices)

The canonical CLI pattern for per-OS / per-shell install sprawl:

```markdown
<details>
<summary>macOS</summary>

| Manager | Command |
| ------- | ------- |
| Homebrew | `brew install <tool>` |
</details>
```

## GitHub alert callouts

The modern replacement for bold "Note:" lines:

```markdown
> [!NOTE]
> Requires Node 18+.

> [!WARNING]
> The `--force` flag deletes the cache.
```

## Table of contents + back-to-top (content repos)

Generate a TOC from the headings; add back-to-top after each section once the doc runs long:

```markdown
**[⬆ back to top](#table-of-contents)**
```

On GitHub a TOC is auto-generated, so only add a manual one for long content repos or on request
(`references/toggles.md`).

## Consistent list entries (content repos)

One shape per line so the eye can skip: `- [Name](url) - one-line description.` Nest a multi-part
series under an unlinked parent label.
