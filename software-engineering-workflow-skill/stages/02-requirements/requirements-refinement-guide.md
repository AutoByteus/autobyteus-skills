# Stage 2 Requirements Refinement Guide

Use this guide to turn `requirements.md` from `Draft` into `Design-ready` or `Refined`.

Valid draft inputs include direct user intent, bug evidence, investigation evidence, and Product Manager feature briefs routed through Stage 0. A Product Manager brief is input evidence, not a replacement for `requirements.md`.

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
- source brief / evidence references, including Product Manager brief path or message reference, Product Iteration Plan reference, and selected slice ID when present

## Required Mappings

- requirement-to-use-case coverage
- acceptance-criteria-to-scenario intent
- confirmed scope classification (`Small` / `Medium` / `Large`)

## Stage 2 Rules

- refine from the latest `investigation-notes.md`, any Product Manager feature brief, Product Iteration Plan reference, and selected slice ID captured in Stage 0, not from memory alone
- keep Solution Designer / requirements refinement focused on a concrete brief; Product Manager remains authoritative for next-feature proposal and continuous product iteration
- do not move to Stage 3 until the requirements are design-ready
- if later stages reveal behavior gaps, update the same `requirements.md` in place and mark it `Refined`
- do not let a Product Manager brief bypass Stage 3 design, Stage 5 review, Stage 6 code-edit locks, Stage 7 validation, Stage 8 review, Stage 9 docs sync, Stage 10 Product Manager acceptance or user verification as applicable, or release/deployment controls
