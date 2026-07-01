# Handoff Summary

Use this template for:
- `tickets/in-progress/<ticket-name>/handoff-summary.md`

After applicable verification/acceptance and ticket archival, this file normally moves with the ticket to:
- `tickets/done/<ticket-name>/handoff-summary.md`

## Summary Meta

- Ticket:
- Date:
- Current Status: `Awaiting User Verification` / `Awaiting Product Manager Acceptance` / `Verified` / `Product Manager Accepted` / `Needs Rework` / `Blocked`
- Workflow State Source:

## Delivery Summary

- Delivered scope:
- Planned scope reference:
- Deferred / not delivered:
- Key architectural or ownership changes:
- Removed / decommissioned items:

## Verification Summary

- Unit / integration verification:
- API / E2E verification:
- Acceptance-criteria closure summary:
- Infeasible criteria / user waivers (if any):
- Residual risk:

## Documentation Sync Summary

- Docs sync artifact:
- Docs result: `Updated` / `No impact`
- Docs updated:
- Notes:

## Release Notes Status

- Release notes required: `Yes` / `No`
- Release notes artifact:
- Notes:

## Verification / Acceptance Hold

- Verification owner: `User` / `Product Manager`
- Waiting for explicit user verification: `Yes` / `No` / `N/A - Product Manager acceptance`
- User verification received:
- Product Manager acceptance status: `N/A` / `Requested` / `Accepted` / `Needs Rework` / `Blocked` (`Requested` is pre-decision only; only `Accepted` unlocks product-iteration ticket archival/finalization)
- Verification / acceptance reference:
- Notes:

## Product Manager Iteration Acceptance Callback

- Product iteration mode: `Inactive` / `Active`
- Product Iteration Loop Status: `Inactive` / `Active` / `Paused` / `Blocked` / `Stopped`
- Product Manager recipient: `product_manager` / `N/A`
- Acceptance callback status: `Not Required` / `Not Started` / `Sent` / `Pending` / `Blocked`
- Acceptance packet source / payload path:
- `send_message_to(product_manager)` sent timestamp:
- Pending / blocker reason:
- Required packet fields confirmed (`ticket name`, `delivered scope`, `source brief/requirements reference`, `verification summary`, `docs sync result`, `release/publication/deployment/finalization state or explicit not-yet-finalized status`, `residual risks/deferred items`, `relevant artifact paths`, `product implications/follow-up context`, `request for Product Manager acceptance and next feature if accepted`): `Yes` / `No`
- Relevant artifact paths:
- Product Manager acceptance status: `N/A` / `Requested` / `Accepted` / `Needs Rework` / `Blocked` (`Requested` is pre-decision only; only `Accepted` unlocks product-iteration ticket archival/finalization)
- Product implications / follow-up context:
- Next iteration status: `N/A` / `Proposal Sent` / `Pending` / `Blocked`
- Next Product Feature Brief path / message reference:
- Notes:

## Finalization Record

- Ticket archived to:
- Ticket worktree path:
- Ticket branch:
- Finalization target remote:
- Finalization target branch:
- Commit status:
- Push status:
- Merge status:
- Release/publication/deployment status:
- Worktree cleanup status:
- Local branch cleanup status:
- Blockers / notes:
