# Investigation Notes

## Goal and boundary

Create one repository skill, `skill-optimizer`, that improves existing skills while preserving their intended behavior. The skill should focus on instruction quality and skill topology, not on rewriting a skill merely to make it shorter.

## Sources consulted

- `/Users/normy/.codex/skills/.system/skill-creator/SKILL.md`
- `/Users/normy/.codex/skills/.system/skill-creator/references/openai_yaml.md`
- `software-engineering-workflow-skill/SKILL.md`
- `software-engineering-workflow-skill/shared/design-principles.md`
- `software-engineering-workflow-skill/stages/06-code-review/code-review-principles.md`
- `bilingual-author-style-writer/SKILL.md`
- `deep-research-article/SKILL.md`
- `product-ui-prototyping/SKILL.md`
- `ux-journey-definition/SKILL.md`
- `README.md`
- `agents/openai.yaml` files across existing skills

Commands used:

- `rg --files` to map skill topology
- `wc -l` to compare guide sizes
- `rg -n` to locate flow, redundancy, artifact, transition, and guardrail language
- `git worktree list`, `git remote -v`, and `git log` to establish repository state

## Current findings

1. `SKILL.md` is the trigger and routing surface. Detailed rules belong in directly linked references, and the skill creator explicitly discourages README, quick-reference, changelog, and other auxiliary files.
2. Existing skills often mix the main workflow, quality gates, artifact topology, and specialized rules. The optimization skill must review those relationships rather than optimize isolated sentences only.
3. The software-engineering design principles transfer well to skills:
   - identify the primary instruction flow before editing local wording;
   - assign each rule to one authoritative owner/file;
   - keep supporting concerns attached to the rule or workflow step they serve;
   - remove empty indirection and duplicated parallel sources;
   - treat obsolete content removal as explicit work.
4. The main failure mode described by the user is low-value defensive wording: a positive instruction is followed by prohibitions against implausible alternatives. The skill needs a test for whether a negative instruction closes a realistic, costly, or safety-relevant branch before removing it.
5. The other important failure modes are unsupported claims, abrupt transitions, duplicated rules, contradictory file conventions, stale references, and behavior changes hidden inside a prose cleanup.
6. This repository's metadata convention is a minimal `agents/openai.yaml` with `display_name`, `short_description`, and `default_prompt`. No README is required for the new skill.
7. A factually correct host-context label can still be a quality defect. For example, `Codex skills` narrows a general skill concept even when the optimizer itself runs inside Codex. This requires an explicit scope-and-audience-fit check, not only factual grounding.
8. Redundancy often originates in structure: duplicated rules across files or repeated sections may indicate missing ownership, competing sources of truth, or a poor content boundary. The optimizer therefore needs a macro-first gate before local wording cleanup.
9. The optimizer's in-place output default could bypass repository-specific worktree, ticket-artifact, or finalization conventions. It needs an explicit repository-boundary rule and an external-side-effect hold.

## Design implications

- Preserve a target skill's explicit behavioral invariants first: artifacts, worktrees, stage transitions, safety boundaries, required validation, and user-requested outputs.
- Separate diagnosis from editing so the agent does not delete a rule before understanding its purpose.
- Require two review passes: a behavior/structure pass and a concision/flow pass.
- Keep the new skill's `SKILL.md` as a compact workflow and put the detailed rubric in one reference file.
- Use concrete evidence from the target skill and its referenced files; label inferences and ask when an assumption would change behavior.
- Give each major rubric criterion a compact positive and negative example so the optimizer can apply the principle rather than merely repeat its name.
- Make the review order explicit: package topology and ownership -> content architecture and logical flow -> factual and behavioral grounding -> clarity and precision -> redundancy and economy. Check cross-file consistency throughout.
