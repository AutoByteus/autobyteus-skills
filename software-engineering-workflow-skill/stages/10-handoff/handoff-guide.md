# Stage 10 Handoff Guide

## Purpose

Stage 10 turns engineering completion into a finished delivery record.
It separates:

- engineering completion
- user verification
- ticket archival
- repository finalization and release

## Inputs

- completed implementation, Stage 7, Stage 8, and Stage 9 outputs
- current `workflow-state.md`

## Canonical Artifact

- Create or update `tickets/in-progress/<ticket-name>/handoff-summary.md` as the canonical Stage 10 artifact.
- Use `handoff-summary-template.md` as the starting structure.
- After the ticket is moved to `tickets/done/<ticket-name>/`, this file should move with the ticket archive.

## Handoff Summary Requirements

Record at least:

- delivered scope versus planned scope
- verification summary
- docs updated or no-impact rationale
- release-note status

## User-Verification Hold

- After the handoff summary is written, keep Stage 10 open.
- Do not move the ticket to `done`, commit, push, merge, or release before the user explicitly confirms completion or verification.

## Ticket Archival

- Stage 10 owns the move from `tickets/in-progress/<ticket-name>/` to `tickets/done/<ticket-name>/`.
- Perform that move only after explicit user confirmation or explicit user move instruction.
- Move the ticket before the final commit so the committed state contains the archived ticket path.
- If the ticket is reopened later, the next Stage 0 bootstrap should move it back to `tickets/in-progress/<ticket-name>/` before any new updates.

## Release Notes

When the ticket produces a user-facing release or GitHub Release body:

- create `tickets/in-progress/<ticket-name>/release-notes.md`
- keep notes short and user-facing
- omit internal refactors, tests, docs-only changes, and low-level implementation detail
- after the ticket is archived, hand the archived `tickets/done/<ticket-name>/release-notes.md` artifact into the release path

## Finalization Order For Git Repositories

After explicit user confirmation:

1. Move `tickets/in-progress/<ticket-name>/` to `tickets/done/<ticket-name>/`.
2. Commit all in-scope changes on the ticket branch, including the moved ticket files.
3. Push the ticket branch.
4. Update the resolved Stage 0 target branch from remote.
5. Merge the ticket branch into that updated target branch.
6. Push the updated target branch.
7. Run the release script.

Use the Stage 0 resolved base remote and base branch as the default finalization target unless the user explicitly overrides it later.

## Blockers

If any move, commit, push, merge, or release step fails:

- record the blocker in `workflow-state.md`
- keep Stage 10 open
- do not mark the workflow complete until the blocker is resolved

## Exit Gate

This stage is complete only when explicit user verification is received and all required archival/finalization work is complete.
