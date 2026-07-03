# Executable Validation Guide

## Purpose

Prove the changed behavior across the real boundary of the system, or record why unit/integration evidence is sufficient for this task.

Executable validation may include API, browser/UI, desktop UI, CLI, worker/process, lifecycle, integration, or another executable surface.

## Inputs

- requirements or acceptance criteria
- implementation notes or current diff
- design sketch when one exists
- unit/integration verification evidence

## Actions

- Decide which executable scenarios are needed.
- Map critical acceptance criteria to executable scenarios.
- Prefer durable repo-resident validation when it should govern future changes.
- Use temporary scripts, probes, local setup, mocks, containers, CLI harnesses, desktop automation, lifecycle checks, or browser automation when durable tests alone cannot prove the behavior.
- Record scenario source, validation mode, platform/runtime target, expected outcome, command or harness, and result.
- Remove temporary validation-only scaffolding unless keeping it is clearly useful.

## Outputs

- executable validation commands/results or no-additional-boundary rationale
- durable validation assets when useful
- `tickets/in-progress/<ticket-name>/executable-validation.md`

## Exit Condition

Executable validation is complete when critical acceptance criteria have passing evidence or an explicit no-additional-boundary rationale, temporary scaffolding is cleaned up or intentionally retained, and unresolved blockers or residual risks are recorded.

## Next Step

Proceed to `stages/06-code-review/stage-guide.md`.

## Problem Routing

- `Local Fix`: implementation defect; fix code and rerun relevant validation.
- `Validation Gap`: validation is insufficient; strengthen scenario coverage or evidence.
- `Requirement Gap`: intended behavior is missing or ambiguous; return to requirements.
- `Design Impact`: ownership, API, placement, or structure needs redesign before more coding.
- `Unclear`: return to investigation.
