---
name: software-engineering-workflow-skill
description: "An artifact-driven software engineering feedback-loop skill for staged delivery. It drives work from bootstrap through investigation, requirements, design, runtime validation, implementation, API/E2E verification, code review, documentation sync, and final handoff with explicit gates, re-entry paths, and durable artifacts."
---

# Software Engineering Workflow Skill

## Overview

This skill is an artifact-driven software engineering feedback loop, not just a checklist.
It structures delivery through staged artifacts, explicit gates, and controlled re-entry so later validation can correct earlier assumptions instead of letting weak reasoning flow downstream.

The root `SKILL.md` is the workflow contract and feedback-loop router.
Stage-owned operating detail lives in the corresponding stage folders.

## Feedback Loop Model

- The workflow's purpose is feedback, not one-way document generation.
- Each stage writes durable artifacts that later stages validate against implementation reality, test evidence, and review findings.
- When later stages expose weak reasoning upstream, the workflow feeds structured corrections back through classified re-entry.
- `workflow-state.md` is the persisted control surface for that loop: it records current stage, gates, transitions, re-entry, blockers, and code-edit lock state.
- The execution model is state-machine-like, but the higher-level framing is an artifact-driven engineering feedback loop.

## Skill Layout

- `SKILL.md`: top-level workflow contract, stage sequence, transition rules, and global gates
- `shared/`: cross-stage references and governance
  - `shared/design-principles.md`
  - `shared/common-design-practices.md`
  - `shared/workflow-state-template.md`
- `stages/`: stage-owned READMEs, guides, templates, and examples
  - each stage `README.md` is the stage entrypoint
  - if a stage is complex, use its local `*-guide.md`
  - templates describe artifact shape, not the entire workflow contract

## Terminology

- `Subsystem` / `capability area`: a larger functional area that owns a broader category of work and may contain multiple files plus optional module groupings
- `Module`: an optional intermediate grouping inside a subsystem when the codebase benefits from it; in this skill, `module` is not a synonym for one file or the default ownership term
- `File`: one concrete source file and the primary unit where one concrete concern should land
- `Folder` / `directory`: a physical grouping used to organize files and any optional module groupings

## Workflow Contract

### Ticket Lifecycle Policy

- Each task uses one ticket folder with `in-progress` and `done` lifecycle states.
- Archival requires explicit user confirmation or explicit user move instruction; never auto-archive based only on internal assessment.
- Reopened work returns the ticket to `in-progress` before new updates begin.
- Stage 0 owns bootstrap into `in-progress`; Stage 10 owns archival into `done`.

### Workflow-State Control

- Create and maintain `tickets/in-progress/<ticket-name>/workflow-state.md` from `shared/workflow-state-template.md`.
- Treat `workflow-state.md` as the execution lock controller, not passive documentation.
- Update it before every stage transition, gate decision, re-entry declaration, or code-edit lock change.
- No source-code edits are allowed unless `workflow-state.md` explicitly shows:
  - `Current Stage = 6`
  - `Code Edit Permission = Unlocked`
- On any Stage 7 or Stage 8 failure, lock code edits first, record classification and return path, and only then begin re-entry work.

### Audible Notifications

- Use the `Speak` tool for persisted stage transitions, gate decisions, re-entry decisions, and code-edit lock changes.
- For required workflow notifications, call `Speak` with `play=true` unless the user explicitly requests silent mode.
- Update `workflow-state.md` first, then speak.
- Keep messages short, status-first, and action-oriented.
- If `Speak` is unavailable, continue and provide the same update in text.

### Global Governance

- No backward compatibility, no legacy retention, and no compatibility wrappers across design, implementation, and review.
- Removal and decommission work are first-class. A clearer owner or reusable structure should usually remove redundant fragments in scope, not coexist with them indefinitely.
- Stage-owned execution detail belongs in the stage folder, not in the root contract.
- Stage 3 design and Stage 5 review use:
  - `shared/design-principles.md`
  - `shared/common-design-practices.md`
- Stage 8 uses:
  - `stages/08-code-review/code-review-principles.md`
- Later stages are allowed to invalidate earlier artifacts. When that happens, use classified re-entry rather than patching around the problem downstream.
- On any failing gate, persist the stage decision, classification, and return path in `workflow-state.md` before changing downstream artifacts or source code.
- For post-implementation findings, update the required artifacts first; do not jump straight to source edits.

### Execution Gates

- Complete Stage 0 bootstrap and write `requirements.md` as `Draft` before investigation.
- Complete Stage 1 investigation before `requirements.md` becomes `Design-ready`.
- Do not start Stage 3 design until `requirements.md` is `Design-ready` or `Refined`.
- Do not start Stage 4 runtime modeling until the Stage 3 design basis is current.
- Do not start Stage 6 source implementation until Stage 5 reaches `Go Confirmed`.
- Unlock source edits only in Stage 6 after the Stage 5 gate is `Go Confirmed` and required upstream artifacts are current.
- Do not start Stage 7 API/E2E work until Stage 6 implementation plus required unit/integration verification is complete.
- Do not start Stage 8 code review until Stage 7 is `Pass`.
- Do not start Stage 9 docs sync until Stage 8 is complete.
- After Stage 9, keep Stage 10 open until the user explicitly confirms completion or verification.
- Do not move the ticket to `done`, commit, push, merge, or release before that explicit user signal.
- For git repositories, Stage 10 finalization uses the Stage 0 resolved base remote and base branch as the default merge target unless the user later overrides it.
- If move-to-done, commit, push, merge, or release fails, keep Stage 10 open and record the blocker in `workflow-state.md`.

## Canonical Stage Sequence

| Stage | Purpose | Primary Artifact / Gate | Code Edit Permission | Local Guidance |
| --- | --- | --- | --- | --- |
| 0 | Bootstrap ticket context and capture initial requirement intent | `workflow-state.md` initialized + `requirements.md = Draft` | Locked | `stages/00-bootstrap/README.md`, `stages/00-bootstrap/bootstrap-checklist.md` |
| 1 | Build current-state understanding and triage scope | `investigation-notes.md` current + `Small` / `Medium` / `Large` triage | Locked | `stages/01-investigation/README.md`, `stages/01-investigation/investigation-guide.md` |
| 2 | Refine requirements into a design-ready contract | `requirements.md = Design-ready` or `Refined` | Locked | `stages/02-requirements/README.md`, `stages/02-requirements/requirements-refinement-guide.md` |
| 3 | Define the target architecture and ownership model | `Small`: design section in `implementation.md`; `Medium` / `Large`: `proposed-design.md` | Locked | `stages/03-design/README.md`, `stages/03-design/design-guide.md`, `stages/03-design/proposed-design-template.md` |
| 4 | Model future-state runtime behavior | `future-state-runtime-call-stack.md` | Locked | `stages/04-future-state-runtime-call-stack/README.md`, `stages/04-future-state-runtime-call-stack/future-state-runtime-call-stack-template.md` |
| 5 | Deep-review the future-state runtime model and unlock implementation | `future-state-runtime-call-stack-review.md` with `Go Confirmed` | Locked | `stages/05-future-state-runtime-call-stack-review/README.md`, `stages/05-future-state-runtime-call-stack-review/call-stack-review-guide.md`, `stages/05-future-state-runtime-call-stack-review/future-state-runtime-call-stack-review-template.md` |
| 6 | Implement source changes and complete unit/integration verification | `implementation.md` current + source implementation complete | Unlocked | `stages/06-implementation/README.md`, `stages/06-implementation/implementation-guide.md`, `stages/06-implementation/implementation-template.md` |
| 7 | Validate acceptance criteria and runtime spines through API/E2E scenarios | `api-e2e-testing.md` + Stage 7 gate result | Unlocked | `stages/07-api-e2e/README.md`, `stages/07-api-e2e/api-e2e-guide.md`, `stages/07-api-e2e/api-e2e-testing-template.md` |
| 8 | Run the independent code-review gate | `code-review.md` + Stage 8 decision | Locked | `stages/08-code-review/README.md`, `stages/08-code-review/code-review-guide.md`, `stages/08-code-review/code-review-principles.md`, `stages/08-code-review/code-review-template.md` |
| 9 | Promote durable knowledge into long-lived docs | `docs-sync.md` + docs updated or `No impact` rationale | Locked | `stages/09-docs-sync/README.md`, `stages/09-docs-sync/docs-sync-guide.md`, `stages/09-docs-sync/docs-sync-template.md` |
| 10 | Persist handoff, wait for explicit user verification, archive, and finalize | `handoff-summary.md` + optional `release-notes.md` + finalization record | Locked | `stages/10-handoff/README.md`, `stages/10-handoff/handoff-guide.md`, `stages/10-handoff/handoff-summary-template.md`, `stages/10-handoff/release-notes-template.md` |

