# Agent Team Track

## Goal

Create or refactor a self-operating agent team without reintroducing a centralized workflow-control document that duplicates what the individual agents already know.

## Team File Responsibilities

### `team.md`

Keep this lightweight.

Recommended contents:

- team identity
- short description of how the team operates
- member roster
- short description of each member

Do not turn `team.md` into a giant workflow manual when the individual agents already own their own routing and runtime behavior.

### `team-config.json`

Use this to define:

- team members
- the starting coordinator or initial entry role
- other team-configuration data required by the framework

### Team `shared/`

Use team-shared files only for doctrine that is truly cross-role.

Good examples:

- design principles used by multiple engineering roles
- common design practices
- one small shared taxonomy used by several roles

Bad examples:

- duplicating one agent's local runtime rules
- putting the whole workflow logic in a team-shared document
- turning shared docs into a second `team.md`

## Self-Operating Team Rule

When agents communicate directly with each other:

- the team doc does not need a workflow matrix
- the team doc does not need stage-control prose
- the team doc does not need a centralized reroute table

Instead:

- each agent decides who to message based on its own artifact and classification rules
- each agent writes its artifact before sending the next handoff
- each agent hands off artifact paths explicitly

## Team And Agent Relationship

The team layer should not repeat detailed agent-local runtime instructions.

Use this split:

- `team.md`: what the team is
- agent `agent.md`: what each role is
- agent `SKILL.md`: how each role executes

## Communication Standard

For self-operating artifact-driven teams, keep these rules consistent:

- write the authoritative artifact before handoff
- place durable artifacts in the assigned task workspace
- use absolute filesystem paths in cross-agent handoffs
- keep classifications and reroute logic in the agent skill, not in the team doc

## Recommended Authoring Order

1. Define or refine the member roster and entry role in `team-config.json`.
2. Reduce `team.md` to team identity and roster-level guidance.
3. Move routing and execution detail into the individual agents.
4. Add team-shared doctrine only when several roles genuinely need the same material.
5. Verify the team can still be understood without a central workflow matrix.

## Final Checklist

- `team.md` is lightweight.
- `team-config.json` carries the membership and start-role facts.
- Agent-local routing is not duplicated in team docs.
- Cross-role doctrine in `shared/` is genuinely shared.
- The authored team matches the actual operating architecture: self-operating agents, not one hidden centralized controller.

