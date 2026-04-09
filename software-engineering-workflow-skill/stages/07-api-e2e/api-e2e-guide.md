# Stage 7 API/E2E And Executable Validation Guide

## Purpose

Stage 7 is the executable validation gate between implementation and code review.
It proves that the implemented system satisfies acceptance criteria and important design-risk behavior across the real executable boundaries of the system, not only through HTTP APIs or browser-only flows.

## Inputs

- current `requirements.md`
- current design basis
- current implementation output from Stage 6

## Scenario Sources

- `Requirement`: validates explicit requirement behavior
- `Design-Risk`: validates technical or architectural risks introduced by the design

## Mandatory Validation Structure

- build an acceptance-criteria matrix from `requirements.md`
- map every in-scope acceptance criterion to at least one executable validation scenario
- map every relevant spine to at least one executable scenario, or mark it `N/A` with rationale
- treat `relevant spine` explicitly as:
  - every in-scope primary business spine,
  - every meaningful return/event spine,
  - every bounded local spine that materially affects behavior
- if multiple primary business paths are in scope, map each primary spine explicitly instead of collapsing them into one generic scenario
- when a bounded local spine is in scope, keep it attached to its parent owner in the validation reasoning; it adds local proof and does not replace coverage of the longer primary spine
- record scenario source, validation mode, platform/runtime target, expected outcome, command or harness, and result in `api-e2e-testing.md`
- keep one canonical `api-e2e-testing.md` path across reruns; do not create versioned copies by default
- on round `>1`, recheck prior unresolved failures first and update the prior-failure resolution section before declaring the new gate result
- treat the latest recorded validation round as authoritative while keeping earlier rounds as history
- reuse the same scenario IDs across reruns for the same scenarios; create new IDs only for newly discovered coverage
- during Stage 7 execution, `workflow-state.md` should show `Current Stage = 7` and `Code Edit Permission = Unlocked`
- treat scenario type as problem-dependent rather than hardcoded: API, browser UI, native desktop UI, CLI, process/lifecycle, integration, and distributed-system checks are all valid Stage 7 forms when they are the real boundary being proven

## Execution And Depth Expectations

- enter Stage 7 immediately after Stage 6 completes for the current scope
- implement or update durable repo-resident validation first when that validation should remain as future protection in the codebase
- build the acceptance-criteria matrix and spine coverage matrix before execution starts, not only after failures happen
- for API scenarios, validate contract-level behavior, including schema shape, required fields, status codes, and mapped error behavior
- for lifecycle-sensitive scenarios, record the relevant `from` / `to` version, platform/runtime target, package or update channel when relevant, restart or relaunch evidence, and persisted-state outcome
- for client/server, multi-service, or multi-process scope, include cross-boundary scenarios that prove trigger -> boundary handoff -> downstream effect -> returned or observable state
- unstructured manual-only testing is not part of the default Stage 7 standard; if human-assisted execution is unavoidable, record exact steps, automated evidence captured, constraints, and residual risk

## Validation Asset Rules

- Start with durable validation first: add or update the tests, harnesses, and validation assets that should remain in the repository and govern future changes.
- If durable repo-resident validation is not enough to prove behavior, continue with broader executable validation such as temporary scripts, probes, environment setup, containerized setups, mocked or emulated dependencies, CLI harnesses, native desktop automation, lifecycle/update/restart checks, multi-process or multi-node orchestration, or browser/computer automation.
- Record clearly which validation assets were durable in-repo additions versus temporary validation-only methods or scaffolding.
- Remove temporary validation-only scaffolding after the result is recorded unless keeping it is clearly useful as durable future coverage.

## Scenario Pattern Examples

- Backend/service API: request -> service/domain execution -> persistence or downstream effect -> returned contract and error behavior.
- Browser UI: user action -> rendered state transition -> network side effect -> final success or failure presentation.
- Native desktop updater: version `from` -> update download/apply -> relaunch/restart -> version `to` -> persisted state or migration verification.
- Worker/process lifecycle: enqueue or trigger -> background loop/process handoff -> side effect -> completion, ack, or durable state transition.
- Distributed or multi-node: action on node A -> sync/replication/failover -> observable state or behavior on node B.

## Feasibility Rules

- If a scenario is infeasible in the current environment, record the exact reason, constraints, compensating evidence, and residual risk.
- If the scenario is platform- or lifecycle-sensitive, record the relevant OS/runtime/version/package or update-feed specifics instead of reducing the blocker to a generic environment note.
- Keep Stage 7 `Blocked` until the user explicitly waives infeasible acceptance criteria.

## Failure Classification

- `Local Fix`: rerun `Stage 6 -> Stage 7`
- `Design Impact`: rerun `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`
- `Requirement Gap`: rerun `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`
- `Unclear`: rerun `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`
- After recording the re-entry path in `workflow-state.md`, immediately resume the first returned stage by default, without waiting for another user message. Do not stop after only describing the rerun path.

Do not classify a fix as `Local Fix` when it works only by degrading ownership, spine clarity, or file placement.

## Exit Gate

This stage is complete only when all executable in-scope acceptance criteria are `Passed`, all relevant executable primary/return-event/bounded-local spines have evidence (or explicit `N/A` rationale), and no unresolved failures or blockers remain across the real in-scope boundaries of the system.
