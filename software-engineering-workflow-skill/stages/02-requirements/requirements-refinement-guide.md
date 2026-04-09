# Stage 2 Requirements Refinement Guide

Use this guide to turn `requirements.md` from `Draft` into `Design-ready` or `Refined`.

## Artifact Discipline

- update one canonical file: `tickets/in-progress/<ticket-name>/requirements.md`
- requirement writing is mandatory for `Small`, `Medium`, and `Large` scope
- do not create versioned duplicates such as `requirements-v2.md`

## Maturity Flow

- `Draft`: initial capture from user input, bug evidence, or Stage 0 bootstrap
- `Design-ready`: refined after the Stage 1 understanding pass
- `Refined`: updated in place when later stages discover missing behavior, ambiguity, or new constraints

## Required Quality

- requirements describe verifiable behavior, not only narrative intent
- each requirement has a stable `requirement_id`
- each acceptance criterion has a stable `acceptance_criteria_id`
- expected outcomes are measurable enough to drive Stage 7 validation

## Minimum Sections

- status
- goal / problem statement
- in-scope use cases
- acceptance criteria
- constraints / dependencies
- assumptions
- open questions / risks

## Required Mappings

- requirement-to-use-case coverage
- acceptance-criteria-to-scenario intent
- confirmed scope classification (`Small` / `Medium` / `Large`)

## Stage 2 Rules

- refine from the latest `investigation-notes.md`, not from memory alone
- do not move to Stage 3 until the requirements are design-ready
- design-ready means the intended behavior is clear enough to support design and future-state runtime call stacks
- confirm the current scope classification (`Small` / `Medium` / `Large`) and rationale in the requirements artifact
- if later stages reveal behavior gaps, update the same `requirements.md` in place and mark it `Refined`
