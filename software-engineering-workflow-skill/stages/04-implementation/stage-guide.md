# Implementation Guide

## Purpose

Make the code change while preserving repository patterns, ownership boundaries, validation intent, and cleanup quality.

## Inputs

- requirements or acceptance criteria
- investigation findings
- design sketch or proposed design, if one exists
- repository instructions and existing code patterns

## Actions

- Create or update `implementation.md` only when a durable plan/progress record helps.
- Implement foundational dependencies before dependents.
- Keep edits scoped to the requested behavior.
- Add or update unit/integration tests where they provide useful coverage.
- Remove obsolete code, tests, flags, adapters, and helpers in scope.
- Preserve ownership boundaries and file placement.
- Avoid compatibility wrappers, dual-path behavior, and legacy retention unless the user explicitly requests that policy.
- Watch changed source-file size:
  - effective non-empty line count: `rg -n "\\S" <file-path> | wc -l`
  - changed-line delta: `git diff --numstat <base-ref>...HEAD -- <file-path>`

## Outputs

- source and test changes
- unit/integration verification evidence
- optional `tickets/in-progress/<ticket-name>/implementation.md`

## Exit Condition

Implementation is complete when the requested behavior is implemented, relevant local tests/checks have run or constraints are recorded, obsolete in-scope code is removed, and the change is ready for executable validation or code review.

## Next Step

- If behavior needs proof across API, UI, CLI, process, lifecycle, integration, or another executable boundary, proceed to `stages/05-executable-validation/stage-guide.md`.
- Otherwise proceed to `stages/06-code-review/stage-guide.md`.

## Problem Routing

- If behavior is missing or ambiguous, return to requirements.
- If ownership, API, data shape, or file placement is wrong, return to design.
- If root cause is unclear, return to investigation.
