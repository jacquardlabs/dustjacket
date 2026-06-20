---
description: Restyle a repository's README to its repo-type house style and a chosen voice, without fabricating anything. Optional args — a path to the README and/or a voice (technical-writer, product, friendly-OSS, reference-manual).
---

Run the dustjacket skill in **prettify** mode on this repository.

Arguments (all optional): $ARGUMENTS

- If a file path is given, prettify that README; otherwise find the repository's root README.
- If a voice is named, use it; otherwise use the repo type's default voice.

Follow the prettify workflow in the `dustjacket` skill exactly: detect the repo type, pick the voice,
inventory the real content, restructure to the house style, strip the AI tells, apply helpers within
the toggles, flag gaps as TODOs, and show a diff for approval before writing. Never fabricate.
