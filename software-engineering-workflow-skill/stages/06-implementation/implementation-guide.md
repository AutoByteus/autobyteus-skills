# Stage 6 Implementation Guide

## Purpose

Stage 6 finalizes the implementation baseline and executes the code changes for the current ticket.

## Inputs

- current `workflow-state.md`
- current `investigation-notes.md`
- current `requirements.md`
- current design basis
- current `future-state-runtime-call-stack.md`
- current `future-state-runtime-call-stack-review.md`
- `implementation-template.md`

## Artifact Model

- use one canonical `implementation.md` file
- treat `Plan Baseline` sections as the stable implementation baseline
- treat `Execution Tracking` sections as the live execution log
- keep detailed Stage 7, Stage 8, and Stage 9 evidence in their own canonical artifacts and leave only short handoff pointers here

## Implementation Rules

- do not start source edits until `workflow-state.md` shows `Current Stage = 6` and `Code Edit Permission = Unlocked`
- finalize the implementation baseline only after Stage 5 reaches `Go Confirmed`
- implement bottom-up where dependencies require it, but keep the sequencing spine-led and owner-led rather than file-order-led
- write or update required unit and integration checks alongside the implementation work
- preserve the shared design principles during coding; if file-level reality exposes a design weakness, classify `Design Impact` instead of patching around it locally
- do not introduce backward-compatibility shims, dual paths, or legacy retention
- remove dead code, obsolete files, unused helpers, replaced paths, and dormant flags in scope before closing Stage 6
- keep touched files in the folder and boundary that own the concern; move or split when placement is misleading
- treat the Stage 8 source-file size gates as active Stage 6 guardrails: avoid changed source files over `500` effective non-empty lines and act on `>220` changed-line pressure before review

## Re-Entry Rules

- local implementation issues can stay in Stage 6
- if the issue is non-local, classify and return upstream:
  - `Design Impact`: `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`
  - `Requirement Gap`: `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`
  - `Unclear`: `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`
- record the classification and return path in `workflow-state.md`, set the code-edit lock appropriately, and resume the first returned stage by default

## Artifact Rule

Use `implementation-template.md` as the canonical Stage 6 artifact structure.
Use `implementation-example.md` only as a supporting example, not as the source of rules.

## Exit Gate

Stage 6 is complete only when the implementation baseline is delivered, required unit/integration verification passes, no scoped legacy or compatibility debt remains, and the code is ready for Stage 7 executable validation.
