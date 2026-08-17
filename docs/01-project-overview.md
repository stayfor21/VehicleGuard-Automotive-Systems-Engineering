# VehicleGuard Project Overview

## 1. Document Purpose

This document defines the initial scope, purpose, boundaries, assumptions, and operational concept of VehicleGuard.

It provides a common reference for the requirements, architecture, risk analysis, prototype development, and verification activities that follow.

The document describes VehicleGuard at the system level. Detailed requirements, internal architecture, interfaces, and test procedures are maintained in separate project documents.

---

## 2. Problem Statement

Modern vehicles continuously generate information about their operating condition through sensors and electronic control units.

Parameters such as coolant temperature, battery voltage, oil pressure, engine speed, and brake condition can provide important information about the current state of a vehicle.

Raw vehicle data alone, however, does not provide a complete diagnostic result.

The received information must be checked for validity, evaluated against defined operating conditions, and interpreted before it can be used to identify abnormal vehicle behaviour.

A monitoring system therefore needs to distinguish between:

* normal vehicle operation;
* abnormal operating conditions;
* critical conditions;
* invalid or implausible input data.

When an abnormal condition is detected, the system must also determine how the event should be classified and what information should be provided to the driver or diagnostic process.

VehicleGuard is designed as a conceptual system that explores this monitoring and diagnostic process.

---

## 3. System Purpose

The purpose of VehicleGuard is to receive vehicle operating data and transform it into structured information about the current condition of the vehicle.

VehicleGuard evaluates selected vehicle parameters, identifies abnormal conditions, classifies detected faults, and generates appropriate diagnostic information.

The system is intended to demonstrate the following processing chain:

```text
Vehicle Data
     |
     v
Input Validation
     |
     v
Condition Monitoring
     |
     v
Fault Detection
     |
     v
Severity Classification
     |
     v
Warning and Diagnostic Information
```

VehicleGuard does not replace existing vehicle control systems and does not directly control safety-critical vehicle functions.

Its role is limited to monitoring, evaluation, fault detection, classification, and diagnostic output within the defined project scope.

---

## 4. Project Objectives

VehicleGuard V1 has the following main objectives:

* Define a clear set of stakeholder and system requirements.
* Monitor a limited set of simulated vehicle parameters.
* Validate incoming vehicle data before diagnostic evaluation.
* Detect selected abnormal operating conditions.
* Distinguish between vehicle condition faults and invalid input data.
* Classify detected conditions according to a defined severity model.
* Generate understandable warning information.
* Generate structured diagnostic information.
* Maintain traceability between requirements and verification activities.
* Develop a lightweight prototype for requirement verification.
* Verify selected system behaviour through defined test cases.
* Demonstrate controlled engineering change during a later project phase.

The objective is not to reproduce the complete diagnostic architecture of a production vehicle.

The project focuses on demonstrating a structured systems engineering process using a manageable technical system.

---

## 5. Operational Concept

VehicleGuard operates as a monitoring and diagnostic system.

In the conceptual automotive environment, vehicle sensors provide physical measurements to one or more vehicle ECUs. Vehicle information is then made available through the vehicle communication environment.

VehicleGuard receives selected vehicle data from this environment.

For the VehicleGuard prototype, a software-based vehicle simulator replaces the physical vehicle, sensors, ECUs, and communication network.

The relationship between the conceptual automotive environment and the prototype environment is therefore:

```text
Conceptual Automotive Environment

Physical Sensors
      |
      v
Vehicle ECU
      |
      v
Vehicle Network
      |
      v
VehicleGuard


Prototype Environment

Vehicle Simulator
      |
      v
VehicleGuard Prototype
```

This separation allows the project to explore system behaviour without claiming to implement a production vehicle communication architecture.

During normal operation, VehicleGuard receives valid vehicle parameters and reports no abnormal condition.

When a monitored value enters a defined abnormal range, VehicleGuard evaluates the condition and generates the corresponding diagnostic result.

When input data is missing, invalid, or implausible, the system should identify the problem as an input or communication-related condition instead of automatically interpreting it as a real vehicle fault.

---

## 6. System Boundary

The system boundary defines which functions belong to VehicleGuard and which elements are considered external to the system.

Vehicle sensors, physical vehicle ECUs, and the actual vehicle communication network are outside the VehicleGuard system boundary.

VehicleGuard begins when vehicle information is provided through its defined input interface.

Within the system boundary, VehicleGuard is responsible for:

* receiving vehicle data;
* validating received input;
* monitoring selected parameters;
* detecting defined abnormal conditions;
* determining condition severity;
* creating warning information;
* creating diagnostic event information.

The driver and external diagnostic or service systems are also outside the VehicleGuard boundary. They receive information generated by VehicleGuard but are not implemented as part of the core V1 system.

![VehicleGuard System Context Diagram](../diagrams/system-context.png)

<p align="center">
  <em>Figure 1 - VehicleGuard system context and external interfaces</em>
</p>

The diagram represents the system at context level. Internal VehicleGuard components are intentionally not shown here and will be defined later in the system architecture.

---

## 7. VehicleGuard V1 Scope

The V1 scope is intentionally limited.

The purpose of this limitation is to allow the project to develop requirements, architecture, verification, and traceability in sufficient depth without attempting to model an entire vehicle.

### 7.1 In Scope

VehicleGuard V1 includes:

* reception of simulated vehicle operating data;
* monitoring of selected vehicle parameters;
* basic input validation;
* configurable operating thresholds;
* detection of selected abnormal conditions;
* fault severity classification;
* driver warning generation;
* diagnostic event generation;
* software-based vehicle signal simulation;
* controlled fault injection for verification;
* requirement-based testing;
* basic requirements traceability.

### 7.2 Out of Scope

The following areas are outside VehicleGuard V1:

* direct connection to a real vehicle;
* physical sensor development;
* development of a production automotive ECU;
* control of engine, braking, steering, or other vehicle actuators;
* production CAN communication stack;
* complete AUTOSAR implementation;
* real cloud infrastructure;
* real service center integration;
* machine learning based predictive maintenance;
* autonomous driving functionality;
* production cybersecurity implementation;
* functional safety certification;
* homologation;
* production deployment.

Some of these areas may be discussed conceptually or considered as future extensions, but they are not required for completion of VehicleGuard V1.

---

## 8. Monitored Vehicle Parameters

VehicleGuard V1 focuses on five vehicle parameters.

| Parameter           | Purpose                                                                  |
| ------------------- | ------------------------------------------------------------------------ |
| Coolant Temperature | Monitor engine thermal condition and detect overheating scenarios        |
| Battery Voltage     | Monitor electrical system voltage and detect abnormal voltage conditions |
| Oil Pressure        | Detect potentially abnormal engine lubrication conditions                |
| Engine RPM          | Monitor engine operating speed and support operating condition analysis  |
| Brake Condition     | Represent the condition of the braking system for monitoring purposes    |

The exact operating ranges, warning thresholds, and critical thresholds are not defined in this overview.

They will be defined later through system requirements and configuration data.

Values used by the prototype are demonstration values and must not be interpreted as production limits for real vehicles.

---

## 9. System Inputs and Outputs

At system level, VehicleGuard has one primary category of input and two primary categories of output.

### Inputs

Vehicle operating data is provided to VehicleGuard through the defined input interface.

Initial V1 signals include:

```text
Coolant Temperature
Battery Voltage
Oil Pressure
Engine RPM
Brake Condition
```

Additional metadata may later be introduced where required for validation or diagnostics.

### Driver Output

VehicleGuard may provide a driver-oriented status or warning.

The information should communicate the condition without requiring the driver to interpret raw diagnostic data.

Possible condition levels include:

```text
NORMAL
INFO
WARNING
CRITICAL
```

The exact warning strategy will be defined through system requirements.

### Diagnostic Output

VehicleGuard may also generate structured diagnostic information.

A diagnostic event may contain information such as:

```text
Fault Identifier
Affected Parameter
Measured Value
Condition
Severity
Timestamp
```

