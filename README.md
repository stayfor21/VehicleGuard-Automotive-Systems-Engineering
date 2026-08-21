# VehicleGuard

### Automotive Predictive Maintenance & Safety System

VehicleGuard is a portfolio systems engineering project focused on the design of a conceptual automotive monitoring, diagnostic and safety system.

The project explores how vehicle condition data can be collected, evaluated and transformed into useful diagnostic information for drivers and service personnel.

The main goal is not to develop a production-ready automotive ECU or a complete vehicle diagnostic platform. Instead, VehicleGuard is designed as a practical systems engineering case study covering the complete development process from the initial problem statement and stakeholder needs to system requirements, architecture, risk analysis, verification and change management.

A lightweight software prototype is used to simulate vehicle signals and verify selected system requirements.

Current prototype commands:

```text
python -m prototype.vehicle_simulator
python -m pytest
```

Current verification status: VehicleGuard V1 prototype verification passed on 2026-08-21 with 95 automated pytest tests passing and 0 failures.

---

## 1. Project Motivation

Modern vehicles contain a large number of sensors, electronic control units and communication interfaces.

These systems continuously generate information about the condition of the vehicle, including:

* engine temperature;
* electrical system voltage;
* engine speed;
* oil pressure;
* braking system condition;
* communication status between electronic components;
* diagnostic faults.

Collecting these values alone is not sufficient.

A useful vehicle monitoring system must be able to determine whether the received data represents normal vehicle operation, an abnormal condition or a potentially critical failure.

The system must then decide how this information should be communicated.

For example:

```text
Coolant temperature: 91 °C
Battery voltage: 13.8 V
Oil pressure: 3.2 bar
Engine speed: 2450 rpm

Vehicle status: NORMAL
```

During abnormal operation:

```text
Coolant temperature: 118 °C

Fault detected:
Engine coolant temperature above critical threshold

Severity:
CRITICAL

Recommended action:
Stop the vehicle safely and inspect the cooling system.
```

VehicleGuard investigates this process from a systems engineering perspective.

---

## 2. Project Objective

The objective of VehicleGuard is to design a conceptual automotive system capable of:

1. receiving simulated vehicle operating data;
2. validating incoming data;
3. monitoring important vehicle parameters;
4. detecting abnormal operating conditions;
5. classifying faults according to their severity;
6. generating driver warnings;
7. storing diagnostic information;
8. providing diagnostic data that could later be used by service personnel;
9. maintaining traceability between stakeholder needs, system requirements and verification activities.

The project also demonstrates how engineering changes can be introduced and evaluated during system development.

---

## 3. Engineering Focus

VehicleGuard is primarily a **systems engineering and requirements engineering project**.

Software development is only one part of the project.

The main areas covered are:

* stakeholder analysis;
* requirements engineering;
* system decomposition;
* functional analysis;
* system architecture;
* interface definition;
* vehicle diagnostics;
* risk analysis;
* requirements traceability;
* verification and validation planning;
* test case development;
* change management;
* technical documentation;
* basic project planning.

The intention is to demonstrate the ability to understand and structure a technical system as a whole rather than focusing only on software implementation.

---

## 4. Project Scope

The first version of VehicleGuard focuses on a limited number of vehicle parameters.

This limitation is intentional.

The project is designed to explore the engineering process in sufficient depth without attempting to simulate an entire vehicle.

### Initial monitored parameters

VehicleGuard V1 will monitor:

| Parameter           | Purpose                                                       |
| ------------------- | ------------------------------------------------------------- |
| Coolant temperature | Detection of engine overheating                               |
| Battery voltage     | Monitoring of electrical system condition                     |
| Oil pressure        | Detection of potentially unsafe engine lubrication conditions |
| Engine RPM          | Monitoring engine operating conditions                        |
| Brake condition     | Monitoring braking system degradation or abnormal status      |

Additional parameters may be introduced in later project versions through controlled change requests.

---

## 5. Out of Scope

VehicleGuard is not intended to represent a production-ready automotive system.

The following areas are currently outside the scope of the project:

* development of a real automotive ECU;
* connection to an actual vehicle;
* implementation on safety-certified hardware;
* complete AUTOSAR implementation;
* production CAN communication stack;
* homologation;
* cybersecurity certification;
* functional safety certification;
* development according to a complete production ISO 26262 lifecycle;
* real predictive maintenance based on machine learning;
* real service infrastructure integration;
* production-level cloud connectivity.

