# VehicleGuard Project Roadmap

## 1. Purpose

This roadmap defines the main development phases of the VehicleGuard project.

Its purpose is to provide a clear path from the initial system concept to a documented and verified engineering prototype.

The roadmap focuses on major engineering activities rather than individual development tasks. Detailed implementation tasks, bug fixes, and minor documentation changes are not tracked here.

The roadmap may be updated as the project develops, but significant changes to the planned scope should be reviewed before they are introduced.

---

## 2. Development Approach

VehicleGuard follows a structured systems engineering approach.

The project starts with defining the problem and system boundaries before moving into detailed requirements and architecture. Prototype implementation begins only after the expected system behaviour has been sufficiently defined.

The general development flow is:

```text
Project Definition
        |
        v
Stakeholder Analysis
        |
        v
System Requirements
        |
        v
System Architecture
        |
        v
System Risk Analysis
        |
        v
Prototype Development
        |
        v
Verification
        |
        v
Controlled System Change
        |
        v
Final Engineering Review
```

The process is not strictly linear. Findings during architecture development, implementation, or verification may require earlier engineering decisions to be reviewed.

Any significant change should remain documented and traceable.

---

## 3. Project Status

The following status values are used throughout the roadmap:

* `Not Started` - Work on the phase has not started.
* `In Progress` - Activities within the phase are currently being performed.
* `Completed` - The planned activities and outputs of the phase have been completed.
* `Under Review` - The main work is complete but requires review before the phase can be considered finished.

### Current Overview

| Phase   | Description                           | Status      |
| ------- | ------------------------------------- | ----------- |
| Phase 1 | Project Definition                    | Completed   |
| Phase 2 | Stakeholder and Requirements Analysis | Completed   |
| Phase 3 | System Architecture                   | Completed   |
| Phase 4 | System Risk Analysis                  | Completed   |
| Phase 5 | Prototype Development                 | Completed   |
| Phase 6 | Verification                          | Completed   |
| Phase 7 | Controlled System Change              | Not Started |
| Phase 8 | Final Engineering Review              | Not Started |

---

# Phase 1 - Project Definition

**Status:** `Completed`

## Objective

Establish a clear foundation for VehicleGuard before detailed system development begins.

This phase defines what problem the system is intended to address, what functionality belongs within the project, and which areas are intentionally excluded.

## Main Activities

* Define the project problem statement.
* Define the purpose of VehicleGuard.
* Define the initial project objectives.
* Establish the V1 project scope.
* Define what is outside the project scope.
* Identify initial assumptions and constraints.
* Define the system boundary.
* Define the intended operational context.
* Establish the initial project risk register.

## Expected Outputs

* `README.md`
* `docs/01-project-overview.md`
* `project-management/risk-register.md`
* Initial system boundary definition
* Initial project assumptions and constraints

## Completion Criteria

Phase 1 can be considered complete when the purpose, scope, system boundary, assumptions, and main project limitations are clearly documented.

---

# Phase 2 - Stakeholder and Requirements Analysis

**Status:** `Completed`

## Objective

Identify the main stakeholders of VehicleGuard and translate their relevant needs into structured and verifiable system requirements.

## Main Activities

* Identify relevant project stakeholders.
* Describe stakeholder roles and expectations.
* Define initial stakeholder needs.
* Create stakeholder requirement identifiers.
* Derive system requirements from stakeholder needs.
* Define expected system behaviour.
* Define requirements for monitored vehicle parameters.
* Define fault detection requirements.
* Define warning and severity classification requirements.
* Define data validation requirements.
* Define initial verification methods.
* Review requirements for clarity and testability.

## Expected Outputs

* `docs/02-stakeholders.md`
* `docs/03-system-requirements.md`
* Requirements register
* Initial requirement identifiers
* Initial stakeholder-to-system requirement traceability

## Completion Criteria

Phase 2 can be considered complete when the main V1 system behaviour is described through requirements that are understandable, traceable, and verifiable.

---

# Phase 3 - System Architecture

**Status:** `Completed`

## Objective

Define how VehicleGuard is structured and how the main parts of the system interact.

The architecture should support the previously defined requirements without introducing unnecessary complexity.

## Main Activities

* Create the system context.
* Define the main system functions.
* Perform functional decomposition.
* Define logical system components.
* Define data flow between components.
* Define system interfaces.
* Define the conceptual vehicle data source.
* Define the relationship between vehicle signals and diagnostic processing.
* Define warning and diagnostic outputs.
* Review architecture against system requirements.

## Expected Outputs

* `docs/04-system-architecture.md`
* `docs/05-interfaces.md`
* `diagrams/system-context.png`
* `diagrams/system-architecture.png`
* `diagrams/functional-decomposition.png`

## Completion Criteria

Phase 3 can be considered complete when the main components, responsibilities, interfaces, and data flows of VehicleGuard are clearly defined and connected to the system requirements.

---

# Phase 4 - System Risk Analysis

**Status:** `Completed`

## Objective

Identify technical failure scenarios and system-level risks associated with the behaviour of VehicleGuard.

This phase is separate from the project risk register. The project risk register tracks risks affecting the development process, while this phase focuses on risks associated with the designed system.

## Main Activities

