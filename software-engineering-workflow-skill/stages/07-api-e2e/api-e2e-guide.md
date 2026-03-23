# Stage 7 API/E2E Guide

## Purpose

Stage 7 is the executable validation gate between implementation and code review.
It proves that the implemented system satisfies acceptance criteria and important design-risk behavior end to end.

## Inputs

- current `requirements.md`
- current design basis
- current implementation output from Stage 6

## Scenario Sources

- `Requirement`: validates explicit requirement behavior
- `Design-Risk`: validates technical or architectural risks introduced by the design

## Mandatory Validation Structure

- build an acceptance-criteria matrix from `requirements.md`
- map every in-scope acceptance criterion to at least one executable API/E2E scenario
- map every relevant spine to at least one executable scenario, or mark it `N/A` with rationale
- record scenario source, expected outcome, command or harness, and result in `api-e2e-testing.md`

## Feasibility Rules

- If a scenario is infeasible in the current environment, record the exact reason, constraints, compensating evidence, and residual risk.
- Keep Stage 7 `Blocked` until the user explicitly waives infeasible acceptance criteria.

## Failure Classification

- `Local Fix`: rerun `Stage 6 -> Stage 7`
- `Design Impact`: rerun `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`
- `Requirement Gap`: rerun `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`
- `Unclear`: rerun `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`

Do not classify a fix as `Local Fix` when it works only by degrading ownership, spine clarity, or file placement.

## Exit Gate

This stage is complete only when all executable in-scope acceptance criteria are `Passed`, all relevant executable spines have evidence, and no unresolved failures or blockers remain.
