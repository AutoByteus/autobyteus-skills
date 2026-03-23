# Stage 6 Implementation Guide

## Purpose

Stage 6 turns the approved design and runtime model into source changes and implementation evidence.
It is also the stage where cleanup, consolidation, and ownership preservation must happen in practice.

## Inputs

- `implementation.md` baseline
- current design basis
- current future-state runtime call stack and review artifacts
- unlocked Stage 6 state in `workflow-state.md`

## Required Execution Order

1. Finalize the `implementation.md` baseline sections.
2. Initialize execution-tracking sections.
3. Start source changes only after `workflow-state.md` records Stage 6 entry and `Code Edit Permission = Unlocked`.
4. Update `implementation.md` continuously during execution.

## Implementation Rules

- Keep implementation ownership-led: do not leave touched files in the wrong subsystem or folder just to minimize edits.
- Preserve ownership-driven dependency quality: no unjustified shortcuts, cycles, or tight coupling.
- Remove dead code, obsolete files, unused helpers/tests/flags/adapters, dormant replaced paths, and compatibility shims in scope.
- Do not retain backward-compatibility wrappers, dual-path reads/writes, or legacy fallback branches.
- Keep shared structures tight in code as well as in design:
  - prefer one clear owned shared shape over duplicated near-copies
  - if there is a real common core, keep it tight and specialize meaningfully
  - do not grow one-for-all shared base structures full of optional fields
- Use one-file-at-a-time execution by default, but record cross-file blocking dependencies explicitly when sequencing requires them.

## Tracking Expectations

Use `implementation.md` to track:

- plan baseline
- execution progress per change or file
- unit and integration test status
- blockers and dependency edges
- deviations from plan
- cleanup and removal work
- brief downstream handoff notes and status pointers only for Stages 7, 8, and 9

Keep the detailed records for later stages in their own canonical artifacts:

- Stage 7: `api-e2e-testing.md`
- Stage 8: `code-review.md`
- Stage 9: `docs-sync.md`

## Failure Classification

- `Local Fix`: remain in Stage 6
- `Design Impact`: return through `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`
- `Requirement Gap`: return through `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`
- `Unclear`: return through `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`

## Exit Gate

This stage is complete only when implementation scope is delivered, required unit/integration tests pass, cleanup is complete in scope, and the changed code still preserves clear ownership and correct placement.
