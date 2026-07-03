# Code Review

Use this artifact for the code review stage.

Write to:
- `tickets/in-progress/<ticket-name>/code-review.md`

For straightforward changes, an internal diff review plus final-summary notes may be enough.

## Review Meta

- Ticket:
- Review round:
- Trigger: post-validation / rerun after fix / other
- Latest authoritative round:
- Investigation notes reviewed:
- Requirements reviewed:
- Design/implementation notes reviewed:
- Validation evidence reviewed:
- Shared Design Principles: `shared/design-principles.md`
- Code Review Principles: `stages/06-code-review/code-review-principles.md`

## Scope

- Files reviewed:
- Related files checked:
- Why this scope is sufficient:

## Source File Size And Structure Audit

This audit applies to changed source implementation files only. Test files remain in review scope for correctness, maintainability, and evidence quality.

| Source File | Effective Non-Empty Lines | Changed-Line Delta | Size Risk | SoC/File Placement Result | Required Action |
| --- | --- | --- | --- | --- | --- |
|  |  |  | `Pass`/`Risk`/`Fail` |  |  |

Commands:

- effective non-empty line count: `rg -n "\\S" <file-path> | wc -l`
- changed-line delta: `git diff --numstat <base-ref>...HEAD -- <file-path>`

Guidance:

- `>500` effective non-empty lines in a changed source file should normally fail review or trigger a split/refactor plan.
- `>220` changed lines in one source file requires explicit structure review even when total file size is acceptable.

## Review Scorecard

Score only when useful for the change. For risky changes, use the full scorecard. For straightforward changes, a shorter findings-first review is acceptable.

| Priority | Category | Score (`1.0-10.0` or `N/A`) | Rationale | Weakness / Follow-Up |
| --- | --- | --- | --- | --- |
| 1 | Data-flow spine inventory and clarity |  |  |  |
| 2 | Ownership clarity and boundary encapsulation |  |  |  |
| 3 | API/interface/query/command clarity |  |  |  |
| 4 | Separation of concerns and file placement |  |  |  |
| 5 | Shared-structure/data-model tightness |  |  |  |
| 6 | Naming quality and local readability |  |  |  |
| 7 | Validation strength |  |  |  |
| 8 | Runtime correctness and edge cases |  |  |  |
| 9 | No backward compatibility / no legacy retention |  |  |  |
| 10 | Cleanup completeness |  |  |  |

## Mandatory Checks

| Check | Result (`Pass`/`Fail`/`N/A`) | Evidence | Required Action |
| --- | --- | --- | --- |
| Changed behavior is correct under expected and edge cases |  |  |  |
| Validation evidence is sufficient |  |  |  |
| Data-flow and ownership remain clear |  |  |  |
| Authoritative Boundary Rule is preserved |  |  |  |
| Interfaces expose clear subjects and identity shape |  |  |  |
| File placement matches owning concern |  |  |  |
| No unjustified duplication or generic helper drift |  |  |  |
| No compatibility shims, dual-path behavior, or legacy retention in scope |  |  |  |
| Obsolete code and tests in scope are removed |  |  |  |
| Tests are maintainable |  |  |  |

## Findings

- If none, write `None`.
- Otherwise use:
  - `[CR-001] File: ... | Type: Correctness/Validation/Ownership/API/SoC/Placement/Naming/Duplication/Legacy/FileSize/Cleanup | Severity: Blocker/Major/Minor | Evidence: ... | Required update: ...`

## Failure Classification

If review fails, choose the shortest honest loop:

- `Local Fix`: implementation defect; fix and rerun relevant tests/review.
- `Validation Gap`: insufficient evidence; strengthen validation and rerun review.
- `Requirement Gap`: missing or ambiguous intended behavior; update requirements first.
- `Design Impact`: ownership/API/placement/structure problem; update solution sketch or design first.
- `Unclear`: return to investigation.

## Review Decision

- Latest authoritative round:
- Decision: `Pass` / `Fail`
- Blocking findings:
- Required loop if failed:
- Ready for docs sync/handoff:
