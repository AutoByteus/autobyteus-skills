# Investigation Notes

Use one canonical file:
- `tickets/in-progress/<ticket-name>/investigation-notes.md`

Purpose:
- capture durable investigation evidence in enough detail that later stages can reuse the work without repeating the same major searches unless facts have changed
- keep the artifact readable with short synthesis sections, but preserve concrete evidence, source paths, URLs, commands, and observations

## Investigation Status

- Current Status: `Draft` / `In Progress` / `Current`
- Scope Triage: `Small` / `Medium` / `Large`
- Triage Rationale:
- Investigation Goal:
- Primary Questions To Resolve:

## Source Log

| Date | Source Type (`Code`/`Doc`/`Spec`/`Web`/`Repo`/`Issue`/`Command`/`Trace`/`Log`/`Data`/`Setup`/`Other`) | Exact Source / Query / Command | Why Consulted | Relevant Findings | Follow-Up Needed |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | Code | `src/example/file.ts` | Verify current owner and entrypoint | `ExampleController` still owns the request entrypoint | No |
| YYYY-MM-DD | Web | `https://docs.example.com/...` | Confirm API constraint | API requires room IDs to be unique per host | Yes |
| YYYY-MM-DD | Repo | `https://github.com/example-org/example-sdk` @ `v1.4.2` | Check upstream integration behavior | Sample app shows the callback fires only after explicit session join | Yes |
| YYYY-MM-DD | Command | `rg -n "Start Recording All Occupied Rooms" src` | Find all affected call sites | Found two handlers and one stale helper | No |

## Current Behavior / Codebase Findings

### Entrypoints And Boundaries

- Primary entrypoints:
- Execution boundaries:
- Owning subsystems / capability areas:
- Optional modules involved:
- Folder / file placement observations:

### Relevant Files / Symbols

| Path | Symbol / Area | Current Responsibility | Finding / Observation | Ownership / Placement Implication |
| --- | --- | --- | --- | --- |
| `src/example/file.ts` | `ExampleController` | Request entrypoint | Delegates to stale helper before routing to service | Controller remains correct owner; stale helper likely removable |

### Runtime / Probe Findings

| Date | Method (`Repro`/`Trace`/`Probe`/`Script`/`Test`/`Setup`) | Exact Command / Method | Observation | Implication |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD | Trace | `npm test -- example.spec.ts` | Failure only on occupied-room path | Focus on worker-allocation branch |

### External Code / Dependency Findings

- Upstream repo / package / sample examined:
- Version / tag / commit / release:
- Files, endpoints, or examples examined:
- Relevant behavior, contract, or constraint learned:
- Confidence and freshness:

### Reproduction / Environment Setup

- Required services, mocks, or emulators:
- Required config, feature flags, or env vars:
- Required fixtures, seed data, or accounts:
- External repos, samples, or artifacts cloned/downloaded for investigation:
- Setup commands that materially affected the investigation:
- Cleanup notes for temporary investigation-only setup:

## External / Internet Findings

| Source | Fact / Constraint | Why It Matters | Confidence / Freshness |
| --- | --- | --- | --- |
| `https://docs.example.com/...` | API rejects duplicate room assignment in one host session | Requirements and design must enforce uniqueness | High / 2026-03-25 |

## Constraints

- Technical constraints:
- Environment constraints:
- Third-party / API constraints:

## Unknowns / Open Questions

- Unknown:
- Why it matters:
- Planned follow-up:

## Implications

### Requirements Implications

- Requirement implication:

### Design Implications

- Design implication:

### Implementation / Placement Implications

- Implementation implication:

## Re-Entry Additions

Append new dated evidence here when later stages reopen investigation.

### YYYY-MM-DD Re-Entry Update

- Trigger:
- New evidence:
- Updated implications:
