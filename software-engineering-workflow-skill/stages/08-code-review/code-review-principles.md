# Code Review Principles

Use these principles for Stage 8 code review.
Code review is an independent engineering gate.
Its primary authority is the shared design principles, common design practices, and the Stage 8 code-review rules themselves.
Earlier design artifacts are context and evidence, not truth sources.
If the review shows that the earlier design basis was weak, incomplete, or wrong, classify that as `Design Impact` instead of lowering the Stage 8 bar.
This is a stricter review, not a weaker one: it must enforce scope-appropriate separation of concerns and file-size discipline while also enforcing spine and ownership clarity.

## Primary Review Questions

- Does the implementation produce a clear, traceable data-flow spine inventory, including any bounded local spines that materially affect behavior?
- Are ownership boundaries still clear in the code?
- Do off-spine concerns still serve clear owners instead of becoming orchestration blobs?
- Did the implementation reuse or extend existing capability areas where appropriate, instead of introducing fresh ad hoc helpers beside the flow?
- Were repeated data structures, types, normalizers, converters, mappers, or schemas extracted into reusable owned files under the correct subsystem instead of being copied across several files?
- Does the changed scope avoid unjustified duplicated code, repeated structures, or repeated policy logic that should now live in one reusable owned file or one clear owner?
- Are shared data structures still tight after the change, with no kitchen-sink base type, no mostly-optional one-for-all model, and meaningful specialization/composition where cases genuinely diverge?
- Is separation of concerns still scope-appropriate, with each file owning a coherent responsibility and each optional module grouping, if used, grouping a coherent set of files instead of mixed unrelated work?
- Do dependencies follow ownership, with no forbidden shortcuts or unjustified cycles?
- Do file paths still match ownership, and do any optional module groupings still reflect the right capability grouping?
- Is the resulting subsystem, folder, and file layout readable for the scope, without becoming too flat or too artificially fragmented?
- Do interfaces, APIs, queries, commands, and reused service methods still have one clear subject, one responsibility, and explicit identity shape?
- Do file names, folder names, optional module names, API names, type/schema names, function/method names, parameter names, and local variable names still match their real responsibility and behavior after the change?
- Do names stay concrete and unsurprising, without misleading abbreviations, vague placeholders, or names that hide side effects or ownership?
- Do changed source files still respect the file-size hard limit and diff-size gate without hiding design drift?
- Are the file-size hard limit and diff-size gate being applied only to changed source implementation files, while test files remain under qualitative review instead of the source-file hard limit?
- Did any manager, registry, adapter, helper, or shared utility absorb business logic it should not own?
- Is validation evidence sufficient for the changed behavior?
- Were obsolete or compatibility-only paths removed when they were in scope?
- Were dead code, obsolete files, unused helpers/tests/flags/adapters, and dormant replaced paths removed when they were in scope?
- Does the implementation avoid compatibility wrappers, dual-path behavior, and legacy old-behavior retention as a hard rule rather than a tradeoff?

## Review Smells

- Main flow is hard to trace or only seems acceptable if you rely on stale design assumptions
- Ownership moved into helpers, utils, mappers, or registries
- Support branches now contain sequencing that belongs to a spine owner
- A new helper/service was added even though an existing subsystem already owned that category of responsibility
- Repeated structures were copied across several files instead of being extracted into a reusable owned file
- A shared/base type was widened into a one-for-all structure with mostly-optional fields instead of using a tighter shared core plus meaningful specialization
- The same logic or policy was copied into multiple changed files instead of being owned once in the right place
- One file or optional module grouping now mixes unrelated concerns or responsibilities that should be split
- A file is in the wrong folder for its real concern
- The layout is technically valid per-file but now feels too flat or too over-split for the real ownership structure
- An interface/API/query/command/service method accepts an ambiguous ID or selector and has to guess what subject or owner that input refers to
- A file, optional module grouping, or API name no longer matches the responsibility it actually owns
- Function, type, parameter, or local variable names are vague, misleading, over-abbreviated, or hide important side effects or ownership
- A changed source file crossed the hard size limit or diff-size gate in a way that signals structural drift
- A working patch introduces empty indirection or patch-on-patch complexity
- Duplicated code remains in changed scope even though one reusable owned file or one clear owner would remove it cleanly
- Dead code, obsolete files, unused helpers/tests/flags/adapters, or dormant replaced paths remain in changed scope after the change
- Compatibility wrappers, dual-path behavior, or preserved legacy fallback branches remain in place for replaced behavior
- Validation is too weak to prove the changed flow
- Legacy fallback or compatibility logic remains without strong reason

## Classification Guidance

### Local Fix

- The issue is bounded and can be fixed without changing shared design reasoning, intended behavior, or workflow artifacts.
- Ownership boundaries remain intact.
- No design or requirement artifact updates are needed.
- Any duplication problem is small, local, and removable without upstream redesign.

### Validation Gap

- The main issue is insufficient validation coverage or evidence.
- The code may be acceptable, but Stage 7 proof is not strong enough yet.
- Reopen Stage 7 before accepting Stage 8.

### Design Impact

- Independent review shows an architectural or structural problem in the current code, even if earlier design artifacts missed it.
- The implementation drifted from a healthy spine inventory, ownership model, off-spine concern structure, or readable placement shape under the shared principles.
- The earlier design basis itself may be weak, incomplete, or wrong and must be corrected before implementation can be accepted.
- The implementation introduces naming drift, misleading local identifiers, or a layout shape that is too flat or too fragmented for a healthy design.
- Duplicated code, repeated structures, or repeated policy logic remain in changed scope in a way that shows ownership or decomposition is still wrong.
- A shared/base structure became a kitchen-sink model, which shows the decomposition or ownership model is still wrong.
- Dead code, obsolete files, unused helpers/tests/flags/adapters, or dormant replaced paths remain in scope after the change.
- A changed file crossed the size/shape threshold in a way that shows decomposition or ownership boundaries are no longer healthy.
- A working fix would degrade the design if left as-is.
- Compatibility wrappers, dual-path behavior, or legacy old-behavior retention remain in scope after the change.

### Requirement Gap

- The review exposes missing or ambiguous intended behavior.

### Unclear

- Root cause is cross-cutting or confidence is too low to classify cleanly.
