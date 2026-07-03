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
- API/E2E/CLI/process/lifecycle validation:
- Manual or human-assisted checks, if unavoidable:
- Known validation constraints:

## Execution Log

| Time/Date | Update | Evidence/Command | Result | Follow-Up |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Validation Summary

- Unit/integration result:
- Executable validation result:
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
- No obsolete code left in scope:
- File placement remains coherent:
- Validation evidence is sufficient:
- Ready for code review:
