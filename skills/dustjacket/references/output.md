# Output contract

How prettify delivers its result. **Never silently overwrite a README.**

## Steps

1. **Build the new README** in full, applying the workflow.
2. **Show a diff, not just the new file.** Present a unified diff of the existing README vs. the
   proposed one so the user sees exactly what changed:

   ```bash
   diff -u README.md README.dustjacket.md
   ```

   (Write the proposal to a temp path like `README.dustjacket.md` to diff against, or show the diff
   inline.) Call out, in a short list: sections reordered, lines rewritten for slop, and every `TODO`
   you inserted for a gap.
3. **Wait for approval.** Do not write `README.md` until the user approves. If they request changes,
   revise and re-show the diff.
4. **On approval, back up then write.** Copy the original to `README.bak` (or `README.md.bak`), then
   write the approved content to `README.md`. Tell the user the backup path.
5. **Remove the temp proposal file** if you created one.

## Summary to show with the diff

- **Type & voice:** detected type, chosen voice, and any non-default toggles applied.
- **Changed:** what was reordered/rewritten (brief).
- **TODOs:** each gap you flagged instead of filling (this is the honesty surface — make it visible).

## Mode boundaries

- **prettify** writes (after approval) and leaves a backup.
- **check** (planned) is read-only — it never writes, only reports.
- **generate** (planned) writes a new README where none exists; same diff-and-approve courtesy if one
  exists.

## Don't

- Don't overwrite without showing the diff first.
- Don't write without a backup.
- Don't bury the TODOs — a clean-looking diff that hides three invented-gap flags defeats the point.
