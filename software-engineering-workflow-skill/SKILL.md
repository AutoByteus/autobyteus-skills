---
name: software-engineering-workflow-skill
description: "Run a staged software-engineering delivery feedback loop from bootstrap through investigation, requirements, design, runtime review, implementation, API/E2E and executable validation, code review, docs sync, and final handoff with durable artifacts and explicit re-entry."
---

# Software Engineering Workflow Skill

## Overview

Run a staged software-engineering delivery workflow for software changes: bootstrap ticket context, investigate and refine requirements, build design and future-state runtime artifacts, drive implementation with one implementation artifact that carries both a stable baseline and live progress tracking, validate behavior with API/E2E and other executable validation evidence appropriate to the system, apply independent code review, synchronize long-lived docs, and finish with explicit user-verified handoff and repository finalization. For medium/large scope, include a full proposed design document organized by data-flow spine inventory, ownership, off-spine concerns, and derived separation of concerns.
This workflow is stage-gated. Do not batch-generate all artifacts by default.
In this skill, future-state runtime call stacks are future-state (`to-be`) execution models. They are not traces of current (`as-is`) implementation behavior.

## Skill Layout

- `SKILL.md` is the workflow router. It defines the stage rules and points each stage to its owned templates/references.
- `shared/` stores cross-stage references that multiple stages reuse:
  - `shared/design-principles.md`
  - `shared/common-design-practices.md`
  - `shared/workflow-state-template.md`
- `stages/` stores stage-owned templates and references:
  - `stages/00-bootstrap/`
  - `stages/01-investigation/`
  - `stages/02-requirements/`
  - `stages/03-design/`
  - `stages/04-future-state-runtime-call-stack/`
  - `stages/05-future-state-runtime-call-stack-review/`
  - `stages/06-implementation/`
  - `stages/07-api-e2e/`
  - `stages/08-code-review/`
  - `stages/09-docs-sync/`
  - `stages/10-handoff/`
- Keep stage-specific material in the matching stage folder. Use `shared/` only for genuinely cross-stage references.
- When a stage has a local guide or checklist, use that stage-owned file first before falling back to generic workflow prose.

## Terminology

- `Subsystem` / `capability area`: a larger functional area that owns a broader category of work and may contain multiple files plus optional module groupings.
- `Module`: an optional intermediate grouping inside a subsystem when the codebase benefits from it. In this skill, `module` is not a synonym for one file or the default ownership term.
- `Folder` / `directory`: a physical grouping used to organize files and any optional module groupings.
- `File`: one concrete source file and the primary unit where one concrete concern should land.

## Workflow

### Ticket Folder Convention (Project-Local)

- For each task, create/use one ticket folder under `tickets/in-progress/`.
- Folder naming: use a clear, short kebab-case name (no date prefix required).
- Write all task planning artifacts into the `in-progress` ticket folder while work is active.
- Standard states:
  - active work path: `tickets/in-progress/<ticket-name>/`
  - completed archive path: `tickets/done/<ticket-name>/`
- Move rule (mandatory): move a ticket from `in-progress` to `done` only when the user explicitly confirms completion (for example: "done", "finished", or "verified") or explicitly asks to move it.
- Final archive ordering rule (mandatory): when explicit user completion/verification also triggers repository finalization, move the ticket folder to `tickets/done/<ticket-name>/` before the final commit so the committed state includes the archived ticket path.
- Reopen rule (mandatory): if the user asks to continue/reopen a completed ticket, move it from `tickets/done/<ticket-name>/` back to `tickets/in-progress/<ticket-name>/` before making new updates.
- Never auto-move a ticket to `done` based only on internal assessment.
- If the user specifies a different location, follow the user-specified path.

### Ticket + Worktree Bootstrap (Mandatory First Action)

- Before investigation, bootstrap work context in this order:
  - create/use `tickets/in-progress/<ticket-name>/`,
  - if the project is a git repository:
    - resolve the bootstrap base branch from explicit user instruction when provided; otherwise infer the tracked remote default/integration branch with highest confidence,
    - when creating a new ticket worktree/branch, refresh tracked remote refs first so bootstrap starts from the latest remote state instead of a stale local head,
    - create/reuse a dedicated ticket worktree for the ticket branch before writing artifacts,
    - when creating a new ticket branch, create `codex/<ticket-name>` from the latest tracked remote base branch,
  - create/update `requirements.md` with status `Draft` from user-provided requirement intent.
- Investigation must not start before the ticket bootstrap and `requirements.md` `Draft` are physically written.
- If a dedicated worktree already exists for the ticket, reuse it instead of creating a new one.
- If the user specifies a base branch, always use the latest tracked remote state of that branch rather than guessing from a local copy.
- If remote refresh or base-branch resolution fails, keep Stage 0 `Blocked` and record the blocker before investigation.
- If the environment is not a git repository, continue without worktree setup and still enforce ticket-folder + `Draft` requirement capture.

### Workflow State File (Mandatory Enforcement Artifact)

- Create and maintain `tickets/in-progress/<ticket-name>/workflow-state.md` as the canonical stage-control artifact.
- Initialize it during Stage 0 immediately after ticket bootstrap with:
  - `Current Stage = 0`,
  - `Code Edit Permission = Locked`,
  - `Stage 0 Bootstrap Record` filled with bootstrap mode plus, when git repo, requested base branch if any, resolved base remote/base branch, remote-refresh result when performed, worktree path, and ticket branch,
  - stage gate rows in `Not Started`/`In Progress` state.
- Update model (mandatory):
  - rewrite `Current Snapshot` in place on every stage transition,
  - append one row to `Transition Log` for every transition/re-entry,
  - keep `Stage Gates` rows current with evidence links/paths.
- Source-code edit lock (hard rule):
  - no source code edits are allowed unless `workflow-state.md` explicitly shows `Code Edit Permission = Unlocked`,
  - default state is `Locked`; unlock source-code edits only when Stage 6 prerequisites are satisfied.
- Re-entry lock rule:
  - on any Stage 7/8 failure, set `Code Edit Permission = Locked` before re-entry actions,
  - record trigger/classification/return path in `workflow-state.md` before proceeding.
- Violation protocol:
  - if source code is edited while `Code Edit Permission = Locked`, record a violation entry in `workflow-state.md`,
  - pause further source edits, declare re-entry, and return to the required upstream stage path.

### Audible Notifications (Speak Tool, Required)

- Use the `Speak` tool for workflow-state transition updates so the user can follow where execution is and what is next.
- Playback rule (mandatory): for required audible notifications, call `Speak` with `play=true` explicitly.
- Do not set `play=false` by default for required transition notifications.
- Exception: set `play=false` only when the user explicitly requests silent mode.
- Transition-driven speak rule (mandatory):
  - speak only when `workflow-state.md` is updated for a stage transition, gate decision, re-entry decision, or code-edit lock/unlock change,
  - do not speak for low-level command execution, intermediate analysis notes, or partial drafts.
- Required audible events:
  - workflow kickoff (`task accepted`, `next stage`),
  - every stage transition (`From Stage -> To Stage`) after `workflow-state.md` transition log is appended,
  - every gate decision (`Pass`/`Fail`/`Blocked`) after gate evidence is written,
  - every re-entry declaration (classification + return path) after `workflow-state.md` re-entry section is updated,
  - every `Code Edit Permission` change (`Locked`/`Unlocked`) after snapshot update.
- Speak ordering rule:
  - update `workflow-state.md` first,
  - then emit audible notification reflecting the persisted state.
- Spoken message content (mandatory):
  - current stage,
  - what just completed/changed (transition or gate result),
  - next stage/action,
  - code-edit lock state when it changed.
- If multiple transitions happen close together, batch them into one short message after the final persisted update.
- Keep each spoken message short (1-2 sentences), status-first, and action-oriented.
- If the `Speak` tool fails or is unavailable, continue the workflow and provide the same update in text.
- Do not speak secrets, tokens, or full sensitive payloads.

### Execution Model (Strict Stage Gates)

- Work in explicit stages and complete each gate before producing downstream artifacts.
- Before every stage transition, update `workflow-state.md` first (snapshot + transition log + gate statuses), then proceed.
- Treat `workflow-state.md` as an execution lock controller, not optional documentation.
- Transition authority rule (mandatory): stage movement is controlled by the Stage Transition Contract + Transition Matrix. When a trigger condition is met, transition immediately to the mapped path; do not continue in the current stage by preference.
- Transition Execution Rule (mandatory): whenever `workflow-state.md` is updated to declare a stage transition or classified re-entry, immediately enter and execute the target stage by default, without waiting for another user message. Recording the transition and describing the next step is not sufficient. The transition is not complete until work has actually resumed in the target stage. Stop only for a real blocker or an explicit user-only gate.
- Requirements can start as rough `Draft` from user input/bug report artifacts before deep analysis.
- Do not start investigation until ticket/worktree bootstrap is complete and `requirements.md` status `Draft` is physically written.
- Do not mark understanding pass complete until `investigation-notes.md` is physically written and current for the ticket.
- Do not draft design artifacts (`proposed-design.md` or small-scope solution sketch in `implementation.md`) until deep understanding pass is complete and `requirements.md` reaches `Design-ready`.
- Do not finalize `implementation.md` baseline sections or start execution tracking sections until the future-state runtime call stack review gate is fully satisfied for the current scope.
- Do not start implementation execution until `implementation.md` baseline is finalized and its execution-tracking sections are initialized.
- Do not start source-code edits until all of the following are true in `workflow-state.md`:
  - `Current Stage = 6`,
  - `Code Edit Permission = Unlocked`,
  - Stage 5 gate is `Go Confirmed`,
  - required upstream artifacts are marked `Pass` with evidence.
