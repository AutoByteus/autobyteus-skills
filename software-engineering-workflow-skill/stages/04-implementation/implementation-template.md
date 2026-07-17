# Implementation

Use this artifact for the implementation stage.

Write to:
- `tickets/in-progress/<ticket-name>/implementation.md`

Keep this document concise.

## Inputs

- Investigation notes:
- Requirements:
- Design sketch or proposed design:
- Relevant project instructions:

## Solution Sketch

- Current behavior:
- Target behavior:
- Owning boundary/files:
- API or interface changes:
- Data/storage/schema changes:
- Rendered frontend affected (`Yes`/`No`):
- File placement decision:
- Obsolete code to remove:
- Risks/open questions:

## Implementation Plan

| Task ID | File/Area | Action (`Add`/`Modify`/`Move`/`Remove`) | Owner/Concern | Depends On | Status (`Planned`/`In Progress`/`Done`/`Blocked`) | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| T-001 |  |  |  |  | Planned |  |

## Guardrails

- Follow existing project patterns.
- Keep changes scoped to the requested behavior.
- Preserve ownership boundaries and clear dependency direction.
- Do not add compatibility wrappers, dual-path behavior, or legacy retention unless the user explicitly rejects the no-legacy policy.
- Remove obsolete code, flags, tests, adapters, or helpers in scope.
- Keep file names and folder placement aligned with the owning concern.
- Watch changed source-file size:
  - effective non-empty line count command: `rg -n "\\S" <file-path> | wc -l`
  - changed-line delta command: `git diff --numstat <base-ref>...HEAD -- <file-path>`
  - if a changed source file exceeds `500` effective non-empty lines or a single-file diff exceeds `220` changed lines, consider split/refactor/escalation.

## Test Strategy

- Unit tests:
- Integration tests:
- Frontend rendered-result self-check:
- Stage 05 executable-validation handoff/readiness:
- Manual or human-assisted checks, if unavoidable:
- Known validation constraints:

## Frontend Rendered-Result Check

Use this section when the change affects a rendered frontend or user interaction. If not applicable, write `Not Applicable` with a short reason.

- Affected surfaces/journeys:
- Approved UI/UX, interaction, requirement, or design references:
- Design system, shared components, and adjacent product surfaces reviewed:
- Development or preview surface used:
- States, layouts, viewports, and interactions inspected:
- Visual or interaction issues found and corrected:
- Supporting evidence, screenshots if useful, and remaining unverified states or limitations:

This is implementation self-validation and polish. It does not replace Stage 05 executable validation.

## Execution Log

| Time/Date | Update | Evidence/Command | Result | Follow-Up |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Validation Summary

- Unit/integration result:
- Frontend rendered-result check:
- Stage 05 executable-validation readiness:
- Acceptance criteria covered:
- Blocked or waived validation:

## Review Prep

- Changed source files:
- Changed tests:
- Related files reviewed:
- Known risks for code review:
- Docs impact:

## Completion Check

- Implementation complete:
- Required tests pass:
- Frontend rendered-result check complete or not applicable:
- No obsolete code left in scope:
- File placement remains coherent:
- Validation evidence is sufficient:
- Ready for code review:
