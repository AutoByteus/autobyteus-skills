# Code Review Guide

## Purpose

Review the changed code and validation evidence before docs sync and handoff.

## Inputs

- current diff and changed files
- validation evidence
- requirements or acceptance criteria
- investigation, design, or implementation notes when they explain the changed scope
- `code-review-principles.md`

## Actions

- Check data-flow spine and ownership clarity.
- Check API, interface, query, and command clarity.
- Check separation of concerns and file placement.
- Check naming, duplication, patch-on-patch complexity, cleanup, and legacy retention.
- Check validation sufficiency.
- Review runtime correctness and edge cases.
- Apply source-file size policy to changed source implementation files:
  - effective non-empty line count: `rg -n "\\S" <file-path> | wc -l`
  - changed-line delta: `git diff --numstat <base-ref>...HEAD -- <file-path>`
- Persist `code-review.md` only when durable review evidence is useful.
- Use `code-review-principles.md` for the full scorecard order when a detailed durable review is useful.

## Outputs

- internal review findings in working context, or
- `tickets/in-progress/<ticket-name>/code-review.md`

## Exit Condition

Review is complete when blocking findings are resolved or explicitly accepted by the user with residual risk, validation evidence is sufficient for the changed behavior, and the final decision is recorded or summarized.

## Next Step

Proceed to `stages/07-docs-sync/stage-guide.md`.

## Problem Routing

- `Local Fix`: fix implementation and rerun relevant tests/review.
- `Validation Gap`: strengthen validation and rerun review.
- `Requirement Gap`: clarify requirements, then update implementation/tests/review.
- `Design Impact`: update solution sketch or design, then implementation/tests/review.
- `Unclear`: return to investigation first.
