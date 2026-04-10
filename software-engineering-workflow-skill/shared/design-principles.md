# Design Principles

Single canonical design doctrine for Stage 3 design work, Stage 5 future-state review, and Stage 8 code review.
This file is the shared design language for this workflow.
The Stage 8 priority-ordered review scorecard is derived from this language:
data-flow spine inventory and clarity -> ownership and boundary encapsulation -> API shape -> separation of concerns and placement -> shared structures -> naming -> validation -> runtime edge cases -> no backward-compatibility / no legacy retention -> cleanup completeness.
One especially important law in this workflow is the `Authoritative Boundary Rule`: callers above a subject's authoritative boundary must depend on that boundary, not on that boundary and one of its internals at the same time.

## Terminology

- `Subsystem` / `capability area`: a larger functional area that owns a broader category of work and may contain multiple files plus optional module groupings.
- `Module`: an optional intermediate grouping inside a subsystem when the codebase benefits from it. Do not use `module` as a synonym for one file or as the default ownership term.
- `Folder` / `directory`: a physical grouping used to organize files and any optional module groupings.
- `File`: one concrete source file and the primary unit where one concrete concern should land.
- `Primary spine`: the main top-level business-relevant spine for one in-scope use case. There can be multiple primary spines in one design when multiple use cases or major business paths are in scope.
- `Return/Event spine`: a meaningful return path, callback path, or event-propagation path that matters to the behavior. It may move outward, upward, or back across boundaries; direction is not the deciding factor, business relevance is.
- `Bounded local spine`: an internal flow inside one owner, such as an event loop, worker cycle, state machine, queue dispatcher, or callback dispatch path. It is attached to a parent owner and adds local detail; it does not replace the longer primary spine.

## Core Principles

### 1. Data-Flow Spine Inventory And Clarity

- Identify and inventory the relevant data-flow spines for each in-scope use case.
- Enumerate all relevant spines explicitly, not only the biggest one:
  - primary spines
  - secondary spines
  - return/event spines
  - bounded local spines inside one owner when a loop, worker cycle, state machine, or dispatcher materially affects the design
- `Primary` is per use case/path, not globally singular. If two important use cases each have a top-level business path, both can have their own primary spine.
- For each spine, state its start, end, owner, and why it exists.
- Keep only true main-line nodes on each spine.
- `Spine Span Sufficiency Rule` (mandatory): a primary spine must be stretched far enough to expose the real business path, not only the local edited segment.
- The primary spine should usually show:
  - the initiating surface or caller
  - the important orchestration or boundary crossing
  - the authoritative owner boundary
  - any critical downstream mechanism or dependency
  - the meaningful downstream effect, returned result, or emitted consequence
- Practical default: use at least `4-5` meaningful nodes on the primary spine unless the full real path is genuinely smaller.
- A bounded local spine is additive detail. It does not replace the longer primary spine when the longer spine is needed to judge ownership, API shape, or business meaning correctly.
- If the declared spine inventory is incomplete, or if the main line, secondary line, or bounded local spines are hard to draw, the design is probably fragmented.

### 2. Ownership Clarity And Boundary Encapsulation

- Each main-line node must own something concrete:
  - state
  - lifecycle
  - invariants
  - sequencing
  - contracts
  - transformations
- Ownership is the concrete form of separation of concerns.
- Main domain subject nodes on the spine should stay coherent; do not force one node to absorb every nearby responsibility just because it is on the main line.
- When additional responsibilities are needed to make one node work, split them into clear off-spine concerns around that owner instead of creating hidden mixed-concern blobs.
- If a concern has no clear owner, the boundary is wrong.
- `Authoritative Boundary Rule` (mandatory): callers above a subject's authoritative boundary must depend on that boundary, not on that boundary and one of its internals at the same time. This is the `no boundary bypass / no mixed-level dependency` rule.
- This rule is about authority and encapsulation, not about specific labels like `service`, `manager`, `repository`, `controller`, or `facade`.
- When one boundary intentionally encapsulates lower-level concerns, callers above it should depend on the authoritative outer boundary instead of bypassing it and mixing in the internals directly.
- If callers only bypass an internal concern because the outer boundary does not expose enough usable API, strengthen that authoritative boundary or redesign the ownership split explicitly instead of normalizing the bypass.
- API, interface, query, and command shape should be derived from this ownership and boundary model, not designed independently from it.

### 3. Off-Spine Concerns Around The Spine

- Off-spine concerns should serve a clear owner on the spine.
- Keep off-spine concerns off the main line unless they truly own core sequencing.
- Off-spine concerns may resolve, persist, adapt, map, publish, observe, or translate, but they should not compete with the spine.
- Before creating a new off-spine concern, check whether an existing capability area or subsystem already fits that responsibility and should be reused or extended.
- `Spine`, `owner`, and `off-spine concern` are architecture relationship terms, not naming templates.
- Do not name files, folders, services, classes, or types with vague labels like `Support`, `Supporting`, `OffSpine`, `SideConcern`, or `Helper` just because they sit off the main line. Name them by the concrete concern they own.

## Applied Design Workflow

### 1. Model The Path

- Read the current code path before defining the target design.
- Start by writing the spine inventory in a compact table:
  - `spine_id`
  - scope (`Primary End-to-End` / `Return-Event` / `Bounded Local`)
  - start
  - end
  - owner
  - why the spine matters
- Write the primary execution/data-flow spine(s) as short arrow chains when that makes the main path easier to understand quickly.
- Name the main-line nodes with natural domain language.
- Define what each node owns before splitting out off-spine concerns.
- If one spine node starts collecting too many unrelated duties, split off-spine concerns around that owner rather than turning the node into a god-object.
- If one owned node contains an event loop, worker loop, state machine, or dispatch cycle that materially shapes the behavior, describe that bounded local spine separately and connect it back to the parent owner.
- Separation of concerns is still mandatory, and it should get stronger as the spine and ownership model become clearer. It is derived from the spine, main subject nodes, and ownership boundaries rather than treated as the starting point.

### 2. Map Ownership Into Structure

- Draft file responsibilities first. Then extract reusable owned structures where repetition appears, re-tighten the file responsibilities, and only after that finalize folder and path mapping.
- When repeated data structures, types, normalizers, converters, mappers, or schemas appear across several files, extract them into reusable owned files under the correct subsystem instead of duplicating them.
- Reusable owned structures must also be semantically tight: remove redundant attributes, collapse overlapping parallel shapes, and keep each field's meaning singular and explicit.
- Shared cores and specialized variants are valid only when the shared base is truly coherent. Do not create one-for-all base structures with mostly optional fields for unrelated cases; prefer meaningful specialization or composition under a clear subsystem owner.
- Dependency direction follows ownership; name allowed directions and forbidden shortcuts explicitly when design risk exists.
- Specify target subsystems and files explicitly; mention module groupings only when they materially help readability or reflect an established codebase pattern.
- Map subsystems, folders, and files from the spine and ownership model. Use optional module groupings only when they materially improve readability.
- Distinct structural depths often deserve distinct folders, but do not force artificial over-splitting. If a flatter layout is clearer, justify it explicitly.
- If the layout stays flatter, record why that is clearer for this scope. If the layout splits more, make sure each split reflects a real owner or boundary.
- File placement must follow ownership. Move or split files when their paths no longer match their real concern.
- Interfaces, APIs, queries, commands, and reused service methods must also follow ownership and separation of concerns: one boundary, one subject, one responsibility, explicit identity shape.
- The design document should read spine-first, not file-first. Files, folders, and optional module groupings are derived implementation mapping, not the primary structure of the architecture story.

### 3. Record The Change Plan

- Record change inventory explicitly: `Add`, `Modify`, `Rename/Move`, `Remove`.
- Define migration/refactor sequence explicitly when the change is not greenfield.
- Treat removal as first-class architecture work. When clearer ownership, reusable owned structures, or better file responsibilities make redundant pieces unnecessary, name and remove or decommission those pieces explicitly in scope.
- Treat addition and removal symmetrically: when a clearer subsystem owner, reusable owned structure, or file responsibility replaces fragmented or duplicated pieces, record what becomes unnecessary and remove or decommission it in scope.
- No backward compatibility or legacy retention is a hard modernization rule for in-scope behavior. Design the clean-cut target directly and make removal of obsolete paths explicit.
- Prefer clean-cut replacement over compatibility wrappers or dual-path behavior. If old behavior is being replaced, design and record its removal explicitly.
- Add short concrete examples when they materially improve clarity, especially for a non-obvious spine, interface split, folder choice, or bounded local flow. Do not leave a non-obvious design entirely abstract when a short example would explain the intended shape faster.
- Layering is optional explanatory output only. Do not use layering as a first principle. If layering is used as explanation, it must still follow ownership and encapsulation: a higher layer should not skip an owning boundary and directly reach into a deeper layer that the intermediate boundary already owns.

## Structural Triggers

- Repeated coordination trigger:
  - if provider selection, fallback, retry, aggregation, routing, or fan-out logic repeats across callers, give that policy a clear owner
- Responsibility overload trigger:
  - if one file owns multiple unrelated concerns, split it; if a subsystem or optional module grouping becomes a mixed catch-all, reorganize it into clearer owned files and boundaries
- Ambiguous-boundary trigger:
  - if one API, query, command, or service method accepts a generic ID or selector that may refer to different subjects, or returns a generic mixed-subject list, split it into explicit subject-owned boundaries or require an explicit compound identity shape
- Empty indirection trigger:
  - if a proposed layer or module only forwards calls and owns no policy, translation, or boundary concern, remove it
- Authoritative-boundary trigger:
  - if a caller depends on both an outer boundary and one of that boundary's internal managers, repositories, helpers, or lower-level concerns, keep one authoritative entrypoint and remove the bypass
- Shared-folder trigger:
  - put code in a shared or common folder only when it is truly cross-cutting and concern-agnostic
- Shared-structure tightness trigger:
  - if a proposed shared type, schema, or model still contains redundant fields, overlapping representations, or mixed-purpose attributes, tighten the shape before promoting it into a reusable owned file
- Shared-base overreach trigger:
  - if a proposed base or shared type is accumulating optional fields mainly to serve divergent cases, split it into a tighter shared core plus meaningful specialized variants, or use composition instead
- Capability-area reuse trigger:
  - if the spine needs status, events, handlers, persistence, streaming, bootstrap, shutdown, or similar off-spine behavior, first check whether an existing subsystem already owns that work before creating a new local helper
- Legacy-cleanup trigger:
  - if a proposed solution keeps compatibility wrappers, dual-path reads or writes, or fallback branches only to preserve old behavior, redesign it toward a clean-cut replacement and explicit removal plan
- Example-clarity trigger:
  - if a design point would otherwise remain abstract or easy to misread, add a short good-shape example and, when useful, a bad-shape anti-example

## Common Local Mechanisms

Use these only when they solve a local problem inside a clear owner or off-spine concern.

### State Machine

- Best fit: lifecycle-driven behavior inside one owner
- Avoid: spreading one state machine across several owners

### Event Loop / Worker Loop

- Best fit: continuous dispatch or runtime work inside one owner
- Avoid: letting the loop become the architecture instead of the mechanism of one owner

### Factory

- Best fit: controlled construction at a clear boundary
- Avoid: turning it into a hidden service locator

### Registry

- Best fit: indexed lookup or capability registration
- Avoid: hiding orchestration or business decisions inside it

### Adapter

- Best fit: translation between external and internal contracts
- Avoid: embedding core business behavior in boundary translation code

### Strategy

- Best fit: interchangeable behavior variants behind one stable contract
- Avoid: using it when the variants are actually different owners or flows

### Repository

- Best fit: persistence boundary serving a clear owner
- Avoid: putting orchestration or validation rules inside it
- Avoid: callers above the owning service or boundary depending on both that boundary and the repository directly

### Manager

- Best fit: top-level coordination only when authority and lifecycle ownership are explicit
- Avoid: vague coordination blobs with mixed responsibilities
- Avoid: callers above the owning service or boundary depending on both that boundary and the manager directly

## Example Shapes

### Spine Span Sufficiency

