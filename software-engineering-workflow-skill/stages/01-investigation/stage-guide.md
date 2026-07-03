# Investigation Guide

## Purpose

Build accurate understanding before requirements, design, and implementation. Investigation is not read-only; use whatever bounded evidence-gathering work the problem requires.

## Inputs

- user request
- initial requirement artifact, if one exists
- repository code, docs, configs, tests, logs, and relevant external references

## Actions

- Read relevant code, tests, docs, configs, schemas, logs, and data.
- Run focused commands, reproductions, probes, or traces when needed.
- Write small diagnostic scripts, focused tests, or temporary instrumentation when they expose current behavior.
- Set up minimal local, containerized, emulated, mocked, or fixture-backed environments when needed.
- Check public docs, specs, issue trackers, SDK docs, upstream code, or sample repositories when local code is not enough.
- Identify entrypoints, execution boundaries, owners, likely touched files, constraints, and unknowns.

## Outputs

- `tickets/in-progress/<ticket-name>/investigation-notes.md`

Include:

- investigation goals, questions, or hypotheses
- task goal and investigation boundary
- exact sources consulted: files, URLs, commands, setup, search queries when material
- current entrypoints, execution boundaries, owners, modules, folders, and likely file-placement concerns
- runtime/probe findings when used
- constraints, unknowns, and design implications

## Exit Condition

Investigation is complete when the intended change, current behavior, likely affected area, major constraints, and likely validation method are clear enough to clarify requirements.

## Next Step

Proceed to `stages/02-requirements/stage-guide.md`.

## Problem Routing

- If root cause or behavior is still unclear, continue investigation.
- If a durable validation asset or production change is needed, defer it to implementation or executable validation.
- If later work exposes unclear or cross-cutting issues, return here and append new evidence instead of replacing earlier findings silently.
