---
name: dustjacket
description: Use when a repository's README needs writing or improving — restyling an existing README, drafting a new one, or auditing whether it has drifted from the code. Triggers on requests to clean up, prettify, rewrite, polish, generate, or review a README, or when a README reads like generic AI boilerplate ("comprehensive", "powerful", "seamless").
---

# dustjacket

## Overview

A dust jacket sells and summarizes a book. A README does the same for a repo. dustjacket fixes or
writes a README so it reads like the *great* READMEs in its category — and it does this without
inventing anything that isn't true of the repo.

**Core principle: never fabricate.** dustjacket restyles, reorganizes, and sharpens what the repo
actually supports. Missing facts become flagged TODOs, never invented prose. This is the line that
separates the skill from the AI slop it exists to remove. **REQUIRED:** read `references/fabrication.md`
before writing any README content.

## When to use

- An existing README is messy, generic, or reads like AI boilerplate → **prettify**.
- A repo has no README, or a stub → **generate** (`references/generate.md`).
- A README may no longer match the code → **check** (`references/check.md`).

If the user only wants a quick edit to one line, just make the edit — don't run the full workflow.

## Modes

| Mode | Job | How |
|------|-----|-----|
| `prettify` | Restyle an existing README to its repo-type house style and a chosen voice | the workflow below |
| `check` | Read-only drift gate; fails when the README no longer matches reality | `references/check.md` |
| `generate` | Build a README from repo signals, interviewing for gaps | `references/generate.md` |

**check** never writes — it reports and exits non-zero (CI gate). **prettify** and **generate** write
only after the diff-and-approve contract (`references/output.md`).

## Prettify workflow

Follow these steps in order. Each references a file under `references/` — read it when you reach it.

1. **Detect the repo type** — CLI, library, framework, product, content, or plugin/skill. Apply `references/repo-types.md`.
   State your guess and confidence; if unsure, ask the user to confirm before proceeding.
2. **Choose the format** — the layout-level axis. Default to the repo type's default format
   (`references/repo-types.md`); honor an explicit user request. Apply `references/formats.md`. State the
   choice and the alternatives: "Using **standard** (default for a library) — say the word for reference,
   tutorial, landing, or minimal."
3. **Pick a voice** — the tone axis, orthogonal to format. Default to the format's default voice
   (`references/formats.md`); honor an explicit user request. Apply `references/voice-modes.md`; say which
   you chose.
4. **Read the existing README and the repo.** Inventory every real claim, command, path, and code
   sample. You will preserve these; you will not invent new ones (`references/fabrication.md`).
5. **Restructure to the format.** Lay out the chosen format's section ordering (`references/formats.md`),
   using the type's devices and assets (`references/house-styles.md`) and the consensus spine in
   `references/prettify.md`.
6. **Strip the AI tells.** Apply `references/anti-slop.md` to every line — bans, requires, red flags.
7. **Apply mechanical helpers** as the format and toggles allow — `references/helpers.md` and
   `references/toggles.md` (emoji defaults from the format; overridable).
8. **Handle assets.** Scaffold the scriptable, coach the visual, verify code output — `references/assets.md`
   and `references/verify-code.md`. Never reference an asset that doesn't exist; flag it instead.
9. **Flag the gaps.** Any required section with no real source becomes a `> TODO:` note, never fiction.
10. **Show a diff and get approval before writing.** Apply the output contract in `references/output.md`.

## Quick reference

- Two things every README must have: a real one-line description and a License section.
- Both zero-emoji and systematic-heading-emoji are fine; emoji sprinkled through prose is never fine.
- The README is a doorway — front-load value, link out for depth.
- When a claim has no support in the repo, flag it; do not write it.

## Reference files

- `references/repo-types.md` — detect the type from signals; the type's default format
- `references/formats.md` — the five formats (layout axis): minimal, standard, reference, tutorial, landing
- `references/house-styles.md` — per-type devices and assets; cross-type rules
- `references/voice-modes.md` — the four voices (tone axis)
- `references/anti-slop.md` — the ban/require ruleset (discipline)
- `references/fabrication.md` — the no-fabrication line (discipline)
- `references/helpers.md` — theme-aware images, badges, details, callouts, TOC
- `references/toggles.md` — contested choices and their defaults
- `references/prettify.md` — the consensus skeleton and ordering
- `references/assets.md` — scaffold/coach/verify for screenshots, GIFs, diagrams
- `references/verify-code.md` — run code samples, capture real output
- `references/check.md` — drift gate (deterministic script + model-assisted layer)
- `references/generate.md` — greenfield README + profile READMEs
- `references/output.md` — diff-and-approve output contract
