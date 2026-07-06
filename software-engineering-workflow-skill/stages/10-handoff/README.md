# Stage 10 Final Handoff

## Purpose

Persist the final delivery summary, wait for explicit user verification, archive the ticket, perform repository finalization when applicable, run any applicable release/publication/deployment step, and complete required ticket-worktree/branch cleanup.

## Enter This Stage When

- Stage 9 is complete
- engineering delivery is complete and the workflow is ready to wait for user verification

## Stage-Owned Outputs

- `tickets/in-progress/<ticket-name>/handoff-summary.md`
- `tickets/in-progress/<ticket-name>/release-notes.md` when required
- archived ticket state and repository finalization record when applicable
- release/publication/deployment record when applicable
- post-finalization worktree/branch cleanup record when applicable

## Exit Gate

Leave Stage 10 only when the user explicitly confirms completion or verification and any required move-to-done, repository finalization, applicable release/publication/deployment work, and required post-finalization cleanup are complete or explicitly recorded as not required.

## Local Files

- `handoff-guide.md`: handoff, verification-hold, and finalization rules
- `handoff-summary-template.md`: canonical handoff-summary structure
- `release-notes-template.md`: release-notes structure when applicable
