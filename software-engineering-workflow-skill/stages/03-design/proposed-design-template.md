# Proposed Design Document

## Design Version

- Current Version: `v1` / `v2` / ...

## Revision History

| Version | Trigger | Summary Of Changes | Related Review Round |
| --- | --- | --- | --- |
| v1 | Initial draft |  | 1 |

## Artifact Basis

- Investigation Notes: `tickets/in-progress/<ticket-name>/investigation-notes.md`
- Requirements: `tickets/in-progress/<ticket-name>/requirements.md`
- Requirements Status: `Design-ready` / `Refined`
- Shared Design Principles: `shared/design-principles.md`
- Common Design Practices: `shared/common-design-practices.md`

## Terminology

- `Subsystem` / `capability area`: a larger functional area that owns a broader category of work and may contain multiple files plus optional module groupings.
- `Module`: an optional intermediate grouping inside a subsystem when the codebase benefits from it. In this template, `module` is not a synonym for one file and not the default ownership term.
- `File`: one concrete source file and the primary unit where one concrete concern should land.
- `Folder` / `directory`: a physical grouping used to organize files and any optional module groupings.

## Design Reading Order

Read and write this design from abstract to concrete:

1. data-flow spine
2. subsystem / capability-area allocation
3. draft file responsibilities -> extract reusable owned structures -> finalize file responsibilities
4. folder/path mapping

## Reading Rule

- This document must be organized around the data-flow spine inventory first.
- Main domain subject nodes and ownership boundaries are the primary design story.
- Support branches are described in relation to the spine they serve.
- Existing capability areas/subsystems should be reused or extended when they naturally fit a support need.
- Files are the main concrete mapping target for concerns, and subsystems are the broader ownership context. Optional module groupings may appear only as derived implementation mapping when they help readability.
- Subsystem, folder, and file mapping should be spine-led and ownership-led, but not mechanical. Optional module groupings are secondary structure only when they help the reader.

## Summary

## Goal / Intended Change

## Legacy Removal Policy (Mandatory)

- Policy: `No backward compatibility; remove legacy code paths.`
- Required action: identify and remove obsolete legacy paths/files included in this scope.
- Treat removal as first-class design work: when clearer subsystem ownership, reusable owned structures, or tighter file responsibilities make fragmented or duplicated pieces unnecessary, name and remove/decommission them in scope.
- Gate rule: design is invalid if it depends on compatibility wrappers, dual-path behavior, or legacy fallback branches.

## Requirements And Use Cases

| Requirement ID | Description | Acceptance Criteria ID(s) | Acceptance Criteria Summary | Use Case IDs |
| --- | --- | --- | --- | --- |
| R-001 |  | AC-001 |  | UC-001 |

## Current-State Read

| Area | Findings | Evidence (files/functions) | Open Unknowns |
| --- | --- | --- | --- |
| Entrypoints / Current Spine Or Fragmented Flow |  |  |  |
| Current Ownership Boundaries |  |  |  |
| Current Coupling / Fragmentation Problems |  |  |  |
| Existing Constraints / Compatibility Facts |  |  |  |
| Relevant Files / Components |  |  |  |

## Current State (As-Is)

## Data-Flow Spine Inventory

List every relevant spine that matters to understanding the design.

| Spine ID | Scope (`Primary End-to-End`/`Return-Event`/`Bounded Local`) | Start | End | Owning Node / Governing Owner | Why It Matters |
| --- | --- | --- | --- | --- | --- |
| DS-001 |  |  |  |  |  |

Rule:
- If a loop, worker cycle, state machine, or dispatcher materially shapes behavior inside one owner, add a `Bounded Local` spine for it instead of leaving it implicit.

## Primary Execution / Data-Flow Spine(s)

Write each primary end-to-end line as a short arrow chain.

Examples:
- `Frontend -> API -> Service -> Repository -> Database`
- `Input -> RunManager -> Run -> RunBackend -> Runtime -> Provider`

## Spine Actors / Main-Line Nodes

| Node | Role In Spine | What It Advances |
| --- | --- | --- |
|  |  |  |

## Spine Narratives (Mandatory)

For each important spine, describe the end-to-end motion in prose so a reader can understand the design by following the flow instead of reconstructing it from file names.

| Spine ID | Short Narrative | Main Domain Subject Nodes | Governing Owner | Key Support Branches |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Ownership Map

| Node / Owner | Owns | Must Not Own | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Return / Event Spine(s) (If Applicable)

Write each return/event line using the same approach as the execution spine.

## Bounded Local / Internal Spines (If Applicable)

Use this section for important internal flows inside one owner, such as:
- event loop / worker loop flow,
- state-machine transition flow,
- queue dispatch flow,
- runtime callback/dispatch flow.

For each one, write:
- parent owner,
- start and end,
- short arrow chain,
- why it must be explicit in the design.

## Support Structure Around The Spine

| Support Branch / Service | Serves Which Owner | Responsibility | Must Stay Off Main Line? (`Yes`/`No`) |
| --- | --- | --- | --- |
|  |  |  |  |

## Existing Capability / Subsystem Reuse Check

| Need / Concern | Existing Capability Area / Subsystem | Decision (`Reuse`/`Extend`/`Create New`) | Why | If New, Why Existing Areas Are Not Right |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Subsystem / Capability-Area Allocation

Use this section to show which broader functional areas own which parts of the target behavior before you map concrete concerns into files.

| Subsystem / Capability Area | Owns Which Concerns | Related Spine ID(s) | Governing Owner(s) Served | Decision (`Reuse`/`Extend`/`Create New`) | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Ownership-Driven Dependency Rules

- Allowed dependency directions:
- Forbidden shortcuts:
- Temporary exceptions and removal plan:

## Architecture Direction Decision (Mandatory)

- Chosen direction:
- Rationale (`complexity`, `testability`, `operability`, `evolution cost`):
- Data-flow spine clarity assessment: `Yes` / `No`
- Spine inventory completeness assessment: `Yes` / `No`
- Ownership clarity assessment: `Yes` / `No`
- Support structure clarity assessment: `Yes` / `No`
- File placement within the owning subsystem assessment: `Yes` / `No`
- Outcome (`Keep`/`Add`/`Split`/`Merge`/`Move`/`Remove`):
- Note: `Keep` is valid only when the current spine, ownership boundaries, support structure, and file placement are already coherent for the in-scope behavior.

## Common Design Practices Applied (If Any)

| Practice / Pattern | Where Used | Why It Helps Here | Owner / Support Branch | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Ownership And Structure Checks (Mandatory)

| Check | Result (`Yes`/`No`) | Evidence | Decision |
| --- | --- | --- | --- |
| Repeated coordination policy across callers exists and needs a clearer owner |  |  | Extract clear owner / Keep |
| Responsibility overload exists in one file or one optional module grouping |  |  | Split / Keep |
| Proposed indirection owns real policy, translation, or boundary concern |  |  | Keep / Remove |
| Every support branch has a clear owner on the spine |  |  | Fix / Keep |
| Existing capability area/subsystem was reused or extended where it naturally fits |  |  | Reuse/Extend / Create New |
| Repeated structures were extracted into reusable owned files where needed |  |  | Extract / Keep Local |
| Current structure can remain unchanged without spine/ownership degradation |  |  | Keep / Change |

### Optional Alternatives (Use For Non-Trivial Or Uncertain Changes)

| Option | Summary | Pros | Cons | Decision (`Chosen`/`Rejected`) | Rationale |
| --- | --- | --- | --- | --- | --- |
| A |  |  |  |  |  |
| B |  |  |  |  |  |

## Change Inventory (Delta)

| Change ID | Change Type (`Add`/`Modify`/`Rename/Move`/`Remove`) | Current Path | Target Path | Rationale | Impacted Areas | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| C-001 |  |  |  |  |  |  |

## Removal / Decommission Plan (Mandatory)

Use this section to make removal first-class instead of leaving the design as addition-only.

| Item To Remove / Decommission | Why It Becomes Unnecessary | Replaced By Which Owner / File / Structure | Scope (`In This Change`/`Follow-up`) | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Draft File Responsibility Mapping

Draft the concrete file responsibilities after the spine and subsystem allocations are clear.
Treat this as the first concrete pass, not the final answer.

| Candidate File | Owning Subsystem / Capability Area | Owner / Boundary | Concrete Concern | Why This Is One File | Reuses Shared Structure? |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Reusable Owned Structures Check (If Needed)

| Repeated Structure / Logic | Candidate Shared File | Owning Subsystem | Why Shared | Must Not Become |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Final File Responsibility Mapping

Re-tighten file responsibilities after extracting reusable owned structures and before final folder/path placement.

| File | Owning Subsystem / Capability Area | Owner / Boundary | Concrete Concern | Why This Is One File | Reuses Shared Structure? |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Derived Implementation Mapping (Secondary)

This section exists to map the spine-and-ownership design into concrete implementation locations.
It must not replace the spine-first explanation above.
Use judgment: the goal is readable ownership and structural depth, not a rigid one-folder-per-spine-step rule.

| Target File | Change Type | Mapped Spine ID | Owner / Support Branch | Responsibility | Key APIs / Interfaces | Notes |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## File Placement And Ownership Check (Mandatory)

| File | Current Path | Target Path | Owning Concern / Platform | Path Matches Concern? (`Yes`/`No`) | Flat-Or-Over-Split Risk (`Low`/`Medium`/`High`) | Action (`Keep`/`Move`/`Split`/`Promote Shared`) | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

Rules:
- Use a flatter layout when it is genuinely clearer for the scope, but justify it.
- Do not split folders, optional module groupings, and files so aggressively that the structure becomes artificial and ownerless.
- Do not keep a flat mixed folder when it hides real ownership or structural depth.

## Concrete Examples / Shape Guidance (Mandatory When Needed)

Use this section when a short example would make the design materially easier to understand.

| Topic | Good Example | Bad / Avoided Shape | Why The Example Matters |
| --- | --- | --- | --- |
|  |  |  |  |

## Backward-Compatibility Rejection Log (Mandatory)

| Candidate Compatibility Mechanism | Why It Was Considered | Rejection Decision (`Rejected`/`N/A`) | Replacement Clean-Cut Design |
| --- | --- | --- | --- |
|  |  |  |  |

Hard block:
- Any design that depends on backward-compatibility wrappers, dual-path behavior, or retained legacy flow for in-scope replaced behavior fails review.

## Derived Interface Boundary Mapping

| Owning File | Mapped Spine ID | Owner / Support Branch | Subject Owned | Concern / Responsibility | Interfaces / APIs / Methods | Accepted Identity Shape(s) | Inputs/Outputs | Dependencies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

Rule:
- Do not use one generic interface/API/query/command/service method when the subject or identity shape differs. Split boundaries by subject or require an explicit compound identity shape.

## Scope-Appropriate Separation Of Concerns Check

- UI/frontend scope: responsibility is clear at view/component/store boundaries.
- Non-UI scope: responsibility is clear at file and service boundaries, with subsystem grouping still readable.
- Integration/infrastructure scope: each adapter or integration-focused file/group owns one integration concern with clear contracts.
- Ownership note: separation of concerns should follow ownership and support structure, not precede them.
- File-placement note: folder/path should make the owning concern obvious; platform-specific files should not live in unrelated or ambiguous locations.
- Layout note: a compact structure is acceptable when it stays clearer, but over-flat or over-split layouts should be corrected.

## Interface Boundary Check (Mandatory)

| Interface / API / Query / Command / Method | Subject Owned | Responsibility Is Singular? (`Yes`/`No`) | Identity Shape Is Explicit? (`Yes`/`No`) | Ambiguous-ID Or Generic-Selector Risk (`Low`/`Medium`/`High`) | Corrective Action |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Rule:
- If one interface accepts a generic ID or selector and must guess what kind of subject that input represents, or exposes a generic mixed-subject list surface, the design is not clean enough yet.

## Naming Decisions (Natural And Implementation-Friendly)

| Item Type (`File`/`Module`/`API`) | Current Name | Proposed Name | Reason | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Naming Drift Check (Mandatory)

| Item | Current Responsibility | Does Name Still Match? (`Yes`/`No`) | Corrective Action (`Rename`/`Split`/`Move`/`N/A`) | Mapped Change ID |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Existing-Structure Bias Check (Mandatory)

| Candidate Area | Current-File-Layout Bias Risk | Architecture-First Alternative | Decision | Why |
| --- | --- | --- | --- | --- |
|  | Low/Medium/High |  | Keep/Change |  |

Rule:
- Do not keep a misplaced file in place merely because many callers already import it from there; that is structure bias, not design quality.

## Anti-Hack Check (Mandatory)

| Candidate Change | Shortcut/Hack Risk | Proper Structural Fix | Decision | Notes |
| --- | --- | --- | --- | --- |
|  | Low/Medium/High |  |  |  |

Rule:
- A functionally working local fix is still invalid here if it degrades the data-flow spine, ownership boundaries, or support structure.

## Dependency Flow And Cross-Reference Risk

| Dependency Boundary | Upstream Dependencies | Downstream Dependents | Cross-Reference Risk | Mitigation / Boundary Strategy |
| --- | --- | --- | --- | --- |
|  |  |  | Low/Medium/High |  |

## Decommission / Cleanup Plan

| Item To Remove/Rename | Cleanup Actions | Legacy Removal Notes | Verification |
| --- | --- | --- | --- |
|  |  |  |  |

## Data Models (If Needed)

## Error Handling And Edge Cases

## Use-Case Coverage Matrix (Design Gate)

| use_case_id | Requirement | Use Case | Primary Path Covered (`Yes`/`No`) | Fallback Path Covered (`Yes`/`No`/`N/A`) | Error Path Covered (`Yes`/`No`/`N/A`) | Runtime Call Stack Section |
| --- | --- | --- | --- | --- | --- | --- |
| UC-001 | R-001 |  |  |  |  |  |

## Migration / Rollout (If Needed)

## Change Traceability To Implementation

| Change ID | Implementation Task(s) | Verification (Unit/Integration/API/E2E) | Status |
| --- | --- | --- | --- |
| C-001 |  |  | Planned |

## Design Feedback Loop Notes (From Review/Implementation)

| Date | Trigger (Review/File/Test/Blocker) | Classification (`Local Fix`/`Design Impact`/`Requirement Gap`/`Unclear`) | Design Smell | Requirements Updated? | Design Update Applied | Status |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Yes/No |  |  |

## Open Questions