* Identify important system failure scenarios.
* Analyze possible invalid or missing input data.
* Analyze missed fault detection.
* Analyze false warning generation.
* Analyze incorrect severity classification.
* Analyze communication failure scenarios.
* Identify possible mitigation measures.
* Review whether additional requirements are necessary.
* Consider introducing a simplified FMEA where useful.

## Expected Outputs

* `docs/06-risk-analysis.md`
* Initial system risk analysis
* Updated requirements where risk analysis identifies missing behaviour
* Simplified FMEA if required

## Completion Criteria

Phase 4 can be considered complete when the main system failure scenarios have been identified and appropriate mitigation measures or requirements have been defined.

---

# Phase 5 - Prototype Development

**Status:** `Completed`

## Objective

Develop a lightweight prototype that demonstrates selected VehicleGuard system behaviour and provides a practical environment for requirement verification.

The prototype is not intended to represent production automotive software.

## Main Activities

* Implement the vehicle data simulator.
* Generate normal vehicle operating data.
* Implement controlled fault injection.
* Implement basic input validation.
* Implement diagnostic evaluation logic.
* Implement fault detection.
* Implement severity classification.
* Generate driver warning information.
* Generate diagnostic event information.
* Keep configurable demonstration thresholds separate from core logic where practical.

## Expected Outputs

* `prototype/vehicle_simulator.py`
* `prototype/diagnostics.py`
* Prototype configuration
* Demonstration scenarios

## Completion Criteria

Phase 5 can be considered complete when the prototype can simulate the required V1 vehicle parameters and demonstrate the system behaviour necessary for planned verification activities.

---

# Phase 6 - Verification

**Status:** `Completed`

## Objective

Verify that the implemented prototype behaves according to the defined VehicleGuard system requirements.

## Main Activities

* Define the verification strategy.
* Create requirement-based test cases.
* Create normal operation tests.
* Create warning condition tests.
* Create critical condition tests.
* Perform boundary value testing.
* Perform invalid input testing.
* Perform fault injection testing.
* Record actual test results.
* Compare expected and actual behaviour.
* Identify failed or incomplete requirements.
* Update requirement-to-test traceability.

## Expected Outputs

* `docs/07-verification-validation.md`
* `tests/test-cases.md`
* `tests/test-report.md`
* Requirements-to-test traceability
* Verification results

## Completion Criteria

Phase 6 can be considered complete when the selected V1 system requirements have defined verification evidence and the prototype test results have been documented.

---

# Phase 7 - Controlled System Change

**Status:** `Not Started`

## Objective

Demonstrate how VehicleGuard responds to a significant requirement change after the initial system has already been designed and verified.

The purpose of this phase is to practice impact analysis, change management, traceability, and regression testing.

## Main Activities

* Introduce a formal change request.
* Document the reason for the requested change.
* Identify affected stakeholder and system requirements.
* Analyze the impact on system architecture.
* Analyze the impact on interfaces.
* Analyze additional risks.
* Estimate the required implementation changes.
* Update affected documentation.
* Implement the approved change.
* Add or update test cases.
* Perform regression testing.
* Record the final change decision and result.

## Expected Outputs

* `docs/08-change-management.md`
* Formal change request
* Change impact analysis
* Updated requirements
* Updated architecture where required
* Updated prototype
* Additional test cases
* Regression test results

## Completion Criteria

Phase 7 can be considered complete when the selected change has been analyzed, implemented, verified, and documented with traceability to all affected project elements.

---

# Phase 8 - Final Engineering Review

**Status:** `Not Started`

## Objective

Review VehicleGuard as a complete engineering case study and confirm that the project documentation, requirements, architecture, prototype, and verification results remain consistent.

## Main Activities

* Review the final project scope.
* Review stakeholder requirements.
* Review system requirements.
* Review system architecture.
* Review system risks.
* Review requirement traceability.
* Review verification results.
* Review open project risks.
* Review implemented change requests.
* Identify unresolved limitations.
* Document lessons learned.
* Update the main project documentation.
* Prepare the repository for final portfolio presentation.

## Expected Outputs

* Final requirements baseline
* Final architecture documentation
* Final verification report
* Updated risk register
* Final traceability information
* Documented project limitations
* Lessons learned
* Updated `README.md`

## Completion Criteria

VehicleGuard V1 can be considered complete when the planned system scope has been documented, implemented at prototype level, verified, reviewed, and presented with consistent engineering documentation.

---

## 4. Planned V1 Result

At the end of VehicleGuard V1, the repository should demonstrate a complete engineering path from an initial system idea to a verified prototype.

The final project should provide evidence of:

* project definition and scope management;
* stakeholder analysis;
* requirements engineering;
* requirements traceability;
* system architecture;
* interface definition;
* system risk analysis;
* technical decision-making;
* prototype development;
* requirement-based verification;
* change impact analysis;
* regression testing;
* engineering documentation.

The final result is not intended to demonstrate a production-ready automotive product.

The goal is to demonstrate a structured systems engineering process and the ability to connect requirements, architecture, implementation, verification, risks, and controlled changes within one technical project.

---

## 5. Roadmap Maintenance

This roadmap will be updated as VehicleGuard progresses.

Phase statuses should be changed only when the corresponding completion criteria have been reached.

If project findings require additional work in an earlier phase, that phase may be reopened.

New functionality that significantly changes the V1 scope should not be added directly to the roadmap without first evaluating its impact on existing requirements, architecture, risks, implementation, and verification activities.

