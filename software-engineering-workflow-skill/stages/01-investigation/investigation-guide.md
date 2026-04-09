# Stage 1 Investigation Guide

Investigation is any activity needed to build accurate understanding and verify assumptions.

## Investigation Can Include

Treat the following as examples, not a closed list. Choose whatever evidence-gathering work is necessary for the problem at hand.

- reading code, docs, configs, schemas, logs, and data
- reading public API docs, SDK docs, specs, RFCs, release notes, issue trackers, and migration guides
- running commands, reproductions, probes, or traces
- writing small scripts, focused tests, or temporary instrumentation to expose current behavior
- setting up minimal local, containerized, emulated, mocked, or fixture-backed environments needed to reproduce or narrow the issue
- inspecting upstream, vendor, open-source, or partner source code when local code alone is not enough to explain the behavior
- downloading or cloning external repositories, examples, or sample apps when that is the practical way to verify an integration or reproduce a failure
- checking APIs, external references, or internet sources when needed

## Artifact Standard

- Update `tickets/in-progress/<ticket-name>/investigation-notes.md` in place.
- Treat `investigation-notes.md` as a durable investigation dossier, not a brief recap.
- Write enough detail that later stages can reuse the findings directly instead of repeating the same search/research work unless the facts have changed.
- Use short synthesis sections for readability, but keep the concrete evidence paths, URLs, queries, commands, findings, and implications in the artifact.

## Required Contents

- investigation goals, questions, or hypotheses
- scope triage (`Small` / `Medium` / `Large`) with rationale
- exact sources consulted:
  - local file paths
  - URLs / external docs / public APIs / specs / issue trackers
  - upstream, vendor, or sample repositories when used
  - commands run
  - setup steps that materially affected reproduction or isolation
  - search queries used when material
- current entrypoints, execution boundaries, owners, modules, folders, and likely file-placement concerns
- runtime/probe findings when reproductions, traces, scripts, focused tests, or setup work were used
- external dependency, upstream-source, or sample-app findings when they materially shaped the understanding
- constraints, unknowns, and design implications
- enough codebase/runtime/API detail that later stages do not need to rediscover the same facts from scratch

## Minimum Understanding Pass

Before design begins, investigation should identify at least:

- in-scope entrypoints and execution boundaries
- touched files, affected subsystems, and likely owners
- expected canonical file locations or folder owners for touched concerns
- current naming conventions that new design work should respect or deliberately correct
- unknowns that could invalidate design assumptions

## Scope Triage And Workflow Depth

Use practical signals rather than a rigid file-count rule:

- estimated files touched
- new or changed interface boundaries
- schema, persistence, or runtime-flow impact
- cross-boundary or architectural impact

Choose workflow depth explicitly:

- `Small`: refine a lightweight solution sketch in `implementation.md`, then continue through future-state runtime call stacks and review before implementation execution
- `Medium`: create a proposed design, then continue through future-state runtime call stacks, review, and implementation baseline
- `Large`: follow the same full design-first path as `Medium`, with more explicit architecture and decomposition work

Re-evaluate during later stages. If scope expands or structural smells appear, append the updated triage rationale and escalate to the fuller workflow instead of keeping the old classification by inertia.

## Investigation Rules

- Do not keep results only in memory.
- Do not collapse detailed evidence into a thin summary if later stages would need that detail again.
- When internet or external documentation research is used, record the exact source and the specific fact or constraint taken from it.
- When public APIs, upstream code, issue trackers, release notes, or cloned/downloaded example repositories are used, record the exact source, version/tag/commit when available, and the specific fact or behavior learned from them.
- When codebase search is used, record the exact files, symbols, or paths that matter, not only the conclusion.
- When commands, probes, traces, or reproductions are used, record what was run and the result that mattered.
- When minimal environment setup, fixtures, mocks, feature flags, or temporary instrumentation are required to reproduce or isolate the issue, treat that as valid Stage 1 investigation work and record the setup steps that materially affected the result.
- Small diagnostic scripts, focused repro tests, temporary logs, and narrow probes remain Stage 1 investigation work when their purpose is evidence gathering rather than shipping the fix.
- Disposable investigation-only sandboxes, cloned repos, sample apps, throwaway harnesses, and local mirrors are valid Stage 1 tools when they are used to gather evidence rather than to introduce a permanent dependency or ship a fix.
- If a test, harness, or code change is intended to remain as part of the product behavior or durable validation suite, treat that follow-on work in later stages instead of keeping it inside Stage 1.
- If later stages expose unclear or cross-cutting issues, reopen Stage 1 and append new evidence instead of replacing earlier findings silently.
- Investigation should reduce uncertainty enough for `requirements.md` to become `Design-ready`.
