# Implementation Guide

## Purpose

Make the code change while preserving repository patterns, ownership boundaries, validation intent, and cleanup quality.

## Inputs

- requirements or acceptance criteria
- investigation findings
- design sketch or proposed design, if one exists
- repository instructions and existing code patterns

## Actions

- Create or update `implementation.md`.
- Implement foundational dependencies before dependents.
- Keep edits scoped to the requested behavior.
- Add or update unit/integration tests where they provide useful coverage.
- Remove obsolete code, tests, flags, adapters, and helpers in scope.
- Preserve ownership boundaries and file placement.
- Avoid compatibility wrappers, dual-path behavior, and legacy retention unless the user explicitly requests that policy.
- Close the delivery loop for code-asset requests: the requested source file or project artifact must actually be written or updated before leaving implementation. If inspection finds an existing artifact that already satisfies the request, explicitly reuse that path and verify it instead of announcing an unperformed duplicate.
- For frontend-affecting work, complete a rendered-result feedback loop before leaving implementation:
  - inspect approved UI/UX, interaction, requirement, or design references when they exist,
  - inspect the project's design system, shared components, and adjacent product surfaces,
  - use the project-supported development or preview surface that faithfully renders the changed UI,
  - render and interact with the affected surface through relevant states and viewports,
  - check requirement/journey fidelity, visual hierarchy, layout, spacing, alignment, typography, labels, component consistency, responsive behavior, and applicable loading, empty, error, disabled, focus, keyboard, or accessibility states,
  - iterate until observed visual or interaction defects within scope are corrected,
  - if the UI cannot be rendered or a relevant state cannot be exercised, record the concrete limitation and remaining uncertainty in `implementation.md`.
- Treat frontend rendered-result inspection as implementation self-validation and polish. It does not replace Stage 05 executable validation or downstream API/E2E-style coverage.
- Watch changed source-file size:
  - effective non-empty line count: `rg -n "\\S" <file-path> | wc -l`
  - changed-line delta: `git diff --numstat <base-ref>...HEAD -- <file-path>`

## Outputs

- source and test changes
- unit/integration verification evidence
- frontend rendered-result self-validation evidence when the change affects UI
- `tickets/in-progress/<ticket-name>/implementation.md`

## Exit Condition

Implementation is complete when the requested behavior is implemented, the deliverable exists at the agreed path (or an explicitly reused existing path is reported), relevant local tests/checks have run or constraints are recorded, frontend rendered-result inspection is completed or explicitly marked not applicable, obsolete in-scope code is removed, and the change is ready for executable validation or code review.

## Next Step

Proceed to `stages/05-executable-validation/stage-guide.md`.

## Problem Routing

- If behavior is missing or ambiguous, return to requirements.
- If ownership, API, data shape, or file placement is wrong, return to design.
- If root cause is unclear, return to investigation.
