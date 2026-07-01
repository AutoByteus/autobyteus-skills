# Stage 10 Final Handoff

## Purpose

Persist the final delivery summary, wait for the applicable verification signal, archive the ticket, perform repository finalization when applicable, run any applicable release/publication/deployment step, complete required ticket-worktree/branch cleanup, and, when product-iteration mode is active, notify or record notification status for Product Manager.

## Enter This Stage When

- Stage 9 is complete
- engineering delivery is complete and the workflow is ready for user verification or Product Manager acceptance

## Stage-Owned Outputs

- `tickets/in-progress/<ticket-name>/handoff-summary.md`
- `tickets/in-progress/<ticket-name>/release-notes.md` when required
- archived ticket state and repository finalization record when applicable
- release/publication/deployment record when applicable
- post-finalization worktree/branch cleanup record when applicable
- Acceptance Callback Status when product-iteration mode is active (`Sent`, `Pending`, or `Blocked`) with recipient, packet source/path, Product Iteration Loop Status, and next-iteration status, recorded separately from Product Manager Acceptance Status (`Requested`, `Accepted`, `Needs Rework`, or `Blocked`)

## Product-Iteration Verification Override

When product-iteration mode is active, do not wait for routine user verification. Send or persist the Product Manager acceptance packet, track Acceptance Callback Status separately, and wait for Product Manager Acceptance Status = `Accepted` before ticket archival/finalization. User verification is only required if Product Manager blocks on a user/product decision, an external side effect requires explicit user approval, or the user explicitly requested manual verification.

## Exit Gate

Leave Stage 10 only when the applicable verification signal is satisfied (explicit user verification for one-off runs; Product Manager Acceptance Status = `Accepted` for product-iteration runs), any required move-to-done, repository finalization, applicable release/publication/deployment work, and required post-finalization cleanup are complete or explicitly recorded as not required, and Acceptance Callback Status is recorded when product-iteration mode is active. Callback `Sent` / `Pending` / `Blocked` or persisted packet status alone does not satisfy Product Manager acceptance.

If `send_message_to(product_manager)` is unavailable, persist the acceptance packet path/status and record Acceptance Callback Status `Pending` or `Blocked`; do not mark the callback as `Sent`.

## Local Files

- `handoff-guide.md`: handoff, verification-hold, and finalization rules
- `handoff-summary-template.md`: canonical handoff-summary structure
- `release-notes-template.md`: release-notes structure when applicable
