# README research — exemplars & extracted rules

Reference for the README skill. Every example below was fetched verbatim (raw GitHub source, HTML
intact) and analyzed, except the meta-resources section (canonical specs, from knowledge, flagged).
Companion to `readme-skill-design.md`.

## How to read this

Five repo types, each with a distinct "house style." For each: the exemplars, the signature device
worth stealing, the voice, and the one rule that defines the genre. The cross-type rules at the end
are what every README shares.

---

## 1. CLI / terminal tools

**Exemplars (archetypes):** bat (centered-HTML showcase) · starship (product-grade marketing) ·
gum (GIF-per-command) · ripgrep (anti-marketing engineering doc) · fzf (reference manual).

**Opening formula:** centered `<p align="center">` block — logo image (often *replacing* the H1;
bat/starship/fzf have no `#` title), then badge trio, then one-line tagline, then `•`/`·` anchor nav.
ripgrep is the deliberate counter-example: Setext title + descriptive paragraph *before* badges, no
HTML — and it works because the prose is the credential. The muddy middle (cli/cli: bare title + one
screenshot + link-outs) is the least distinctive.

**Signature devices:**
- Proof *in the terminal*: static screenshots (bat), right-floated demo GIF (starship), GIF-per-command
  via VHS (gum), benchmark tables (ripgrep), token/option tables (fzf). The medium signals maturity.
- `<details>` per-OS/per-shell to collapse combinatorial install matrices — *the* CLI-specific pattern.
- GitHub alert callouts (`> [!NOTE]`/`[!TIP]`/`[!WARNING]`) everywhere.
- Tables that teach *behavior*, not just install (fzf's search-syntax tokens, ripgrep's benchmarks).
- Honesty as credibility: ripgrep's "Why shouldn't I use ripgrep?", got-style "use X instead."

**Voice:** documentation/manual register; the README often *is* the man page. Recipes over features
(composable one-liners). Marketing adjectives absent except starship (the one product-positioned tool).

**Emoji:** splits cleanly — zero/near-zero (ripgrep, bat, fzf) = engineering credibility; systematic
heading emoji (starship 🚀🤝💭❤️🔒📝) = product/community. Sprinkled-through-prose appears nowhere.

**Defining rule:** prove it in the terminal (GIF/benchmark/recipe), and collapse the install sprawl.

---

## 2. Library / SDK / package

**Exemplars:** zod · requests · pydantic · got · typer.

**Opening formula:** identity strip then get out of the way — plain H1 + tagline (requests, pydantic)
or centered logo + tagline (zod, typer, got), one badge row (version/install/CI), done.

**Signature devices:**
- **Code is the hero and it comes FAST** — requests shows code at line ~11, zod ~49. This is the
  defining axis of the genre.
- Code that *demonstrates the payoff inline*, not just calls the API: requests' REPL transcript with
  real return values; pydantic's `#>` comments showing dirty-input → coerced-output; zod's "you'll get
  back a strongly typed result."
- One framing sentence before the block, so code reads as proof, not puzzle.
- Number-bearing feature bullets (zod `2kb core`, `zero dependencies`; typer `1 import, 1 function call`).
- Comparison tables only when positioning against rivals (got vs axios/node-fetch/ky).
- Analogy positioning (typer: "the FastAPI of CLIs").

**Voice:** declarative, confident, occasionally honest to a fault (got steers you to Ky). No throat-
clearing. Almost no visuals — there's nothing to screenshot; `<details>` appears in none of the five.

**The README is a doorway, not the manual** — every one points hard to external docs and hands off
after your first working line.

**Defining rule:** get the reader to runnable code within one screenful, framed by exactly one sentence.

---

## 3. Framework

**Exemplars:** Astro · Svelte (minimalist boundary case) · (Next.js sits between framework and product).

**Opening formula:** banner image + centered tagline + badge cluster. The banner is the brand mark
(Astro has no logo image; the banner *is* it).

**Signature devices:**
- **Monorepo directory table with inline per-package version badges** (Astro) — turns the package list
  into a live, self-updating release dashboard, zero maintenance.
- Theme-aware `<picture>` header (Svelte borrows exactly this one device and nothing else — proof it
  scales down).
- Docs/community/sponsors sections.

**Voice:** marketing-flavored but warm and restrained ("New contributors welcome!").

**Defining rule:** make breadth (the package ecosystem) scannable and self-updating via tables/badges.

---

## 4. Product / app

**Exemplars:** Excalidraw · Supabase · Appwrite · Next.js (brand-disciplined header).

**Opening formula:** the header is a *hero, not a title* — image (banner/logo) stands in for the H1,
followed by a centered nav row and a curated badge cluster.

**Signature devices:**
- **Theme-aware images** (`<picture>` or `#gh-light-mode-only`) — the single highest-leverage,
  most-stolen device; what makes a header look designed, degrades gracefully.
- Product screenshot (Excalidraw `<figure>`+caption, Supabase dashboard, Appwrite 1920×1080 hero),
  occasional GIF framed in `<kbd>`.
- Curated badge clusters with *unified* styling (Next.js all `for-the-badge` + `labelColor=000`;
  Appwrite all `flat-square`) — coherence over count.
- Tables doing structural marketing: Supabase's client-library capability matrix, Appwrite's one-click
  provider-logo grid.
- The inverted badge: Supabase gives visitors a copy-paste "Made with Supabase" badge so downstream
  repos become backlinks.
- Community/commerce: sponsor avatar walls, "Follow Us" rows, language switchers.

**Voice:** marketing intro + technical body. Sells philosophy (Supabase) or benefit (starship-like).

**Emoji:** sparse and structural — leading bullet icons, table dividers, SDK checkmarks, one sponsor
CTA. Next.js/Svelte use zero. None sprinkle through prose.

**Defining rule:** front-load a theme-aware visual hero + product screenshot + community surface. This
maximalism signals "polished thing you can adopt today" — and would bury the API on a library.

---

## 5. Content / awesome / educational (the README *is* the product)

**Exemplars:** public-apis · coding-interview-university · system-design-primer · sindresorhus/awesome ·
project-based-learning.

**The defining problem is navigation across hundreds-to-thousands of lines.**

**Signature devices:**
- **TOC is non-negotiable**, nesting depth tracks content depth (flat → 3-level). Always before body.
- **Back-to-top links**, and their density signals length: public-apis has **51** `**[⬆ Back to
  Index](#index)**`, CIU has **33**. Rule: if a reader can scroll past one screen without a return
  path, add one after every section. (system-design-primer/awesome have zero — they keep sections short
  or delegate depth instead.)
- **Parallel fixed-shape entries**: `[Name](url) - terse description.` on every line, or a fixed-column
  table (public-apis: `API | Description | Auth | HTTPS | CORS`) so you scan a column, not prose.
- **Collapse and delegate**: `<details><summary>Translations:</summary>` (CIU) hides noisy metadata;
  awesome links out to sub-repos rather than inlining.
- Nest multi-part series under an unlinked parent label so a 10-link series reads as one item.

**Voice:** either near-absent (structure is the voice) or a short human hook (CIU's first-person
testimonial blockquote). Never middling throat-clearing between title and TOC.

**Emoji:** austere despite the genre's reputation — the only recurring one is the `⬆` back-to-top arrow.
No category-marker legend in any of the five. Restraint reads as authoritative here.

**Defining rule:** the faster the reader reaches a TOC, and the more consistent every entry's shape,
the better.

---

## 6. Meta-resources — the canonical rulebook (from knowledge, not fetched)

**Sources:** standard-readme (the spec, MUST/SHOULD) · art-of-readme (the philosophy) · makeareadme.com
· Best-README-Template · matiassingers/awesome-readme · GitHub docs.

**Consensus skeleton (always-on spine):** title → one-line description → longer description → install →
usage → contributing → license. The only two truly non-negotiable elements: a one-line description and
a license.

**Contested choices (→ skill toggles):**
| Choice | Range of opinion |
|---|---|
| TOC | standard-readme REQUIRES once >2 H2s; GitHub auto-generates one (often redundant); others silent |
| Badges | Best-Template maximalist → art-of-readme skeptical → makeareadme "maintenance burden" |
| Usage vs. install order | art-of-readme: usage FIRST (show value); everyone else: install first |
| Length | art-of-readme/makeareadme: brevity, link out → Best-Template: comprehensive scaffold |
| Emoji | nobody takes a strong stance — folklore, not spec |
| Visuals | makeareadme/Best-Template: yes → standard-readme: optional banner only |

**Two firmest normative anchors:** build *structure/order* from standard-readme; build *tone/audience*
from art-of-readme ("your README is its sales pitch"; "optimize for the newcomer"; "brevity is a
feature").

---

## Cross-type rules (true everywhere)

1. **One real one-line description, immediately under the title.** Universal, mandatory.
2. **A License section.** The single most-agreed-upon mandatory section.
3. **Show, don't tell** — but the proof medium is type-specific: code (library), terminal GIF/benchmark
   (CLI), screenshot (product), table (content/framework).
4. **The README is a doorway** — front-load value, link out for depth. Brevity is a feature.
5. **Emoji are structural or absent, never decorative prose.** Both zero-emoji and systematic-heading-
   emoji are proven; sprinkled-through-prose appears in zero great READMEs.
6. **Badges cluster and unify** — a curated set with coherent styling, never a scattered wall.
7. **Theme-aware images** (`<picture>` / light-dark) are the highest-leverage polish device when visuals
   apply at all.
8. **Write for the newcomer deciding whether to use this**, not for yourself.
