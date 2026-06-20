# Contested choices and their defaults

The canonical README sources (standard-readme, art-of-readme, makeareadme, Best-README-Template)
disagree on these. dustjacket doesn't pick a religion — it applies a researched default and lets the
user override. State the defaults you applied so the user can flip any of them.

| Choice | Default | Flip when |
|--------|---------|-----------|
| **Badges** | a small honest set: CI, version, packaging | the user wants more (community/social) — never a scattered wall |
| **Emoji** | from the chosen format (landing/tutorial = some structural; minimal/standard/reference = none) | an independent on/off override — the user can force emoji on or off regardless of format. **Never in prose**, only structural (headings, bullets, section markers). |
| **TOC** | off for short docs; **on for content** repos | the doc has many H2s and isn't on GitHub's auto-TOC, or the user asks. Note GitHub auto-generates a TOC, so a manual one is often redundant. |
| **Usage vs. install order** | install-first | "show value fast" libraries → usage-first (lead with the code example) |
| **Visuals** | on for product/CLI; off for library | a library genuinely has a visual (rare); a product without a screenshot |
| **Length** | lean — link out to docs/ | the README is the only docs (reference-manual style); then go long with a TOC |

## The format sets the bundle

The chosen format (`references/formats.md`) sets these toggles as a group — its emoji default, length
target, TOC, and device set. The rows above are individual overrides layered on top: pick a format,
then flip any single toggle. Emoji in particular is a standalone override (force on/off independent of
the format), but it is *never* in prose in any format.

## Honor explicit instructions

A user instruction always overrides a default. "Add a full badge row," "no emoji anywhere," "keep it
under 40 lines" — apply it and don't re-litigate. When you apply a non-default, note it in the summary.
