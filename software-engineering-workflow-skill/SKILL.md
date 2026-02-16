---
name: software-engineering-workflow-skill
description: "Create software-engineering planning artifacts with triaged depth: proposed-design-based runtime call stacks (future-state), runtime call stack review, and implementation planning/progress for all sizes, plus proposed design docs for medium/large scope. Includes requirement clarification, call-stack validation, and iterative refinement."
---

# Software Engineering Workflow Skill

## Overview

Produce a structured planning workflow for software changes: triage scope, build proposed-design-based runtime call stacks per use case, verify those call stacks with a dedicated review artifact, and drive implementation with plan + real-time progress tracking. For medium/large scope, include a full proposed design document organized by separation of concerns.
This workflow is stage-gated. Do not batch-generate all artifacts by default.
In this skill, proposed-design-based runtime call stacks are future-state (`to-be`) execution models. They are not traces of current (`as-is`) implementation behavior.

## Workflow

### Ticket Folder Convention (Project-Local)

- For each task, create/use one ticket folder under the current project's `tickets/` directory.
- Folder naming: use a clear, short kebab-case name (no date prefix required).
- Write all task planning artifacts into that ticket folder.
- If the user specifies a different location, follow the user-specified path.

### Audible Notifications (Speak Tool, Required)

- Use the `Speak` tool for key stage-boundary updates so the user does not need to watch the screen continuously.
- Hard rule: speak at both stage start and stage completion for each key stage below (no selective skipping).
- Required speak stages:
  - workflow kickoff (`task accepted`, `next stage`),
  - scope triage (`started`, then chosen depth finalized: `Small`/`Medium`/`Large`),
  - proposed design stage when in scope (`Medium`/`Large`) (`started`, then `proposed-design.md` written/updated),
  - runtime call stack stage (`started`, then `proposed-design-based-runtime-call-stack.md` written/updated),
  - review loop (each round `started`, then round result with `Go`/`No-Go` and write-back status),
  - implementation planning stage (`started`, then `implementation-plan.md` finalized + `implementation-progress.md` initialized),
  - implementation execution stage (`started`, then implementation completion + verification result),
  - post-implementation docs sync stage (`started`, then `docs/` synchronization completed or explicit no-impact decision recorded),
  - final handoff (`started`, then completed artifact summary).
- Speak trigger policy:
  - do not skip required stage-boundary speak events,
  - for completion events, speak only after the milestone is durably completed (file written + gate state known),
  - do not speak for intermediate thinking or partial drafts between required stage-boundary events,
  - if multiple milestone updates happen close together, batch them into one short status message.
- Keep each spoken message short (1-2 sentences), status-first, with one clear next-step statement.
- If the `Speak` tool fails or is unavailable, continue the workflow and provide the same update in text.
- Do not speak secrets, tokens, or full sensitive payloads.

### Execution Model (Strict Stage Gates)

- Work in explicit stages and complete each gate before producing downstream artifacts.
- Do not finalize `implementation-plan.md` or generate `implementation-progress.md` until the runtime call stack review gate is fully satisfied for the current scope.
- Do not start implementation execution until `implementation-plan.md` is finalized and `implementation-progress.md` is initialized.
- Do not close the task until post-implementation `docs/` synchronization is completed (or explicit no-impact decision is recorded with rationale).
- `Small` scope exception: drafting `implementation-plan.md` (solution sketch only) before review is allowed as design input, but this draft does not unlock implementation kickoff.
- Runtime call stack review must run as iterative deep-review rounds (not one-pass review).
- `Go` cannot be declared immediately after write-backs from a blocking round.
- Stability rule (mandatory): unlock `Go` only after two consecutive deep-review rounds report no blockers and no required write-backs.
- First clean round is provisional (`Candidate Go`), second consecutive clean round is confirmation (`Go`).
- Any review finding with a required design/call-stack update is blocking; regenerate affected artifacts and re-review before proceeding.
- If the user asks for all artifacts in one turn, still enforce stage gates within that turn (iterate review rounds first; only then produce implementation artifacts).
- No mental-only review refinements: if a round finds issues, update the affected artifact files immediately in the same round before starting the next round.
- For each review round, record explicit write-backs in `runtime-call-stack-review.md`:
  - updated files,
  - new artifact versions,
  - changed sections,
  - which findings were resolved.
