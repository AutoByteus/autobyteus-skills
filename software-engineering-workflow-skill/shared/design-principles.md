# Design Principles

Use these principles for Stage 3 design work and Stage 5 future-state review.
They are the shared design language for this workflow.
The Stage 8 priority-ordered review scorecard is derived from this language: data-flow spine inventory and clarity -> ownership and boundary encapsulation -> API shape -> separation of concerns and placement -> shared structures -> naming -> validation -> runtime edge cases -> no backward-compatibility / no legacy retention -> cleanup completeness.

## Terminology

- `Subsystem` / `capability area`: a larger functional area that owns a broader category of work and may contain multiple files plus optional module groupings.
- `Module`: an optional intermediate grouping inside a subsystem when the codebase benefits from it. Do not use `module` as a synonym for one file or as the default ownership term.
- `Folder` / `directory`: a physical grouping used to organize files and any optional module groupings.
- `File`: one concrete source file and the primary unit where one concrete concern should land.

## Core Principles

### 1. Data-Flow Spine Inventory and Clarity

- Identify and inventory the relevant data-flow spines for each in-scope use case.
- Enumerate all relevant spines explicitly, not only the biggest one:
  - primary spines,
  - secondary spines,
  - return/event spines,
  - bounded local spines inside one owner when a loop, worker cycle, state machine, or dispatcher materially affects the design.
- For each spine, state its start, end, owner, and why it exists.
- Keep only true main-line nodes on each spine.
- If the declared spine inventory is incomplete, or if the main line / secondary line / bounded local spines are hard to draw, the design is probably fragmented.

### 2. Ownership Clarity and Boundary Encapsulation

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
- When one boundary intentionally encapsulates lower-level concerns, callers above it should depend on the authoritative outer boundary instead of bypassing it and mixing in the internals directly.
- API/interface/query/command shape should be derived from this ownership and boundary model, not designed independently from it.

### 3. Off-Spine Concerns Around The Spine

- Off-spine concerns should serve a clear owner on the spine.
- Keep off-spine concerns off the main line unless they truly own core sequencing.
- Off-spine concerns may resolve, persist, adapt, map, publish, observe, or translate, but they should not compete with the spine.
- Before creating a new off-spine concern, check whether an existing capability area or subsystem already fits that responsibility and should be reused or extended.
- `Spine`, `owner`, and `off-spine concern` are architecture relationship terms, not naming templates.
- Do not name files, folders, services, classes, or types with vague labels like `Support`, `Supporting`, `OffSpine`, `SideConcern`, or `Helper` just because they sit off the main line. Name them by the concrete concern they own.

## Derived Checks

- Separation of concerns is still mandatory, and it should get stronger as the spine and ownership model become clearer. It is derived from the spine, main subject nodes, and ownership boundaries rather than treated as the starting point.
- No backward compatibility or legacy retention is a hard modernization rule for in-scope behavior. Design the clean-cut target directly and make removal of obsolete paths explicit.
- Removal is first-class architecture work, not optional cleanup. When clearer ownership, reusable owned structures, or better file responsibilities make redundant pieces unnecessary, name and remove/decommission those pieces explicitly in scope.
- Dependency direction follows ownership; name allowed directions and forbidden shortcuts explicitly.
- Boundary encapsulation follows ownership too: when one boundary or owner intentionally encapsulates another concern, callers above it should depend on the outer owner, not on both the outer owner and its internals at the same time.
- This rule is about authority and encapsulation, not about specific labels like `service`, `manager`, `repository`, `controller`, or `facade`.
- If a caller needs both an outer boundary and one of that boundary's internal managers, repositories, helpers, or lower-level concerns, either the boundary is wrong or the caller is bypassing ownership. Resolve that by choosing one authoritative entrypoint, or by redesigning the boundary and responsibilities explicitly.
- If callers only bypass an internal concern because the outer boundary does not expose enough usable API, fix that by strengthening the authoritative boundary or by reshaping ownership explicitly. Do not normalize the bypass as the steady-state design.
- Draft file responsibilities first. Then extract reusable owned structures where repetition appears, re-tighten the file responsibilities, and only after that finalize folder/path mapping.
- Reusable owned structures must also be semantically tight: remove redundant attributes, avoid overlapping parallel representations for the same domain subject, and keep each field's meaning singular and explicit.
- Shared cores and specialized variants are valid only when the shared base is truly coherent. Do not create one-for-all base structures that collect mostly-optional fields for unrelated cases; prefer meaningful specialization or composition under a clear subsystem owner.
- File placement must follow ownership; move or split files when their paths no longer match their real concern. Optional module groupings may be used inside a subsystem only when they improve readability.
- Subsystem, folder, and file mapping should be spine-led and ownership-led, but not mechanical. Optional module groupings are secondary structure only when they help the reader.
- Distinct structural depths often deserve distinct folders, but do not force artificial over-splitting. If a flatter layout is clearer, justify it explicitly.
- Interfaces, APIs, queries, commands, and reused service methods must also follow ownership and separation of concerns: one boundary, one subject, one responsibility, explicit identity shape.
- The design document should read spine-first, not file-first. Files, folders, and any optional module groupings are a derived implementation mapping, not the primary structure of the architecture story.
- Use concrete examples when they materially improve clarity. Do not leave a non-obvious design entirely abstract when a short example would explain the intended shape faster.
- Layering is optional explanatory output only. Do not use layering as a first principle.
- If layering is used as explanation, it must still follow ownership and encapsulation: a higher layer should not skip an owning boundary and directly reach into a deeper layer that the intermediate boundary already owns.

## Required Design Questions

- What are the relevant primary, secondary, return/event, and bounded local data-flow spines for the in-scope use cases?
- Which bounded local/internal spines exist inside owned nodes, and where do they start and end?
- What are the main domain subject nodes on each spine?
- What does each node own?
- What are the return/event spines, if the change is async or event-driven?
- Which off-spine concerns serve which owner on the spine?
- Which off-spine needs should reuse or extend an existing capability area or subsystem instead of creating a new helper?
- Which legacy paths, compatibility wrappers, dual-path branches, obsolete files, or deprecated boundaries are removed in this change?
- Which duplicated, fragmented, or now-unnecessary helpers/files/structures become removable because the new design gives them a clearer owner or replacement?
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
