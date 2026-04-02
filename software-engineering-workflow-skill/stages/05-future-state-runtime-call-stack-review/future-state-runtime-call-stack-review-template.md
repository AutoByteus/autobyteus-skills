# Future-State Runtime Call Stack Review

Use this document as the pre-implementation gate for future-state runtime-call-stack quality and use-case completeness.
This review validates alignment with target (`to-be`) design behavior, not parity with current (`as-is`) code.
Keep one canonical `future-state-runtime-call-stack-review.md` path for the ticket. Record later rounds in the same file, and treat the latest round as authoritative while preserving earlier rounds as history.

## Review Meta

- Scope Classification: `Small` / `Medium` / `Large`
- Current Round: `1` / `2` / `3` / ...
- Current Review Type: `Deep Review`
- Clean-Review Streak Before This Round: `0` / `1` / `2` / ...
- Clean-Review Streak After This Round: `0` / `1` / `2` / ...
- Round State: `Reset` / `Candidate Go` / `Go Confirmed`
- Missing-Use-Case Discovery Sweep Completed This Round: `Yes` / `No`
- New Use Cases Discovered This Round: `Yes` / `No`
- This Round Classification (`Design Impact`/`Requirement Gap`/`Unclear`/`N/A`):
- Required Re-Entry Path Before Next Round:

## Review Basis

- Requirements: `tickets/in-progress/<ticket-name>/requirements.md` (status `Design-ready`/`Refined`)
- Runtime Call Stack Document: `tickets/in-progress/<ticket-name>/future-state-runtime-call-stack.md`
- Source Design Basis:
  - `Small`: `tickets/in-progress/<ticket-name>/implementation.md` (solution sketch)
  - `Medium/Large`: `tickets/in-progress/<ticket-name>/proposed-design.md`
- Shared Design Principles: `shared/design-principles.md`
- Common Design Practices: `shared/common-design-practices.md`
- Artifact Versions In This Round:
  - Requirements Status:
  - Design Version:
  - Call Stack Version:
- Required Persisted Artifact Updates Completed For This Round: `Yes` / `No` / `N/A`

## Review Intent (Mandatory)

- Primary check: Is the future-state runtime call stack a coherent and implementable future-state model?
- Not a pass criterion: matching current-code call paths exactly.
- Shared-principles rule: review uses the same design principles as Stage 3 (`data-flow spine clarity`, `ownership clarity`, `off-spine concerns around the spine`, ownership-driven dependency validation, and boundary encapsulation validation).
- Existing-capability rule: review must fail ad hoc off-spine concern growth when an existing subsystem or capability area should have been reused or extended.
- Spine inventory rule: review must verify that all relevant spines are explicitly listed in the design basis, including bounded local spines when a loop, worker cycle, state machine, or dispatcher materially affects behavior.
- Boundary-encapsulation rule: review must fail designs where callers depend on both an authoritative outer boundary and one of that boundary's internal lower-level concerns instead of using one authoritative entrypoint.
- Not a required action: adding/removing layers by default; describe layering only if it actually adds clarity for this scope.
- Example-clarity rule: if the design uses examples because the shape is non-obvious, review whether those examples actually clarify the target shape.
- Repeated-coordination trigger rule: if coordination policy repeats across callers (provider selection/fallback/retry/aggregation/routing/fan-out), review should require a clearer owner.
- Empty-indirection rule: fail a new boundary that is only pass-through and owns no policy, translation, or boundary concern.
- Local-fix-is-not-enough rule: if a fix works functionally but degrades the spine, ownership, or off-spine concerns, mark `Fail` and require architectural artifact updates via classified re-entry.
- Any finding with a required design/call-stack update is blocking.
- No-backward-compat review rule: if future-state behavior keeps compatibility wrappers, dual-path logic, or legacy fallback branches for old flows, mark `Fail`.
- Ownership-dependency review rule: if future-state behavior introduces tight coupling, bidirectional dependency tangles, or unjustified cycles, mark `Fail`.

## Round History

| Round | Requirements Status | Design Version | Call Stack Version | Findings Requiring Persisted Updates | New Use Cases Discovered | Persisted Updates Completed | Classification (`Design Impact`/`Requirement Gap`/`Unclear`/`N/A`) | Required Re-Entry Path | Clean Streak After Round | Round State | Gate (`Go`/`No-Go`) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  |  | Yes/No | Yes/No | Yes/No/N/A |  |  | 0/1/2+ | Reset/Candidate Go/Go Confirmed |  |
| 2 |  |  |  | Yes/No | Yes/No | Yes/No/N/A |  |  | 0/1/2+ | Reset/Candidate Go/Go Confirmed |  |
| 3 |  |  |  | Yes/No | Yes/No | Yes/No/N/A |  |  | 0/1/2+ | Reset/Candidate Go/Go Confirmed |  |
| N |  |  |  | Yes/No | Yes/No | Yes/No/N/A |  |  | 0/1/2+ | Reset/Candidate Go/Go Confirmed |  |

Notes:
- No fixed round count is hard-coded.
- `Candidate Go` means one clean deep-review round with no blockers, no required persisted artifact updates, and no newly discovered use cases.
- `Go Confirmed` means two consecutive clean deep-review rounds.
- Any round with blockers, required persisted artifact updates, or newly discovered use cases must be classified and routed through the required re-entry path before the next review round.

## Round Artifact Update Log (Mandatory)

| Round | Findings Requiring Updates (`Yes`/`No`) | Updated Files | Version Changes | Changed Sections | Resolved Finding IDs |
| --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |
| N |  |  |  |  |  |

Rule:
- A round is incomplete until required file updates are physically written and logged.
- `Required persisted artifact updates` means file updates produced in the classified re-entry stage path, not in-memory edits inside Stage 5.

## Missing-Use-Case Discovery Log (Mandatory Per Round)

| Round | Discovery Lens | New Use Case IDs (`None` if no new case) | Source Type (`Requirement`/`Design-Risk`) | Why Previously Missing | Classification (`Design Impact`/`Requirement Gap`/`Unclear`/`N/A`) | Upstream Update Required |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Requirement coverage / boundary crossing / fallback-error / design-risk |  |  |  |  |  |
| 2 | Requirement coverage / boundary crossing / fallback-error / design-risk |  |  |  |  |  |
| N | Requirement coverage / boundary crossing / fallback-error / design-risk |  |  |  |  |  |

Rule:
- Missing-use-case discovery must run in every round before gate verdict.
- If any new use case is discovered, the round cannot be marked clean.

## Per-Use-Case Review

Mapping note:
- The Stage 8 scorecard category `Data-Flow Spine Inventory and Clarity` is decomposed here into per-use-case flow clarity plus design-basis spine-inventory completeness so the design review can be more explicit before implementation.

| Use Case | Spine ID(s) | Architecture Fit (`Pass`/`Fail`) | Data-Flow Spine Clarity Within Declared Inventory (`Pass`/`Fail`) | Spine Inventory Completeness (`Pass`/`Fail`) | Ownership Clarity (`Pass`/`Fail`) | Support Structure Clarity (`Pass`/`Fail`) | Existing Capability/Subsystem Reuse (`Pass`/`Fail`/`N/A`) | Ownership-Driven Dependency Check (`Pass`/`Fail`) | Boundary Encapsulation Check (`Pass`/`Fail`) | File Placement Alignment (`Pass`/`Fail`) | Flat-Vs-Over-Split Layout Judgment (`Pass`/`Fail`) | Interface/API/Method Boundary Clarity (`Pass`/`Fail`) | Existing-Structure Bias Check (`Pass`/`Fail`) | Anti-Hack Check (`Pass`/`Fail`) | Local-Fix Degradation Check (`Pass`/`Fail`) | Example-Based Clarity (`Pass`/`Fail`/`N/A`) | Terminology & Concept Naturalness (`Pass`/`Fail`) | File And API Naming Clarity (`Pass`/`Fail`) | Name-to-Responsibility Alignment Under Scope Drift (`Pass`/`Fail`) | Future-State Alignment With Design Basis (`Pass`/`Fail`) | Use-Case Coverage Completeness (`Pass`/`Fail`) | Use-Case Source Traceability (`Pass`/`Fail`) | Design-Risk Justification Quality (`Pass`/`Fail`/`N/A`) | Business Flow Completeness (`Pass`/`Fail`) | Scope-Appropriate SoC Check (`Pass`/`Fail`) | Dependency Flow Smells | Redundancy/Duplication Check (`Pass`/`Fail`) | Simplification Opportunity Check (`Pass`/`Fail`) | Remove/Decommission Completeness (`Pass`/`Fail`/`N/A`) | Legacy Retention Removed (`Pass`/`Fail`) | No Compatibility Wrappers/Dual Paths (`Pass`/`Fail`) | Verdict (`Pass`/`Fail`) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UC-001 | DS-001 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Findings

- If no findings, write `None`.
- Otherwise list only actionable findings:
  - `[F-001] Use case: ... | Type: Architecture/Spine/Ownership/SupportStructure/CapabilityReuse/Placement/InterfaceBoundary/Encapsulation/Hack/LocalFixDegradation/Vocabulary/Naming/MissingUseCase/Gap/Structure/Dependency/Redundancy/Simplification/Legacy/BackwardCompat/Decommission | Severity: Blocker/Major/Minor | Confidence: High/Medium/Low | Evidence: ... | Required update: ... | Classification: Design Impact/Requirement Gap/Unclear`