- A review round cannot be considered complete until its required file updates are physically written.
- Speak each completed round status only after the round record and required write-backs are physically written.

### 0) Triage Change Size First (Decide Workflow Depth)

- Do a requirement + codebase understanding pass before choosing artifacts.
- Minimum codebase understanding pass before design:
  - identify entrypoints and execution boundaries for in-scope flows,
  - identify touched modules/files and owning concerns,
  - identify current naming conventions (file/module/API style),
  - identify unknowns that could invalidate design assumptions.
- Do not draft proposed design or call stacks until this understanding pass is complete.
- Classify as `Small`, `Medium`, or `Large` using practical signals:
  - Estimated files touched (roughly <= 3 is usually `Small` if not cross-cutting).
  - New/changed public APIs, schema/storage changes, or cross-cutting behavior.
  - Multi-layer impact (API + service + persistence + runtime flow) or architectural impact.
- Choose workflow depth:
  - `Small`: create a draft implementation plan (with a short solution sketch), build per-use-case proposed-design-based runtime call stacks from that plan, review them, then refine until review-pass and track progress in real time.
  - `Medium`: create proposed design doc first, build proposed-design-based runtime call stacks from the proposed design doc, run iterative deep-review rounds until stability gate `Go`, and only then create implementation plan and track progress in real time.
  - `Large`: create proposed design doc first, build proposed-design-based runtime call stacks from the proposed design doc, run iterative deep-review rounds until stability gate `Go`, and only then create implementation plan and track progress in real time.
- Re-evaluate during implementation; if scope expands or smells appear, escalate from `Small` to full workflow.
- Speak completion after triage depth is finalized (`Small`/`Medium`/`Large`).

### 1) Clarify Requirements And Scope

- Ask for goals, non-goals, primary use cases, and constraints.
- Confirm the triage result (`Small` vs `Medium` vs `Large`) and why.
- If scope is ambiguous, ask whether to run medium/large depth (includes full proposed design doc). Otherwise proceed with the triaged depth.

### Core Modernization Policy (Mandatory)

- Mandatory stance: no backward compatibility and no legacy code retention.
- Do not preserve legacy behavior, legacy APIs, compatibility wrappers, dual-write paths, or fallback branches kept only for old flows.
- Prefer clean replacement and explicit deletion of obsolete code, files, tests, flags, and adapters in the same ticket.
- Do not add compatibility exceptions in this workflow.

### 2) Draft The Proposed Design Document

- Required for `Medium/Large`. Optional for `Small`.
- For `Small`, do not require a full proposed design doc; use the draft implementation plan solution sketch as the lightweight design basis for runtime call stacks.
- Follow separation of concerns: each file/module owns a clear responsibility.
- Make the proposed design doc delta-aware, not only target-state:
  - include current-state summary (as-is),
  - include target-state summary (to-be),
  - include explicit change inventory rows for `Add`, `Modify`, `Rename/Move`, `Remove`.
- List files/modules and their public APIs.
- For each file/module, state responsibility, key APIs, inputs/outputs, dependencies, and change type.
- Include a naming decisions section:
  - proposed file/module/API names,
  - rationale for each naming choice,
  - mapping from old names to new names when renaming.
