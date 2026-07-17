# Handoff Summary

Use this artifact for the handoff stage.

Write to:
- `tickets/in-progress/<ticket-name>/handoff-summary.md`

If the user later asks to archive the ticket, move this file only to the user-requested archive location.

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

## Latest Base / Finalization Readiness

Use this section when the user explicitly asks for repository finalization, release, publication, or deployment. Otherwise write `Not Applicable` with a short reason.

- Requested finalization/deployment action:
- Bootstrap base branch / tracked remote base:
- Latest tracked remote base reference checked:
- Base advanced beyond current ticket branch integration point: `Yes` / `No` / `Unknown`
- Integration method: `Merge` / `Rebase` / `Already current` / `Not run`
- New base commits integrated into ticket branch: `Yes` / `No`
- Post-integration executable check or smoke path:
- Post-integration result: `Passed` / `Blocked` / `Not required`
- Handoff/docs/release notes updated after integration: `Yes` / `No` / `Not needed`
- Renewed user verification required: `Yes` / `No`
- Blocker or residual risk:

## User-Requested Follow-Up

- Requested action:
- Status:
- Notes:
