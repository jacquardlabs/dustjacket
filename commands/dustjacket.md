---
description: Restyle a repository's README to a chosen format and voice, without fabricating anything. Optional args — a path to the README, a format (minimal, standard, reference, tutorial, landing), and/or a voice (technical-writer, product, friendly-OSS, reference-manual).
---

Run the dustjacket skill in **prettify** mode on this repository.

Arguments (all optional, matched by keyword in any order): $ARGUMENTS

- If a file path is given, prettify that README; otherwise find the repository's root README.
- If a format is named, use it; otherwise use the repo type's default format (`references/repo-types.md`).
- If a voice is named, use it; otherwise use the format's default voice.

Precedence everywhere: an explicit user choice overrides the default. Follow the prettify workflow in
the `dustjacket` skill exactly: detect the repo type, choose the format, pick the voice, inventory the
real content, restructure to the format, strip the AI tells, apply helpers within the toggles, flag gaps
as TODOs, and show a diff for approval before writing. Never fabricate.
