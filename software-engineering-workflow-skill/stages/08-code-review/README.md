# Stage 8 Code Review

## Purpose

Run the independent code-review gate after Stage 7 validation passes.

## Enter This Stage When

- Stage 7 is `Pass`
- `workflow-state.md` has moved to Stage 8 and locked source edits

## Stage-Owned Outputs

- `tickets/in-progress/<ticket-name>/code-review.md`
- final Stage 8 decision plus any re-entry declaration

## Exit Gate

Leave Stage 8 only when the review decision is `Pass` and all mandatory review checks are satisfied.

## Local Files

- `code-review-guide.md`: stage execution and gate rules
- `code-review-principles.md`: shared Stage 8 review philosophy and hard review principles
- `code-review-template.md`: canonical review artifact