## Stage Transition Contract

| Stage | Exit Condition | On Fail / Blocked | Next Stage On Pass |
| --- | --- | --- | --- |
| 0 | Ticket/worktree bootstrap is complete and `requirements.md` exists as `Draft` | Stay in `0` until bootstrap evidence is complete | `1` |
| 1 | `investigation-notes.md` is current and scope triage is recorded | Stay in `1` until the understanding pass is complete | `2` |
| 2 | `requirements.md` is `Design-ready` or `Refined` and usable as design input | Stay in `2` until the requirements are design-ready | `3` |
| 3 | The design basis is current for the ticket scope | Stay in `3` and revise the design basis | `4` |
| 4 | `future-state-runtime-call-stack.md` is current for in-scope use cases | Stay in `4` and regenerate the call stacks | `5` |
| 5 | `Go Confirmed`: two consecutive clean deep-review rounds with no blockers, no required persisted updates, and no newly discovered use cases | Classified re-entry before the next review round | `6` |
| 6 | Source implementation is complete, required unit/integration verification passes, cleanup is complete in scope, and ownership/placement quality is preserved | Local fixes stay in `6`; non-local issues trigger classified re-entry | `7` |
| 7 | Executable in-scope acceptance criteria are `Passed` or explicitly user-`Waived`, and relevant executable spines have evidence | `Blocked` on infeasible/no waiver; otherwise classified re-entry | `8` |
| 8 | The independent code-review decision is `Pass` with all mandatory review checks satisfied | Classified re-entry based on review finding type | `9` |
| 9 | `docs-sync.md` is current and docs are updated or explicit no-impact rationale is recorded | Stay in `9` until docs sync is complete | `10` |
| 10 | Handoff summary is complete, explicit user verification is received, ticket is moved to `done`, and required git finalization is complete when applicable | Stay in `10` until verification and finalization are complete | End |

## Transition Matrix

