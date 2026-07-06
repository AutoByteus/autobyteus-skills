# Codex Project Guidance

This repository uses project-scoped Codex configuration in:
- `.codex/config.toml`
- `.codex/agents/*.toml`

Custom agent-specific instructions live inside each `.codex/agents/*.toml` file under `developer_instructions`.
Do not create one `AGENTS.md` per custom agent.

These custom agents are primarily for work on `software-engineering-workflow-skill`.
Keep core stage behavior in each custom agent file, and use the workflow skill as reusable stage guidance rather than as the agent's only identity.

Use subagents only when the user explicitly asks for subagents, delegation, or parallel agent work.

Preferred delegation shape for workflow-skill work:
- `investigation_analyst`: Stage 1 investigation and investigation-output drafting
- `architect_designer`: spine-first design exploration
- `architect_reviewer`: design review and challenge
- `documentation_engineer`: Stage 9 docs synchronization and durable-doc promotion
- `api_e2e_validator`: Stage 7 scenario/feasibility/execution/failure validation
- `code_reviewer`: Stage 8 review findings and gate checks
- `deployment_engineer`: Stage 10 handoff summary, verification hold, and finalization work
- `implementation_worker`: bounded implementation work only when ownership is disjoint

Parallel-write caution:
- Prefer bounded delegation and clear ownership.
- Use write-capable implementation workers only for disjoint ownership or separate worktrees.

Parent-agent responsibility:
- The main agent remains responsible for final synthesis, artifact updates, workflow-stage decisions, and final gate decisions.