Where relevant, these topics may be discussed conceptually.

The project clearly separates simulated behaviour from real automotive functionality.

---

## 6. System Concept

The conceptual system architecture is based on several logical layers.

```text
+----------------------------------------------------+
|                  Vehicle Sensors                   |
|                                                    |
|  Temperature | Battery | Oil | RPM | Brake Status  |
+--------------------------+-------------------------+
                           |
                           v
+----------------------------------------------------+
|                    Vehicle ECU                     |
|                                                    |
|      Signal acquisition and vehicle processing     |
+--------------------------+-------------------------+
                           |
                           |
                  Vehicle Communication
                  Conceptual CAN Interface
                           |
                           v
+----------------------------------------------------+
|                    VehicleGuard                    |
|                                                    |
|  Data Validation                                   |
|  Signal Monitoring                                 |
|  Fault Detection                                   |
|  Severity Classification                           |
|  Diagnostic Event Management                       |
+--------------------------+-------------------------+
                           |
              +------------+-------------+
              |                          |
              v                          v
+--------------------------+   +------------------------+
|      Driver Warning      |   | Diagnostic Information |
|                          |   |                        |
| INFO                     |   | Fault ID               |
| WARNING                  |   | Timestamp              |
| CRITICAL                 |   | Parameter              |
+--------------------------+   | Measured value         |
                               | Severity               |
                               +----------+-------------+
                                          |
                                          v
                               +----------------------+
                               |    Service Concept   |
                               |                      |
                               | Diagnostic analysis  |
                               | Maintenance support  |
                               +----------------------+
```

This architecture will evolve during the project.

The initial diagram represents the logical system concept rather than a final physical architecture.

---

## 7. Stakeholders

Several stakeholders are considered during the development of VehicleGuard.

### Driver

The driver needs understandable and timely information when the vehicle enters an abnormal operating condition.

The driver should not be required to interpret raw sensor values or diagnostic codes.

### Vehicle Manufacturer

The manufacturer requires a structured system that can detect faults consistently and provide information that supports vehicle reliability and maintainability.

### Service Technician

Service personnel require diagnostic information that can help identify the reason for a warning or fault.

### Systems Engineer

The systems engineer is responsible for defining system behaviour, interfaces, requirements and interactions between subsystems.

### Software / ECU Development Team

The implementation team requires clear and testable system requirements.

### Test and Validation Team

The validation team needs traceable requirements and defined acceptance criteria in order to verify system behaviour.

---

## 8. Initial Stakeholder Needs

The initial stakeholder needs include:

### STK-001 — Driver Safety Information

The driver needs to be informed about vehicle conditions that may affect safety or vehicle reliability.

### STK-002 — Fault Identification

The system should provide sufficient diagnostic information to identify abnormal vehicle operating conditions.

### STK-003 — Understandable Warning

Warnings should communicate the seriousness of a detected problem without requiring the driver to understand technical diagnostic data.

### STK-004 — Service Diagnostics

Service personnel should have access to information describing detected vehicle faults.

### STK-005 — Reliable Fault Detection

The system should avoid generating warnings based on invalid or implausible sensor data where possible.

These stakeholder needs will later be refined into formal system requirements.

---

## 9. Requirements Engineering Approach

VehicleGuard uses a structured requirements hierarchy.

```text
Problem / Business Need
        |
        v
Stakeholder Need
        |
        v
Stakeholder Requirement
        |
        v
System Requirement
        |
        v
System Component
        |
        v
Verification Method
        |
        v
Test Case
```

Each important system requirement will receive a unique identifier.

Example:

### SYS-TEMP-001

The system shall monitor the engine coolant temperature during vehicle operation.

### SYS-TEMP-002

The system shall compare the received coolant temperature value against defined operating thresholds.

### SYS-TEMP-003

The system shall generate a coolant temperature warning when the defined warning condition is reached.

### SYS-TEMP-004

The system shall classify a critical coolant temperature condition as `CRITICAL`.

Requirements will be written so that they can be verified through inspection, analysis, demonstration or testing.

---

## 10. Requirements Quality

Requirements will be reviewed according to several criteria.

A requirement should be:

* clear;
* necessary;
* implementation-independent where possible;
* unambiguous;
* traceable;
* verifiable;
* consistent with other requirements.

For example, the following requirement would be considered insufficient:

```text
The system should warn the driver when the engine gets too hot.
```

The term `too hot` is not sufficiently defined.

A more precise requirement would define the monitored parameter and the expected behaviour.

For example:

```text
The system shall generate a high coolant temperature warning
when the coolant temperature reaches or exceeds the configured
warning threshold.
```

The exact threshold may be maintained as a configurable system parameter instead of being embedded directly into the requirement.

---

## 11. Fault Severity Concept

VehicleGuard will initially classify system conditions into four levels.

### NORMAL

No abnormal condition is currently detected.

Example:

```text
Coolant temperature: 90 °C
Status: NORMAL
```

### INFO

The system has detected information relevant to the driver or service process that does not currently require immediate action.

### WARNING

An abnormal condition has been detected.

Vehicle operation may continue depending on the type of fault, but the condition should be investigated.

### CRITICAL

A condition has been detected that may affect vehicle safety, reliability or mechanical integrity.

Immediate driver attention may be required.

The exact classification logic will be defined through system requirements and verified through test cases.

---

## 12. Data Validation

VehicleGuard should not automatically assume that every incoming signal is valid.

The system concept therefore includes basic signal validation.

Potential validation cases include:

* value outside the physically possible range;
* missing signal;
* frozen signal;
* communication timeout;
* inconsistent values;
* sudden unrealistic signal change.

For example:

```text
Battery voltage = -40 V
```

Such a value should not immediately be interpreted as a real low-voltage battery fault.

Instead, the system should first determine whether the input itself is valid.

This distinction between a **vehicle fault** and a **signal/data fault** is important for the system architecture.

---

## 13. Vehicle Communication

The conceptual architecture assumes that vehicle data is transferred through a vehicle communication network.

CAN will be used as the primary conceptual example because of its widespread use in automotive systems.

However, VehicleGuard V1 will not implement a production CAN communication stack.

The initial prototype will simulate the reception of decoded vehicle signals.

Example:

```text
coolant_temperature = 91.4
battery_voltage = 13.8
engine_rpm = 2450
oil_pressure = 3.2
brake_condition = 82
```

A later extension may introduce simulated CAN frames or integration with CAN-related development tools.

---

## 14. Prototype Strategy

A lightweight software prototype will be developed after the system requirements and initial architecture have been defined.

The prototype will consist of two main parts.

### Vehicle Simulator

The simulator will generate vehicle operating data.

Example:

```text
Vehicle state:

RPM:                  2450 rpm
Coolant temperature:  91 °C
Battery voltage:       13.8 V
Oil pressure:          3.2 bar
Brake condition:       82 %
```

It will also be capable of generating abnormal conditions.

Example:

```text
FAULT INJECTION

Coolant temperature: 118 °C
```

### VehicleGuard Diagnostic Logic

The diagnostic component will receive simulated data and evaluate it according to the defined requirements.

Example output:

```text
FAULT DETECTED

Fault ID:
TEMP_HIGH_001

Parameter:
Engine Coolant Temperature

Measured value:
118 °C

Severity:
CRITICAL

Recommended action:
Stop the vehicle safely and inspect the cooling system.
```

The prototype is intended for requirement verification rather than production use.

---

## 15. Verification and Validation

Testing is an important part of VehicleGuard.

Each important system requirement should be connected to at least one verification activity.

Example traceability:

```text
STK-001
Driver must be informed about critical vehicle conditions
        |
        v
SYS-TEMP-003
System generates coolant warning
        |
        v
SYS-TEMP-004
Critical temperature is classified as CRITICAL
        |
        v
TC-TEMP-003
Critical coolant temperature test
```

---

## 16. Example Test Case

### TC-TEMP-001 — Normal Coolant Temperature

**Related requirements**

* SYS-TEMP-001
* SYS-TEMP-002
* SYS-TEMP-003

**Precondition**

VehicleGuard monitoring is active.

**Input**

```text
Coolant temperature = 90 °C
```

**Expected result**

```text
Temperature status = NORMAL
No driver warning generated
```

**Actual result**

To be completed after prototype implementation.

**Test result**

`NOT EXECUTED`

---

## 17. Boundary Testing

Boundary conditions are particularly important when system behaviour depends on thresholds.

Assume the warning threshold is configured at:

```text
105 °C
```

Relevant tests may include:

