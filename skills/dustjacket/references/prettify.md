# Prettify: skeleton and ordering

How to restructure an existing README. The goal is the right *shape* — the type's house style laid over
a consensus spine — while preserving every real claim (`references/fabrication.md`).

## The consensus skeleton (always-on spine)

Every README, regardless of type, is built on this order:

1. **Title** (single H1, or an image standing in for it per the type's house style)
2. **One-line description** (mandatory)
3. **Longer description / what & why**
4. **Install**
5. **Usage / examples**
6. **(type-specific sections)** — API, configuration, features, deploy, etc.
7. **Contributing**
8. **License** (mandatory)

Then overlay the type's ordering and devices from `references/house-styles.md`. Examples:
- **library** → move a real code example to right after the description (usage-forward), add API.
- **CLI** → feature tour with proof (screenshot/GIF/benchmark) before install; collapse install in
  `<details>`.
- **product** → hero header, screenshot, community sections.
- **content** → TOC right after the intro; back-to-top links; consistent entry shape.

## Procedure

1. **Map the existing README.** List its current sections and every real claim, command, link, and code
   block. This inventory is what you're allowed to keep.
2. **Map to the skeleton.** Place each real piece into the right skeleton slot. Merge duplicates. Drop
   pure filler (a "Features" section that's all empty adjectives → fold real items into a tight list).
3. **Reorder to the house style.** Apply the type's ordering and signature devices.
4. **Fill structural gaps with TODOs,** never fiction. Missing License/Install/one-liner → flag.
5. **Rewrite each line through `references/anti-slop.md`.**
6. **Apply helpers within the toggles** (`references/helpers.md`, `references/toggles.md`).

## Preserve, don't paraphrase away

- Keep exact commands, flags, file paths, and code verbatim — restyle the prose *around* them.
- Keep working links and real badges; fix only broken/duplicated ones.
- If the existing README states a fact you can't verify in the repo, keep it but flag it for the user
  rather than asserting it more strongly or deleting it silently.

## Length

Lean by default — the README is a doorway. If a section grows past a screen of reference detail and the
repo has a docs site, summarize and link out. If the README *is* the docs (reference-manual style), go
long but add a TOC.
