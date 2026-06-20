# The anti-slop ruleset

The default AI README voice is recognizable: empty adjectives, filler verbs, throat-clearing, emoji on
every bullet. This ruleset strips it. **Apply it to every line, in every mode and every voice** — even
`product` voice obeys the bans; it just allows a hero line and a benefit list.

**Violating the letter of these rules is violating the spirit.** "It reads better with a little
flourish" is the exact instinct that produces slop. The specs are the adjectives.

## Ban — rewrite or cut on sight

- **Empty self-adjectives:** comprehensive, powerful, robust, seamless, blazing-fast (unless a
  benchmark backs it), cutting-edge, elegant, beautiful (unless a screenshot does the work),
  state-of-the-art, flexible, simple/easy (show it instead).
- **Filler verbs:** leverage, utilize, facilitate, empower, unlock, supercharge, delve, dive into,
  streamline. Use plain verbs (use, let, add, run).
- **Throat-clearing:** "In today's fast-paced world," "Whether you're a beginner or a pro," "Look no
  further," "is a tool that," "In conclusion," "Simply put."
- **Decoration:** bold on every other phrase; emoji on every bullet; emoji anywhere in prose.
- **Vague quantifiers:** various, several, a number of, many, a wide range of. Replace with a count or cut.
- **Hype rhythm:** the relentless triad ("fast, simple, and powerful").
- **Em-dash overuse:** em-dashes are a recognized AI tell. At most **one per paragraph**, and **never
  two on one line** (a double aside). Reach for a period or colon instead. `scripts/dustjacket_check.py`
  flags the two-on-a-line case deterministically; the one-per-paragraph cap is your judgment at rewrite
  time.

## Require

- A real **one-line description** under the title — what it does, concretely.
- A **License** section.
- **Numbers, names, or versions** on claims, or cut the claim. "3 adapters," not "several adapters."
- **Alt text** on every image; **descriptive link text** (never "click here").
- **Real, runnable code** — not pseudocode. (Verifying output is M2; for now, keep examples real.)

## Rewrite examples

| Slop | Clean |
|------|-------|
| "A powerful, comprehensive library for seamlessly handling HTTP requests." | "An HTTP client for Python. 2 dependencies." |
| "Simply leverage our intuitive API to supercharge your workflow." | "Call `client.get(url)`. It returns a typed response." |
| "Supports a wide range of various platforms." | "Runs on macOS, Linux, and Windows." |
| "🚀 Blazing fast! ⚡ Super simple! 🎉 Powerful!" | "Parses 1M rows/sec (see benchmarks)." |

## Red flags — STOP, you're writing slop

- You reached for an adjective instead of a number.
- You wrote "is a tool that" or "is a library that."
- Every bullet starts with an emoji.
- You're describing how it *feels* (powerful, elegant) instead of what it *does*.
- You're padding to fill a section that has no real content (→ flag it as a TODO instead; see
  `references/fabrication.md`).

## Rationalizations and the reality

| Excuse | Reality |
|--------|---------|
| "Marketing voice needs the adjectives" | `product` voice sells with specifics and a hero line, not with "powerful." |
| "It sounds flat without flourish" | Flat and true beats lively and empty. Readers skim for facts. |
| "The user will expect a polished tone" | Polished = precise, not decorated. The exemplars prove it. |
| "One emoji per bullet looks friendly" | The great READMEs use zero or structural emoji; none sprinkle prose. |
| "I don't have a number, so the adjective stays" | No number means no claim. Cut it or find the number in the repo. |
