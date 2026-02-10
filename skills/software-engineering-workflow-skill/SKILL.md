---
name: software-engineering-workflow-skill
description: "Create software-engineering planning artifacts with triaged depth: runtime simulation + implementation planning/progress for all sizes, plus design docs for medium/large scope. Includes requirement clarification, call-stack validation, and iterative refinement."
---

# Software Engineering Workflow Skill

## Overview

Produce a structured planning workflow for software changes: triage scope, validate per-use-case runtime call stacks, and drive implementation with plan + real-time progress tracking. For medium/large scope, include a full design document organized by separation of concerns.

## Workflow

### Ticket Folder Convention (Project-Local)

- For each task, create/use one ticket folder under the current project's `tickets/` directory.
- Folder naming: use a clear, short kebab-case name (no date prefix required).
- Write all task planning artifacts into that ticket folder.
- If the user specifies a different location, follow the user-specified path.

### 0) Triage Change Size First (Decide Workflow Depth)

- Do a quick requirement + codebase scan before choosing artifacts.
- Classify as `Small`, `Medium`, or `Large` using practical signals:
  - Estimated files touched (roughly <= 3 is usually `Small` if not cross-cutting).
  - New/changed public APIs, schema/storage changes, or cross-cutting behavior.
  - Multi-layer impact (API + service + persistence + runtime flow) or architectural impact.
- Choose workflow depth:
  - `Small`: create a draft implementation plan (with a short solution sketch), run per-use-case runtime simulation from that plan, then refine the same plan until simulation-validated and track progress in real time.
  - `Medium/Large`: create design doc first, run runtime simulation from the design doc, then create implementation plan and track progress in real time.
- Re-evaluate during implementation; if scope expands or smells appear, escalate from `Small` to full workflow.

### 1) Clarify Requirements And Scope

- Ask for goals, non-goals, primary use cases, and constraints.
- Confirm the triage result (`Small` vs `Medium/Large`) and why.
- If scope is ambiguous, ask whether to run medium/large depth (includes full design doc). Otherwise proceed with the triaged depth.

### 2) Draft The Design Document

- Required for `Medium/Large`. Optional for `Small`.
- For `Small`, do not require a full design doc; use the draft implementation plan solution sketch as the simulation basis.
- Follow separation of concerns: each file/module owns a clear responsibility.
- Make the design doc delta-aware, not only target-state:
  - include current-state summary (as-is),
  - include target-state summary (to-be),
  - include explicit change inventory rows for `Add`, `Modify`, `Rename/Move`, `Remove`.
- List files/modules and their public APIs.
- For each file/module, state responsibility, key APIs, inputs/outputs, dependencies, and change type.
- Document dependency flow and cross-reference risk explicitly (including how cycles are avoided or temporarily tolerated).
- For `Rename/Move` and `Remove`, include decommission/cleanup intent (import cleanup, migration compatibility, dead-code removal).
- Capture data models and error-handling expectations if relevant.
- Use the template in `assets/design-template.md` as a starting point.

### 3) Simulate Runtime Call Stacks Per Use Case

- Required for all sizes (`Small`, `Medium`, `Large`).
- For `Small`, keep it concise but still cover each in-scope use case with primary path plus key fallback/error branch when relevant.
- Simulation basis by scope:
  - `Small`: simulate against the draft implementation plan solution sketch.
  - `Medium/Large`: simulate against the design document.
- For each use case, write a simulated call stack from entry point to completion in a debug-trace format.
- Include file and function names at every frame using `path/to/file.ts:functionName(...)`.
- Show architectural boundaries explicitly (e.g., controller -> service -> repository -> external API).
- Include primary path and fallback/error paths, not only happy path.
- Mark async/event boundaries (`await`, queue enqueue/dequeue, worker loop handoff).
- Mark state mutations and persistence points (`in-memory state`, `cache write`, `DB/file write`).
- Capture decision gates and conditions that choose one branch over another.
- Note key data transformations (input schema -> domain model -> output payload).
- Look for design smells: cross-cutting responsibilities, leaky abstractions, missing boundaries, hidden side effects, or overly long call chains.
- Use the template in `assets/simulated-runtime-call-stack-template.md`.

### 4) Iterate The Design Based On Call Stacks

- Run a cleanliness review on each use-case call stack before implementation:
  - use case can be fully achieved end-to-end,
  - separation of concerns is clear (each file/module has one primary responsibility),
  - boundaries and API ownership are clear,
  - dependency flow is reasonable (no accidental cycles/leaky cross-references),
  - no major design/code-structure smells are visible in the flow.
- If issues are found:
  - `Medium/Large`: revise the design document, then regenerate/refine call stacks.
  - `Small`: refine the implementation plan (and add/update design notes if needed), then regenerate/refine call stacks.
- Repeat until call stacks are clean and feasible for all in-scope use cases.

### 5) Produce Implementation Plan And Progress Tracker

- Use a bottom-up, test-driven approach: implement foundational dependencies first.
- For each file/module, define unit tests and integration tests as needed.
- Finalize planning artifacts before kickoff:
  - `Small`: refine the draft implementation plan until simulation-validated.
  - `Medium/Large`: create implementation plan after simulation validates the design doc.
- Create the implementation progress document at implementation kickoff, after required pre-implementation artifacts are ready.
- Implementation plan + real-time progress tracking are required for all sizes (`Small`, `Medium`, `Large`).
- Treat runtime simulation as a pre-implementation verification gate: ensure each use case is represented before coding starts.
- Start implementation only after the simulation gate is marked clean/pass for all in-scope use cases.
- Ensure traceability when a design doc exists: every design change-inventory row (especially `Rename/Move` and `Remove`) maps to implementation tasks and verification steps.
- Use "one file at a time" as the default execution strategy, not an absolute rule.
- When rare cross-referencing is unavoidable, allow limited parallel/incomplete implementation, but explicitly record:
  - the cross-reference smell,
  - the blocked dependency edge,
  - the condition to unblock,
  - the required design-document update.
- Update progress in real time during implementation (immediately after file status changes, test runs, blocker discoveries, and design-feedback-loop updates).
- Track change IDs and change types in progress (`Add`/`Modify`/`Rename/Move`/`Remove`) so refactor deltas remain explicit through execution.
- Track file build state explicitly (`Pending`, `In Progress`, `Blocked`, `Completed`, `N/A`).
- Track unit/integration test state separately (`Not Started`, `In Progress`, `Passed`, `Failed`, `Blocked`, `N/A`).
- If a file is blocked by unfinished dependencies, mark it `Blocked` and record the dependency and unblock condition.
- Mark a file `Completed` only when implementation is done and required tests are passing.
- Use `assets/implementation-plan-template.md` and `assets/implementation-progress-template.md`.

## Output Defaults

If the user does not specify file paths, write to a project-local ticket folder:

- `tickets/<ticket-name>/simulated-runtime-call-stack.md`
- `tickets/<ticket-name>/implementation-plan.md`
- `tickets/<ticket-name>/implementation-progress.md`

For `Medium/Large`, also write in the same ticket folder:

- `tickets/<ticket-name>/design.md`

## Templates

- `assets/design-template.md`
- `assets/simulated-runtime-call-stack-template.md`
- `assets/implementation-plan-template.md`
- `assets/implementation-progress-template.md`
