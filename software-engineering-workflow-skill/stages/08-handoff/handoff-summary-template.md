# Handoff Summary

Use this artifact only when a durable handoff record is useful.

Write to:
- `tickets/in-progress/<ticket-name>/handoff-summary.md`

If the user later confirms the ticket is finished and asks to archive it, move this file with the ticket to:
- `tickets/done/<ticket-name>/handoff-summary.md`

## Summary Meta

- Ticket:
- Date:
- Current Status: `Delivered` / `Awaiting User Verification` / `Blocked`

## Delivery Summary

- Delivered scope:
- Planned/requested scope:
- Deferred / not delivered:
- Key ownership or architecture changes:
- Removed / decommissioned items:

## Verification Summary

- Unit / integration verification:
- Executable validation:
- Acceptance-criteria coverage:
- Infeasible or blocked validation:
- Residual risk:

## Review Summary

- Code review result:
- Findings resolved:
- Remaining findings or accepted risks:

## Documentation Sync Summary

- Docs sync artifact:
- Docs result: `Updated` / `No impact`
- Docs updated:
- Notes:

## Release Notes Status

- Release notes required: `Yes` / `No`
- Release notes artifact:
- Notes:

## Optional User-Requested Finalization

- Ticket archived to:
- Branch:
- Commit status:
- Push status:
- Merge status:
- Release/publication/deployment status:
- Branch/worktree cleanup status:
- Blockers / notes:
