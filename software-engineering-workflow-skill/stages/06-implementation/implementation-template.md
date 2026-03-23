# Implementation

Use this single artifact for both:
- the stable Stage 6 implementation baseline
- the live Stage 6 execution/progress record
- brief downstream handoff/status pointers for Stages 7, 8, and 9

Write to:
- `tickets/in-progress/<ticket-name>/implementation.md`

Document discipline:
- `Plan Baseline` sections are the intended implementation shape and should change only when replanning or classified re-entry requires it.
- `Execution Tracking` sections are live logs and should be updated continuously during implementation and when downstream stage status changes materially.
- `Implementation Work Table` is the primary file/task tracker. Prefer change IDs elsewhere instead of repeating the same file list unless exact paths are the point of that section.
- Keep applying the shared design principles and common design practices during implementation. Do not treat the reviewed design artifact as mechanically complete if file-level reality reveals a tighter or safer shape.
- Detailed Stage 7, Stage 8, and Stage 9 records belong in their own canonical artifacts. Keep only handoff inputs and short status pointers here.

## Scope Classification

- Classification: `Small` / `Medium` / `Large`
- Reasoning:
- Workflow Depth:
  - `Small` -> draft `implementation.md` solution sketch -> future-state runtime call stack -> future-state runtime call stack review (iterative deep rounds until `Go Confirmed`) -> finalize `implementation.md` baseline -> implementation execution
  - `Medium` -> proposed design doc -> future-state runtime call stack -> future-state runtime call stack review (iterative deep rounds until `Go Confirmed`) -> `implementation.md` baseline -> implementation execution
  - `Large` -> proposed design doc -> future-state runtime call stack -> future-state runtime call stack review (iterative deep rounds until `Go Confirmed`) -> `implementation.md` baseline -> implementation execution

## Upstream Artifacts (Required)

- Workflow state: `tickets/in-progress/<ticket-name>/workflow-state.md`
- Investigation notes: `tickets/in-progress/<ticket-name>/investigation-notes.md`
- Requirements: `tickets/in-progress/<ticket-name>/requirements.md`
  - Current Status: `Design-ready` / `Refined`
- Runtime call stacks: `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack.md`
- Future-state runtime call stack review: `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack-review.md`
- Proposed design (required for `Medium/Large`): `tickets/in-progress/<ticket-name>/proposed-design.md`

## Document Status

- Current Status: `Draft` / `Blocked By Review Gate` / `Review-Gate-Validated` / `Ready For Implementation` / `In Execution`
- Notes:

## Plan Baseline (Freeze Until Replanning)

### Preconditions (Must Be True Before Finalizing The Baseline)

- `requirements.md` is at least `Design-ready` (`Refined` allowed):
- Acceptance criteria use stable IDs (`AC-*`) with measurable expected outcomes:
- `workflow-state.md` is current and Stage 5 review-gate evidence is recorded:
- Runtime call stack review artifact exists and is current:
- All in-scope use cases reviewed:
- No unresolved blocking findings:
- Future-state runtime call stack review has `Go Confirmed` with two consecutive clean deep-review rounds (no blockers, no required persisted artifact updates, no newly discovered use cases):
- Missing-use-case discovery sweeps completed for the final two clean rounds:
- No newly discovered use cases in the final two clean rounds:

### Solution Sketch (Required For `Small`, Optional Otherwise)

- Use Cases In Scope:
- Spine Inventory In Scope:
- Primary Owners / Main Domain Subjects:
- Requirement Coverage Guarantee (all requirements mapped to at least one use case):
- Design-Risk Use Cases (if any, with risk/objective):
- Target Architecture Shape:
- New Owners/Boundary Interfaces To Introduce:
- Primary file/task set: see `Implementation Work Table`.
- API/Behavior Delta:
- Key Assumptions:
- Known Risks:

### Runtime Call Stack Review Gate Summary (Required)

| Round | Review Result | Findings Requiring Persisted Updates | New Use Cases Discovered | Persisted Updates Completed | Classification (`Design Impact`/`Requirement Gap`/`Unclear`/`N/A`) | Required Re-Entry Path | Round State (`Reset`/`Candidate Go`/`Go Confirmed`) | Clean Streak After Round |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Pass/Fail | Yes/No | Yes/No | Yes/No/N/A |  |  |  |  |
| 2 | Pass/Fail | Yes/No | Yes/No | Yes/No/N/A |  |  |  |  |
| N | Pass/Fail | Yes/No | Yes/No | Yes/No/N/A |  |  |  |  |

### Go / No-Go Decision

- Decision: `Go` / `No-Go`
- Evidence:
  - Final review round:
  - Clean streak at final round:
  - Final review gate line (`Implementation can start`):
- If `No-Go`, required refinement target:
  - `Small`: refine `implementation.md` solution sketch, then regenerate call stack and re-review.
  - `Medium/Large`: refine proposed design document, then regenerate call stack and re-review.

### Principles

- Bottom-up: implement dependencies before dependents.
- Test-driven: write unit tests and integration tests alongside implementation.
- Spine-led implementation rule: sequence work by spine and owner first; file order is derived from that structure, and any optional module grouping follows the ownership model rather than leading it.
- Mandatory modernization rule: no backward-compatibility shims or legacy branches.
- Mandatory cleanup rule: remove dead code, obsolete files, unused helpers/tests/flags/adapters, and dormant replaced paths in scope before Stage 6 can close.
- Mandatory ownership/decoupling/SoC rule: preserve clear subsystem boundaries, one-way dependency direction, and scope-appropriate file responsibilities; avoid adding tight coupling/cycles or mixed-concern files.
- Mandatory shared-structure coherence rule: when implementing shared data structures, keep the shared core tight. If one case needs extra fields, use a meaningful specialized variant or composition instead of expanding the shared base into a kitchen-sink shape.
- Mandatory file-placement rule: keep each touched file in the folder/boundary that owns its concern; plan explicit moves when current placement is misleading.
- Mandatory shared-principles implementation rule: apply the shared design principles and common design practices independently during coding. If file-level implementation detail reveals that the reviewed design is incomplete, weak, or wrong, record the issue and classify `Design Impact` instead of patching around it locally.
- Mandatory proactive size-pressure rule: treat Stage 8 source-file size gates as active Stage 6 guardrails for changed source implementation files. Do not knowingly expand or leave a changed source implementation file above `500` effective non-empty lines. If one changed source implementation file trends toward that limit or exceeds `220` changed lines in the current diff, split/refactor/escalate during implementation instead of waiting for Stage 8. Test files do not use this hard source-file limit.
- Choose the proper structural change for architecture integrity; do not prefer local hacks just because they are smaller.
- One file at a time is the default; use limited parallel work only when dependency edges require it.

### Spine-Led Dependency And Sequencing Map

| Order | Spine ID | Owner | Task / File | Depends On | Why This Order |
| --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

### File Placement Plan (Mandatory)

| Item | Current Path | Target Path | Owning Concern / Platform | Action (`Keep`/`Move`/`Split`/`Promote Shared`) | Verification |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

### Implementation Work Table (Primary Tracker)

Use this as the main Stage 6 table for planned file responsibilities and live execution status.
Avoid creating separate repeated file lists elsewhere unless the section is specifically about path migration or review evidence.

| Change ID | Spine ID(s) | Owner | Concern | Current Path | Target Path | Action (`Create`/`Modify`/`Move`/`Split`/`Remove`) | Depends On | Implementation Status (`Planned`/`In Progress`/`Completed`/`Blocked`) | Unit Test File | Unit Test Status (`Planned`/`Passed`/`Failed`/`N/A`) | Integration Test File | Integration Test Status (`Planned`/`Passed`/`Failed`/`N/A`) | Stage 8 Review Status (`Planned`/`Passed`/`Failed`/`N/A`) | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-001 | DS-001 |  |  |  |  |  |  | Planned |  | Planned |  | Planned | Planned |  |

### Requirement, Spine, And Design Traceability

| Requirement | Acceptance Criteria ID(s) | Spine ID(s) | Design Section | Use Case / Call Stack | Planned Task ID(s) | Stage 6 Verification (Unit/Integration) | Stage 7 Scenario ID(s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-001 | AC-001 | DS-001 |  | UC-001 |  | Unit/Integration | AV-001 |

### Stage 7 Planned Coverage Mapping (Input Only)

Use this as Stage 6 planning input for Stage 7.
The canonical Stage 7 execution record, closure matrices, feasibility record, and scenario results belong in `tickets/in-progress/<ticket-name>/api-e2e-testing.md`.

| Acceptance Criteria ID | Requirement ID | Spine ID(s) | Expected Outcome | Stage 7 Scenario ID(s) | Test Level (`API`/`E2E`) | Initial Status (`Planned`/`Blocked`) |
| --- | --- | --- | --- | --- | --- | --- |
| AC-001 | R-001 | DS-001 |  | AV-001 | API | Planned |

### Design Delta Traceability (Required For `Medium/Large`)

| Change ID (from proposed design doc) | Planned Task ID(s) | Includes Remove/Rename Work | Verification |
| --- | --- | --- | --- |
| C-001 |  | Yes/No | Unit/Integration + AV-Scenario |

### Decommission / Rename Execution Tasks

| Task ID | Item | Action (`Remove`/`Rename`/`Move`) | Cleanup Steps | Risk Notes |
| --- | --- | --- | --- | --- |
| T-DEL-001 |  |  |  |  |

### Step-By-Step Plan

1.
2.
3.

### Backward-Compat And Decoupling Guardrails (Mandatory)

- Backward-compatibility mechanisms introduced: `None` / `List + redesign required`
- Legacy code retained for old behavior: `No` / `Yes (blocked)`
- Dead/obsolete code or unused helpers/tests/flags/adapters left in scope: `No` / `Yes (blocked)`
- Shared data structures remain tight (no kitchen-sink base or overlapping parallel shapes introduced): `Yes` / `No (blocked)`
- Shared design/common-practice rules reapplied during implementation (and any file-level design weakness routed as `Design Impact` when needed): `Yes` / `No (blocked)`
- Decoupling impact assessment completed: `Yes` / `No`
- New tight coupling or cyclic dependency introduced: `No` / `Yes (blocked)`
- Changed source implementation files kept within proactive size-pressure guardrails (`>500` avoided; `>220` pressure assessed/acted on): `Yes` / `No (blocked)`

### Code Review Gate Plan (Stage 8)

- Gate artifact path: `tickets/in-progress/<ticket-name>/code-review.md`
- Scope (source + tests):
- line-count measurement command (`effective non-empty`):
  - effective non-empty line count: `rg -n "\\S" <file-path> | wc -l`
  - changed-line delta: `git diff --numstat <base-ref>...HEAD -- <file-path>`
- `>500` effective-line source file hard-limit policy and expected design-impact action:
- per-file diff delta gate (`>220` changed lines) assessment approach:
- Hard-limit handling details in `code-review.md` (required re-entry path and split/refactor plan):
- file-placement review approach (how wrong-folder placements will be detected and corrected):

| File | Current Line Count | Adds/Expands Functionality (`Yes`/`No`) | Ownership/SoC Risk (`Low`/`Medium`/`High`) | Required Action (`Keep`/`Split`/`Move`/`Refactor`) | Expected Review Classification if not addressed |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

### Test Strategy

- Unit tests:
- Integration tests:
- Stage 6 boundary: file and service-level verification, while preserving readable subsystem grouping, only (unit + integration).
- Stage 7 handoff notes for API/E2E testing:
  - canonical artifact path: `tickets/in-progress/<ticket-name>/api-e2e-testing.md`
  - expected acceptance criteria count:
  - critical flows to validate (API/E2E):
  - expected scenario count:
  - known environment constraints:
  - detailed scenario execution results, failure history, and escalation records belong in the Stage 7 artifact, not here
- Stage 8 handoff notes for code review:
  - canonical artifact path: `tickets/in-progress/<ticket-name>/code-review.md`
  - predicted design-impact hotspots:
  - predicted file-placement hotspots:
  - predicted interface/API/query/command/service-method boundary hotspots:
  - files likely to exceed size/ownership/SoC thresholds:

### Cross-Reference Exception Protocol

| File | Cross-Reference With | Why Unavoidable | Temporary Strategy | Unblock Condition | Design Follow-Up Status | Owner |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | `Not Needed` / `Needed` / `In Progress` / `Updated` |  |

### Design Feedback Loop

| Smell/Issue | Evidence (Files/Call Stack) | Design Section To Update | Action | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  | Pending |

## Execution Tracking (Update Continuously)

### Kickoff Preconditions Checklist

- Workflow state is current (`tickets/in-progress/<ticket-name>/workflow-state.md`):
- `workflow-state.md` shows `Current Stage = 6` and `Code Edit Permission = Unlocked` before source edits:
- Scope classification confirmed (`Small`/`Medium`/`Large`):
- Investigation notes are current (`tickets/in-progress/<ticket-name>/investigation-notes.md`):
- Requirements status is `Design-ready` or `Refined`:
- Future-state runtime call stack review final gate is `Implementation can start: Yes`:
- Future-state runtime call stack review reached `Go Confirmed` with two consecutive clean deep-review rounds (no blockers, no required persisted artifact updates, no newly discovered use cases):
- No unresolved blocking findings:

### Progress Log

- YYYY-MM-DD: Implementation kickoff baseline created.

### Scope Change Log

| Date | Previous Scope | New Scope | Trigger | Required Action |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD | Small | Medium | Example: architectural complexity exceeded small-scope assumptions | Follow classified re-entry path (`Design Impact`: `1 -> 3 -> 4 -> 5 -> 6`, `Requirement Gap`: `2 -> 3 -> 4 -> 5 -> 6`, `Unclear`: `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6`), rerun review to `Go Confirmed`, then resume implementation. |

### Implementation Work Updates

Update rows in the `Implementation Work Table` above instead of creating another repeated per-file list.
Use this section only for execution-only details that do not belong in the main table.

| Change ID | Last Failure Classification | Last Failure Investigation Required | Cross-Reference Smell | Design Follow-Up | Requirement Follow-Up | Last Verified | Verification Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-001 | Design Impact | Yes | `src/example-a.ts <-> src/example-core.ts` | Needed | Not Needed | YYYY-MM-DD | `pnpm exec vitest --run tests/unit/example-a.test.ts` | Waiting for boundary refactor. |

### Downstream Stage Status Pointers

Use this section only for short cross-stage pointers.
The detailed Stage 7, Stage 8, and Stage 9 records belong in their own canonical artifacts.

| Stage | Canonical Artifact | Current Status | Last Updated | Notes |
| --- | --- | --- | --- | --- |
| 7 API/E2E | `tickets/in-progress/<ticket-name>/api-e2e-testing.md` | `Not Started` / `In Progress` / `Passed` / `Failed` / `Blocked` / `Waived In Part` | YYYY-MM-DD |  |
| 8 Code Review | `tickets/in-progress/<ticket-name>/code-review.md` | `Not Started` / `In Progress` / `Pass` / `Fail` | YYYY-MM-DD |  |
| 9 Docs Sync | `tickets/in-progress/<ticket-name>/docs-sync.md` | `Not Started` / `In Progress` / `Updated` / `No impact` | YYYY-MM-DD |  |

### Blocked Items

| Change ID | Blocked By | Unblock Condition | Owner/Next Action |
| --- | --- | --- | --- |
| C-001 | `src/example-core.ts` | Core API finalized and tests pass | Resume implementation after boundary update. |

### Design Feedback Loop Log

| Date | Trigger File(s) | Smell Description | Design Section Updated | Update Status | Notes |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | `src/example-a.ts`, `src/example-core.ts` | Bidirectional dependency caused blocked implementation order. | `tickets/in-progress/<ticket-name>/proposed-design.md` (or `tickets/in-progress/<ticket-name>/implementation.md` solution sketch for `Small`) -> boundary section | In Progress | Introduce boundary interface to remove cross-reference. |

### Remove/Rename/Legacy Cleanup Verification Log

| Date | Change ID | Item | Verification Performed | Result | Notes |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | C-003 | `src/example-util.ts` | import/reference scan + targeted tests | Passed | No remaining references. |

### Completion Gate

- Mark `Implementation Status = Completed` only when implementation is done and required tests are passing or explicitly `N/A`.
- For `Rename/Move`/`Remove` tasks, verify obsolete references, dead branches, unused helpers/tests/flags/adapters, and dormant replaced paths are removed.
- Mark Stage 6 implementation execution complete only when:
  - implementation baseline scope is delivered (or deviations are documented),
  - required unit/integration tests pass,
  - no backward-compatibility shims or legacy old-behavior branches remain in scope,
  - dead code, obsolete files, unused helpers/tests/flags/adapters, and dormant replaced paths in scope are removed,
  - ownership-dependency/decoupling checks show no new unjustified tight coupling/cycles,
  - touched files have correct placement inside the owning subsystem and folder, or an explicit move/split has been completed,
  - changed source implementation files have proactive Stage 8 size-pressure handling recorded (`>500` avoided and `>220` pressure assessed/acted on where needed).
- Keep Stage 7, Stage 8, and Stage 9 gate authority in their own canonical artifacts:
  - `tickets/in-progress/<ticket-name>/api-e2e-testing.md`
  - `tickets/in-progress/<ticket-name>/code-review.md`
  - `tickets/in-progress/<ticket-name>/docs-sync.md`
