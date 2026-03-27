# Stage 2 Requirements & Success Criteria Guide

Use this stage to turn `requirements.md` from `Draft` into `Plan-ready` or `Refined`.

## Required Quality

- the task definition is explicit enough to plan experiments without guesswork
- each requirement has a stable `requirement_id`
- each success criterion has a stable `success_criteria_id`
- success criteria are measurable and can be closed by Stage 5 evidence

## Minimum Sections

- status
- goal or problem statement
- in-scope task definition
- baseline or comparison target
- success criteria
- constraints and dependencies
- assumptions
- risks and open questions

## Required Deep-Learning Content

- target metric or metrics
- threshold, improvement target, or expected comparison direction
- dataset or split assumptions
- evaluation protocol assumptions
- resource constraints:
  - GPU or accelerator availability,
  - runtime budget,
  - memory limits,
  - storage constraints
- pass, fail, and inconclusive conditions

## Rules

- refine from the latest `investigation-notes.md`, not from memory alone
- do not move to Stage 3 until Stage 5 could truthfully validate the criteria
- if later stages reveal gaps, update the same `requirements.md` in place and mark it `Refined`

## Exit Gate

Leave Stage 2 only when `requirements.md` is `Plan-ready` or `Refined` and every critical outcome has a measurable closure path.
