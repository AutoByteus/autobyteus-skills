# Stage 3 Design Guide

## Purpose

Stage 3 turns `Design-ready` requirements plus investigation evidence into the design basis for later runtime-call-stack work and implementation.

## Inputs

- current `investigation-notes.md`
- current `requirements.md` with status `Design-ready` or `Refined`
- `shared/design-principles.md`
- `proposed-design-template.md`

`shared/design-principles.md` is the single canonical design reference for this stage.

## Scope By Classification

- `Small`: use the solution-sketch section in `implementation.md` as the lightweight design basis
- `Medium` / `Large`: create or refine `tickets/in-progress/<ticket-name>/proposed-design.md`

## Design Operating Model

- design architecture-first, not file-first
- start from the data-flow spine, ownership boundaries, and off-spine concerns before mapping work onto concrete files
- ground the target design in enough current-state reading to understand current flow, current owners, coupling problems, file-placement drift, and migration constraints
- do not anchor the design to the current file layout when the current layout is structurally wrong
- derive subsystem, folder, and file mapping from the spine and ownership model instead of projecting the current layout forward by default
- use `Keep`, `Add`, `Split`, `Merge`, `Move`, `Remove` deliberately; do not default to minimal edits when a structural change is the cleaner design
- reuse or extend an existing capability area when it naturally owns the concern; justify `Create New` only when no current owner fits
- extract repeated coordination policy into a clear owner instead of leaving it fragmented across callers
- reject empty indirection; a new boundary should own real policy, translation, sequencing, or authority
- treat removal as first-class design work when a clearer owner or tighter structure makes old fragments unnecessary
- do not design backward-compatibility wrappers, dual paths, legacy adapters, or fallback branches kept only for old behavior
- use short examples when they materially improve clarity for a non-obvious shape
- version the design during review loops and record what changed between rounds

## Artifact Rule

Use `proposed-design-template.md` as the artifact schema.
The guide defines how to think and sequence the work; the template defines what must be written into the design artifact.

## Exit Gate

Stage 3 is complete only when the current design basis is ready to drive Stage 4 future-state runtime call stacks for the current scope.
