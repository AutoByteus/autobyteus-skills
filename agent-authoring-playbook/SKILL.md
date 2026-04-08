---
name: agent-authoring-playbook
description: Use when creating or refactoring individual agents or self-operating agent teams, especially to keep `agent.md` lean, keep `SKILL.md` runtime-focused, avoid duplicated prompt content, and structure team/shared files cleanly.
---

# Agent Authoring Playbook

## Overview

Use this skill when creating or refactoring:

- one individual agent
- one self-operating agent team
- both together as one coordinated design

This skill exists to prevent the exact failure mode where `agent.md` and `SKILL.md` both carry the same runtime instructions and then get concatenated into one bloated system prompt.

## Core Rule

Treat `agent.md` and `SKILL.md` as two different layers:

- `agent.md`: role contract
- `SKILL.md`: runtime playbook

Do not duplicate detailed execution logic across both files.

## Use The Right Track

- For individual-agent design or refactor work, read [references/individual-agent.md](references/individual-agent.md).
- For team design or refactor work, read [references/agent-team.md](references/agent-team.md).
- If the task includes both, read both references and keep the split consistent.

## Shared Authoring Doctrine

- Assume `agent.md` and `SKILL.md` may both land in the runtime prompt together.
- Keep `agent.md` short and role-defining: identity, owned artifacts, handoff edges, and tone.
- Keep `SKILL.md` operational: ordered behavior, required reads, artifact-writing rules, validation gates, classification logic, and detailed routing rules.
- If a rule is needed for execution, it belongs in `SKILL.md`.
- If a sentence only explains who the role is, what it owns, or who it talks to, it belongs in `agent.md`.
- Avoid a central workflow matrix when the team is self-operating and routing is owned by the individual agents.
- Use team-level shared files only for genuinely cross-role doctrine that multiple agents must read.
- If runtime-critical material cannot be relied on outside the skill folder, keep the skill self-contained.

## Required Checks Before Finishing

- Compare each `agent.md` against its `SKILL.md` and remove duplicated runtime instructions.
- Verify each runtime-critical artifact has one authoritative owner.
- Verify handoff targets and classifications are explicit in `SKILL.md`.
- Verify durable artifact rules are consistent across agents.
- Verify team docs do not reintroduce centralized workflow-control prose when the architecture is self-operating.

## Output Expectation

When you finish, the authored result should make these relationships obvious:

- what the role or team is
- what artifact each role produces
- what runtime instructions belong in the skill
- what shared doctrine is truly shared
- where direct agent-to-agent routing lives

