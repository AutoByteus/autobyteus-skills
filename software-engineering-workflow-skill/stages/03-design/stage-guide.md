# Design Guide

## Purpose

Choose a coherent implementation shape before coding when the change involves ownership, boundaries, APIs, file placement, data shape, or non-obvious validation risk.

## Inputs

- investigation findings
- requirements or acceptance criteria
- `shared/design-principles.md`
- current code structure

## Actions

- Decide whether a durable design artifact is useful.
- For most tasks, write a short solution sketch in `implementation.md` or working context.
- Use `proposed-design-template.md` only when a fuller design document materially reduces risk.
- Identify the owning boundary or file for the change.
- Check whether current file placement and naming still match responsibility.
- Identify new files, APIs, tests, and obsolete code to remove.
- Apply `shared/design-principles.md`, especially data-flow spine clarity, ownership clarity, off-spine concern ownership, and the Authoritative Boundary Rule.

## Outputs

- working-context design decision, or
- solution sketch in `implementation.md`, or
- `tickets/in-progress/<ticket-name>/proposed-design.md` for design-heavy work

## Exit Condition

Design is complete when the agent knows where the change belongs, why that structure is coherent, what will be implemented, and what validation should prove it.

## Next Step

Proceed to `stages/04-implementation/stage-guide.md`.

## Problem Routing

- If design depends on unclear behavior, return to requirements.
- If design depends on unknown current behavior, return to investigation.
- If implementation later reveals ownership, API, placement, or data-shape problems, return here before continuing code changes.
