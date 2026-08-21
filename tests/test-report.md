
# VehicleGuard V1 Test Report

## Execution Summary

| Field | Result |
|---|---|
| Execution date | 2026-08-21 |
| Environment | Windows, pytest platform `win32` |
| Python version | 3.14.2 |
| pytest version | 9.1.1 |
| Command used | `python -m pytest` |
| Total tests | 95 |
| Passed | 95 |
| Failed | 0 |
| Blocked | 0 |
| Skipped | 0 |
| Overall result | PASS |

The result above is based on the actual pytest execution completed on 2026-08-21.

## Requirement and Test Coverage Summary

The automated test suite executed tests corresponding to the planned VehicleGuard V1 test case categories:

| Category | Planned test cases covered | Status |
|---|---|---|
| Input | TC-INP-001 through TC-INP-002 | PASS |
| Validation | TC-VAL-001 through TC-VAL-006 | PASS |
| Monitoring | TC-MON-001 through TC-MON-002 | PASS |
| Diagnostics | TC-DIAG-001 through TC-DIAG-004 | PASS |
| Severity | TC-SEV-001 through TC-SEV-005 | PASS |
| Warnings | TC-WRN-001 through TC-WRN-003 | PASS |
| Events | TC-EVT-001 through TC-EVT-002 | PASS |
| Configuration | TC-CFG-001 through TC-CFG-003 | PASS |
| System | TC-SYS-001 through TC-SYS-004 | PASS |
| Simulator scenarios | SIM-SCN-001 | PASS |

The executable tests include the documented diagnostic boundary values and supported input range boundaries. Verification evidence is recorded in:

```text
tests/results/verification-results.json
tests/results/verification-matrix-update.csv
```

## Failed Test Details

No failed tests were reported by the final pytest execution.