| Trigger | Required Transition Path | Notes |
| --- | --- | --- |
| Normal forward pass | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10` | Use only when each stage gate passes. |
| Stage 5 blocker `Design Impact` | `3 -> 4 -> 5` | Use when the issue is clearly in spine, ownership, support structure, boundaries, or naming. |
| Stage 5 blocker `Requirement Gap` | `2 -> 3 -> 4 -> 5` | Use when requirements or acceptance criteria are missing or ambiguous. |
| Stage 5 blocker `Unclear` | `1 -> 2 -> 3 -> 4 -> 5` | Use when investigation must be refreshed first. |
| Stage 6 failure `Local Fix` | stay in `6` | Fix within Stage 6; do not advance to Stage 7. |
| Stage 6 failure `Design Impact` | `1 -> 3 -> 4 -> 5 -> 6` | Re-open investigation checkpoint, then return through design/runtime review. |
| Stage 6 failure `Requirement Gap` | `2 -> 3 -> 4 -> 5 -> 6` | Update requirements first, then rerun downstream stages. |
| Stage 6 failure `Unclear` | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6` | Re-open Stage 0 controls in the same ticket context and rerun the chain. |
| Stage 7 failure `Local Fix` | `6 -> 7` | Update artifacts first, then apply the fix and rerun Stage 7. |
| Stage 7 failure `Design Impact` | `1 -> 3 -> 4 -> 5 -> 6 -> 7` | Re-open investigation, then rerun design/runtime/implementation chain. |
| Stage 7 failure `Requirement Gap` | `2 -> 3 -> 4 -> 5 -> 6 -> 7` | Update requirements first, then rerun downstream stages. |
| Stage 7 failure `Unclear` | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7` | Re-open Stage 0 controls in the same ticket context and rerun the full chain. |
| Stage 7 infeasible scenario without user waiver | stay in `Stage 7 (Blocked)` | Record constraints, compensating evidence, and residual risk. |
| Stage 8 failure `Local Fix` | `6 -> 7 -> 8` | Apply the fix and rerun testing before re-review. |
| Stage 8 failure `Validation Gap` | `7 -> 8` | Strengthen Stage 7 evidence first, then rerun code review. |
| Stage 8 failure `Design Impact` | `1 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | Review discovered a structural problem in code or earlier design. |
| Stage 8 failure `Requirement Gap` | `2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | Review exposed missing or ambiguous intended behavior. |
| Stage 8 failure `Unclear` | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | Root cause is cross-cutting or confidence is too low. |
| Stage 10 awaiting explicit user verification | stay in `Stage 10 (In Progress)` | Wait for explicit user confirmation before archive/finalization. |
| Stage 10 archival or repository finalization blocked | stay in `Stage 10 (Blocked)` | Record the blocker and finish Stage 10 only after it is resolved. |

## Default Artifact Paths

If the user does not specify file paths, use the project-local ticket folder:

- `tickets/in-progress/<ticket-name>/workflow-state.md`
- `tickets/in-progress/<ticket-name>/requirements.md`
- `tickets/in-progress/<ticket-name>/investigation-notes.md`
- `tickets/in-progress/<ticket-name>/proposed-design.md` when `Medium` / `Large`
- `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack.md`
- `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack-review.md`
- `tickets/in-progress/<ticket-name>/implementation.md`
- `tickets/in-progress/<ticket-name>/api-e2e-testing.md`
- `tickets/in-progress/<ticket-name>/code-review.md`
- `tickets/in-progress/<ticket-name>/docs-sync.md`
- `tickets/in-progress/<ticket-name>/handoff-summary.md`
- `tickets/in-progress/<ticket-name>/release-notes.md` when required

`Small` scope still uses the same ticket folder; it simply keeps the Stage 3 design basis inside `implementation.md` instead of requiring a separate `proposed-design.md`.

## Stage Files

Use the stage-owned files before inventing new workflow prose:

- Stage 0: `stages/00-bootstrap/README.md`, `stages/00-bootstrap/bootstrap-checklist.md`
- Stage 1: `stages/01-investigation/README.md`, `stages/01-investigation/investigation-guide.md`
- Stage 2: `stages/02-requirements/README.md`, `stages/02-requirements/requirements-refinement-guide.md`
- Stage 3: `stages/03-design/README.md`, `stages/03-design/design-guide.md`, `stages/03-design/proposed-design-template.md`
- Stage 4: `stages/04-future-state-runtime-call-stack/README.md`, `stages/04-future-state-runtime-call-stack/future-state-runtime-call-stack-template.md`
- Stage 5: `stages/05-future-state-runtime-call-stack-review/README.md`, `stages/05-future-state-runtime-call-stack-review/call-stack-review-guide.md`, `stages/05-future-state-runtime-call-stack-review/future-state-runtime-call-stack-review-template.md`
- Stage 6: `stages/06-implementation/README.md`, `stages/06-implementation/implementation-guide.md`, `stages/06-implementation/implementation-template.md`, `stages/06-implementation/implementation-example.md`
- Stage 7: `stages/07-api-e2e/README.md`, `stages/07-api-e2e/api-e2e-guide.md`, `stages/07-api-e2e/api-e2e-testing-template.md`
- Stage 8: `stages/08-code-review/README.md`, `stages/08-code-review/code-review-guide.md`, `stages/08-code-review/code-review-principles.md`, `stages/08-code-review/code-review-template.md`
- Stage 9: `stages/09-docs-sync/README.md`, `stages/09-docs-sync/docs-sync-guide.md`, `stages/09-docs-sync/docs-sync-template.md`
- Stage 10: `stages/10-handoff/README.md`, `stages/10-handoff/handoff-guide.md`, `stages/10-handoff/handoff-summary-template.md`, `stages/10-handoff/release-notes-template.md`
