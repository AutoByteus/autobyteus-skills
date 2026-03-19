# Common Design Practices

These are helper practices and local mechanisms.
They are not first principles.
Always start with the shared design principles first.

## Practical Design Practices

- Read the current code path before defining the target design.
- Write the primary execution/data-flow spine(s) as short arrow chains.
- Create a small spine inventory:
  - `spine_id`,
  - scope (`Primary End-to-End` / `Return-Event` / `Bounded Local`),
  - start,
  - end,
  - owner,
  - why this spine matters.
- Name the main-line nodes with natural domain language.
- Define what each node owns before splitting supporting concerns.
- If one spine node starts collecting too many unrelated duties, split supporting concerns around that owner rather than turning the node into a god-object.
- Keep support branches attached to a clear owner on the spine.
- Before creating a new support helper, check whether an existing capability area or subsystem already owns that category of work and should be reused or extended.
- When repeated data structures, types, normalizers, converters, mappers, or schemas appear across several files, extract them into reusable owned files under the correct subsystem instead of duplicating them.
- Draft file responsibilities first. Then extract reusable owned structures where repetition appears, re-tighten the file responsibilities, and only after that finalize folder/path mapping.
- If one owned node contains an event loop, worker loop, state machine, or dispatch cycle that materially shapes the behavior, describe that bounded local spine separately and connect it back to the parent owner.
- Split APIs/queries/commands/service methods by subject when identity meaning differs; prefer explicit `getAgent...` / `getTeam...` style boundaries over one generic method that guesses what an ID or selector means.
- Specify target subsystems and files explicitly; mention module groupings only when they materially help readability or reflect an established codebase pattern.
- Map subsystems, folders, and files from the spine and ownership model, and add module groupings only when they help readability rather than as a rigid one-folder-per-step rule.
- If the layout stays flatter, record why that is clearer for this scope. If the layout splits more, make sure each split reflects a real owner or boundary.
- Record change inventory explicitly: `Add`, `Modify`, `Rename/Move`, `Remove`.
- Define migration/refactor sequence when the change is not greenfield.
- Remove obsolete code and compatibility shims in the same design when they are in scope.
- Prefer clean-cut replacement over compatibility wrappers or dual-path behavior. If old behavior is being replaced, design and record its removal explicitly.
- Add short concrete examples when they clarify a non-obvious spine, interface split, folder choice, or bounded local flow.

## Common Spine Shapes

- CRUD/request spine:
  - Example: `Frontend -> API -> Service -> Repository -> Database`
- Runtime/worker spine:
  - Example: `API -> Run -> Runtime -> Worker/Event Loop`
- Bounded local loop/state spine:
  - Example: `Queue/Event Source -> Loop/State Machine -> Handler/Transition -> Output/Next Event`
- Rule:
  - A bounded local spine does not replace the primary end-to-end spine. It explains the internal flow of one owned node that is important enough to name explicitly.

## Structural Triggers

- Repeated coordination trigger:
  - If provider selection, fallback, retry, aggregation, routing, or fan-out logic repeats across callers, give that policy a clear owner.
- Responsibility overload trigger:
- If one file owns multiple unrelated concerns, split it. If a subsystem or optional module grouping becomes a mixed catch-all, reorganize it into clearer owned files and boundaries.
- Ambiguous-boundary trigger:
  - If one API/query/command/service method accepts a generic ID or selector that may refer to different subjects, or returns a generic mixed-subject list, split it into explicit subject-owned boundaries or require an explicit compound identity shape.
- Empty indirection trigger:
  - If a proposed layer/module only forwards calls and owns no policy, translation, or boundary concern, remove it.
- Shared-folder trigger:
  - Put code in a shared/common folder only when it is truly cross-cutting and concern-agnostic.
- Capability-area reuse trigger:
  - If the spine needs status, events, handlers, persistence, streaming, bootstrap, shutdown, or similar support behavior, first check whether an existing subsystem already owns that work before creating a new local helper.
- Legacy-cleanup trigger:
  - If a proposed solution keeps compatibility wrappers, dual-path reads/writes, or fallback branches only to preserve old behavior, redesign it toward a clean-cut replacement and explicit removal plan.
- Example-clarity trigger:
  - If a design point would otherwise remain abstract or easy to misread, add a short good-shape example and, when useful, a bad-shape anti-example.

## Common Local Patterns

Use these only when they solve a local problem inside a clear owner or support branch.

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

### Manager

- Best fit: top-level coordination only when authority and lifecycle ownership are explicit
- Avoid: vague coordination blobs with mixed responsibilities
