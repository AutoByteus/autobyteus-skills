# Stage 10 Handoff Guide

## Purpose

Stage 10 turns engineering completion into a finished delivery record.
It separates:

- engineering completion
- user verification
- ticket archival
- repository finalization
- release / publication / deployment when applicable
- post-finalization cleanup when applicable
- Product Manager completion notification when product-iteration mode is active

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
- cleanup status
- Product Manager notification status, recipient, completion packet source/path, sent timestamp or pending/blocker reason, and next-iteration status when product-iteration mode is active

## User-Verification Hold

- After the handoff summary is written, keep Stage 10 open.
- Do not move the ticket to `done`, commit, push, merge, or run release/publication/deployment work before the user explicitly confirms completion or verification.

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
- after the ticket is archived, hand the archived `tickets/done/<ticket-name>/release-notes.md` artifact into the release/publication path when such a path is applicable

## Finalization Order For Git Repositories

After explicit user confirmation:

1. Move `tickets/in-progress/<ticket-name>/` to `tickets/done/<ticket-name>/`.
2. Commit all in-scope changes on the ticket branch, including the moved ticket files.
3. Push the ticket branch.
4. Update the resolved Stage 0 target branch from remote.
5. Merge the ticket branch into that updated target branch.
6. Push the updated target branch.

Use the Stage 0 resolved base remote and base branch as the default finalization target unless the user explicitly overrides it later.

## Release / Publication / Deployment (When Applicable)

- After repository finalization, run the project's documented release/publication/deployment method only when such a step is actually applicable.
- This may be:
  - a release script
  - a documented command
  - a git tag workflow
  - GitHub Release creation
  - another deployment or publication path
- If no such step is applicable, record `release/publication/deployment not required` in the handoff summary and do not block merge/finalization.
- If release notes are required, pass the archived `tickets/done/<ticket-name>/release-notes.md` artifact into that release/publication path when it runs.

## Post-Finalization Cleanup (When Applicable)

- If Stage 0 created or reused a dedicated ticket worktree/branch for this ticket, cleanup is part of Stage 10 completion rather than optional housekeeping.
- After repository finalization and any applicable release/publication/deployment work are complete:
  - if needed, step out to a safe parent repo checkout before removing the ticket worktree,
  - remove the dedicated ticket worktree recorded in Stage 0,
  - run worktree-prune cleanup,
  - when the local ticket branch is fully merged into the resolved finalization target and no longer needed, delete the local ticket branch.
- Do not delete remote branches unless explicit user instruction or documented project policy requires it.

## Product Manager Completion Callback (Product-Iteration Mode)

When product-iteration mode is active, Stage 10 also closes the delivery-to-product loop.

Timing:

- Prepare the completion packet only after the handoff summary can report truthful delivery status.
- Send or persist the Product Manager callback after explicit user verification and after required archival, repository finalization, applicable release/publication/deployment work, and required post-finalization cleanup are complete or have truthful blocker status.
- Do not send a Product Manager completion packet before user verification/finalization gates just to keep the loop moving.

Use `send_message_to(product_manager)` when the runtime exposes both the tool and the `product_manager` recipient:

- set recipient to exactly `product_manager`
- make the message self-contained
- include relevant artifact paths as references
- request that Product Manager propose the next feature and route it back through Engineering Intake / Stage 0

Completion packet fields:

- ticket name
- delivered scope
- verification summary
- docs sync result
- release/publication/deployment/finalization state
- residual risks or deferred items
- relevant artifact paths
- product implications or follow-up context
- explicit request for Product Manager to propose the next feature

Fallback when messaging is unavailable:

- persist the completion packet source/path in `handoff-summary.md`
- update `workflow-state.md` Product Iteration Record
- record status as `Pending` when the packet is ready but cannot be sent now
- record status as `Blocked` when a concrete blocker prevents a usable packet or route
- never mark the Product Manager callback as `Sent` unless `send_message_to(product_manager)` succeeds

Ownership:

- Delivery/Deployment Engineer owns packet emission and truthful status.
- Product Manager owns the next-feature proposal.
- The next feature must route through Engineering Intake / Stage 0 and must not bypass code-edit locks, validation, review, docs sync, explicit user verification, finalization, release/publication/deployment, or cleanup rules.

## Blockers

If any move, commit, push, or merge step fails:

- record the blocker in `workflow-state.md`
- keep Stage 10 open
- do not mark the workflow complete until the blocker is resolved

If an applicable release/publication/deployment step fails or is undocumented:

- record that blocker in `workflow-state.md`
- keep Stage 10 open
- do not undo completed repository finalization

If required worktree/branch cleanup fails:

- record that blocker in `workflow-state.md`
- keep Stage 10 open
- do not treat the ticket as fully done until cleanup is complete

If Product Manager notification cannot be sent in product-iteration mode:

- persist the completion packet path/status in `handoff-summary.md` and `workflow-state.md`
- keep callback status `Pending` or `Blocked`
- do not report the product loop callback as successful

## Exit Gate

This stage is complete only when explicit user verification is received, all required archival/repository-finalization work is complete, any applicable release/publication/deployment work is complete or explicitly recorded as not required, required post-finalization cleanup is complete when applicable, and Product Manager notification status is recorded when product-iteration mode is active.
