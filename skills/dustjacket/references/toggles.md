# Contested choices and their defaults

The canonical README sources (standard-readme, art-of-readme, makeareadme, Best-README-Template)
disagree on these. dustjacket doesn't pick a religion — it applies a researched default and lets the
user override. State the defaults you applied so the user can flip any of them.

| Choice | Default | Flip when |
|--------|---------|-----------|
| **Badges** | a small honest set: CI, version, packaging | the user wants more (community/social) — never a scattered wall |
| **Emoji** | off | the user wants them, or the type's style uses systematic heading emoji (e.g. CLI). Never in prose. |
| **TOC** | off for short docs; **on for content** repos | the doc has many H2s and isn't on GitHub's auto-TOC, or the user asks. Note GitHub auto-generates a TOC, so a manual one is often redundant. |
| **Usage vs. install order** | install-first | "show value fast" libraries → usage-first (lead with the code example) |
| **Visuals** | on for product/CLI; off for library | a library genuinely has a visual (rare); a product without a screenshot |
| **Length** | lean — link out to docs/ | the README is the only docs (reference-manual style); then go long with a TOC |

## Defaults are per-type, not global

The table's defaults already account for type via `references/house-styles.md` (e.g. emoji-off globally
but CLI may use heading emoji; visuals on for product, off for library). When type and the table
conflict, the type's house style wins for *which devices apply*; the toggle controls *how much*.

## Honor explicit instructions

A user instruction always overrides a default. "Add a full badge row," "no emoji anywhere," "keep it
under 40 lines" — apply it and don't re-litigate. When you apply a non-default, note it in the summary.