- Use natural, unsurprising, implementation-friendly names; naming choices should be understandable without domain-specific insider context.
- Document dependency flow and cross-reference risk explicitly (including how cycles are avoided or temporarily tolerated).
- For `Rename/Move` and `Remove`, include decommission/cleanup intent (import cleanup and dead-code removal).
- Capture data models and error-handling expectations if relevant.
- Add a use-case coverage matrix in the design doc with at least:
  - `use_case_id`,
  - primary path covered (`Yes`/`No`),
  - fallback path covered (`Yes`/`No`/`N/A`),
  - error path covered (`Yes`/`No`/`N/A`),
  - mapped sections in runtime call stack doc.
- Version the design during review loops (`v1`, `v2`, ...) and record what changed between rounds.
- Use the template in `assets/proposed-design-template.md` as a starting point.
- Speak completion after `proposed-design.md` is physically written/updated.

### 3) Build Proposed-Design-Based Runtime Call Stacks Per Use Case

- Required for all sizes (`Small`, `Medium`, `Large`).
- For `Small`, keep it concise but still cover each in-scope use case with primary path plus key fallback/error branch when relevant.
- Basis by scope:
  - `Small`: use the draft implementation plan solution sketch as the design basis.
  - `Medium/Large`: use the proposed design document as the design basis.
- For each use case, write a proposed-design-based runtime call stack from entry point to completion in a debug-trace format.
- Use stable `use_case_id` values and ensure IDs match the design coverage matrix and review artifact.
- Treat this artifact as `to-be` architecture behavior derived from the proposed design (or small-scope solution sketch), not as-is code tracing.
- If current code differs from target design, model the target design behavior and record migration/transition notes separately.
- Include file and function names at every frame using `path/to/file.ts:functionName(...)`.
- Show architectural boundaries explicitly (e.g., controller -> service -> repository -> external API).
- Include primary path and fallback/error paths, not only happy path.
- Include explicit use-case coverage status per use case (primary/fallback/error) and mark intentional `N/A` branches.
- Mark async/event boundaries (`await`, queue enqueue/dequeue, worker loop handoff).
- Mark state mutations and persistence points (`in-memory state`, `cache write`, `DB/file write`).
- Capture decision gates and conditions that choose one branch over another.
- Note key data transformations (input schema -> domain model -> output payload).
- Version call stacks to match design revisions from review loops (`v1`, `v2`, ...).
- Use the template in `assets/proposed-design-based-runtime-call-stack-template.md`.
- Speak completion after `proposed-design-based-runtime-call-stack.md` is physically written/updated.

### 4) Review Proposed-Design-Based Runtime Call Stacks (Future-State + Naming + Cleanliness Gate)

- Create `runtime-call-stack-review.md` as a mandatory review artifact.
- Review focus is future-state correctness and implementability against target design, not parity with current code structure.
- Run review in explicit rounds and record each round in the same review artifact.
- Review each use case against these criteria:
  - terminology and concept vocabulary is natural and intuitive (`Pass`/`Fail`),
  - file/API naming is clear and unsurprising for implementation mapping (`Pass`/`Fail`),
  - future-state alignment with proposed design (`Pass`/`Fail`),
  - use-case coverage completeness (primary/fallback/error coverage) (`Pass`/`Fail`),
  - business flow completeness (`Pass`/`Fail`),
  - gap findings,
  - structure and separation-of-concerns check (`Pass`/`Fail`),
  - dependency flow smells,
  - redundancy/duplication check (`Pass`/`Fail`),
  - simplification opportunity check (`Pass`/`Fail`),
  - remove/decommission and obsolete/deprecated/dead-path cleanup completeness for impacted changes (`Pass`/`Fail`),
  - no-legacy/no-backward-compat check (`Pass`/`Fail`),
  - overall verdict (`Pass`/`Fail`).
- Round policy:
  - use deep review for every round (challenge assumptions, edge cases, and cleanup quality),
  - if a round finds blocker/issues, apply write-backs immediately and reset clean-review streak to 0,
  - if a round finds no blocker/issues, mark `Candidate Go` and increment clean-review streak,
  - open `Go` only when clean-review streak reaches 2 consecutive deep-review rounds.
