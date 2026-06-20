# Generate mode

Build a README where none exists (or only a stub). Same rules as prettify — detect the type, apply the
house style and voice, obey the anti-slop ruleset, and **never invent** (`references/fabrication.md`).
The difference: there's little existing prose to preserve, so you derive from repo signals and
interview the user for the rest.

## Procedure

1. **Detect the type** (`references/repo-types.md`).
2. **Choose the format** — default from the repo type, honor an explicit user request, state the choice
   (`references/formats.md`). Then **pick a voice** (the format's default, or the user's;
   `references/voice-modes.md`).
3. **Gather real signals:**
   - Manifest: name, version, description, license, entry points, dependencies.
   - Code: the public API / commands / exported symbols; `examples/` and `tests/` for real usage.
   - Files: LICENSE, CI workflows (for badges), existing docs, `.env.example` for config.
4. **Lay down the chosen format's section ordering** (`references/formats.md`), using the type's devices
   (`references/house-styles.md`), and fill each slot from signals.
5. **Pull a usage example from real code** and verify its output (`references/verify-code.md`).
6. **Interview for genuine gaps** — ask the user the few things the repo can't tell you (the one-line
   pitch, the intended audience, the roadmap). Keep it to 2–4 questions; don't interrogate.
7. **TODO whatever remains** — a slot with no signal and no answer becomes a flagged TODO, never filler.
8. **Output:** write the new README. If one already exists (a stub), use the diff-and-approve contract
   (`references/output.md`); for a truly absent README, write it and summarize what you flagged.

## Interview, don't invent

The line is the same as everywhere: when you don't know, **ask or flag** — never guess in the reader's
favor. A generated README full of confident, unverified claims is the failure this skill exists to
prevent. Prefer a shorter true README with three TODOs over a complete-looking fiction.

## Profile READMEs (`username/username`)

A personal profile README is its own type — there's no codebase to derive from, so it's almost entirely
interview-driven.

- **Structure:** a short intro (who you are, what you work on) → current focus → selected projects →
  how to reach you. No install/usage/license skeleton — it's not a project.
- **Source every fact from the user.** Never invent a job title, employer, location, project, or social
  handle. Ask for them; TODO what's unanswered.
- **Voice:** default `friendly-OSS` or `technical-writer`; honor the person's preference.
- Keep it lean — a profile README is a greeting, not a résumé dump.
