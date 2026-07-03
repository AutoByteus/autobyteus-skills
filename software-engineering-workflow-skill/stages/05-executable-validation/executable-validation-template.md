# Executable Validation

Use this artifact for the executable validation stage.

Write to:
- `tickets/in-progress/<ticket-name>/executable-validation.md`

This artifact records executable evidence for API, browser/UI, desktop UI, CLI, process/lifecycle, integration, or other real system boundaries.

## Validation Meta

- Ticket:
- Validation round:
- Trigger: implementation complete / rerun after fix / validation gap / other
- Latest authoritative round:
- Requirements source:
- Implementation source:
- Design source, if any:

## Scope

- Changed behavior:
- Interface/system boundary in scope: `API` / `Browser UI` / `Desktop UI` / `CLI` / `Worker/Process` / `Lifecycle` / `Integration` / `Other`
- Platform/runtime targets:
- Environment constraints:

## Coverage Rules

- Every critical acceptance criterion should map to at least one executable scenario.
- Use stable scenario IDs with `AV-` prefix.
- Prefer durable repo-resident tests when they will govern future behavior.
- Temporary probes are allowed when durable tests cannot prove the behavior in the current environment.
- Human-assisted checks are acceptable only when automation is not practical; record exact steps, evidence captured, and residual risk.
- Validation is not complete while critical scenarios are `Failed`, `Blocked`, or `Not Run` unless the user explicitly accepts the risk.

## Acceptance Criteria Coverage

| Acceptance Criteria ID | Criterion Summary | Scenario ID(s) | Status (`Not Run`/`Passed`/`Failed`/`Blocked`/`Waived`) | Evidence |
| --- | --- | --- | --- | --- |
| AC-001 |  | AV-001 | Not Run |  |

## Scenario Catalog

| Scenario ID | Source (`Requirement`/`Risk`) | Validation Mode | Expected Outcome | Command/Harness | Durable Asset(s) | Temporary Method | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AV-001 | Requirement | API/E2E/CLI/etc. |  |  |  |  | Not Started |

## Round History

| Round | Trigger | Scenarios Run | New Failures | Result (`Pass`/`Fail`/`Blocked`) | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |

## Failure Log

| Scenario ID | Failure Summary | Classification (`Local Fix`/`Validation Gap`/`Requirement Gap`/`Design Impact`/`Unclear`) | Required Loop | Resolved |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Classification guide:

- `Local Fix`: implementation defect; fix code and rerun relevant validation.
- `Validation Gap`: scenario or evidence is insufficient; strengthen validation.
- `Requirement Gap`: intended behavior is missing or ambiguous; update requirements first.
- `Design Impact`: ownership, API, placement, or structure needs redesign before coding.
- `Unclear`: return to investigation.

## Temporary Validation Cleanup

| Temporary Asset/Method | Keep or Remove | Rationale | Cleanup Status |
| --- | --- | --- | --- |
|  |  |  |  |

## Validation Decision

- Latest authoritative round:
- Result: `Pass` / `Fail` / `Blocked`
- Critical acceptance criteria passed:
- Critical scenarios passed:
- Durable validation assets updated:
- Temporary scaffolding cleaned up or intentionally retained:
- Residual risk:
- Ready for code review:
