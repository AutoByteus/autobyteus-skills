# Stage 10 Final Handoff

## Purpose

Persist the final delivery summary, wait for explicit user verification, archive the ticket, and perform repository finalization when applicable.

## Enter This Stage When

- Stage 9 is complete
- engineering delivery is complete and the workflow is ready to wait for user verification

## Stage-Owned Outputs

- `tickets/in-progress/<ticket-name>/handoff-summary.md`
- `tickets/in-progress/<ticket-name>/release-notes.md` when required
- archived ticket state and repository finalization record when applicable

## Exit Gate

Leave Stage 10 only when the user explicitly confirms completion or verification and any required move-to-done, git finalization, and release work are complete.

## Local Files

- `handoff-guide.md`: handoff, verification-hold, and finalization rules
- `handoff-summary-template.md`: canonical handoff-summary structure
- `release-notes-template.md`: release-notes structure when applicable
