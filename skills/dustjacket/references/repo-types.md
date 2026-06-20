# Repo-type detection

Detect the type first — it decides which house style applies. Style is earned differently per type, so
a wrong guess applies the wrong template. Detection is a default, not a gate: state your guess and
confidence, and **ask the user to confirm when signals are mixed or weak.**

## Signals

Inspect the repo (manifest, entrypoints, directory layout, existing README) and match against these.

| Type | Strong signals | Tie-breakers |
|------|----------------|--------------|
| **CLI** | `bin` field in package.json; `[project.scripts]` / `console_scripts` in pyproject; `cmd/` + a CLI framework (cobra, clap, click, typer); a single installed binary; README shows terminal usage | ships a command users *run* in a shell |
| **library / SDK** | published package with an importable API and no entrypoint binary; `src/` or a package dir; exported symbols; tests exercising an API | users `import`/`require` it; the value is the API |
| **framework** | monorepo with `packages/`; a plugin/adapter ecosystem; scaffolding CLI plus libraries; many sub-packages versioned together | users *build on top of* it; breadth of packages |
| **product / app** | Dockerfile + a frontend (`app/`, `web/`, framework config); a hosted/deployed offering; env config for a running service; screenshots in the README | users *run or sign up for* a UI |
| **content / awesome** | README/markdown is the deliverable; `awesome-*` name; mostly curated lists or tutorials; little or no executable code | the README *is* the product |
| **plugin / skill** | `.claude-plugin/plugin.json`; `skills/*/SKILL.md`, `commands/*.md`, or `agents/*.md`; no binary, no frontend; distributed via a marketplace | an AI-agent plugin users install, not import or run |
| **profile** | repo name equals the owner's username (`username/username`); README renders on the GitHub profile; little or no project code | it's a *person*, not a project |

## Procedure

1. Gather signals: read the package manifest, list the top-level directories, check for a binary
   entrypoint, a frontend, a Dockerfile, and the shape of the existing README.
2. Score each type. Pick the strongest. Note the runner-up if it's close.
3. **Report:** "Detected **<type>** (confidence: high/medium/low) because <signals>. Runner-up: <type>."
4. If confidence is low or two types tie, ask the user to confirm before continuing. A single yes/no
   beats restyling against the wrong template.

## Mixed cases

- **Library that ships a CLI** (e.g., typer) — treat as the one whose README the user cares about. Show
  both a code example *and* a run example; default to library style if the API is the headline.
- **Framework vs product** — if there's a hosted product *and* an open package set, ask which README
  this is (the product landing README differs from the framework package README).
- **Profile README** (`username/username`) — its own type; it's a personal page, not a project, so it
  has no install/usage/license skeleton. Handle it with the profile flow in `references/generate.md`.