Rule:
- Any finding with a `Required update` is blocking and must be resolved in a later review round before implementation can start.

## Blocking Findings Summary

- Unresolved Blocking Findings: `Yes` / `No`
- Remove/Decommission Checks Complete For Scoped `Remove`/`Rename/Move`: `Yes` / `No` / `N/A`

## Gate Decision

- Implementation can start: `Yes` / `No`
- Clean-review streak at end of this round:
- Gate rule checks (all must be `Yes` for `Implementation can start = Yes`):
  - Architecture fit is `Pass` for all in-scope use cases:
  - Data-flow spine clarity within declared inventory is `Pass` for all in-scope use cases:
  - Spine inventory completeness is `Pass` for the design basis:
  - Combined `Data-Flow Spine Inventory and Clarity` reasoning is clean enough for later Stage 8 review:
  - Ownership clarity is `Pass` for all in-scope use cases:
  - Support structure clarity is `Pass` for all in-scope use cases:
  - Existing capability/subsystem reuse is `Pass` or `N/A` for all in-scope use cases:
  - Ownership-driven dependency check is `Pass` for all in-scope use cases:
  - Boundary encapsulation check is `Pass` for all in-scope use cases:
  - File-placement alignment is `Pass` for all in-scope use cases:
  - Flat-vs-over-split layout judgment is `Pass` for all in-scope use cases:
  - interface/API/method boundary clarity is `Pass` for all in-scope use cases:
  - Existing-structure bias check is `Pass` for all in-scope use cases:
  - Anti-hack check is `Pass` for all in-scope use cases:
  - Local-fix degradation check is `Pass` for all in-scope use cases:
  - Example-based clarity is `Pass` or `N/A` for all in-scope use cases:
  - Terminology and concept vocabulary is natural/intuitive across in-scope use cases:
  - File/API naming clarity is `Pass` across in-scope use cases:
  - Name-to-responsibility alignment under scope drift is `Pass` across in-scope use cases:
  - Future-state alignment with target design basis is `Pass` for all in-scope use cases:
  - Scope-appropriate separation of concerns is `Pass` for all in-scope use cases:
  - Use-case coverage completeness is `Pass` for all in-scope use cases:
  - Use-case source traceability is `Pass` for all in-scope use cases:
  - Requirement coverage closure is `Pass` (all requirements map to at least one use case):
  - Design-risk justification quality is `Pass` for all design-risk use cases:
  - Redundancy/duplication check is `Pass` for all in-scope use cases:
  - Simplification opportunity check is `Pass` for all in-scope use cases:
  - All use-case verdicts are `Pass`:
  - No unresolved blocking findings:
  - Required persisted artifact updates completed for this round:
  - Missing-use-case discovery sweep completed for this round:
  - No newly discovered use cases in this round:
  - Remove/decommission checks complete for scoped `Remove`/`Rename/Move` changes:
  - Legacy retention removed for impacted old-behavior paths:
  - No compatibility wrappers/dual paths retained for old behavior:
  - Two consecutive deep-review rounds have no blockers, no required persisted artifact updates, and no newly discovered use cases:
  - Findings trend quality is acceptable across rounds (issues declined in count/severity or became more localized), or explicit design decomposition update is recorded:
- If `No`, required refinement actions:
  - If classification is `Design Impact` (clear/high-confidence design issue): `Stage 3 -> Stage 4 -> Stage 5`:
  - If classification is `Requirement Gap`: update `requirements.md` first in `Stage 2` (status `Refined`), then `Stage 3 -> Stage 4 -> Stage 5`:
  - If classification is `Unclear` (cross-cutting or low confidence): update `investigation-notes.md` in `Stage 1`, then `Stage 2 -> Stage 3 -> Stage 4 -> Stage 5`:
  - After the re-entry path is recorded in `workflow-state.md`, immediately resume the first returned stage by default, without waiting for another user message. Do not stop after only declaring the path.
  - Regenerate `future-state-runtime-call-stack.md`:
  - Re-run this review from updated files:

## Speak Log (Optional Tracking)

- Stage/gate transition spoken after `workflow-state.md` update: `Yes` / `No`
- Review gate decision spoken after persisted gate evidence: `Yes` / `No`
- Re-entry or lock-state change spoken (if applicable): `Yes` / `No` / `N/A`
- If any required speech was not emitted, fallback text update recorded: `Yes` / `No` / `N/A`
