# Stage 10 Handoff Guide

## Purpose

Stage 10 turns engineering completion into a finished delivery record.
It separates:

- engineering completion
- user verification for one-off runs
- Product Manager acceptance for product-iteration runs
- ticket archival
- repository finalization
- release / publication / deployment when applicable
- post-finalization cleanup when applicable
- Product Manager acceptance callback when product-iteration mode is active

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
- Product Manager acceptance callback status, recipient, acceptance packet source/path, sent timestamp or pending/blocker reason, acceptance status, and next-iteration status when product-iteration mode is active

## Verification / Acceptance Hold

- Product-iteration override: when product-iteration mode is active, do not ask the user for routine verification. Send the Product Manager acceptance packet and treat Product Manager's response as the verification/acceptance path.
- After the handoff summary is written, keep Stage 10 open until the applicable verification path is satisfied.
- For normal one-off engineering runs, wait for explicit user completion or verification.
- For product-iteration runs, do not ask the user for routine verification; send the Product Manager acceptance packet and treat Product Manager acceptance as the product-loop verification signal.
- Do not move the ticket to `done`, commit, push, merge, or run release/publication/deployment work before the applicable verification signal unless the project explicitly documents a safe pre-verification checkpoint.

## Ticket Archival

- Stage 10 owns the move from `tickets/in-progress/<ticket-name>/` to `tickets/done/<ticket-name>/`.
- Perform that move only after the applicable verification signal or explicit user move instruction.
- Move the ticket before the final commit so the committed state contains the archived ticket path.
- If the ticket is reopened later, the next Stage 0 bootstrap should move it back to `tickets/in-progress/<ticket-name>/` before any new updates.

## Release Notes

When the ticket produces a user-facing release or GitHub Release body:

- create `tickets/in-progress/<ticket-name>/release-notes.md`
- keep notes short and user-facing
- omit internal refactors, tests, docs-only changes, and low-level implementation detail
- after the ticket is archived, hand the archived `tickets/done/<ticket-name>/release-notes.md` artifact into the release/publication path when such a path is applicable

## Finalization Order For Git Repositories

After the applicable verification signal:

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

## Product Manager Acceptance Callback (Product-Iteration Mode)

When product-iteration mode is active, including runs that started in the Product Iteration Team, Stage 10 also closes the delivery-to-product acceptance loop.

Timing:

- Prepare the acceptance packet only after the handoff summary can report truthful delivery status and verification evidence.
- Send or persist the Product Manager acceptance callback before routine user verification in product-iteration mode; Product Manager is the verification owner for the loop.
- Do not ask the user to verify every product-loop feature unless Product Manager marks the acceptance as blocked on user/product clarification or the project explicitly requires human approval for a high-risk external side effect.

Use `send_message_to(product_manager)` when the runtime exposes both the tool and the `product_manager` recipient:

- set recipient to exactly `product_manager`
- make the message self-contained
- include relevant artifact paths as references
- request that Product Manager accept the delivery or route rework, and if accepted propose the next feature and route it back through Engineering Intake / Stage 0

Acceptance packet fields:

- ticket name
- delivered scope
- source Product Feature Brief / requirements reference when available
- verification summary
- docs sync result
- release/publication/deployment/finalization state or explicit not-yet-finalized status
- residual risks or deferred items
- relevant artifact paths
- product implications or follow-up context
- explicit request for Product Manager to accept or route rework and, if accepted, propose the next feature

Fallback when messaging is unavailable:

- persist the acceptance packet source/path in `handoff-summary.md`
- update `workflow-state.md` Product Iteration Record
- record status as `Pending` when the packet is ready but cannot be sent now
- record status as `Blocked` when a concrete blocker prevents a usable packet or route
- never mark the Product Manager callback as `Sent` unless `send_message_to(product_manager)` succeeds

Ownership:

- Delivery/Deployment Engineer owns packet emission and truthful status.
- Product Manager owns product acceptance and the next-feature proposal.
- The next feature must route through Engineering Intake / Stage 0 and must not bypass code-edit locks, validation, review, docs sync, Product Manager acceptance or user verification as applicable, finalization, release/publication/deployment, or cleanup rules.

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

If Product Manager acceptance callback cannot be sent in product-iteration mode:

- persist the acceptance packet path/status in `handoff-summary.md` and `workflow-state.md`
- keep callback status `Pending` or `Blocked`
- do not report the product acceptance callback as successful

## Exit Gate

This stage is complete only when the applicable verification path is satisfied (explicit user verification for one-off runs; Product Manager acceptance request sent/persisted and acceptance status tracked for product-iteration runs), all required archival/repository-finalization work is complete, any applicable release/publication/deployment work is complete or explicitly recorded as not required, required post-finalization cleanup is complete when applicable, and Product Manager acceptance callback status is recorded when product-iteration mode is active.
