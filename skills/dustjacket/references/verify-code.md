# Verify code samples

A code example lands because its output is **true** (requests' REPL transcript, pydantic's `#>`
coercion comments). Invented output is fabrication (`references/fabrication.md`). So: don't assert
output you didn't produce.

## Procedure

1. **Source the example from the repo,** not your imagination — prefer `tests/`, `examples/`, the
   docstring, or the existing README. The closer to a real test, the better.
2. **Run it** in the repo's environment when you can:
   - Python: `python -c "..."` or run the example file (`uv run`, `python examples/x.py`).
   - Node: `node example.mjs`.
   - Shell/CLI: run the actual command and copy its real stdout.
3. **Embed the real output** as a comment or a transcript:
   ```python
   slugify("Hello, World!")   # "hello-world"   ← captured from a real run
   ```
4. **If you can't run it** (no environment, side effects, network, secrets), then either:
   - show the call **without** asserting a specific return value, or
   - mark it: `# output not verified` and flag a TODO.

   Never guess the output and present it as fact.

## What counts as "can't run"

- Needs network, credentials, a database, or a running service you can't start.
- Has side effects you shouldn't trigger (writes, sends, deletes).
- The repo doesn't install in the current environment.

In all of these, degrade to an unasserted example + TODO. A call with no output line is honest; a call
with a made-up output line is a lie.

## Red flags

- You typed an output comment without running the code.
- You "remember" what a function like this usually returns.
- You adjusted the example to match the output you expected, instead of the reverse.

## Example: real run beats assumption

`str.isalnum()` is Unicode-aware, so `slugify("Café & Crème")` returns `"café-crème"` — not the
`"caf-cr-me"` an assumption would produce. A 2-second run settles it; a guess ships a wrong example.