- Across rounds, track trend quality: issues should decline in count/severity or become more localized; otherwise escalate design refinement before proceeding.
- Round write-back discipline (mandatory):
  - Step A: run review and record findings in the current round.
  - Step B: if findings require updates, immediately modify design/call-stack artifacts and bump versions (`vN -> vN+1`).
  - Step C: record an "Applied Updates" entry in the review artifact (what changed, where, and why).
  - Step D: start the next round from updated files only; do not carry unresolved edits in memory.
  - Step E: record clean-review streak state in the review artifact (`Reset`, `Candidate Go`, or `Go Confirmed`).
- Gate `Go` criteria (all required):
  - terminology/concept vocabulary is `Pass` for all in-scope use cases,
  - file/API naming clarity is `Pass` for all in-scope use cases,
  - future-state behavior is consistent with proposed design across all in-scope use cases,
  - use-case coverage completeness is `Pass` for all in-scope use cases,
  - redundancy/duplication check is `Pass` for all in-scope use cases,
  - simplification opportunity check is `Pass` for all in-scope use cases,
  - all in-scope use cases have overall verdict `Pass`,
  - no unresolved blocking findings (including any required design/call-stack updates),
  - for any impacted `Add`/`Modify`/`Rename/Move`/`Remove` scope items, decommission/cleanup and obsolete/deprecated/dead-path checks are `Pass`,
  - two consecutive deep-review rounds have no blockers and no required write-backs.
- If issues are found:
  - `Medium/Large`: revise the proposed design document, regenerate runtime call stacks, then rerun review.
  - `Small`: refine the implementation plan (and add design notes if needed), regenerate runtime call stacks, then rerun review.
- Even when a round reports no findings, still complete the round record in-file and run another deep-review round until the two-consecutive-clean stability rule is satisfied.
- Repeat until all gate `Go` criteria are satisfied.
- Use the template in `assets/runtime-call-stack-review-template.md`.

### 5) Produce Implementation Plan And Progress Tracker

- Use a bottom-up, test-driven approach: implement foundational dependencies first.
- Sequence is mandatory:
  - first finalize `implementation-plan.md`,
  - then start implementation,
  - then keep `implementation-progress.md` updated continuously during execution.
- In `implementation-plan.md`, include a verification strategy for each use case:
  - unit tests,
  - integration tests across module/service boundaries,
  - end-to-end (E2E) test feasibility.
- Integration test coverage is required for behavior that crosses module boundaries, process boundaries, storage boundaries, or external API boundaries. If any such behavior is not covered, record a concrete rationale.
- E2E policy:
  - if E2E is feasible in the current environment, include and run at least one representative E2E scenario per critical user flow before marking implementation complete,
  - if E2E is not feasible (for example missing secrets/tokens, third-party environment dependency, or partner-system access limits), record a concrete infeasibility reason and current constraint details in both plan and progress tracker.
  - when E2E is infeasible, record best-available non-E2E verification evidence (integration/manual) and residual risk notes.
- Finalize planning artifacts before kickoff:
  - `Small`: refine the draft implementation plan until runtime call stack review passes.
  - `Medium/Large`: create implementation plan only after runtime call stack review passes final stability gate (`Go`).
- Create the implementation progress document at implementation kickoff, after required pre-implementation artifacts are ready (including the proposed design document for Medium/Large).
- Implementation plan + real-time progress tracking are required for all sizes (`Small`, `Medium`, `Large`).
- Treat proposed-design-based runtime call stack + review as a pre-implementation verification gate: ensure each use case is represented and reviewed before coding starts.
- Start implementation only after the review gate says implementation can start and all in-scope use cases are `Pass`.
- Ensure traceability when a proposed design doc exists: every design change-inventory row (especially `Rename/Move` and `Remove`) maps to implementation tasks and verification steps.
- Enforce clean-cut implementation: do not keep legacy compatibility paths.
- Use "one file at a time" as the default execution strategy, not an absolute rule.
- When rare cross-referencing is unavoidable, allow limited parallel/incomplete implementation, but explicitly record:
  - the cross-reference smell,
  - the blocked dependency edge,
  - the condition to unblock,
  - the required proposed-design-document update.
