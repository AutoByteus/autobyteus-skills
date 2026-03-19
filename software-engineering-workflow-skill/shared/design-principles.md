# Design Principles

Use these principles for Stage 3 design work and Stage 5 future-state review.
They are the shared design language for this workflow.

## Terminology

- `Subsystem` / `capability area`: a larger functional area that owns a broader category of work and may contain multiple files plus optional module groupings.
- `Module`: an optional intermediate grouping inside a subsystem when the codebase benefits from it. Do not use `module` as a synonym for one file or as the default ownership term.
- `File`: one concrete source file and the primary unit where one concrete concern should land.
- `Folder` / `directory`: a physical grouping used to organize files and any optional module groupings.

## Core Principles

### 1. Data-Flow Spine Clarity

- Identify the primary end-to-end spine for each in-scope use case.
- Enumerate all relevant spines explicitly, not only the biggest one:
  - primary end-to-end spines,
  - return/event spines,
  - bounded local spines inside one owner when a loop, worker cycle, state machine, or dispatcher materially affects the design.
- For each spine, state its start, end, owner, and why it exists.
- Keep only true main-line nodes on each spine.
- If the main line or bounded local spines are hard to draw, the design is probably fragmented.

### 2. Ownership Clarity

- Each main-line node must own something concrete:
  - state
  - lifecycle
  - invariants
  - sequencing
  - contracts
  - transformations
- Ownership is the concrete form of separation of concerns.
- Main domain subject nodes on the spine should stay coherent; do not force one node to absorb every nearby responsibility just because it is on the main line.
- When additional responsibilities are needed to make one node work, split them into clear supporting concerns around that owner instead of creating hidden mixed-concern blobs.
- If a concern has no clear owner, the boundary is wrong.

### 3. Support Structure Around The Spine

- Supporting branches should serve a clear owner on the spine.
- Keep support branches off the main line unless they truly own core sequencing.
- Support branches may resolve, persist, adapt, map, publish, observe, or translate, but they should not compete with the spine.
- Before creating a new support branch, check whether an existing capability area or subsystem already fits that responsibility and should be reused or extended.

## Derived Checks

- Separation of concerns is still mandatory, and it should get stronger as the spine and ownership model become clearer. It is derived from the spine, main subject nodes, and ownership boundaries rather than treated as the starting point.
- No backward compatibility or legacy retention is a hard modernization rule for in-scope behavior. Design the clean-cut target directly and make removal of obsolete paths explicit.
- Dependency direction follows ownership; name allowed directions and forbidden shortcuts explicitly.
- Draft file responsibilities first. Then extract reusable owned structures where repetition appears, re-tighten the file responsibilities, and only after that finalize folder/path mapping.
- File placement must follow ownership; move or split files when their paths no longer match their real concern. Optional module groupings may be used inside a subsystem only when they improve readability.
- Subsystem, folder, and file mapping should be spine-led and ownership-led, but not mechanical. Optional module groupings are secondary structure only when they help the reader.
- Distinct structural depths often deserve distinct folders, but do not force artificial over-splitting. If a flatter layout is clearer, justify it explicitly.
- Interfaces, APIs, queries, commands, and reused service methods must also follow ownership and separation of concerns: one boundary, one subject, one responsibility, explicit identity shape.
- The design document should read spine-first, not file-first. Files, folders, and any optional module groupings are a derived implementation mapping, not the primary structure of the architecture story.
- Use concrete examples when they materially improve clarity. Do not leave a non-obvious design entirely abstract when a short example would explain the intended shape faster.
- Layering is optional explanatory output only. Do not use layering as a first principle.

## Required Design Questions

- What are the primary execution/data-flow spines for the in-scope use cases?
- Which bounded local/internal spines exist inside owned nodes, and where do they start and end?
- What are the main domain subject nodes on each spine?
- What does each node own?
- What are the return/event spines, if the change is async or event-driven?
- Which support branches serve which owner on the spine?
- Which support needs should reuse or extend an existing capability area or subsystem instead of creating a new helper?
- Which legacy paths, compatibility wrappers, dual-path branches, obsolete files, or deprecated boundaries are removed in this change?
- Which dependencies are allowed, and which shortcuts are forbidden?
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
- Support services sitting on the main line without owning sequencing
- New helper or service pieces created ad hoc even though an existing subsystem already owns that kind of work
- Compatibility wrappers, dual-path behavior, or legacy fallback branches kept only to preserve old flows
- Generic interface boundaries, list/query surfaces, or service methods that accept one ambiguous ID or selector and then guess what subject it belongs to
- Names that do not describe the actual owner or role
- Misplaced files whose paths hide the real concern
- Folder layouts that are so flat they hide boundaries, or so split that they create artificial structure with no real owner
- Empty indirection layers that only pass through work
