# Requirements Guide

## Purpose

Clarify what behavior the task must deliver and how success will be verified.

## Inputs

- user request
- investigation findings
- existing `requirements.md`, if one exists

## Actions

- State the goal or problem.
- Define in-scope behavior.
- Capture acceptance criteria with measurable expected outcomes.
- Record constraints, assumptions, open questions, and validation expectations.
- Use stable requirement or acceptance-criteria IDs when there are multiple checks.
- Keep requirements concise; do not expand them into design or implementation detail.

## Outputs

- updated `tickets/in-progress/<ticket-name>/requirements.md`

## Exit Condition

Requirements are clear enough when the agent can explain the expected behavior, what is out of scope, and which checks will prove the task is done.

## Next Step

Proceed to `stages/03-design/stage-guide.md`.

## Problem Routing

- If expected behavior is ambiguous, ask the user or return to investigation.
- If later implementation, validation, or review reveals missing behavior, update requirements before continuing downstream.