- Update progress in real time during implementation (immediately after file status changes, test runs, blocker discoveries, and design-feedback-loop updates).
- Track change IDs and change types in progress (`Add`/`Modify`/`Rename/Move`/`Remove`) so refactor deltas remain explicit through execution.
- Track file build state explicitly (`Pending`, `In Progress`, `Blocked`, `Completed`, `N/A`).
- Track unit/integration/E2E test state separately (`Not Started`, `In Progress`, `Passed`, `Failed`, `Blocked`, `N/A`).
- If a file is blocked by unfinished dependencies, mark it `Blocked` and record the dependency and unblock condition.
- Mark a file `Completed` only when implementation is done and required tests are passing.
- Mark implementation execution complete only when:
  - implementation plan scope is delivered (or deviations are explicitly documented),
  - required unit/integration tests pass,
  - feasible E2E scenarios pass, or E2E infeasibility is documented with concrete reason/constraints plus best-available non-E2E verification evidence.
- Use `assets/implementation-plan-template.md` and `assets/implementation-progress-template.md`.
- Speak when `implementation-plan.md` is written/updated, when `implementation-progress.md` is created/updated, and when implementation execution completes.

### 6) Synchronize Project Documentation (Mandatory Post-Implementation)

- After implementation execution is complete, update project documentation under `docs/` (and other canonical architecture docs such as `ARCHITECTURE.md` when impacted) so docs reflect the latest codebase behavior.
- Update docs for:
  - new modules/files/APIs,
  - changed runtime flows,
  - renamed/moved/removed components,
  - updated operational or testing procedures when behavior changed.
- If there is no docs impact, record an explicit "No docs impact" decision with rationale in `implementation-progress.md`.
- Do not treat ticket artifacts as long-term source of truth; docs must represent post-implementation reality.
- Speak completion after docs synchronization result is recorded (`Updated`/`No impact`).

### 7) Final Handoff

- Complete handoff only after implementation execution and docs synchronization are complete.
- Handoff summary must include:
  - delivered scope vs planned scope,
  - verification summary (unit/integration/E2E, documented E2E infeasibility reasons/constraints, and compensating non-E2E verification evidence),
  - docs files updated (or explicit no-impact rationale).
- Speak final handoff completion after all required artifacts and docs sync outputs are written.

## Output Defaults

If the user does not specify file paths, write to a project-local ticket folder in stage order:
These defaults list file-producing stages; gating and handoff rules still follow the full workflow above.

- Stage 1 (design basis):
  - `Small`: start/refine `tickets/<ticket-name>/implementation-plan.md` (solution sketch section only for design basis).
  - `Medium/Large`: create/refine `tickets/<ticket-name>/proposed-design.md`.
- Stage 2 (runtime modeling):
  - `tickets/<ticket-name>/proposed-design-based-runtime-call-stack.md`
- Stage 3 (review gate, iterative):
  - `tickets/<ticket-name>/runtime-call-stack-review.md`
- Stage 4 (only after gate `Go`):
  - finalize/update `tickets/<ticket-name>/implementation-plan.md`
  - `tickets/<ticket-name>/implementation-progress.md`
- Stage 5 (post-implementation documentation sync):
  - update impacted project docs in place (for example `docs/**/*.md`, `ARCHITECTURE.md`)
  - record docs sync result in `tickets/<ticket-name>/implementation-progress.md` (`Updated`/`No impact` + rationale)

## Templates

- `assets/proposed-design-template.md`
- `assets/proposed-design-based-runtime-call-stack-template.md`
- `assets/runtime-call-stack-review-template.md`
- `assets/implementation-plan-template.md`
- `assets/implementation-progress-template.md`
