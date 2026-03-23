# Stage 8 Code Review Guide

## Purpose

Stage 8 is an independent engineering gate.
It uses the shared design principles, shared common practices, and Stage 8 hard review gates to judge the implementation after testing.

## Inputs

- current code and changed scope
- Stage 7 validation evidence
- earlier design artifacts as context only
- `code-review-principles.md`

## Review Authority

- Earlier design artifacts are context, not authority.
- If review shows the earlier design basis was weak, wrong, or incomplete, classify `Design Impact`.
- Do not pass code merely because it matches an earlier approved design.

## Scope

- changed source files
- changed test files
- directly impacted related files when structural risk exists

## Mandatory Review Areas

- data-flow spine, ownership, and support-structure quality
- existing-capability reuse and reusable-owned-structure extraction
- shared-structure/data-model tightness and shared-base coherence
- separation of concerns, file responsibility, and file placement
- dependency quality, boundary quality, and naming alignment
- no unjustified duplication or repeated structures in changed scope
- patch-on-patch complexity control
- cleanup completeness for dead, obsolete, replaced, and legacy code in scope
- test quality, test maintainability, and validation sufficiency
- no backward compatibility and no legacy retention

## Source-File Size Policy

- The `>500` effective non-empty-line hard limit and `>220` changed-line delta gate apply to changed source implementation files only.
- Test files remain in review scope for correctness and maintainability, but they do not fail the gate only because they are long.
- A changed source file over the hard limit defaults to `Design Impact` and `Fail`.

## Failure Classification

- `Local Fix`: rerun `Stage 6 -> Stage 7 -> Stage 8`
- `Validation Gap`: rerun `Stage 7 -> Stage 8`
- `Design Impact`: rerun `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`
- `Requirement Gap`: rerun `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`
- `Unclear`: rerun `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`

## Exit Gate

This stage is complete only when all mandatory Stage 8 checks pass and the final review decision is recorded as `Pass`.
