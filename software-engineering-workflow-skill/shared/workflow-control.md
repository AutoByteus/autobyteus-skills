# Workflow Control

Canonical cross-stage workflow-control reference.
Use `SKILL.md` for the stage map and stage-owner routing.
Use the stage guides for detailed stage behavior.
Use this reference for stage movement, workflow-state enforcement, edit locks, re-entry control, and transition notifications.

## Control Principles

- Work in explicit stage gates. Do not batch-generate all downstream artifacts by default.
- Even when the user asks for everything in one turn, still enforce the stage gates within that same turn.
- `tickets/in-progress/<ticket-name>/workflow-state.md` is the mandatory execution-control artifact.
- Update `workflow-state.md` before every stage transition, gate decision, re-entry declaration, or code-edit lock change.
- Transition authority rule: when a trigger condition matches the Stage Transition Contract or Transition Matrix below, follow that mapped path instead of continuing in the current stage by preference.
- Transition execution rule: after recording a transition in `workflow-state.md`, immediately resume the target stage by default. A transition is not complete until work has actually resumed there.
- Re-entry completion rule: after recording a classified return path in `workflow-state.md`, immediately resume the first returned stage by default. Recording the path alone is not enough.
- Persist required artifact updates in the owning returned stage. Do not carry required refinements only in memory across rounds.
- Stage 0 handles ticket bootstrap/start rules.
- Stage 10 handles explicit user verification, archival, repository finalization, release/publication/deployment, and post-finalization cleanup.

## Workflow-State And Code-Edit Lock

- Initialize `workflow-state.md` in Stage 0 from `shared/workflow-state-template.md`.
- Treat `workflow-state.md` as an execution lock controller, not optional documentation.
- No source-code edits are allowed unless all of the following are true in `workflow-state.md`:
  - `Current Stage = 6`
  - `Code Edit Permission = Unlocked`
  - Stage 5 gate is `Go Confirmed`
  - required upstream artifacts are marked current for the ticket
- On any Stage 7 or Stage 8 failure that requires re-entry, lock source edits before starting upstream return work.
- If code is edited while the lock is active, record the violation in `workflow-state.md`, stop further source edits, and return through the required classified path.

## Transition Notifications

- Use required audible notifications only for persisted workflow-state changes.
- For required audible updates, call `Speak` with `play=true` unless the user explicitly requests silent mode.
- Do not emit audible updates for low-level command execution, intermediate analysis notes, or partial drafts.
- Update `workflow-state.md` first, then emit the audible update.
- Required audible events:
  - workflow kickoff
  - stage transitions
  - gate decisions
  - re-entry declarations
  - code-edit lock changes
- Include:
  - current stage
  - what just changed
  - next stage or next action
  - code-edit lock state when it changed
- If multiple transitions happen close together, batch them into one short message after the final persisted update.
- Keep spoken updates short, status-first, and action-oriented.
- Do not speak secrets, tokens, or sensitive payloads.
- If the `Speak` tool is unavailable, continue and provide the same status in text.

## Stage Transition Contract

| Stage | Exit Condition | On Fail / Blocked | Next Stage On Pass |
| --- | --- | --- | --- |
| 0 | ticket bootstrap is complete and `requirements.md` status is `Draft` | stay in `0` until bootstrap is complete | `1` |
| 1 | `investigation-notes.md` is current and scope triage is recorded | stay in `1` until investigation evidence is complete | `2` |
| 2 | `requirements.md` is `Design-ready` or `Refined` with coverage mappings | stay in `2` until requirements are design-ready | `3` |
| 3 | current design basis exists for the current scope | stay in `3` and refine the design basis | `4` |
| 4 | `future-state-runtime-call-stack.md` is current for in-scope use cases | stay in `4` and regenerate the runtime call stack artifact | `5` |
| 5 | review reaches `Go Confirmed` with no blockers, no required persisted updates, and no new use cases in the confirming rounds | classify and re-enter before the next round | `6` |
| 6 | implementation is complete, required unit/integration checks pass, and no scoped legacy, placement, or ownership blockers remain | stay in `6` for local fixes; classify and re-enter for non-local issues | `7` |
| 7 | executable validation scenarios are implemented and all executable mapped acceptance criteria are `Passed` or explicitly `Waived` by user decision | `Blocked` for infeasible or unwaived scenarios; otherwise classify and re-enter | `8` |
| 8 | code review decision is `Pass` with all mandatory review checks satisfied | classify and re-enter | `9` |
| 9 | docs are current or explicit no-impact rationale is recorded | classify and re-enter when truthful docs require upstream change; stay `Blocked` for external docs-only blockers | `10` |
| 10 | explicit user verification is received and required archival/finalization work is complete | stay in `10` until verification and finalization are complete | End |

