# Stage 3 Design Guide

## Purpose

Stage 3 translates design-ready requirements into a target architecture that later stages can validate.
It is the place to decide the target shape, not just describe the current file layout.

## Inputs

- current `requirements.md`
- current `investigation-notes.md`
- `shared/design-principles.md`
- `shared/common-design-practices.md`

## Output By Scope

- `Small`: concise design basis inside `implementation.md`
- `Medium` / `Large`: `proposed-design.md` using `proposed-design-template.md`

## Operating Order

1. Ground the design in the current system enough to understand the real owners, coupling problems, and placement drift.
2. Define the target data-flow spine or execution-flow spine.
3. Identify the main domain subjects and subsystem or capability-area ownership on that spine.
4. Draft file responsibilities under those owners.
5. Extract reusable owned structures when repeated shapes, mappers, schemas, or converters appear.
6. Re-tighten file responsibilities after that extraction.
7. Finalize folder and path mapping only after ownership and file responsibility are clear.

## Mandatory Design Rules

- Design from the target architecture first, not from the current file layout.
- Use `Keep`, `Add`, `Split`, `Merge`, `Move`, `Remove` deliberately; do not default to minimal edits.
- Reuse or extend an existing subsystem before creating a new support helper.
- When clearer ownership makes older fragments unnecessary, name the removal or decommission work explicitly.
- Reject patch-on-patch structure that hides architecture problems behind local fixes.
- Keep interfaces, queries, commands, and reused service methods aligned with explicit ownership and clear identity shape.
- Keep shared data structures tight:
  - remove redundant attributes
  - avoid overlapping parallel representations for the same subject
  - prefer a tight shared core plus meaningful specialization or composition over a kitchen-sink base structure
- Keep file placement ownership-led. If a touched file lives under the wrong subsystem or folder, propose the move or split.
- No backward compatibility, legacy retention, dual-path behavior, or compatibility wrappers.

## Design Artifact Expectations

- include current-state summary, target-state summary, and explicit change inventory
- record subsystem allocation, file responsibilities, reusable owned structures, and path mapping
- record naming decisions and naming-drift corrections
- include use-case coverage mapping into Stage 4 runtime call stacks
- version the design through review loops (`v1`, `v2`, ...)

## Exit Gate

This stage is complete only when the design basis is current, structurally coherent, and concrete enough to drive Stage 4 runtime modeling without guessing.
