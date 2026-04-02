# Stage 8 Code Review Guide

## Purpose

Stage 8 is an independent engineering gate.
It uses the shared design principles, shared common practices, and Stage 8 hard review gates to judge the implementation after testing.

## Inputs

- current code and changed scope
- Stage 7 validation evidence
- latest `investigation-notes.md` when it materially explains the changed scope, current behavior, external constraints, or a review finding
- earlier design artifacts as context only
- `code-review-principles.md`

## Review Authority

- Earlier design artifacts are context, not authority.
- Investigation notes are context, not authority.
- If review shows the earlier design basis was weak, wrong, or incomplete, classify `Design Impact`.
- Do not pass code merely because it matches an earlier approved design.

## Scope

- changed source files
- changed test files
- directly impacted related files when structural risk exists

## Mandatory Review Scorecard

- Record a detailed scorecard in `code-review.md` on every Stage 8 review round.
- Score each category from `1.0` to `10.0` in `0.5` increments.
- For every scored category, record:
  - why the code earned that score,
  - what concrete weakness, gap, or drag kept the score lower,
  - what specific improvement is expected.
- Mandatory scorecard categories:
  - spine clarity and traceability
  - ownership clarity and boundary encapsulation
  - separation of concerns and file placement
  - API/interface/query/command clarity
  - shared-structure/data-model tightness and reusable owned structures
  - dependency quality and shortcut avoidance
  - naming quality and local readability
  - validation strength
  - runtime correctness under edge cases
  - modernization / cleanup / no legacy
- Use an equal-weight average across the ten categories and report it as both `Overall: X.X / 10` and `YY / 100`.
- The scorecard is diagnostic, not the gate by itself. Scores never override blocking findings or failed mandatory checks.

## Mandatory Review Areas

- data-flow spine, ownership, and off-spine concern quality
- existing-capability reuse and reusable-owned-structure extraction
- shared-structure/data-model tightness and shared-base coherence
- separation of concerns, file responsibility, and file placement
- dependency quality, boundary quality, boundary encapsulation quality, and naming quality across files, folders, APIs, types, functions, parameters, and variables
- names must stay concrete and unsurprising; reject misleading abbreviations, vague placeholders, or names that hide side effects or ownership
- `spine`, `owner`, and `off-spine concern` are relationship terms, not naming templates; reject generic names like `Support`, `Supporting`, `OffSpine`, `SideConcern`, or `Helper` when they hide the concrete concern actually handled
- no unjustified duplication or repeated structures in changed scope
- patch-on-patch complexity control
- cleanup completeness for dead, obsolete, replaced, and legacy code in scope
- test quality, test maintainability, and validation sufficiency
- no backward compatibility and no legacy retention
- mandatory scorecard coverage with evidence-backed rationale, weaknesses, and required improvements for every category
- keep one canonical `code-review.md` path across reruns; do not create versioned copies by default
- on round `>1`, recheck prior unresolved findings first and update the prior-findings resolution section before declaring the new gate result
- reuse the same finding IDs across reruns for the same unresolved issues; create new IDs only for newly discovered findings

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
- After recording the re-entry path in `workflow-state.md`, immediately resume the first returned stage by default, without waiting for another user message. Do not stop after only describing the rerun path.

## Exit Gate

This stage is complete only when all mandatory Stage 8 checks pass, the final review decision is recorded as `Pass`, and the detailed review scorecard is recorded.
