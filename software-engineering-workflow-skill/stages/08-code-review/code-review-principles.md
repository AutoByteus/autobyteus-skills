# Code Review Principles

Use these principles for Stage 8 code review.
Code review should verify that the implementation still reflects the approved design basis and the shared design principles.
This is a stricter review, not a weaker one: it must preserve scope-appropriate separation of concerns and file-size discipline while also enforcing spine and ownership clarity.

## Primary Review Questions

- Does the implementation preserve the approved data-flow spine inventory, including bounded local spines that were part of the design basis?
- Are ownership boundaries still clear in the code?
- Do support branches still serve clear owners instead of becoming orchestration blobs?
- Did the implementation reuse or extend existing capability areas where appropriate, instead of introducing fresh ad hoc helpers beside the flow?
- Is separation of concerns still scope-appropriate, with each file/module owning a coherent responsibility instead of mixed unrelated work?
- Do dependencies follow ownership, with no forbidden shortcuts or unjustified cycles?
- Do file/module paths still match ownership?
- Is the resulting folder/module/file layout still readable for the scope, without becoming too flat or too artificially fragmented?
- Do interfaces, APIs, queries, commands, and reused service methods still have one clear subject, one responsibility, and explicit identity shape?
- Do file/module/API names still match their real responsibility after the change?
- Do changed source files still respect the file-size hard limit and diff-size gate without hiding design drift?
- Did any manager, registry, adapter, helper, or shared utility absorb business logic it should not own?
- Is validation evidence sufficient for the changed behavior?
- Were obsolete or compatibility-only paths removed when they were in scope?
- Does the implementation avoid compatibility wrappers, dual-path behavior, and legacy old-behavior retention as a hard rule rather than a tradeoff?

## Review Smells

- Main flow is harder to trace than in the approved design
- Ownership moved into helpers, utils, mappers, or registries
- Support branches now contain sequencing that belongs to a spine owner
- A new helper/service was added even though an existing subsystem already owned that category of responsibility
- One file or module now mixes unrelated concerns or responsibilities that should be split
- A file is in the wrong folder for its real concern
- The layout is technically valid per-file but now feels too flat or too over-split for the real ownership structure
- An interface/API/query/command/service method accepts an ambiguous ID or selector and has to guess what subject or owner that input refers to
- A file/module/API name no longer matches the responsibility it actually owns
- A changed source file crossed the hard size limit or diff-size gate in a way that signals structural drift
- A working patch introduces empty indirection or patch-on-patch complexity
- Compatibility wrappers, dual-path behavior, or preserved legacy fallback branches remain in place for replaced behavior
- Validation is too weak to prove the changed flow
- Legacy fallback or compatibility logic remains without strong reason

## Classification Guidance

### Local Fix

- The issue is bounded inside the approved design.
- Ownership boundaries remain intact.
- No design or requirement artifact updates are needed.

### Validation Gap

- The main issue is insufficient validation coverage or evidence.
- The code may be acceptable, but Stage 7 proof is not strong enough yet.
- Reopen Stage 7 before accepting Stage 8.

### Design Impact

- The implementation drifted from the approved spine inventory, ownership model, support structure, or file placement.
- The implementation introduces naming drift or a layout shape that is too flat or too fragmented for the approved design.
- A changed file crossed the size/shape threshold in a way that shows decomposition or ownership boundaries are no longer healthy.
- A working fix would degrade the design if left as-is.
- Compatibility wrappers, dual-path behavior, or legacy old-behavior retention remain in scope after the change.

### Requirement Gap

- The review exposes missing or ambiguous intended behavior.

### Unclear

- Root cause is cross-cutting or confidence is too low to classify cleanly.