- Do not start Stage 7 executable-validation implementation and execution until implementation execution is complete with required unit/integration verification and Stage 6 modernization/ownership-dependency checks are satisfied.
- Do not start code review until the Stage 7 executable-validation gate is `Pass`.
- Do not start post-testing `docs/` synchronization until code review is complete (for infeasible acceptance criteria in Stage 7, explicit user waiver + constraints + compensating evidence + residual risk must be recorded).
- Do not close the task until post-testing `docs/` synchronization is completed (or explicit no-impact decision is recorded with rationale), and do not mark final completion until any required Stage 10 user-verification/archive/finalization work is complete.
- User-verification hold rule (mandatory): after Stage 9 passes, persist the handoff summary and keep Stage 10 open until the user explicitly confirms completion/verification (for example after manual testing). Do not commit, push, merge, run release/publication/deployment work, or move the ticket to `done` before that user signal.
- Release-notes artifact rule (mandatory when applicable): if the ticket leads to a user-facing app release or any GitHub Release body, Stage 10 must also persist `tickets/in-progress/<ticket-name>/release-notes.md` with short functional user-facing notes before final release. If not applicable, record an explicit `release-notes not required` rationale in the handoff summary.
- Repository finalization rule (mandatory for git repositories): after the explicit user completion/verification signal is received and before Stage 10 is marked complete, first move the ticket folder to `tickets/done/<ticket-name>/`, then commit all in-scope changes on the ticket branch (including the moved ticket files), push the ticket branch to remote, update the resolved finalization target branch from remote, merge the ticket branch into that updated target branch locally, and push the updated target branch.
- Release/publication/deployment rule (conditional): after repository finalization, if the project has an applicable documented release, publication, tagging, or deployment step, run that project-specific method. This may be a release script, a documented command, a git tag workflow, GitHub Release creation, or another documented deployment/publication path. If no such step is applicable, record `release/publication/deployment not required` (or equivalent rationale) in the handoff summary instead of blocking repository finalization.
- Release publication handoff rule (mandatory when release notes are required): after the ticket is moved to `tickets/done/<ticket-name>/`, pass the archived ticket-local `tickets/done/<ticket-name>/release-notes.md` artifact into the project release/publication path when such a step is applicable (for example via a release script, a documented command, a tag/release workflow, or the repo's release-body source file).
- Finalization-target rule (mandatory): use the Stage 0 `Resolved Base Remote` and `Resolved Base Branch` as the default Stage 10 merge target unless the user explicitly overrides that target later. If the target cannot be derived with high confidence, pause Stage 10 and ask once before merge/finalization instead of guessing.
- Post-finalization cleanup rule (mandatory when a dedicated ticket worktree/branch exists): after repository finalization and any applicable release/publication/deployment work are complete (or explicitly recorded as not required), remove the dedicated ticket worktree recorded in Stage 0, run worktree-prune cleanup, and, when the local ticket branch is fully merged into the resolved finalization target and no longer needed, delete that local ticket branch. Do not delete remote branches unless explicit user instruction or documented project policy requires it. If cleanup requires stepping out of the ticket worktree, execute it from a safe parent repo checkout instead of skipping it.
- Stage 10 blockage rule (mandatory): if the move to `tickets/done/`, commit, push, target-branch update, merge, or required post-finalization cleanup fails after user confirmation, keep Stage 10 `In Progress`/`Blocked`, record the blocker in `workflow-state.md`, and do not mark final handoff complete. If a release/publication/deployment step is applicable and later fails or is undocumented, record that blocker too, but do not undo completed repository finalization.
- Keep the ticket folder under `tickets/in-progress/` until explicit user completion confirmation is received.
- Treat engineering completion, user verification, ticket archival, repository finalization, release/publication/deployment, and post-finalization cleanup as separate gates: engineering completion ends at implementation + Stage 7 executable-validation gate + code review + docs sync; after that, wait for explicit user completion/verification; only then move the ticket to `tickets/done/`, complete required Stage 10 repository finalization, run any applicable release/publication/deployment work, and complete any required worktree/branch cleanup.
- `Small` scope exception: drafting `implementation.md` (solution sketch section only) before review is allowed as design input, but this draft does not unlock implementation kickoff.
- Future-state runtime call stack review must run as iterative deep-review rounds (not one-pass review).
- `Go Confirmed` cannot be declared immediately after required upstream artifact updates from a blocking round.
- Stability rule (mandatory): unlock `Go Confirmed` only after two consecutive deep-review rounds report no blockers, no required persisted artifact updates, and no newly discovered use cases.
- First clean round is provisional (`Candidate Go`), second consecutive clean round is confirmation (`Go Confirmed`).
- Missing-use-case discovery rule (mandatory): every Stage 5 round must run a dedicated missing-use-case discovery sweep (requirement coverage, boundary crossings, fallback/error branches, and design-risk scenarios).
- A Stage 5 round is not clean if it discovers new use cases, requires persisted artifact updates, or finds blockers.
- Any review finding with a required design/call-stack update is blocking; regenerate affected artifacts and re-review before proceeding.
- If design/review reveals missing understanding or requirement ambiguity, return to understanding + requirements stages, update `requirements.md`, then continue design/review.
- Stage 5 classified re-entry mapping (mandatory):
  - `Design Impact` (clear spine/ownership/boundary/naming/architecture issue with high confidence): return to `Stage 3 -> Stage 4 -> Stage 5`.
  - `Requirement Gap` (missing/ambiguous requirement or acceptance criterion): return to `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5`.
  - `Unclear` (cross-cutting scope or low root-cause confidence): return to `Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5`.
- For any Stage 5 blocking round, record classification + return path in `future-state-runtime-call-stack-review.md` and `workflow-state.md` before starting the next round.
- Stage 6 non-local re-entry rule (mandatory): if a Stage 6 issue is classified as `Design Impact`, `Requirement Gap`, or `Unclear`, record classification + return path in `workflow-state.md`, set `Code Edit Permission = Locked`, and transition to the mapped upstream stage path before further source edits.
- Re-entry declaration rule (mandatory): when a post-implementation gate (`Stage 7` executable validation or `Stage 8` code review) finds issues, explicitly record:
  - trigger stage (`7`/`8`),
  - classification (`Local Fix`/`Validation Gap`/`Design Impact`/`Requirement Gap`/`Unclear`),
  - required return stage path before any code edit.
- Re-entry declaration must be recorded in `workflow-state.md` before any artifact/code update work begins.
- Re-entry Completion Rule (mandatory): after a classified re-entry is recorded and the target return path is persisted in `workflow-state.md`, immediately resume the first returned stage by default, without waiting for another user message. Do not stop after only updating state and describing what should happen next. Re-entry is not complete until work has actually resumed in that returned stage.
- No-direct-patch rule (mandatory): for post-implementation gate findings, do not edit source code first. Update required upstream artifacts first based on classification path.
- Re-entry mapping (mandatory):
  - `Local Fix`: update implementation artifacts (`implementation.md` / `api-e2e-testing.md` / `code-review.md` as applicable), then implement fix, then rerun `Stage 6 -> Stage 7`; once Stage 7 passes, continue to `Stage 8`.
  - `Design Impact`: return to `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`; once Stage 7 passes, continue to `Stage 8`.
  - `Requirement Gap`: return to `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`; once Stage 7 passes, continue to `Stage 8`.
  - `Unclear` (or cross-cutting root cause): return to `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`; once Stage 7 passes, continue to `Stage 8`.
- Stage 0 in a re-entry path means re-open bootstrap controls in the same ticket/worktree (`workflow-state.md`, lock state, artifact baselines); do not create a new ticket folder.
- If the user asks for all artifacts in one turn, still enforce stage gates within that turn (iterate review rounds first; only then produce implementation artifacts).
- Stage-first persistence rule: if a Stage 5 round finds issues, first record classification + return path and transition to the required upstream stage in `workflow-state.md`, then persist required artifact updates in that stage.
- No mental-only review refinements: do not carry unresolved updates in memory across rounds.
- For each review round, record explicit persisted artifact updates in `future-state-runtime-call-stack-review.md`:
  - updated files,
  - new artifact versions,
  - changed sections,
  - which findings were resolved.
- A review round cannot be considered complete until its required file updates are physically written.
- If announcing review-round status, do it only after the round record + required staged artifact updates are physically written and the related Stage 5 gate status is persisted in `workflow-state.md`.

### Canonical Stage Sequence (Quick Map)

| Stage | Name | Core Deliverable/Gate | Code Edit Permission |
| --- | --- | --- | --- |
| 0 | Bootstrap + Draft Requirement | Ticket/worktree bootstrap complete (ticket path + if git repo: base branch resolved from tracked remote, remote freshness handled for new bootstrap, dedicated ticket worktree/branch created or reused) + `requirements.md` = `Draft` | Locked |
| 1 | Investigation + Triage | `investigation-notes.md` current + scope triage complete | Locked |
| 2 | Requirements Refinement | `requirements.md` reaches `Design-ready`/`Refined` | Locked |
| 3 | Design Basis | `implementation.md` solution sketch (`Small`) or `proposed-design.md` (`Medium/Large`) | Locked |
| 4 | Future-State Runtime Call Stack | `future-state-runtime-call-stack.md` current | Locked |
| 5 | Future-State Runtime Call Stack Review | `Go Confirmed` (two consecutive clean rounds with no blockers/persisted updates/new use cases) | Locked |
| 6 | Source Implementation + Unit/Integration | Source code + required unit/integration checks complete + no backward-compat/legacy retention + ownership-driven dependency quality preserved + boundary encapsulation preserved + touched files correctly placed | Unlocked |
| 7 | API/E2E + Executable Validation Gate | executable validation scenarios implemented and acceptance-criteria + spine coverage closure complete | Unlocked |
| 8 | Code Review Gate | Code review decision recorded (`Pass`/`Fail`) with `<=500` effective-line hard-limit on changed source files only + required `>220` delta-gate assessments on changed source files only + data-flow spine inventory/ownership/off-spine concern checks + existing-capability reuse + reusable-owned-structure extraction + shared-structure/data-model tightness + shared-base coherence + repeated-coordination ownership + empty-indirection + scope-appropriate separation of concerns + ownership-driven dependency quality + boundary encapsulation preservation + file placement within the correct subsystem and folder, with any optional module grouping justified + flat-vs-over-split layout judgment + interface-boundary clarity + naming quality across files/folders/APIs/types/functions/parameters/variables + naming-to-responsibility alignment + no unjustified duplication of code/repeated structures in changed scope + patch-on-patch complexity control + test quality + test maintainability + validation-evidence sufficiency + no-backward-compat/no-legacy checks | Locked |
| 9 | Docs Sync | `docs-sync.md` current + `docs/` updates complete or no-impact rationale recorded | Locked |
| 10 | Final Handoff | Delivery summary ready + explicit user verification -> move ticket to `done` -> repository finalization into resolved target branch (when git repo) + any applicable release/publication/deployment step completed or explicitly recorded as not required + required post-finalization worktree/branch cleanup complete when applicable + ticket state decision recorded | Locked |

### Stage Transition Contract (Enforcement)

| Stage | Exit Condition (Must Be True To Transition) | On Fail/Blocked | Next Stage On Pass |
| --- | --- | --- | --- |
| 0 Bootstrap + Draft Requirement | Ticket/worktree bootstrap is complete, the base branch/worktree decision is recorded, and `requirements.md` status is `Draft` | Stay in `0` until bootstrap is complete | `1` |
| 1 Investigation + Triage | `investigation-notes.md` is current and scope triage (`Small`/`Medium`/`Large`) is recorded | Stay in `1` until investigation evidence is complete | `2` |
| 2 Requirements | `requirements.md` is `Design-ready` (or `Refined`) with requirement/acceptance-criteria coverage maps | Stay in `2` until requirements are design-ready | `3` |
| 3 Design Basis | Design basis artifact is current (`implementation.md` solution sketch for `Small`, `proposed-design.md` for `Medium/Large`) | Stay in `3` and revise design basis | `4` |
| 4 Future-State Runtime Call Stack | `future-state-runtime-call-stack.md` is current for in-scope use cases | Stay in `4` and regenerate the future-state runtime call stack | `5` |
| 5 Future-State Runtime Call Stack Review | Future-state runtime call stack review reaches `Go Confirmed` (two consecutive clean rounds with no blockers, no required persisted artifact updates, and no newly discovered use cases) | Classified re-entry before next review round (`Design Impact`: `3 -> 4 -> 5`, `Requirement Gap`: `2 -> 3 -> 4 -> 5`, `Unclear`: `1 -> 2 -> 3 -> 4 -> 5`) | `6` |
| 6 Source + Unit/Integration | Source implementation complete, required unit/integration checks pass, no backward-compatibility/legacy-retention paths remain in scope, ownership-driven dependencies remain valid (no new unjustified cycles/tight coupling), boundary encapsulation remains valid (no new bypass of authoritative boundaries), and touched files sit in the correct folder under the correct owning subsystem | Local issues: stay in `6`; classified re-entry for non-local issues (`Design Impact`: `1 -> 3 -> 4 -> 5 -> 6`, `Requirement Gap`: `2 -> 3 -> 4 -> 5 -> 6`, `Unclear`: `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6`) | `7` |
| 7 API/E2E + Executable Validation Gate | executable validation scenarios are implemented and all executable mapped acceptance criteria are `Passed` (or explicitly `Waived` by user for infeasible cases), and all relevant executable spines have passing scenario evidence (or explicit `N/A` rationale) | `Blocked` on infeasible/no waiver; otherwise re-enter by classification (`Local Fix`: `6 -> 7`, `Design Impact`: `1 -> 3 -> 4 -> 5 -> 6 -> 7`, `Requirement Gap`: `2 -> 3 -> 4 -> 5 -> 6 -> 7`, `Unclear`: `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7`) | `8` |
| 8 Code Review Gate | Code review decision is `Pass` with all mandatory review checks satisfied (including `<=500` effective-line hard-limit on changed source files only + required `>220` delta-gate assessments on changed source files only + data-flow spine inventory/ownership/off-spine concern checks + existing-capability reuse + reusable-owned-structure extraction + shared-structure/data-model tightness + shared-base coherence + repeated-coordination ownership + empty-indirection + scope-appropriate separation of concerns + ownership-driven dependency quality + boundary encapsulation preservation + file placement within the correct subsystem and folder, with any optional module grouping justified + flat-vs-over-split layout judgment + interface/API/query/command/service-method boundary clarity + naming quality across files/folders/APIs/types/functions/parameters/variables + naming-to-responsibility alignment + no unjustified duplication of code/repeated structures in changed scope + patch-on-patch complexity control + test quality + test maintainability + validation-evidence sufficiency + no-backward-compat/no-legacy) | Re-enter by classification (`Local Fix`: `6 -> 7 -> 8`, `Validation Gap`: `7 -> 8`, `Design Impact`: `1 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8`, `Requirement Gap`: `2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8`, `Unclear`: `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8`) | `9` |
| 9 Docs Sync | `docs-sync.md` is current and docs updates are completed, or explicit no-impact rationale is recorded | If docs cannot yet be made truthful, classify and re-enter (`Local Fix`: `6 -> 7 -> 8 -> 9`, `Requirement Gap`: `2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9`, `Unclear`: `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9`); stay in `9 (Blocked)` only for external docs blockers that do not require upstream artifact changes | `10` |
| 10 Final Handoff | Handoff summary is complete, explicit user completion/verification instruction is received, the ticket has been moved to `tickets/done/<ticket-name>/`, and, when in a git repository, repository finalization is complete, any applicable release/publication/deployment step is complete or explicitly recorded as not required, and required post-finalization worktree/branch cleanup is complete when applicable | Stay in `Stage 10` until the user verifies completion and Stage 10 archival/finalization/cleanup is complete | End |

### Transition Matrix (Pass/Fail/Blocked)

| Trigger | Required Transition Path | Notes |
| --- | --- | --- |
| Normal forward pass | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10` | Use only when each stage gate is `Pass`. |
| Stage 5 blocker classified `Design Impact` | `3 -> 4 -> 5` | Use when issue is clearly in spine/ownership/off-spine concern/boundary/naming decisions. |
| Stage 5 blocker classified `Requirement Gap` | `2 -> 3 -> 4 -> 5` | Use when missing/ambiguous requirement or acceptance criteria is discovered. |
| Stage 5 blocker classified `Unclear` | `1 -> 2 -> 3 -> 4 -> 5` | Use when root cause is uncertain or cross-cutting and investigation must be refreshed first. |
| Stage 6 failure classified `Local Fix` | stay in `Stage 6` | Fix implementation/tests within Stage 6; do not advance to Stage 7. |
| Stage 6 failure classified `Design Impact` | `1 -> 3 -> 4 -> 5 -> 6` | Re-open investigation checkpoint, then re-enter design/runtime chain before continuing implementation. |
| Stage 6 failure classified `Requirement Gap` | `2 -> 3 -> 4 -> 5 -> 6` | Update requirements first, then rerun downstream chain before continuing implementation. |
| Stage 6 failure (`Unclear`/cross-cutting root cause) | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6` | Re-open Stage 0 controls in the same ticket context, then rerun full chain before continuing implementation. |
| Stage 7 failure classified `Local Fix` | `6 -> 7` | Update artifacts first, then code fix, then rerun Stage 7 scenarios. |
| Stage 7 failure classified `Design Impact` | `1 -> 3 -> 4 -> 5 -> 6 -> 7` | Re-open investigation, then re-enter design/runtime chain before retrying Stage 7. |
| Stage 7 failure classified `Requirement Gap` | `2 -> 3 -> 4 -> 5 -> 6 -> 7` | Update requirements first, then rerun downstream chain. |
| Stage 7 failure (`Unclear`/cross-cutting root cause) | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7` | Re-open Stage 0 controls in the same ticket context, then rerun full chain. |
| Stage 7 infeasible scenario without user waiver | stay in `Stage 7 (Blocked)` | Record constraints + compensating evidence; wait for explicit user waiver or environment fix. |
| Stage 8 fail classified `Local Fix` | `6 -> 7 -> 8` | Apply fix and rerun test gate before re-review. |
| Stage 8 fail classified `Validation Gap` | `7 -> 8` | Strengthen Stage 7 coverage/evidence first, then rerun code review. |
| Stage 8 fail classified `Design Impact` | `1 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | Re-open investigation, then return to design chain before re-review. |
| Stage 8 fail classified `Requirement Gap` | `2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | Return to requirements then rerun full downstream chain. |
| Stage 8 failure (`Unclear`/cross-cutting root cause) | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | Re-open Stage 0 controls in the same ticket context, then rerun full chain before re-review. |
| Stage 9 blocked docs-sync result classified `Local Fix` | `6 -> 7 -> 8 -> 9` | Use when docs cannot yet be made truthful until a small concrete implementation or ticket-artifact correction is completed. |
| Stage 9 blocked docs-sync result classified `Requirement Gap` | `2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9` | Use when missing or ambiguous intended behavior prevents truthful docs. |
| Stage 9 blocked docs-sync result classified `Unclear` | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9` | Use when final behavior is too unclear or cross-cutting to document truthfully. |
| Stage 9 blocked by external docs/access issue only | stay in `Stage 9 (Blocked)` | Use when no upstream artifact changes are needed and the blocker is purely docs-environment or docs-access related. |
| Stage 10 awaiting explicit user verification | stay in `Stage 10 (In Progress)` | Wait for explicit user completion/verification before moving the ticket to `done` and starting repository finalization. |
| Stage 10 archival/repository finalization/release-publication-deployment/cleanup blocked | stay in `Stage 10 (Blocked)` | Record the move/commit/git/release-publication-deployment/cleanup blocker, resolve it, then finish handoff. |

### 0) Bootstrap Ticket + Capture Draft Requirement

- Use `stages/00-bootstrap/bootstrap-checklist.md`.
- Run mandatory first-action sequence:
  - create/use `tickets/in-progress/<ticket-name>/`,
  - if git repo, resolve bootstrap base branch from explicit user instruction when provided; otherwise infer the tracked remote default/integration branch with highest confidence,
  - if git repo and a new ticket worktree/branch is needed, refresh tracked remote refs first,
  - if git repo, create/reuse dedicated ticket worktree for `codex/<ticket-name>`; when creating a new ticket branch, branch it from the latest tracked remote base,
  - create/update `tickets/in-progress/<ticket-name>/workflow-state.md` from `shared/workflow-state-template.md`, set `Current Stage = 0`, `Code Edit Permission = Locked`, and fill `Stage 0 Bootstrap Record`,
  - capture initial requirement snapshot (`requirements.md` status `Draft`) from user input/bug report evidence first (text, images, logs, repro notes, constraints).
- Do not run deep investigation before Stage 0 bootstrap and `requirements.md` `Draft` are physically written.
- If remote refresh, base-branch resolution, or ticket-worktree creation fails, keep Stage 0 blocked and record the failure in `workflow-state.md` instead of falling back to a stale local branch.
- Before transitioning to Stage 1, update `workflow-state.md` snapshot + transition log + stage gate evidence.

### 1) Investigation + Understanding Pass + Triage

- Use `stages/01-investigation/investigation-guide.md`.
- Create/update `tickets/in-progress/<ticket-name>/investigation-notes.md` continuously during investigation. Treat it as a durable evidence log, not a brief summary. Do not keep investigation results only in memory.
- Investigation is not read-only: when needed to establish current behavior or isolate root cause, actively reproduce the issue, run focused commands/tests, write small diagnostic scripts, add temporary probes/instrumentation, perform the minimal environment setup or mocks needed to observe the problem, read public APIs/specs/issues, and inspect or clone upstream/vendor/sample repositories when that is the practical way to gather evidence.
- Treat Stage 1 methods as problem-dependent and non-exhaustive: use whatever bounded evidence-gathering work is needed to reduce uncertainty and verify assumptions before design.
- Minimum codebase understanding pass before design:
  - identify entrypoints and execution boundaries for in-scope flows,
  - identify touched files, affected modules/subsystems, and owning concerns,
  - identify expected canonical file locations/folder owners for touched concerns (for example: platform-specific vs shared),
  - identify current naming conventions (subsystem names, file names, optional module names when relevant, API style),
  - identify unknowns that could invalidate design assumptions.
- In `investigation-notes.md`, record in enough detail that later stages can reuse the investigation without repeating the same major search/research work unless the facts have changed:
  - investigation goals/questions,
  - detailed source log (`local file paths`, `web links`, `open-source references`, `papers`, exact commands run, and search queries when those materially shaped the result),
  - key findings, constraints, and observed behavior tied back to the exact source used,
  - codebase findings with exact files/symbols/entrypoints/owners where relevant,
  - file-placement observations (which files are already under the right owning folder, which are misplaced, and what the canonical location should be),
  - runtime/probe findings when reproductions, traces, or scripts were used,
  - reproduction prerequisites and environment/setup details when those materially affected the investigation outcome,
  - external dependency, public API, upstream-source, issue-tracker, or sample-app findings when those materially shaped the understanding,
  - open unknowns/questions,
  - implications for requirements/design.
- Prefer structured, detailed notes over compressed summaries. Use short synthesis sections for readability, but keep enough concrete evidence in the artifact that later stages do not need to rediscover the same facts from scratch.
- Boundary rule: narrowly scoped repro scripts/tests, temporary logs, investigation-only setup, disposable cloned repos, and throwaway harnesses remain Stage 1 work when they exist to gather evidence; durable production fixes and durable validation assets still belong to later stages.
- Re-entry rule: when later implementation/testing uncovers large or unclear issues, reopen this understanding stage and append new evidence, unknowns, and implications before changing requirements/design artifacts.
- Do not draft design artifacts or runtime call stacks until this understanding pass is complete and `requirements.md` reaches `Design-ready`.
- Classify as `Small`, `Medium`, or `Large` using practical signals:
  - Estimated files touched (roughly <= 3 is usually `Small` if not cross-cutting).
  - New/changed interface boundaries, schema/storage changes, or cross-cutting behavior.
  - Multi-boundary impact (API + service + persistence + runtime flow) or architectural impact.
- Choose workflow depth:
  - `Small`: create a draft `implementation.md` solution sketch, build per-use-case future-state runtime call stacks from that basis, review them, then refine until stability gate `Go Confirmed` and continue in the same `implementation.md` artifact with live execution tracking.
  - `Medium`: create proposed design doc first, build future-state runtime call stacks from the proposed design doc, run iterative deep-review rounds until stability gate `Go Confirmed`, and only then create `implementation.md` as the combined implementation baseline + live execution tracker.
  - `Large`: create proposed design doc first, build future-state runtime call stacks from the proposed design doc, run iterative deep-review rounds until stability gate `Go Confirmed`, and only then create `implementation.md` as the combined implementation baseline + live execution tracker.
- Re-evaluate during implementation; if scope expands or smells appear, escalate from `Small` to full workflow.
- Before transitioning to Stage 2, update `workflow-state.md` snapshot + transition log + stage gate evidence.
- After triage depth is finalized (`Small`/`Medium`/`Large`) and `investigation-notes.md` is current, announce only with the persisted `workflow-state.md` transition/gate update.

### 2) Refine Requirements Document To Design-Ready (Mandatory)

- Use `stages/02-requirements/requirements-refinement-guide.md`.
- Create/update `tickets/in-progress/<ticket-name>/requirements.md` for all sizes (`Small`, `Medium`, `Large`).
- Requirement writing is mandatory even for small tasks (small can be concise).
- Use one canonical file path only: update `requirements.md` in place. Do not create versioned duplicates such as `requirements-v2.md`.
- Requirements maturity flow:
  - `Draft`: rough capture from report/input evidence,
  - `Design-ready`: refined after deep understanding pass,
  - `Refined`: further updates when design/review/implementation feedback reveals gaps.
- Minimum required sections in `requirements.md`:
  - status (`Draft`/`Design-ready`/`Refined`),
  - goal/problem statement,
  - in-scope use cases,
  - acceptance criteria,
  - constraints/dependencies,
  - assumptions,
  - open questions/risks.
- Requirements quality rule (mandatory): requirements must be verifiable behavior specifications, not only descriptive narratives.
- For each requirement, include a stable `requirement_id` and explicit expected outcome.
- For each acceptance criterion, include a stable `acceptance_criteria_id` (for example: `AC-001`) and an explicit measurable expected outcome.
- Acceptance criteria must be testable and cover primary behavior plus relevant edge/error behavior.
- Include a requirement coverage map to call-stack use cases (all requirements must map to at least one use case).
- Include an acceptance-criteria coverage map to Stage 7 scenarios (all acceptance criteria must map to at least one executable validation scenario).
- Confirm the triage result (`Small` vs `Medium` vs `Large`) and rationale in the requirements doc.
- Refine requirements from the latest `investigation-notes.md`; do not derive requirements from memory-only investigation.
- Design-ready requirement gate must make expected behavior clear enough to draft design and runtime call stacks.
- If understanding is not sufficient to reach `Design-ready`, continue understanding pass and refine requirements first.
- After `requirements.md` reaches `Design-ready` and is confirmed as design input, announce only with the persisted `workflow-state.md` transition/gate update.

### Core Modernization Policy (Mandatory)

- Mandatory stance: no backward compatibility and no legacy code retention.
- Do not preserve legacy behavior, legacy APIs, compatibility wrappers, dual-write paths, or fallback branches kept only for old flows.
- Prefer clean replacement and explicit deletion of obsolete code, files, tests, flags, and adapters in the same ticket.
- Do not add compatibility exceptions in this workflow.

### Shared Design Principles (Design + Review, Mandatory)

- Design and review must use the same principles and vocabulary. Review is a check of design quality, not a different rule system.
- Use `shared/design-principles.md` as the primary shared reference for Stage 3 design work and Stage 5 review.
- Use `shared/common-design-practices.md` for helper practices and local pattern choices only when they clarify a clearly owned spine node or off-spine concern.
- Use `stages/08-code-review/code-review-principles.md` as the Stage 8 review reference.
- The core principles are:
  - `data-flow spine clarity`,
  - `ownership clarity`,
  - `off-spine concerns around the spine`.
- Separation of concerns is still mandatory, and in this workflow it should become stronger, not weaker. The difference is ordering: start with spine and ownership, then decompose concerns around that structure so each boundary stays coherent.
- Ownership is the concrete form of separation of concerns: if a concern has no clear owner, the structure is wrong.
- Dependency direction follows ownership. State allowed directions and forbidden shortcuts explicitly when design risk exists.
- Boundary encapsulation follows ownership too: when one boundary is the authoritative public entrypoint for a domain subject, callers above it should depend on that boundary rather than on both the boundary and one of its internal owned mechanisms at the same time.
- If callers only bypass an internal concern because the outer boundary does not expose enough usable API, strengthen that authoritative boundary or redesign the ownership split explicitly instead of normalizing the bypass.
- Off-spine concern reuse follows ownership too. Before adding a new helper or off-spine concern, check whether an existing capability area or subsystem already owns that responsibility.
- `Spine`, `owner`, and `off-spine concern` are architecture relationship terms, not naming templates. Do not literalize them into file, folder, class, service, or type names.
- Module placement and file placement follow ownership. If a file's path no longer matches the real concern, move, split, or rename it instead of rationalizing the mismatch.
- Subsystem, folder, and file mapping should be spine-led and ownership-led, but not mechanical. Optional module groupings are secondary structure only when they make boundaries easier to read.
- Distinct structural depths often deserve distinct folders, but do not force artificial over-splitting. If a flatter layout is clearer, justify it explicitly.
- Interface-boundary rule: APIs, queries, commands, and reused service methods must also follow ownership and separation of concerns. Prefer one boundary per subject/responsibility with explicit identity shape; avoid generic boundaries that infer subject type from ambiguous IDs or generic selectors.
- Use examples when they materially improve clarity. Do not keep a non-obvious design fully abstract when a short example would explain the intended shape faster.
- `Keep` is valid when the current structure already preserves a readable spine, clear ownership, and off-spine concerns that do not compete with the spine.

### 3) Draft The Proposed Design Document

- Required for `Medium/Large`. Optional for `Small`.
- Prerequisite: `requirements.md` is `Design-ready` (or `Refined`) and current for this ticket.
- For `Small`, do not require a full proposed design doc; use the draft `implementation.md` solution sketch as the lightweight design basis for runtime call stacks.
- Architecture-first rule: define the target architecture shape before mapping work onto existing files.
- Design from the data-flow spine first:
  - identify the primary execution/data-flow spine(s),
  - enumerate all relevant spines that matter to understanding the design,
  - name the main domain subject nodes on each spine,
  - define what each main-line node owns,
  - identify off-spine concerns that serve those owners,
  - check whether those off-spine needs should reuse or extend existing capability areas/subsystems before creating anything new,
  - record the return/event spine(s) when the change is async or event-driven,
  - record bounded local/internal spines when a loop, worker cycle, state machine, or dispatcher materially shapes one owner's behavior.
- Separation-of-concerns rule (mandatory): once the spine and owners are clear, split off-spine responsibilities so each main node and each off-spine concern remains self-encapsulated. Do not overload one spine node with every concern just because it sits on the main line.
- Boundary-encapsulation rule (mandatory): identify which boundaries are authoritative public entrypoints versus internal owned sub-layers. Callers above an authoritative boundary should not depend on both that boundary and one of its internal managers, repositories, helpers, or lower-level concerns at the same time.
- Do not anchor design to current file layout when the layout is structurally wrong for the target behavior.
- File-placement rule (mandatory): target file paths must match owning concern/boundary/platform; if a file is codex-specific, cloud-specific, UI-specific, infra-specific, or otherwise scope-bound, place it in that canonical area instead of near whichever caller currently imports it.
- Folder-layout rule (mandatory): map subsystems/folders/files from the spine and ownership model, and add optional module groupings only when they materially help readability rather than by default. Do it with judgment rather than as a rigid one-folder-per-step projection. If a flatter layout is clearer, justify it. If a split is proposed, it should reflect a real owner or boundary.
- Interface-boundary rule (mandatory): design APIs, queries, commands, and reused service methods around explicit subject ownership and explicit identity shape. Do not use one generic boundary that accepts an ambiguous ID or generic selector and guesses whether the subject is, for example, an agent run, team run, or team member run.
- Current-state grounding rule (mandatory): before finalizing the target design, read the current implementation enough to understand the existing main flow, current owners, coupling problems, file placement drift, and real migration constraints.
- Explicitly evaluate whether new subsystem-internal module groupings, boundary interfaces, or orchestration owners should be introduced.
- Explicitly evaluate whether existing subsystems/owners should be split, merged, moved, or removed.
- Explicitly evaluate whether an existing capability area or subsystem should absorb the new off-spine responsibility instead of introducing a fresh helper beside the spine.
- When coordination policy is repeated across callers (provider selection, fallback, retry, aggregation, routing, fan-out), extract that policy into a clear owner instead of leaving it fragmented.
- Reject empty indirection: if a proposed layer or optional module grouping only passes work through and owns no real policy, boundary, or sequencing, keep the structure flatter.
- Record the architecture direction decision and rationale (`complexity`, `testability`, `operability`, `evolution cost`).
- For straightforward local changes, one concise decision is enough; alternatives are optional.
- For non-trivial or uncertain architecture changes, include a small alternatives comparison before deciding.
- Choose the proper structural change for the problem (`Keep`, `Add`, `Split`, `Merge`, `Move`, `Remove`) without bias toward minimal edits.
- Removal-first tightening rule (mandatory): when the target design introduces a clearer owner, reusable structure, or better file boundary, explicitly identify what redundant/fragmented pieces become unnecessary and remove/decommission them in scope when possible.
- `Keep` is a valid outcome when the current data-flow spine, ownership boundaries, and off-spine concerns are already coherent.
- If a file's concern and folder disagree, `Keep` is usually invalid; prefer explicit `Move`, `Split`, or justified `Promote Shared`.
- Functional/local correctness is not sufficient: if a bug fix "works" but degrades the data-flow spine, ownership boundaries, or off-spine concerns, redesign the structure instead of accepting the patch.
- Reject patch-on-patch hacks that bypass clear boundaries just to make a local change compile.
- Follow separation of concerns after the target architecture direction is chosen: each file should own a clear responsibility, and each subsystem should own a coherent category of work. Optional module groupings may exist inside a subsystem when they make the structure easier to read. This is a stronger SoC check, not a weaker one, because off-spine concerns must also land in explicit owners instead of drifting into generic blobs.
- Ownership-driven dependency rule (mandatory): define and preserve clear subsystem, service, and component boundaries so allowed dependencies follow ownership and forbidden shortcuts are explicit.
- Existing-capability reuse rule (mandatory): do not create a new helper/off-spine concern by default. Reuse or extend an existing well-owned subsystem when the fit is natural, and justify `Create New` when no current area is appropriate.
- Reusable-owned-structure rule (mandatory): when repeated data structures, types, normalizers, converters, mappers, or schemas appear across several files, extract them into reusable owned files under the correct subsystem instead of duplicating them.
- Data-model-tightness rule (mandatory): when a shared structure is extracted or revised, tighten it. Remove redundant attributes, avoid overlapping parallel representations for the same subject, and keep each field's meaning singular and explicit.
- Shared-base coherence rule (mandatory): use a shared base/core only when it represents a real common shape. If one case needs extra fields or behavior, prefer meaningful specialized variants or composition instead of growing a one-for-all structure full of optional attributes.
- For `Small`, the solution sketch in `implementation.md` must still include a concise architecture sketch (target ownership boundaries and any new files, plus optional module groupings only when they help readability).
- Apply separation-of-concerns at the correct technical boundary for the stack:
  - frontend/UI scope: evaluate responsibility at view/component level (each component should own a clear concern),
  - non-UI scope (backend/service/worker/domain): evaluate responsibility at file and service level, while keeping subsystem grouping readable,
  - integration/infrastructure scope: each adapter or integration-focused file/group should own one integration concern with clear contracts.
- Make the proposed design doc delta-aware, not only target-state:
  - include current-state summary (as-is),
  - include target-state summary (to-be),
  - include explicit change inventory rows for `Add`, `Modify`, `Rename/Move`, `Remove`.
- Proposed design document organization rule (mandatory): write the design spine-first, not file-first. The main structure of the document should be the spine inventory, main domain subject nodes, ownership, and off-spine concerns.
- Design concretion order (mandatory): after the spine and ownership model are clear, move through subsystem/capability-area allocation, then draft file responsibilities, then extract reusable owned structures where repetition appears, then finalize file responsibilities, then folder/path mapping.
- File sections are required, and subsystem shape plus optional module groupings may be included where they add clarity, but only as derived implementation mapping after the spine-led explanation is clear.
- Example rule (mandatory when needed): if a short good-shape example or bad-shape anti-example would make a non-obvious design materially clearer, include it in the proposed design doc instead of leaving the point abstract.
- For each file, state mapped spine, target owner/boundary placement, responsibility, key APIs, inputs/outputs, dependencies, and change type. Mention subsystem placement and optional module grouping where relevant.
- For each new off-spine concern, state whether it reuses/extends an existing capability area or why a new area is required.
- For each file, state whether its target path matches the owning concern and record the move/split rationale when placement changes are required.
- Include a naming decisions section:
  - proposed file names, subsystem names, optional module names when relevant, and API names,
  - rationale for each naming choice,
  - mapping from old names to new names when renaming.
- Use natural, unsurprising, implementation-friendly names; naming choices should be understandable without domain-specific insider context.
- Add a naming-drift check section in the design doc:
  - verify each file name and any subsystem/module name still matches its current responsibility after scope expansion,
  - identify drifted names (name no longer represents real behavior),
  - choose corrective action per drifted item (`Rename`, `Split`, `Move`, or `N/A` with rationale),
  - map each corrective action to change inventory rows and implementation tasks.
- Document dependency flow and cross-reference risk explicitly (including how cycles are avoided or temporarily tolerated).
- Document allowed dependency directions between ownership boundaries and note any temporary violations with removal plan.
- For `Rename/Move` and `Remove`, include decommission/cleanup intent (import cleanup and dead-code removal).
- Do not produce an addition-only design when the real improvement comes from both adding a clearer owner and removing redundant fragments that the new owner makes unnecessary.
- Capture data models and error-handling expectations if relevant.
- Add a use-case coverage matrix in the design doc with at least:
  - `use_case_id`,
  - primary path covered (`Yes`/`No`),
  - fallback path covered (`Yes`/`No`/`N/A`),
  - error path covered (`Yes`/`No`/`N/A`),
  - mapped sections in runtime call stack doc.
- Version the design during review loops (`v1`, `v2`, ...) and record what changed between rounds.
- Use the template in `stages/03-design/proposed-design-template.md` as a starting point.
- No-backward-compat design gate (mandatory): proposed design must not introduce compatibility wrappers, dual-read/dual-write flows, legacy adapters, or fallback branches kept only for old behavior.
- If backward-compatibility or legacy-retention mechanisms are required to make the design work, classify as `Fail` and redesign the architecture direction before continuing.
- Do not speak solely because `proposed-design.md` changed; announce only when the related `workflow-state.md` transition/gate update is persisted.

### 4) Build Future-State Runtime Call Stacks Per Use Case

- Required for all sizes (`Small`, `Medium`, `Large`).
- For `Small`, keep it concise but still cover each in-scope use case with primary path plus key fallback/error branch when relevant.
- Basis by scope:
  - `Small`: use the draft `implementation.md` solution sketch as the design basis.
  - `Medium/Large`: use the proposed design document as the design basis.
- For each use case, write a future-state runtime call stack from entry point to completion in a debug-trace format.
- Use stable `use_case_id` values and ensure IDs match the design coverage matrix and review artifact.
- For each use case, record mapped spine ID(s), spine scope, and governing owner from the design basis.
- Use two allowed use-case source types:
  - `Requirement`: derived from explicit requirement behavior.
  - `Design-Risk`: derived from architecture or technical risk that must be validated.
- Coverage rule (mandatory): every in-scope requirement must be covered by at least one `Requirement` use case.
- For each `Design-Risk` use case, record the technical objective/risk justification and expected observable outcome.
- Treat this artifact as `to-be` architecture behavior derived from the proposed design (or small-scope solution sketch), not as-is code tracing.
- If current code differs from target design, model the target design behavior and record migration/transition notes separately.
- Include file and function names at every frame using `path/to/file.ts:functionName(...)`.
- Show architectural boundaries explicitly (e.g., controller -> service -> repository -> external API).
- Include primary path and fallback/error paths, not only happy path.
- Include explicit use-case coverage status per use case (primary/fallback/error) and mark intentional `N/A` branches.
- If a use case exercises a bounded local spine, make that explicit instead of hiding it inside a generic end-to-end stack.
- Mark async/event boundaries (`await`, queue enqueue/dequeue, worker loop handoff).
- Mark state mutations and persistence points (`in-memory state`, `cache write`, `DB/file write`).
- Capture decision gates and conditions that choose one branch over another.
- Note key data transformations (input schema -> domain model -> output payload).
- Version call stacks to match design revisions from review loops (`v1`, `v2`, ...).
- Use the template in `stages/04-future-state-runtime-call-stack/future-state-runtime-call-stack-template.md`.
- Do not speak solely because `future-state-runtime-call-stack.md` changed; announce only when the related `workflow-state.md` transition/gate update is persisted.

### 5) Review Future-State Runtime Call Stacks (Future-State + Architecture + Naming + Cleanliness Gate)

- Create `future-state-runtime-call-stack-review.md` as a mandatory review artifact.
- Review focus is future-state correctness and implementability against the target design basis (`proposed-design.md` for `Medium/Large`, small-scope solution sketch in `implementation.md` for `Small`), not parity with current code structure.
- Review must challenge architecture choice itself (spine/ownership/off-spine concerns/allocation), not only file-level separation of concerns.
- Review must reuse the same shared design principles from Stage 3; do not apply a different principle set in review.
- Review must explicitly verify file placement against the Stage 3 design basis; wrong folder placement is a structural defect, not a cosmetic nit.
- Review must explicitly judge whether the proposed layout is readable for the scope or whether it is either too flat or too artificially fragmented.
- Review must explicitly check example-based clarity when the design uses examples or when the design would otherwise stay too abstract.
- Run review in explicit rounds and record each round in the same review artifact.
- In every round, run a dedicated missing-use-case discovery sweep before verdicting the round.
- Review each use case against these criteria:
  - architecture fit check (`Pass`/`Fail`): chosen architecture shape is appropriate for this use case and expected growth,
  - data-flow spine clarity check (`Pass`/`Fail`): the main end-to-end motion and any bounded local spines are readable and not fragmented across peer coordinators,
  - spine inventory completeness check (`Pass`/`Fail`): all relevant spines are explicitly named with clear start/end boundaries and owner relationships,
  - ownership clarity check (`Pass`/`Fail`): main-line nodes and off-spine concerns have clear owners with concrete authority,
  - off-spine concern clarity check (`Pass`/`Fail`): off-spine concerns serve the spine without competing with it or owning hidden sequencing,
  - boundary placement check (`Pass`/`Fail`): responsibilities are assigned to the right owner or subsystem boundary,
  - ownership-driven dependency check (`Pass`/`Fail`): dependencies follow ownership, avoid tight cross-subsystem coupling, and avoid unjustified cyclic cross-references,
  - boundary encapsulation check (`Pass`/`Fail`): callers use the authoritative boundary instead of depending on both an outer owner and one of its internal lower-level concerns,
  - file-placement alignment check (`Pass`/`Fail`): each file path matches the owning concern/boundary/platform, and any shared placement is explicitly justified,
  - flat-vs-over-split layout judgment (`Pass`/`Fail`): layout is neither too flat nor artificially fragmented for the scope,
  - interface/API/service-method boundary clarity (`Pass`/`Fail`): APIs, queries, commands, and reused service methods expose one clear subject/responsibility with explicit identity shape instead of generic ambiguous IDs or mixed-subject selectors,
  - existing-structure bias check (`Pass`/`Fail`): design is not forced to mirror current files when that harms target architecture,
  - anti-hack check (`Pass`/`Fail`): no patch-on-patch tricks that hide architecture issues behind local fixes,
  - local-fix degradation check (`Pass`/`Fail`): a functionally working fix does not degrade the data-flow spine, ownership boundaries, or off-spine concerns,
  - example-based clarity (`Pass`/`Fail`/`N/A`): non-obvious areas use examples when needed, and the examples actually clarify the target shape,
  - terminology and concept vocabulary is natural and intuitive (`Pass`/`Fail`),
  - file and API naming is clear and unsurprising for implementation mapping (`Pass`/`Fail`),
  - name-to-responsibility alignment under scope drift (`Pass`/`Fail`),
  - future-state alignment with target design basis (`Pass`/`Fail`),
  - use-case coverage completeness (primary/fallback/error coverage) (`Pass`/`Fail`),
  - use-case source traceability (`Pass`/`Fail`) (`Requirement` or `Design-Risk`, with source reference),
  - requirement coverage closure (`Pass`/`Fail`) (all requirements mapped to at least one use case),
  - design-risk use-case justification quality (`Pass`/`Fail`) (clear objective/risk and expected outcome),
  - business flow completeness (`Pass`/`Fail`),
  - gap findings,
  - ownership-appropriate separation-of-concerns check (`Pass`/`Fail`) (frontend/UI: view/component boundary; non-UI: file and service boundaries with readable subsystem grouping),
  - dependency flow smells,
  - redundancy/duplication check (`Pass`/`Fail`),
  - simplification opportunity check (`Pass`/`Fail`),
  - remove/decommission and obsolete/deprecated/dead-path cleanup completeness for impacted changes (`Pass`/`Fail`),
  - legacy-retention cleanup check (`Pass`/`Fail`) (obsolete old-behavior/deprecated/dead paths are removed for impacted scope),
  - backward-compatibility mechanism check (`Pass`/`Fail`) (no compatibility wrappers, dual-path behavior, or legacy fallback branches retained),
  - overall verdict (`Pass`/`Fail`).
- Round policy:
  - use deep review for every round (challenge assumptions, edge cases, and cleanup quality),
  - if a round finds blockers, requires persisted artifact updates, or discovers new use cases, classify the round (`Design Impact`/`Requirement Gap`/`Unclear`), apply required upstream updates through the classified stage path, and reset clean-review streak to 0,
  - if a round finds no blockers, no required persisted artifact updates, and no newly discovered use cases, mark `Candidate Go` and increment clean-review streak,
  - open `Go` only when clean-review streak reaches 2 consecutive deep-review rounds.
- Across rounds, track trend quality: issues should decline in count/severity or become more localized; otherwise escalate design refinement before proceeding.
- Round staged re-entry discipline (mandatory):
  - Step A: run review + missing-use-case discovery and record findings in the current round.
  - Step B: classify blockers as exactly one of `Design Impact`/`Requirement Gap`/`Unclear`.
  - Step C: if findings require updates, transition to the classified upstream stage path first, then modify required artifacts there and bump versions (`vN -> vN+1`).
  - Step D: record an "Applied Updates" entry in the review artifact (what changed, where, and why), including classification + return path.
  - Step E: start the next round from updated files only; do not carry unresolved edits in memory.
  - Step F: record clean-review streak state in the review artifact (`Reset`, `Candidate Go`, or `Go Confirmed`).
- Gate `Go` criteria (all required):
  - architecture fit check is `Pass` for all in-scope use cases,
  - data-flow spine clarity check is `Pass` for all in-scope use cases,
  - spine inventory completeness check is `Pass` for the design basis,
  - ownership clarity check is `Pass` for all in-scope use cases,
  - off-spine concern clarity check is `Pass` for all in-scope use cases,
  - boundary placement check is `Pass` for all in-scope use cases,
  - ownership-driven dependency check is `Pass` for all in-scope use cases,
  - boundary encapsulation check is `Pass` for all in-scope use cases,
  - file-placement alignment check is `Pass` for all in-scope use cases,
  - interface/API/service-method boundary clarity is `Pass` for all in-scope use cases,
  - existing-structure bias check is `Pass` for all in-scope use cases,
  - anti-hack check is `Pass` for all in-scope use cases,
  - local-fix degradation check is `Pass` for all in-scope use cases,
  - terminology/concept vocabulary is `Pass` for all in-scope use cases,
  - file and API naming clarity is `Pass` for all in-scope use cases,
  - name-to-responsibility alignment under scope drift is `Pass` for all in-scope use cases,
  - future-state behavior is consistent with target design basis across all in-scope use cases,
  - ownership-appropriate separation-of-concerns check is `Pass` for all in-scope use cases,
  - use-case coverage completeness is `Pass` for all in-scope use cases,
  - use-case source traceability is `Pass` for all in-scope use cases,
  - requirement coverage closure is `Pass` for the full in-scope requirement set,
  - design-risk use-case justification quality is `Pass` for all design-risk use cases,
  - redundancy/duplication check is `Pass` for all in-scope use cases,
  - simplification opportunity check is `Pass` for all in-scope use cases,
  - all in-scope use cases have overall verdict `Pass`,
  - no unresolved blocking findings (including any required design/call-stack updates),
  - for any impacted `Add`/`Modify`/`Rename/Move`/`Remove` scope items, decommission/cleanup and obsolete/deprecated/dead-path checks are `Pass`,
  - no new use cases are discovered in either of the two clean rounds,
  - legacy-retention cleanup check is `Pass` for all in-scope use cases,
  - backward-compatibility mechanism check is `Pass` for all in-scope use cases,
  - two consecutive deep-review rounds have no blockers, no required persisted artifact updates, and no newly discovered use cases.
- If issues are found:
  - classify each blocking round as exactly one of `Design Impact`/`Requirement Gap`/`Unclear` and record it in `future-state-runtime-call-stack-review.md` and `workflow-state.md`.
  - `Design Impact` (clear and high-confidence design issue): update design basis in Stage 3 (`Medium/Large`: `proposed-design.md`; `Small`: design section in `implementation.md`), regenerate call stacks in Stage 4, then return to Stage 5.
  - `Requirement Gap`: update `requirements.md` first in Stage 2 (status `Refined`), then update design basis in Stage 3, regenerate call stacks in Stage 4, then return to Stage 5.
  - `Unclear` (cross-cutting/low-confidence): update `investigation-notes.md` in Stage 1 first, then proceed through `2 -> 3 -> 4 -> 5`.
- If naming drift is found, prefer explicit rename/split/move updates in the same review loop instead of carrying stale names forward.
- Even when a round reports no findings, still complete the round record in-file and run another deep-review round until the two-consecutive-clean stability rule is satisfied.
- Repeat until all gate `Go Confirmed` criteria are satisfied.
- Use the template in `stages/05-future-state-runtime-call-stack-review/future-state-runtime-call-stack-review-template.md`.

### 6) Implement Source + Unit/Integration And Track Progress

- Use a bottom-up, test-driven approach: implement foundational dependencies first.
- Sequence is mandatory:
  - first ensure `implementation.md` baseline is finalized,
  - then initialize/update the execution-tracking sections in `implementation.md`,
  - then execute source implementation with required unit/integration verification.
- Stage separation rule (mandatory):
  - Stage 6 implements source code and verifies file and service boundaries, while preserving readable subsystem grouping, with unit/integration tests.
  - Stage 7 implements executable validation assets and runs the mapped Stage 7 scenarios against acceptance criteria.
  - Stage 8 runs the code review gate after Stage 7 passes.
- Include requirement traceability in plan/progress (`requirement -> design section -> call stack/use_case -> implementation tasks/tests`).
- Include spine traceability in plan/progress (`spine -> owner -> use case -> implementation tasks -> validation scenarios`).
- Integration test coverage is required for behavior that crosses module boundaries, process boundaries, storage boundaries, or external API boundaries. If any such behavior is not covered, record a concrete rationale.
- Finalize planning artifacts before kickoff:
  - `Small`: refine the draft `implementation.md` solution sketch until future-state runtime call stack review passes final stability gate (`Go Confirmed`).
  - `Medium/Large`: create `implementation.md` only after future-state runtime call stack review passes final stability gate (`Go Confirmed`).
- Initialize the execution-tracking sections in `implementation.md` at implementation kickoff, after required pre-implementation artifacts are ready (including the proposed design document for Medium/Large).
- One merged implementation artifact with both baseline planning and live tracking is required for all sizes (`Small`, `Medium`, `Large`).
- Keep detailed Stage 7, Stage 8, and Stage 9 records in their own canonical artifacts. `implementation.md` should carry only implementation-owned planning/tracking plus downstream handoff inputs and short status pointers.
- Treat future-state runtime call stack + review as a pre-implementation verification gate: ensure each use case is represented and reviewed before coding starts.
- Start implementation only after the review gate says implementation can start and all in-scope use cases are `Pass`.
- Before first source-code edit in Stage 6, update `workflow-state.md`:
  - set `Current Stage = 6`,
  - set `Code Edit Permission = Unlocked`,
  - record transition evidence that Stage 5 gate is `Go Confirmed` and pre-edit checklist is satisfied.
- Ensure traceability when a proposed design doc exists: every design change-inventory row (especially `Rename/Move` and `Remove`) maps to implementation tasks and verification steps.
- Enforce clean-cut implementation: do not keep legacy compatibility paths, dead code, or dormant replaced paths in scope.
- No-backward-compat implementation rule (mandatory): reject compatibility wrappers, dual-path reads/writes, and old-behavior fallback branches even if they make rollout easier.
- Shared-principles implementation rule (mandatory): implementation must continue applying the shared design principles and common design practices independently at file-level detail. The reviewed design artifact is the current target, not permission to ignore tighter realities discovered during coding.
- Ownership-dependency preservation rule (mandatory): implementation must not introduce new tight coupling, forbidden shortcuts, or cyclic dependencies across owners or subsystem boundaries.
- File-placement preservation rule (mandatory): do not leave touched files in the wrong concern folder just to minimize edits; move/split them when the current path no longer matches ownership.
- Implementation completeness rule (mandatory): implementation is not complete until obsolete code paths, dead code, unused helpers/tests/flags/adapters, dormant replaced paths, and compatibility shims in scope are removed.
- Proactive source-file size rule (mandatory): treat the Stage 8 source-file size gates as active Stage 6 guardrails for changed source implementation files. Do not knowingly grow or leave a changed source implementation file above `500` effective non-empty lines. If a changed source implementation file trends toward that limit, or if one file's current diff exceeds `220` changed lines, split/refactor/escalate during implementation instead of waiting for Stage 8 to reject it. Test files stay outside that hard source-file limit.
- Stage 6 failure classification rule (mandatory):
  - `Local Fix`: issue is bounded and does not require requirement/design/call-stack updates; remain in Stage 6.
  - `Design Impact`: issue indicates architecture/ownership-dependency or compatibility-policy breach requiring upstream design/runtime updates; re-enter `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`.
  - `Requirement Gap`: missing/ambiguous requirement or acceptance criteria discovered during implementation; re-enter `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`.
  - `Unclear`: cross-cutting/low-confidence root cause; re-enter `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`.
- If detailed implementation work reveals that the reviewed design is incomplete, weak, or wrong, do not patch around it locally. Record the issue and classify `Design Impact` so upstream design/runtime artifacts are corrected before further source edits.
- If a change only "works" by leaving a file in the wrong folder or adding new misplaced files, do not classify it as `Local Fix`; treat it as `Design Impact` unless the real issue is missing requirements.
- Use "one file at a time" as the default execution strategy, not an absolute rule.
- When rare cross-referencing is unavoidable, allow limited parallel/incomplete implementation, but explicitly record:
  - the cross-reference smell,
  - the blocked dependency edge,
  - the condition to unblock,
  - the required proposed-design-document update.
- Update progress in real time during implementation (immediately after file status changes, test runs, blocker discoveries, and design-feedback-loop updates).
- Track change IDs and change types in progress (`Add`/`Modify`/`Rename/Move`/`Remove`) so refactor deltas remain explicit through execution.
- Track file build state explicitly (`Pending`, `In Progress`, `Blocked`, `Completed`, `N/A`).
- Track unit/integration test state separately (`Not Started`, `In Progress`, `Passed`, `Failed`, `Blocked`, `N/A`).
- If a file is blocked by unfinished dependencies, mark it `Blocked` and record the dependency and unblock condition.
- Mark a file `Completed` only when implementation is done and required tests are passing.
- Mark Stage 6 complete only when:
  - implementation baseline scope is delivered (or deviations are explicitly documented),
  - required unit/integration tests pass,
  - no backward-compatibility shims or legacy old-behavior branches remain in scope,
  - dead code, obsolete files, unused helpers/tests/flags/adapters, and dormant replaced paths in scope are removed,
  - ownership-driven dependencies remain valid (no newly introduced unjustified tight coupling/cyclic dependencies),
  - touched files either already have correct placement or are moved/split so their paths match owning concerns,
  - changed source implementation files have proactive size-pressure handling recorded (`>500` avoided and `>220` changed-line pressure assessed/acted on where needed).
- Use `stages/06-implementation/implementation-template.md`.
- Do not speak for routine `implementation.md` edits. Announce only for persisted `workflow-state.md` events (Stage 6 entry, lock/unlock change, gate/transition outcomes).

### 7) Implement API/E2E And Other Executable Validation And Run Stage 7 Gate (Mandatory)

- Run this stage immediately after `Stage 6` completes.
- At Stage 7 entry, update `workflow-state.md` and keep `Code Edit Permission = Unlocked` while Stage 7 validation artifacts are being implemented/executed.
- Create/update `tickets/in-progress/<ticket-name>/api-e2e-testing.md` as the canonical scenario + result artifact.
- Multi-round artifact rule (mandatory): keep one canonical `api-e2e-testing.md` path for the ticket. Do not create versioned copies by default. On every rerun, check prior unresolved failures first, then continue validation. The latest round result is authoritative; earlier rounds remain history.
- Round-resolution rule (mandatory): on Stage 7 round `>1`, update the prior-failure resolution check before declaring the new gate result.
- Stage 7 scope includes:
  - implementing durable repo-resident validation assets as needed,
  - implementing API, browser/UI, native desktop/UI, CLI, process/lifecycle, integration, multi-service, or multi-node harnesses as needed,
  - executing Stage 7 scenarios mapped from acceptance criteria.
- Durable validation-first rule (mandatory): first implement or update the validation tests, harnesses, and assets that should live in the repository and govern future changes.
- Broader executable-validation rule (mandatory): if durable repo-resident validation is not enough to prove the behavior, continue with broader executable validation work as needed, including temporary scripts, probes, environment setup, containerized setup, mocked or emulated dependencies, CLI harnesses, native desktop automation, lifecycle/update/restart checks, multi-process or multi-node orchestration, or browser/computer automation when that is the reasonable way to verify the flow.
- Persistence rule (mandatory): validation that should remain useful for future changes should stay in the codebase; one-off proof scaffolding may be temporary.
- Cleanup rule (mandatory): remove temporary validation-only scaffolding after the result is recorded unless keeping it as durable coverage is clearly useful.
- If Stage 7 failures require source-code changes, declare re-entry and return to Stage 6 first.
- Scenario sources (mandatory):
  - requirement-driven scenarios (must cover all critical requirements and flows),
  - design-risk-driven scenarios (must cover technical risks introduced by architecture/design choices).
- Spine coverage rule (mandatory): every relevant spine from the approved design basis must map to at least one Stage 7 scenario, or be explicitly marked `N/A` with rationale.
- Acceptance-criteria closure loop (mandatory):
  - build and maintain an explicit Stage 7 acceptance-criteria matrix sourced from `requirements.md` (`acceptance_criteria_id` -> mapped scenario IDs -> execution status),
  - every in-scope acceptance criterion must map to at least one executable Stage 7 scenario before execution starts,
  - every relevant spine must map to at least one executable Stage 7 scenario before execution starts unless explicitly `N/A`,
  - any acceptance criterion with status `Unmapped`, `Not Run`, `Failed`, or `Blocked` keeps Stage 7 open and requires re-entry unless explicitly marked `Waived` by user decision for infeasible cases,
  - rerun the required re-entry chain and return to Stage 7 until all in-scope acceptance criteria are `Passed` or explicitly `Waived`.
- For each scenario, record at minimum:
  - `scenario_id`,
  - mapped `spine_id` values,
  - mapped `acceptance_criteria_id` values,
  - mapped `requirement_id` and `use_case_id` values,
  - source type (`Requirement`/`Design-Risk`),
  - validation mode (`API`/`Browser-E2E`/`Desktop-UI`/`CLI`/`Integration`/`Process`/`Lifecycle`/`Other`),
  - platform/runtime target,
  - expected outcome,
  - durable validation asset(s) added/updated when applicable,
  - temporary validation method/setup used when applicable,
  - execution command/harness,
  - result (`Passed`/`Failed`/`Blocked`/`N/A`).
- Stable scenario-ID rule (mandatory): reuse the same `scenario_id` for the same scenario across reruns. Add a new `scenario_id` only for newly discovered coverage.
- Scenario-pattern examples (illustrative, not exhaustive):
  - backend/service API change: request -> handler -> domain/service -> persistence -> response contract,
  - browser UI flow: user action -> UI state change -> network effect -> rendered confirmation/error state,
  - native desktop updater flow: version `from` -> update download/apply -> relaunch/restart -> version `to` -> persisted state/migration check,
  - worker/process flow: enqueue/trigger -> worker loop/process handoff -> side effect -> completion/ack state,
  - distributed/multi-node flow: node A action -> replication/sync -> node B visible state or failover behavior.
- API test depth rule (mandatory): when validation mode is `API`, validate contract-level behavior including required fields/schema shape, status codes, and error payload behavior for mapped acceptance criteria.
- Lifecycle/update rule (mandatory): when a scenario covers install/update/startup/restart/shutdown/migration/recovery behavior, record version `from`/`to` when relevant, platform/runtime target, package/update channel or feed when relevant, relaunch/restart evidence, and persisted-state outcome.
- Cross-boundary test rule (mandatory): for client/server, multi-service, or multi-process scope, include Stage 7 scenarios that validate cross-boundary interaction behavior (trigger -> boundary handoff -> downstream effect -> returned or observable state).
- Manual testing policy: unstructured manual-only testing is not part of the default workflow. If OS/platform constraints make a human-assisted execution step unavoidable, record the exact steps, automated evidence captured, constraints, and residual risk; do not treat ad hoc manual confirmation as sufficient Stage 7 coverage.
- Feasibility policy:
  - if a scenario is not executable in current environment (missing secrets/tokens, unavailable partner system, infra limit), record concrete infeasibility reasons and constraints in `api-e2e-testing.md`; reflect only a short downstream status pointer in `implementation.md` when needed,
  - record compensating automated evidence and residual risk notes for each infeasible critical scenario,
  - mark Stage 7 as `Blocked` unless the user explicitly accepts a waiver for the infeasible acceptance criteria.
- Validation retention policy:
  - if a validation asset should govern future behavior in the repository, keep it and record its path,
  - if a validation asset exists only to prove the current ticket in a non-durable way, record it as temporary and clean it up after use unless there is clear value in keeping it.
- Test feedback escalation policy (mandatory):
  - classify each failing Stage 7 scenario as exactly one of `Local Fix`, `Design Impact`, `Requirement Gap`, or `Unclear`,
  - before final classification, run an investigation screen:
    - if issue scope is cross-cutting, touches unknown runtime paths, or root-cause confidence is low, mark `Investigation Required` and reopen understanding stage first (`investigation-notes.md` must be updated before design/requirements artifact updates),
    - if issue is clearly bounded with high root-cause confidence, continue classification directly.
  - `Local Fix` is allowed only when responsibility boundaries stay intact, no new use case/acceptance criterion is needed, and no requirement/design changes are needed.
  - if a fix works functionally but degrades the data-flow spine, ownership boundaries, or off-spine concerns, it is **not** `Local Fix`; classify as `Design Impact`.
  - if a fix only works by leaving a file in the wrong folder or adding a new misplaced file, it is **not** `Local Fix`; classify as `Design Impact`.
  - classify as `Requirement Gap` when failing behavior reveals missing functionality/use case or missing/ambiguous acceptance criteria.
  - apply re-entry declaration before source code edits when source/design/requirement updates are needed.
  - `Local Fix` path: update artifacts first, then rerun `Stage 6 -> Stage 7`.
  - `Design Impact` path: `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`.
  - `Requirement Gap` path: `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`.
  - `Unclear`/cross-cutting root cause path: `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`.
- Stage completion gate:
  - durable executable validation that should live in the repository has been implemented or updated,
  - all in-scope acceptance criteria from `requirements.md` are mapped to Stage 7 scenarios,
  - all relevant spines from the design basis are mapped to Stage 7 scenarios or explicitly `N/A`,
  - all executable in-scope acceptance criteria have execution status `Passed`,
  - all executable relevant spines have scenario evidence that passed,
  - all executable mapped Stage 7 scenarios are resolved (`Passed`), with no unresolved failures/blockers,
  - temporary validation-only scaffolding is either cleaned up or explicitly retained with rationale,
  - if any acceptance criterion is infeasible due to environment constraints, Stage 7 remains `Blocked` until explicit user waiver is recorded with constraints + compensating evidence + residual risk.
- Before transitioning to Stage 8, update `workflow-state.md` with Stage 7 gate result and transition evidence.
- Use `stages/07-api-e2e/api-e2e-testing-template.md`.
- Do not speak for `api-e2e-testing.md` edits alone. Announce when `workflow-state.md` records Stage 7 entry, gate result, and any re-entry declaration/lock-state change.

### 8) Run Code Review Gate (Mandatory, Post-Testing)

- Run this stage only after the `Stage 7` executable-validation gate is `Pass`.
- At Stage 8 entry, update `workflow-state.md` and set `Code Edit Permission = Locked`.
- Create/update `tickets/in-progress/<ticket-name>/code-review.md` as the canonical code review artifact.
- Investigation-context rule (mandatory): Stage 8 may read the latest `investigation-notes.md` as upstream context when it materially explains the changed scope, current-behavior findings, external constraints, or a review finding. Investigation notes are context, not review authority.
- Multi-round artifact rule (mandatory): keep one canonical `code-review.md` path for the ticket. Do not create versioned copies by default. On every rerun, recheck prior unresolved findings first, then run a fresh review pass. The latest review round is authoritative; earlier rounds remain history.
- Round-resolution rule (mandatory): on Stage 8 round `>1`, update the prior-findings resolution check before declaring the new gate result.
- Scope:
  - source files and test files,
  - include changed files and directly impacted related files when structural risk exists.
- File-size gate scope (mandatory): the `>500` effective-line hard limit and `>220` changed-line delta gate apply to changed source implementation files only. Test files stay in review scope for correctness, maintainability, and validation quality, but they do not fail the gate merely for exceeding those source-file size thresholds.
- Mandatory review scorecard rule (mandatory): record a detailed priority-ordered scorecard in `code-review.md` on every Stage 8 round. Score these ten categories from `1.0` to `10.0` in `0.5` increments and record for each row why it earned that score, what is weak, and what should improve:
  - `1` `Data-Flow Spine Inventory and Clarity`,
  - `2` `Ownership Clarity and Boundary Encapsulation`,
  - `3` `API / Interface / Query / Command Clarity`,
  - `4` `Separation of Concerns and File Placement`,
  - `5` `Shared-Structure / Data-Model Tightness and Reusable Owned Structures`,
  - `6` `Naming Quality and Local Readability`,
  - `7` `Validation Strength`,
  - `8` `Runtime Correctness Under Edge Cases`,
  - `9` `No Backward-Compatibility / No Legacy Retention`,
  - `10` `Cleanup Completeness`.
- Review-order rule (mandatory): judge the scorecard in the listed order because the design reasoning should flow from data-flow spine inventory -> ownership/boundary authority -> API shape -> separation of concerns and placement -> shared structures -> naming -> validation -> runtime edge cases -> no backward-compatibility / no legacy retention -> cleanup completeness.
- Scorecard overall rule (mandatory): report `Overall: X.X / 10` and `YY / 100` for summary/trend visibility only. If an overall score is reported, a simple average is acceptable, but the average is never the Stage 8 pass/fail rule.
- Per-category gate rule (mandatory): every scorecard category is mandatory. Clean Stage 8 pass target is `>= 9.0` in every category. Any category below `9.0` is a real gap and should normally fail Stage 8.
- Scorecard interpretation rule (mandatory): the scorecard is diagnostic and comparative, but it is not an averaging escape hatch. A high overall score never overrides a low-priority-category failure or a failed mandatory Stage 8 check.
- Score-row ownership note (mandatory): ownership-driven dependency quality and shortcut avoidance are judged mainly inside `Ownership Clarity and Boundary Encapsulation` plus `API / Interface / Query / Command Clarity` and `Separation of Concerns and File Placement`, rather than as a separate top-level score row.
- Mandatory review checks:
  - data-flow spine inventory preservation,
  - ownership boundary preservation,
  - off-spine concern clarity,
  - existing capability/subsystem reuse,
  - reusable-owned-structure extraction where repeated structures should not stay duplicated,
  - shared-structure/data-model tightness and shared-base coherence,
  - repeated-coordination ownership,
  - empty-indirection control,
  - scope-appropriate separation of concerns and file responsibility clarity,
  - ownership-driven dependency quality (low coupling, no unjustified cycles, no forbidden shortcuts),
  - boundary encapsulation preservation (no caller depends on both an authoritative boundary and one of its internal lower-level concerns),
  - architecture/boundary quality under the shared design principles and common design practices,
  - file placement and folder ownership quality under the shared design principles and common design practices,
  - flat-vs-over-split layout judgment,
  - interface/API/query/command/service-method boundary clarity with explicit identity shapes,
  - naming quality across files/folders/APIs/types/functions/parameters/variables,
  - naming-to-responsibility alignment and drift,
  - no unjustified duplication of code or repeated structures in changed scope,
  - patch-on-patch complexity smells,
  - dead/obsolete code cleanup completeness in changed scope,
  - no backward-compatibility mechanisms and no legacy code retention,
  - test quality, test maintainability, and validation-evidence sufficiency.
- Stable finding-ID rule (mandatory): reuse the same finding ID for the same unresolved issue across review rounds. Create a new finding ID only for newly discovered issues.
- Earlier design artifacts are Stage 8 context only, not the authority. If independent review shows the earlier design basis was weak, incomplete, or wrong, classify `Design Impact`.
- Source file size policy (mandatory):
  - measure line counts explicitly per changed source file:
    - effective non-empty line count command: `rg -n "\\S" <file-path> | wc -l`
    - per-file changed-line delta command: `git diff --numstat <base-ref>...HEAD -- <file-path>`
  - enforcement baseline uses effective non-empty line count.
  - for changed source files with effective non-empty line count `<= 500`, run normal review checks.
  - hard limit rule: if any changed source file has effective non-empty line count `> 500`, default classification is `Design Impact` and Stage 8 decision is `Fail`.
  - for `> 500` hard-limit cases, do not continue by default; trigger re-entry with investigation checkpoint first (`Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`).
  - no soft middle band (`501-700`) and no default exception path in this workflow.
  - delta gate (mandatory): if a single changed source file has `> 220` changed lines in the current diff, record a design-impact assessment even when file size is `<= 500`.
- Gate decision:
- `Pass`: continue to `Stage 9` only when all mandatory review checks (including `<=500` hard-limit + required `>220` delta-gate assessments + data-flow spine inventory/ownership/off-spine concern checks + existing-capability reuse + reusable-owned-structure extraction + shared-structure/data-model tightness + shared-base coherence + repeated-coordination ownership + empty-indirection control + scope-appropriate separation of concerns + file placement within the correct subsystem and folder, with any optional module grouping justified + flat-vs-over-split layout judgment + interface/API/query/command/service-method boundary clarity + naming quality across files/folders/APIs/types/functions/parameters/variables + naming-to-responsibility alignment + no unjustified duplication of code/repeated structures in changed scope + patch-on-patch complexity control + dead/obsolete code cleanup completeness in changed scope + test quality + test maintainability + validation-evidence sufficiency + no-backward-compat/no-legacy checks) are `Pass`, the detailed review scorecard is recorded in the canonical priority order, and no scorecard category is below `9.0`.
  - `Fail`: apply re-entry declaration and follow re-entry mapping before any source code edits.
- Stage 8 failure classification rule (mandatory):
  - `Local Fix`: the issue requires source changes but remains inside the shared design principles and intended behavior without requiring design or requirement artifact updates; rerun `Stage 6 -> Stage 7 -> Stage 8`.
  - `Validation Gap`: the main issue is insufficient Stage 7 coverage or evidence; rerun `Stage 7 -> Stage 8` without forcing design or source changes by default.
  - `Design Impact`: independent review found an architectural or structural problem in the code, or revealed that the earlier design basis was weak/wrong/incomplete; rerun `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`.
  - `Requirement Gap`: review exposed missing or ambiguous intended behavior; rerun `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`.
  - `Unclear`: root cause is cross-cutting or confidence is too low; rerun `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`.
- Treat wrong-location files as review failures when the path obscures ownership (for example, platform-specific code outside its platform folder without explicit shared-boundary rationale).
- If code review requires source changes, rerun `Stage 6 -> Stage 7 -> Stage 8`.
- If code review only requires stronger validation evidence, rerun `Stage 7 -> Stage 8`.
- Use `stages/08-code-review/code-review-template.md`.
- Do not speak for `code-review.md` edits alone. Announce when `workflow-state.md` records Stage 8 entry, gate result, and any re-entry declaration.

### 9) Synchronize Project Documentation (Mandatory Post-Testing + Review)

- Use `stages/09-docs-sync/docs-sync-guide.md`.
- Create/update `tickets/in-progress/<ticket-name>/docs-sync.md` as the canonical Stage 9 artifact.
- Use `stages/09-docs-sync/docs-sync-template.md`.
- After Stage 7 executable validation and Stage 8 code review are complete, update project documentation under the project `docs/` folder (and other canonical architecture docs such as `ARCHITECTURE.md` when impacted) so docs reflect the latest codebase behavior.
- Treat `docs/` as the long-lived canonical source of truth for the current codebase.
- Treat ticket artifacts under `tickets/` as task-local, time-bound records; they are not the long-term source of truth.
- Stage 9 exists to promote durable design and runtime knowledge out of time-bound ticket artifacts and into long-lived project documentation.
- The purpose is not only to say what changed, but to leave the codebase easier to understand after the ticket is archived.
- If relevant docs do not exist yet, create new docs in `docs/` with clear natural names that match current functionality.
- If relevant docs already exist, update them in place instead of creating duplicate overlapping docs.
- Use Stage 9 to explain:
  - what changed,
  - why it changed,
  - what the current subsystem, boundary, or runtime shape is now,
  - what was removed or replaced,
  - what operational or validation expectations changed.
- Update docs for:
  - new files, modules, or APIs,
  - changed runtime flows,
  - renamed/moved/removed components,
  - updated operational or testing procedures when behavior changed.
- If there is no docs impact, record an explicit "No docs impact" decision with rationale in `docs-sync.md`.
- Stage 9 blocked/reroute policy (mandatory):
  - if docs cannot yet be made truthful because the final implementation state or ticket artifacts still need a small concrete correction, classify `Local Fix` and rerun `Stage 6 -> Stage 7 -> Stage 8 -> Stage 9`,
  - if docs reveal missing or ambiguous intended behavior, classify `Requirement Gap` and rerun `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8 -> Stage 9`,
  - if the final implementation state or intended behavior is too unclear or cross-cutting to document truthfully, classify `Unclear` and rerun `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8 -> Stage 9`,
  - if docs cannot complete only because of an external docs-system or docs-access blocker, keep Stage 9 `Blocked` and stay in Stage 9 until the blocker is resolved,
  - after recording any Stage 9 re-entry path in `workflow-state.md`, immediately resume the first returned stage instead of stopping after only describing it.
- Docs synchronization is complete only when docs content aligns with the final implemented behavior.
- After docs synchronization result is recorded (`Updated`/`No impact`), announce only with the persisted `workflow-state.md` transition/gate update.

### 10) Final Handoff

- Complete handoff only after implementation execution, Stage 7 executable validation, Stage 8 code review, and docs synchronization are complete.
- Create/update `tickets/in-progress/<ticket-name>/handoff-summary.md` as the canonical Stage 10 artifact.
- Use `stages/10-handoff/handoff-guide.md` and `stages/10-handoff/handoff-summary-template.md`.
- Handoff summary must include:
  - delivered scope vs planned scope,
  - verification summary (unit/integration plus Stage 7 executable validation, acceptance-criteria closure status, and for infeasible criteria documented constraints + compensating automated evidence + explicit user waiver reference),
  - docs files updated (or explicit no-impact rationale) plus the `docs-sync.md` artifact path,
  - release-note status (`created` with artifact path, or explicit `not required` rationale).
- When release notes are required, create/update `tickets/in-progress/<ticket-name>/release-notes.md` before waiting for user verification.
- Release-note content rules (mandatory when release notes are required):
  - use short user-facing functional notes only,
  - do not include internal refactors, dependency bumps, tests, docs-only changes, or low-level implementation detail,
  - target `3` to `7` bullets total across all sections,
  - use the template in `stages/10-handoff/release-notes-template.md`,
  - default sections are `## What's New`, `## Improvements`, and `## Fixes`,
  - omit empty sections instead of writing filler content,
  - do not include upgrade steps unless the user explicitly asks for them.
- After the handoff summary is written, keep Stage 10 open until the user explicitly confirms completion/verification (for example after manual testing). Before that user signal, do not move the ticket to `done`, commit, push, merge, or run release/publication/deployment work.
- After the explicit user completion/verification signal, move the ticket folder to `tickets/done/<ticket-name>/` first so the archived ticket path is included in the final committed state.
- If the project is a git repository, repository finalization is mandatory after that move and must run in this order before Stage 10 cleanup can begin:
  - commit all in-scope changes on the ticket branch/worktree, including the moved ticket files,
  - push the ticket branch to remote,
  - update the resolved finalization target branch from remote before merging,
  - merge the ticket branch into the updated target branch,
  - push the updated target branch to remote.
- After repository finalization, if release/publication/deployment is applicable for the project, run the documented project method. This may be a release script, a documented command, a git tag workflow, GitHub Release creation, or another documented deployment/publication path.
- If no release/publication/deployment step is applicable, record that explicitly and do not block repository finalization.
- After repository finalization and any applicable release/publication/deployment work, if Stage 0 recorded a dedicated ticket worktree/branch for this ticket, cleanup is mandatory before Stage 10 is marked complete:
  - if needed, step out to a safe parent repo checkout before removing the ticket worktree,
  - remove the dedicated ticket worktree recorded in Stage 0,
  - run worktree-prune cleanup,
  - when the local ticket branch is fully merged into the resolved finalization target and no longer needed, delete the local ticket branch,
  - do not delete remote branches unless explicit user instruction or documented project policy requires it.
- Resolve the finalization target branch from the Stage 0 bootstrap record by default, or from explicit later user instruction when the user overrides it. If the branch cannot be identified confidently, stop and ask once before merge/finalization instead of guessing.
- If moving the ticket to `done` or any repository-finalization step fails (commit/push/merge conflict/remote rejection), record the blocker in `workflow-state.md`, keep Stage 10 open, and resume only after the blocker is resolved.
- If an applicable release/publication/deployment step later fails or is undocumented, record that blocker in `workflow-state.md`, keep Stage 10 open, and do not undo completed repository finalization.
- If required worktree/branch cleanup fails after repository finalization, record that blocker in `workflow-state.md`, keep Stage 10 open, and finish cleanup before treating the ticket as done.
- Ticket state transition:
  - keep ticket under `tickets/in-progress/<ticket-name>/` by default after handoff and while waiting for explicit user completion/verification,
  - on explicit user confirmation that the ticket is finished/verified (or explicit user move instruction), first move the ticket to `tickets/done/<ticket-name>/`, then run repository finalization if applicable.
  - if the user reopens a completed ticket, move it back to `tickets/in-progress/<ticket-name>/` before any additional artifact updates.
- Speak final handoff completion only after all required artifacts/docs outputs are written and the final `workflow-state.md` transition/gate state is persisted.

## Output Defaults

If the user does not specify file paths, write to a project-local ticket folder in stage order:
These defaults list file-producing stages; gating and handoff rules still follow the full workflow above.

- Stage 0 (bootstrap + draft requirement):
  - create/use `tickets/in-progress/<ticket-name>/`
  - if git repo, resolve bootstrap base branch from explicit user instruction when provided; otherwise infer the tracked remote default/integration branch with highest confidence
  - if git repo and a new ticket worktree/branch is needed, refresh tracked remote refs first
  - if git repo, create/reuse dedicated ticket worktree for `codex/<ticket-name>`; when creating a new ticket branch, branch it from the latest tracked remote base
  - create/update `tickets/in-progress/<ticket-name>/workflow-state.md` (`Current Stage = 0`, `Code Edit Permission = Locked`, `Stage 0 Bootstrap Record` filled)
  - `tickets/in-progress/<ticket-name>/requirements.md` (`Draft`)
- Stage 1 (investigation + understanding + triage):
  - update `tickets/in-progress/<ticket-name>/workflow-state.md` transition (`0 -> 1`)
  - `tickets/in-progress/<ticket-name>/investigation-notes.md`
- Stage 2 (requirements refinement to `Design-ready`):
  - update `tickets/in-progress/<ticket-name>/workflow-state.md` transition (`1 -> 2`)
  - update `tickets/in-progress/<ticket-name>/requirements.md` in place
- Stage 3 (design basis):
  - update `tickets/in-progress/<ticket-name>/workflow-state.md` transition (`2 -> 3`)
  - `Small`: start/refine `tickets/in-progress/<ticket-name>/implementation.md` (solution sketch section only for design basis).
  - `Medium/Large`: create/refine `tickets/in-progress/<ticket-name>/proposed-design.md`.
- Stage 4 (future-state runtime call stack):
  - update `tickets/in-progress/<ticket-name>/workflow-state.md` transition (`3 -> 4`)
  - `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack.md`
- Stage 5 (future-state runtime call stack review, iterative):
  - update `tickets/in-progress/<ticket-name>/workflow-state.md` transition (`4 -> 5`)
  - `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack-review.md`
- Stage 6 (only after gate `Go Confirmed`):
  - update `tickets/in-progress/<ticket-name>/workflow-state.md` (`Current Stage = 6`, `Code Edit Permission = Unlocked` only when pre-edit checklist is `Pass`)
  - finalize/update `tickets/in-progress/<ticket-name>/implementation.md`
  - execute source implementation plus required unit/integration verification and log progress in real time
  - close Stage 6 only when no backward-compatibility/legacy-retention paths remain in scope, ownership-driven dependencies remain valid, and touched files sit in the correct folder under the correct owning subsystem
- Stage 7 (API/E2E + executable validation implementation and gate):
  - update `tickets/in-progress/<ticket-name>/workflow-state.md` (`Current Stage = 7`, `Code Edit Permission = Unlocked`)
  - create/update `tickets/in-progress/<ticket-name>/api-e2e-testing.md`
  - maintain acceptance-criteria matrix (`acceptance_criteria_id` -> scenario coverage -> pass status)
  - maintain spine coverage matrix (`spine_id` -> scenario coverage -> pass status)
  - record scenario execution results and any escalation decisions in `tickets/in-progress/<ticket-name>/api-e2e-testing.md`
- Stage 8 (code review gate, only after `Stage 7 = Pass`):
  - update `tickets/in-progress/<ticket-name>/workflow-state.md` (`Current Stage = 8`, `Code Edit Permission = Locked`)
  - create/update `tickets/in-progress/<ticket-name>/code-review.md`
  - record the detailed review scorecard plus gate result (`Pass`/`Fail`) and any re-entry declaration before `Stage 9`
- Stage 9 (post-testing documentation sync):
  - update `tickets/in-progress/<ticket-name>/workflow-state.md` transition (`8 -> 9`)
  - create/update `tickets/in-progress/<ticket-name>/docs-sync.md`
  - update existing impacted docs in place (for example `docs/**/*.md`, `ARCHITECTURE.md`)
  - create missing relevant docs in `docs/` when no existing doc covers the implemented functionality
  - record docs sync result in `tickets/in-progress/<ticket-name>/docs-sync.md` (`Updated`/`No impact` + rationale)
- Stage 10 (final handoff + wait for user verification + move ticket to done + repository finalization + cleanup):
  - update `tickets/in-progress/<ticket-name>/workflow-state.md` transition (`9 -> 10`) and final state record
  - create/update `tickets/in-progress/<ticket-name>/handoff-summary.md` using `stages/10-handoff/handoff-summary-template.md`
  - persist the handoff summary and wait for explicit user completion/verification instruction
  - when the release is user-facing or publishes a GitHub Release body, create/update `tickets/in-progress/<ticket-name>/release-notes.md` using `stages/10-handoff/release-notes-template.md`; otherwise record explicit no-note rationale in the handoff summary
  - on explicit user completion/verification instruction, first move the ticket folder to `tickets/done/<ticket-name>/`
  - if git repo and the user explicitly confirms completion/verification, commit all in-scope changes on the ticket branch/worktree, including the moved ticket files
  - if git repo and the user explicitly confirms completion/verification, push the ticket branch to remote
  - if git repo and the user explicitly confirms completion/verification, update the resolved finalization target branch from remote, merge the ticket branch into it, and push the updated target branch
  - if git repo and the user explicitly confirms completion/verification and the project has an applicable documented release/publication/deployment step, run that method after repository finalization and feed it the archived ticket release-notes artifact (typically `tickets/done/<ticket-name>/release-notes.md`) when release notes are required
  - if git repo and Stage 0 recorded a dedicated ticket worktree/branch for this ticket, after repository finalization and any applicable release/publication/deployment work, remove that dedicated worktree, run worktree prune, and when the local ticket branch is fully merged into the resolved finalization target and no longer needed, delete the local ticket branch
  - keep ticket in `tickets/in-progress/<ticket-name>/` unless user explicitly confirms completion/verification or asks to move it
  - if user reopens later, move it back to `tickets/in-progress/<ticket-name>/` before new updates

## Templates And References

- Shared:
  - `shared/design-principles.md`
  - `shared/common-design-practices.md`
  - `shared/workflow-state-template.md`
- Stage 0 bootstrap:
  - `stages/00-bootstrap/bootstrap-checklist.md`
- Stage 1 investigation:
  - `stages/01-investigation/investigation-guide.md`
- Stage 2 requirements:
  - `stages/02-requirements/requirements-refinement-guide.md`
- Stage 3 design:
  - `stages/03-design/proposed-design-template.md`
- Stage 4 future-state runtime call stack:
  - `stages/04-future-state-runtime-call-stack/future-state-runtime-call-stack-template.md`
- Stage 5 future-state runtime call stack review:
  - `stages/05-future-state-runtime-call-stack-review/future-state-runtime-call-stack-review-template.md`
- Stage 6 implementation:
  - `stages/06-implementation/implementation-template.md`
  - `stages/06-implementation/implementation-example.md`
- Stage 7 API/E2E + executable validation:
  - `stages/07-api-e2e/README.md`
  - `stages/07-api-e2e/api-e2e-guide.md`
  - `stages/07-api-e2e/api-e2e-testing-template.md`
- Stage 8 code review:
  - `stages/08-code-review/README.md`
  - `stages/08-code-review/code-review-guide.md`
  - `stages/08-code-review/code-review-principles.md`
  - `stages/08-code-review/code-review-template.md`
- Stage 9 docs sync:
  - `stages/09-docs-sync/docs-sync-guide.md`
  - `stages/09-docs-sync/docs-sync-template.md`
- Stage 10 handoff:
  - `stages/10-handoff/README.md`
  - `stages/10-handoff/handoff-guide.md`
  - `stages/10-handoff/handoff-summary-template.md`
  - `stages/10-handoff/release-notes-template.md`
