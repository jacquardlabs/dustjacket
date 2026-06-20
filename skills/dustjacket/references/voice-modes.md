# Voice modes

Voice is the tone register. It's orthogonal to repo type — a library can be terse or warm. These four
are **self-contained** (no external dependency). Default to `technical-writer`. Honor an explicit user
choice; otherwise use the repo type's default voice (see `references/house-styles.md`) and say which you
picked.

**Every voice obeys `references/anti-slop.md`.** Voice changes register, never the ban list. `product`
is not permission to write "powerful, seamless" — it's permission to lead with a benefit and a hero
line, stated in specifics.

| Voice | Register | Use for | Allowed | Still banned |
|-------|----------|---------|---------|--------------|
| **technical-writer** (default) | direct, specific, no hype | most repos; CLI, library | numbers, plain verbs, honest caveats | all slop |
| **product** | benefit-first, confident | product/app, framework landing | a hero line, a short benefit list, a screenshot caption | empty adjectives, hype rhythm |
| **friendly-OSS** | warm, contributor-inviting | community projects, frameworks | "new contributors welcome," a light aside | salesy hype, emoji in prose |
| **reference-manual** | exhaustive, trusts the reader | tools whose README is the docs; content repos | deep tables, long option lists, a TOC | throat-clearing, filler |

## The same project in each voice (one line)

- **technical-writer:** "An HTTP client for Python. Connection pooling, retries, and typed responses."
- **product:** "Make HTTP requests that just work — pooled, retried, and typed out of the box."
- **friendly-OSS:** "A friendly HTTP client for Python. Pooling and retries built in — PRs welcome."
- **reference-manual:** "HTTP client for Python. Supports connection pooling, automatic retries
  (configurable backoff), and typed responses. See the API table below."

All four are specific and slop-free. They differ in warmth and depth, not in honesty.

## Picking and stating the voice

1. If the user named a voice, use it.
2. Else use the repo type's default from `references/house-styles.md`.
3. Tell the user: "Using **<voice>** voice (the default for a <type> repo). Say the word to switch."