The exact diagnostic data structure will be defined during interface and architecture development.

---

## 10. Assumptions

The initial VehicleGuard concept is based on the following assumptions:

* Vehicle data is available to VehicleGuard in a usable and decoded form.
* The V1 prototype uses simulated vehicle data instead of physical vehicle signals.
* The simulator can generate both normal and abnormal operating conditions.
* Demonstration thresholds can be configured for prototype testing.
* VehicleGuard does not directly control vehicle actuators.
* Driver warnings are represented as system outputs rather than through a production vehicle HMI.
* Diagnostic service integration is represented conceptually.
* The project does not assume that demonstration thresholds are valid for all real vehicles.
* The selected V1 parameters provide sufficient complexity to demonstrate the intended engineering process.

These assumptions may be reviewed as the requirements and architecture become more detailed.

---

## 11. Constraints

VehicleGuard is developed as an independent engineering portfolio project and therefore operates under several constraints.

### No Physical Vehicle Integration

The project does not currently have access to a dedicated test vehicle or production automotive ECU environment.

Vehicle behaviour must therefore be represented through simulation.

### Limited System Scope

Only a small number of vehicle parameters are included in V1.

This is intentional and prevents unnecessary project expansion.

### Prototype-Level Implementation

The software implementation is designed to support system demonstration and verification.

Production performance, hardware constraints, real-time guarantees, and automotive software certification are outside the current scope.

### Simplified Automotive Environment

Real vehicle systems contain significantly more ECUs, signals, dependencies, diagnostic functions, and safety mechanisms than represented in VehicleGuard.

The project simplifies this environment to focus on selected systems engineering activities.

---

## 12. Success Criteria

VehicleGuard V1 will be considered successful when the project can demonstrate a consistent engineering path from system definition to verification.

The project should be able to show that:

* the system purpose and boundary are clearly defined;
* relevant stakeholders have been identified;
* stakeholder needs are connected to system requirements;
* system requirements describe the intended V1 behaviour;
* requirements are sufficiently clear to support verification;
* the system architecture supports the defined requirements;
* important system risks and failure scenarios have been considered;
* the prototype demonstrates the selected system behaviour;
* test cases are connected to relevant requirements;
* expected and actual verification results are documented;
* significant system changes can be evaluated through a controlled change process;
* project limitations and assumptions remain clearly documented.

Completion is based on engineering evidence rather than the number of implemented software features.

---

## 13. Current Limitations

VehicleGuard currently represents an early engineering concept.

At this stage:

* stakeholder analysis has not yet been completed;
* detailed system requirements have not yet been baselined;
* internal system architecture has not yet been finalized;
* detailed interfaces have not yet been defined;
* system-level risk analysis has not yet been completed;
* the software prototype has not yet been implemented;
* verification results are not yet available.

These limitations are expected at the current project stage.

The corresponding project elements will be developed according to the project roadmap.

---

## 14. Relationship to Other Project Documents

This overview provides the initial system-level foundation for the rest of the VehicleGuard documentation.

More detailed information will be maintained in dedicated documents.

| Document                              | Purpose                                                               |
| ------------------------------------- | --------------------------------------------------------------------- |
| `02-stakeholders.md`                  | Defines stakeholders, stakeholder needs, and stakeholder expectations |
| `03-system-requirements.md`           | Defines detailed VehicleGuard system requirements                     |
| `04-system-architecture.md`           | Defines internal system structure and functional architecture         |
| `05-interfaces.md`                    | Defines system inputs, outputs, and interfaces                        |
| `06-risk-analysis.md`                 | Analyzes technical and system-level risks                             |
| `07-verification-validation.md`       | Defines the verification and validation approach                      |
| `08-change-management.md`             | Defines how controlled system changes are analyzed and documented     |
| `project-management/roadmap.md`       | Defines the main VehicleGuard development phases                      |
| `project-management/risk-register.md` | Tracks risks affecting project development                            |

Together, these documents provide traceability from the initial VehicleGuard concept through requirements, architecture, implementation, verification, and controlled system change.