```text
104.9 °C
105.0 °C
105.1 °C
```

This forces the engineering requirement to define precisely whether the warning condition is:

```text
temperature > threshold
```

or:

```text
temperature >= threshold
```

The resulting behaviour should not depend on interpretation by the implementation team.

---

## 18. Negative Testing

The project will also include tests for invalid system inputs.

Examples:

```text
Coolant temperature = -200 °C
Battery voltage = 200 V
Engine RPM = -500 rpm
Missing oil pressure signal
Brake signal communication timeout
```

Expected system behaviour must be defined through requirements.

In many cases, the correct reaction should be a diagnostic signal fault rather than a vehicle condition warning.

---

## 19. Risk Analysis

VehicleGuard will maintain a basic engineering risk register.

Initial example:

| ID       | Risk                                          | Probability |   Impact | Mitigation                           |
| -------- | --------------------------------------------- | ----------: | -------: | ------------------------------------ |
| RISK-001 | Invalid sensor data interpreted as real fault |      Medium |     High | Signal plausibility validation       |
| RISK-002 | Critical fault not detected                   |         Low | Critical | Verification of threshold logic      |
| RISK-003 | False critical warning                        |      Medium |     High | Signal filtering and validation      |
| RISK-004 | Vehicle communication failure                 |      Medium |     High | Timeout monitoring                   |
| RISK-005 | Incorrect fault severity classification       |         Low |     High | Requirement review and test coverage |

The risk analysis will be refined as the system architecture evolves.

A simplified FMEA may also be introduced later.

---

## 20. Requirements Traceability

Traceability is one of the central elements of the project.

The objective is to maintain links between:

```text
Stakeholder Requirement
        |
System Requirement
        |
Architecture Component
        |
Implementation
        |
Verification Method
        |
Test Case
        |
Test Result
```

This allows questions such as the following to be answered:

* Why does this requirement exist?
* Which stakeholder need does it support?
* Which system component implements it?
* How is the requirement verified?
* Which tests are affected when the requirement changes?

---

## 21. Change Management

VehicleGuard will intentionally include system changes during development.

The purpose is to demonstrate that engineering projects do not remain static after the initial requirements have been written.

Example future change request:

### CR-001 — Battery Health Monitoring

**Request**

Introduce functionality that detects long-term battery degradation and provides an early maintenance recommendation.

Potential impact:

```text
Stakeholder requirements    affected
System requirements         affected
System architecture         affected
Diagnostic logic            affected
Prototype                   affected
Test specification          affected
Project schedule            affected
```

Before implementation, the requested change must be analysed.

The project will document:

1. reason for the change;
2. affected requirements;
3. affected architecture components;
4. potential risks;
5. required implementation changes;
6. additional verification activities;
7. final decision.

---

## 22. Project Development Process

VehicleGuard follows an iterative systems engineering process.

### Phase 1 — Project Definition

* problem statement;
* project objectives;
* scope;
* limitations;
* stakeholder identification.

### Phase 2 — Requirements Engineering

* stakeholder needs;
* stakeholder requirements;
* system requirements;
* requirement review;
* acceptance criteria.

### Phase 3 — System Architecture

* system context;
* functional decomposition;
* logical architecture;
* interfaces;
* data flow.

### Phase 4 — Risk Analysis

* initial risk register;
* fault scenarios;
* mitigation concepts.

### Phase 5 — Prototype

* vehicle signal simulator;
* diagnostic rules;
* fault detection;
* severity classification.

The V1 prototype is implemented in `prototype/`. It loads diagnostic ranges and thresholds from `prototype/config/vehicleguard-v1.json`, provides deterministic simulator scenarios, and generates structured driver warning and diagnostic event outputs for verification.

### Phase 6 — Verification

* test specification;
* normal operation tests;
* boundary tests;
* fault injection;
* negative tests;
* test report.

### Phase 7 — Change Management

* change request;
* impact analysis;
* requirement modification;
* implementation update;
* regression testing.

### Phase 8 — Project Review

* requirement coverage review;
* architecture review;
* risk review;
* verification results;
* lessons learned.

---

## 23. Planned Repository Structure

The repository will gradually evolve toward the following structure:

```text
VehicleGuard-Automotive-Systems-Engineering/
│
├── README.md
│
├── docs/
│   ├── 01-project-overview.md
│   ├── 02-stakeholders.md
│   ├── 03-system-requirements.md
│   ├── 04-system-architecture.md
│   ├── 05-interfaces.md
│   ├── 06-risk-analysis.md
│   ├── 07-verification-validation.md
│   └── 08-change-management.md
│
├── requirements/
│   └── requirements.xlsx
│
├── diagrams/
│   ├── system-context.png
│   ├── system-architecture.png
│   ├── functional-decomposition.png
│   └── requirements-traceability.png
│
├── prototype/
│   ├── vehicle_simulator.py
│   ├── diagnostics.py
│   └── config/
│
├── tests/
│   ├── test-cases.md
│   └── test-report.md
│
├── project-management/
│   ├── roadmap.md
│   ├── risk-register.md
│   └── change-requests/
│
└── LICENSE
```

The complete structure will not be created in advance.

Directories and documents will be introduced when they become necessary during development.

---

## 24. Project Status

Current status:

```text
[x] Project concept
[x] Initial scope
[x] Initial system idea

[x] Stakeholder analysis
[x] Stakeholder requirements
[x] System requirements
[x] System context diagram
[x] Functional architecture
[x] Risk analysis
[x] Prototype development
[x] Test specification
[x] Verification
[ ] Change request
[ ] Regression testing
[ ] Final engineering review
```

Prototype execution:

```text
python -m prototype.vehicle_simulator
```

Automated verification:

```text
python -m pytest
```

Latest recorded result: 95 passed, 0 failed, 0 skipped or blocked. The verification report and machine-readable evidence are stored in `tests/test-report.md` and `tests/results/`.

---

## 25. Current Development Stage

The project has reached the **VehicleGuard V1 prototype verification stage**.

The V1 requirements, architecture, interfaces, configuration, risk analysis, prototype implementation, and automated verification evidence are now present in the repository.

No production assumptions should be derived from the repository state.

Future architecture, requirement, or diagnostic strategy changes should be handled through the documented change management process when they affect established V1 behaviour.

This development history is intentionally preserved as part of the project.

---

## 26. Future Extensions

Potential future extensions include:

* simulated CAN communication;
* diagnostic trouble code handling;
* battery health estimation;
* maintenance prediction;
* communication timeout monitoring;
* signal plausibility checks;
* additional vehicle sensors;
* service history;
* diagnostic report generation;
* simple driver dashboard;
* simple service dashboard;
* fault history;
* requirement management tooling;
* automated requirements-to-test traceability;
* simplified FMEA;
* Automotive SPICE-inspired documentation structure;
* ISO 26262-related conceptual analysis.

These features are not currently part of the committed V1 scope.

They may be introduced through formal project change requests.

---

## 27. Engineering Principles

Several principles guide the project.

### Requirements before implementation

Important functionality should be defined before it is implemented.

### Traceability

System behaviour should be traceable back to a requirement or engineering decision.

### Verification

A requirement is only useful if it can be verified.

### Controlled changes

New features should be introduced through impact analysis rather than added without reviewing the existing system.

### Clear assumptions

Simulated behaviour, engineering assumptions and real automotive functionality must remain clearly separated.

### Technical simplicity

The prototype should remain as simple as necessary to demonstrate the system concept.

Complex software implementation is not a goal by itself.

---

## 28. Why This Project Exists

VehicleGuard is part of my engineering portfolio and reflects my interest in working at the intersection of:

* computer engineering;
* automotive systems;
* systems engineering;
* requirements engineering;
* technical project work;
* vehicle diagnostics;
* business and technical communication.

My academic background is in Computer Engineering.

One of my previous university projects involved the development of a GSM-based emergency warning system using sensors, communication modules and embedded hardware.

VehicleGuard continues this technical direction while shifting the focus from individual component implementation toward system-level engineering, requirements, architecture, verification and project decision-making.

The project is therefore not intended to demonstrate only programming ability.

Its purpose is to document the engineering process behind the system.

---

## 29. Disclaimer

VehicleGuard is an independent educational and portfolio project.

It is not affiliated with any vehicle manufacturer, automotive supplier or engineering company.

The system architecture, requirements, thresholds, diagnostic logic and safety concepts contained in this repository are created for educational purposes and should not be used in real vehicles or safety-critical systems.

Real automotive development requires additional engineering processes, validated hardware, extensive testing, regulatory compliance and appropriate functional safety activities.

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.