- Good shape:
  - `Browser UI -> Session Bootstrap -> Runtime Invocation -> Exposure Composer -> Browser Surface`
- Bad shape:
  - `Exposure Composer -> Browser Surface`

### Authoritative Boundary Pattern

- Good shape:
  - `Caller -> Outer Boundary`
  - `Outer Boundary -> Internal Owned Mechanism`
- Bad shape:
  - `Caller -> Outer Boundary`
  - `Caller -> Internal Owned Mechanism`
  - `Outer Boundary -> Internal Owned Mechanism`
- Rule:
  - if the outer boundary does not expose enough API for the real use case, expand that boundary or redesign the ownership split; do not normalize the bypass

### Common Spine Shapes

- CRUD or request spine:
  - `Frontend -> API -> Service -> Repository -> Database`
- Runtime or worker spine:
  - `API -> Run -> Runtime -> Worker/Event Loop`
- Bounded local loop or state spine:
  - `Queue/Event Source -> Loop/State Machine -> Handler/Transition -> Output/Next Event`
- Rule:
  - a bounded local spine does not replace the primary end-to-end spine; it explains the internal flow of one owned node that is important enough to name explicitly

## Required Design Questions

- What are the relevant primary, secondary, return/event, and bounded local data-flow spines for the in-scope use cases?
- If there are multiple in-scope use cases or major business paths, did the design name multiple primary spines instead of compressing them into one vague chain?
- Is each primary spine stretched far enough to expose the real business path, authoritative owner, and downstream consequence instead of stopping at the local edited segment?
- Which bounded local/internal spines exist inside owned nodes, and where do they start and end?
- What are the main domain subject nodes on each spine?
- What does each node own?
- What are the return/event spines, if the change is async or event-driven?
- Which off-spine concerns serve which owner on the spine?
- Which off-spine needs should reuse or extend an existing capability area or subsystem instead of creating a new helper?
- Which legacy paths, compatibility wrappers, dual-path branches, obsolete files, or deprecated boundaries are removed in this change?
- Which duplicated, fragmented, or now-unnecessary helpers, files, or structures become removable because the new design gives them a clearer owner or replacement?
- Which shared data structures, schemas, DTOs, mappers, or types need tightening so redundant attributes or overlapping representations are removed instead of standardized?
- Which dependencies are allowed, and which shortcuts are forbidden?
- Which boundaries are public entrypoints versus internal owned sub-layers, and which callers are allowed to depend on each?
- Is any caller currently depending on both an outer owner and one of that owner's internals? If so, which boundary should remain authoritative?
- Which subsystems and files should own the target structure, and are any optional module groupings actually needed?
- Does the subsystem, folder, and file layout make ownership and structural depth readable without becoming artificially fragmented?
- Which interface boundaries exist, what subject does each one own, and what identity shape or selector shape does each one accept?
- Which parts of the design need a concrete example to make the intended shape obvious?
- What is the migration path from current state to target state?

## Design Smells

- Many peer coordinators with no obvious main line
- Important spines are left implicit instead of being named
- The named spine stops at the local edited helper path and hides the real initiating surface, authoritative owner boundary, or downstream consequence
- Event loops or state machines materially affect the behavior, but no bounded local spine is described
- Shared helpers that quietly own business behavior
- Shared structures that still carry redundant fields, overlapping representations, or mixed meanings after extraction
- Off-spine concerns sitting on the main line without owning sequencing
- New helper or service pieces created ad hoc even though an existing subsystem already owns that kind of work
- A caller depends on both a public boundary and one of its internal managers, repositories, helpers, or lower-level concerns at the same time
- Compatibility wrappers, dual-path behavior, or legacy fallback branches kept only to preserve old flows
- Generic interface boundaries, list/query surfaces, or service methods that accept one ambiguous ID or selector and then guess what subject it belongs to
- A higher boundary bypasses the intended owner and reaches directly into a deeper layer that should stay encapsulated
- Names that do not describe the actual owner or role
- Misplaced files whose paths hide the real concern
- Folder layouts that are so flat they hide boundaries, or so split that they create artificial structure with no real owner
- Empty indirection layers that only pass through work