## Transition Matrix

| Trigger | Required Transition Path | Notes |
| --- | --- | --- |
| Stage 5 blocker `Design Impact` | `3 -> 4 -> 5` | clear design or architecture issue |
| Stage 5 blocker `Requirement Gap` | `2 -> 3 -> 4 -> 5` | missing or ambiguous requirement or acceptance criterion |
| Stage 5 blocker `Unclear` | `1 -> 2 -> 3 -> 4 -> 5` | uncertainty requires refreshed investigation |
| Stage 6 failure `Local Fix` | stay in `Stage 6` | bounded implementation repair |
| Stage 6 failure `Design Impact` | `1 -> 3 -> 4 -> 5 -> 6` | non-local structural issue |
| Stage 6 failure `Requirement Gap` | `2 -> 3 -> 4 -> 5 -> 6` | update requirements first |
| Stage 6 failure `Unclear` | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6` | reopen full chain in the same ticket context |
| Stage 7 failure `Local Fix` | `6 -> 7` | update artifacts first, then fix, then rerun |
| Stage 7 failure `Design Impact` | `1 -> 3 -> 4 -> 5 -> 6 -> 7` | architecture or boundary issue |
| Stage 7 failure `Requirement Gap` | `2 -> 3 -> 4 -> 5 -> 6 -> 7` | missing intended behavior |
| Stage 7 failure `Unclear` | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7` | cross-cutting root cause |
| Stage 7 infeasible scenario without user waiver | stay in `Stage 7 (Blocked)` | wait for user waiver or environment fix |
| Stage 8 fail `Local Fix` | `6 -> 7 -> 8` | source change required |
| Stage 8 fail `Validation Gap` | `7 -> 8` | stronger Stage 7 evidence required |
| Stage 8 fail `Design Impact` | `1 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | independent review found structural weakness |
| Stage 8 fail `Requirement Gap` | `2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | intended behavior is incomplete or ambiguous |
| Stage 8 fail `Unclear` | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` | cross-cutting uncertainty |
| Stage 9 blocked `Local Fix` | `6 -> 7 -> 8 -> 9` | docs cannot be truthful until a small correction is made |
| Stage 9 blocked `Requirement Gap` | `2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9` | intended behavior is not clear enough to document |
| Stage 9 blocked `Unclear` | `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9` | final behavior is too unclear to document truthfully |
| Stage 9 external docs-only blocker | stay in `Stage 9 (Blocked)` | no upstream artifact changes required |
| Stage 10 waiting for explicit user verification | stay in `Stage 10 (In Progress)` | wait before archival and finalization |
| Stage 10 archival/finalization/release/cleanup blocker | stay in `Stage 10 (Blocked)` | record and resolve the blocker |

## Re-Entry Rules

- Stage 5 classified re-entry:
  - `Design Impact`: `Stage 3 -> Stage 4 -> Stage 5`
  - `Requirement Gap`: `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5`
  - `Unclear`: `Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5`
- Stage 6 classified re-entry:
  - `Local Fix`: stay in `Stage 6`
  - `Design Impact`: `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`
  - `Requirement Gap`: `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`
  - `Unclear`: `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`
- Stage 7 classified re-entry:
  - `Local Fix`: `Stage 6 -> Stage 7`
  - `Design Impact`: `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`
  - `Requirement Gap`: `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`
  - `Unclear`: `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7`
- Stage 8 classified re-entry:
  - `Local Fix`: `Stage 6 -> Stage 7 -> Stage 8`
  - `Validation Gap`: `Stage 7 -> Stage 8`
  - `Design Impact`: `Stage 1 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`
  - `Requirement Gap`: `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`
  - `Unclear`: `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8`
- Stage 9 classified re-entry:
  - `Local Fix`: `Stage 6 -> Stage 7 -> Stage 8 -> Stage 9`
  - `Requirement Gap`: `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8 -> Stage 9`
  - `Unclear`: `Stage 0 -> Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8 -> Stage 9`
- Stage 0 in a re-entry path means reopen bootstrap controls in the same ticket context. Do not create a new ticket folder.
- For post-implementation gate failures, update required upstream artifacts first. Do not patch source code first and rationalize the design later.
