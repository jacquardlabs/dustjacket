# The no-fabrication line

This is the boundary that separates dustjacket from the slop it removes. **dustjacket restyles what the
repo actually supports. It never invents.**

**Violating the letter of this rule is violating the spirit.** A "reasonable-sounding" install command
you didn't verify is a fabrication. A feature you assume exists because similar projects have it is a
fabrication. A benchmark number with no source is a fabrication.

## The rule

Every claim in the output must be traceable to the repo: the code, the manifest, the existing README,
the tests, or an explicit statement from the user. If you cannot point to the source, you may not write
it as fact.

**Never invent:**
- Features or capabilities the code doesn't have
- Install or run commands you haven't confirmed against the manifest/entrypoint
- Benchmarks, metrics, percentages, or user counts
- Roadmap items, supported platforms, or integrations
- A license (if there's no LICENSE, flag it — don't pick one)
- Links, badges, or screenshot references to assets that don't exist

## What to do with a gap instead

A required section with no real source becomes a flagged TODO, left for the human:

```markdown
## License

> TODO: no LICENSE file found. Add one and state it here.
```

```markdown
## Installation

> TODO: confirm the install command — no published package or entrypoint detected.
```

Flag, don't fill. A TODO is honest; invented prose is a lie that ships.

## Restyle vs. fabricate

- **Restyle (allowed):** reword a true sentence; reorder sections; convert a prose list to a table;
  tighten a real description; move a real example up; add a real badge whose URL resolves.
- **Fabricate (forbidden):** add a feature bullet not backed by code; write a usage example for an API
  you didn't read; state "MIT licensed" without a LICENSE; claim "used by thousands" with no source.

When unsure whether something is true, **ask the user or flag it** — never guess in the reader's favor.

## Red flags — STOP, you may be fabricating

- You're writing an install command but haven't opened the manifest.
- You're adding a feature because "projects like this usually have it."
- You're stating a license without having seen a LICENSE file.
- You're writing a code example without having read the actual API.
- A section felt empty so you filled it with plausible text.

## Rationalizations and the reality

| Excuse | Reality |
|--------|---------|
| "It's almost certainly MIT" | Almost-certainly isn't certainly. Flag it; let the human confirm. |
| "Every CLI has a `--help`, I'll document it" | Document the flags you saw, not the ones you assumed. |
| "A placeholder example is better than none" | A wrong example is worse than a TODO. Flag it. |
| "The user wants it to look complete" | The user wants it to be *true*. A TODO is completeness about what's missing. |
| "I'll write it and they can fix it" | They may not. Shipped fiction is the failure mode this skill exists to prevent. |
