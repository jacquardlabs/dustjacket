# Product context

## Why this product exists

Most READMEs are one of two failures: generic AI boilerplate (the "comprehensive, powerful, robust"
slop) or an afterthought that never explains what the thing does. Meanwhile, *great* READMEs follow
type-specific house styles — a library leads with runnable code in the first screenful, a product
leads with a theme-aware hero image, a content repo leads with navigation. dustjacket restyles,
generates, and drift-checks a repo's README to match how great READMEs in its category actually read —
without fabricating anything.

Origin: a verbatim analysis of exemplar READMEs across five repo types (CLI, library, framework,
product, content) plus the canonical meta-resources (standard-readme, art-of-readme, makeareadme). The
extracted rules live in [docs/research.md](docs/research.md); the skill design in
[docs/design.md](docs/design.md).

## Who uses it

### Primary persona — the maintainer with a weak README

A developer with a working repo and a bad README. They don't want to write marketing copy or learn
README conventions; they want their README to look professional and read well in minutes. Frustrations:
AI-generated slop that all sounds the same, and their own boilerplate that buries what the project does.
Success looks like a README that matches the strong examples in their category, produced fast, that
they trust isn't lying about features or commands.

### Secondary persona — the team preventing doc drift

A team whose README goes stale as the code changes — install commands that no longer work, documented
flags that were removed. They want a CI gate that fails when the README no longer matches reality.

## Product principles

- **Never fabricate** — restyle what exists and flag gaps as TODOs; never invent features, benchmarks,
  or commands. This is the trust boundary that separates prettify from slop.
- **House style by repo type** — one size fits none. Detect the type, apply its skeleton and devices.
- **Strip the AI tells** — the anti-slop ruleset is the cross-cutting quality bar in every mode and
  voice.
- **Scaffold the scriptable, coach the visual, verify the runnable** — for assets the skill can't
  honestly generate (screenshots, GIFs), write the scaffold or the checklist; for code, run it and
  capture real output.
- **The README is a doorway** — front-load value, link out for depth; brevity is a feature.

## Feature tracker

Issue tracker: [GitHub Issues](https://github.com/jacquardlabs/dustjacket/issues) ·
[Milestones](https://github.com/jacquardlabs/dustjacket/milestones)

PRODUCT.md owns strategic context; the tracker owns individual features (22 issues across 5 milestones,
M0 → M4).

## Critical user journeys

- **Prettify** (v1): run on an existing README > skill detects repo type and picks a voice > restyles
  to the house style, strips slop, flags gaps as TODOs > shows a diff > user approves > written with a
  backup.
- **Check / drift gate**: CI runs check mode > deterministic checks (links, TOC, metadata, install
  command) then model-assisted checks (removed flags/API) > severity-ranked report > non-zero exit on
  error-level findings.
- **Generate**: empty/stub repo > skill derives what's knowable from repo signals and interviews for
  the rest > produces a type-appropriate README skeleton with TODOs for genuine gaps.

## What we're NOT building

- **No hosted service** — it's a Claude Code skill, run locally.
- **No general docs-site or multi-file docs generator** — README scope only.
- **No translation / i18n management** — out of scope for v1.
- **No voice-suite dependency** — voice modes are self-contained and portable, by decision.
- **Not all-at-once** — generate and check are layered after prettify, not bundled into v1.

## Current known problems

Pre-implementation; nothing has shipped. The two hardest open risks:

- **Enforcing the no-fabrication line reliably** — needs adversarial tests that bait the skill into
  inventing facts (tracked in #8).
- **Repo-type detection accuracy** — a wrong type applies the wrong house style; detection is a default
  that must fall back to asking (tracked in #2).

## Business model

Open-source Claude Code skill, MIT-licensed, distributed free as part of the jacquardlabs skill
ecosystem. No direct monetization.
