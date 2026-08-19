# VehicleGuard System Architecture

## 1. Purpose

This document defines the system architecture of VehicleGuard V1.

The architecture translates the system requirements defined in `03-system-requirements.md` into a structured set of system elements with clearly separated responsibilities.

The purpose of the architecture is to define:

- the main VehicleGuard system elements;
- the responsibility of each element;
- the functional flow through the system;
- the relationships between system elements;
- the allocation of system requirements to architecture elements;
- the architectural boundaries used for prototype implementation and verification.

The architecture is defined at the system level.

Detailed software implementation decisions are intentionally kept separate unless they are required to explain an architectural responsibility or interface.

---

## 2. Architecture Overview

VehicleGuard V1 is structured as a diagnostic processing system that receives vehicle operating data, validates the received information, evaluates monitored parameters, detects abnormal conditions, determines their severity, and generates appropriate system outputs.

The main processing flow is:

```text
Vehicle Data
     |
     v
Input Interface
     |
     v
Data Validation
     |
     v
Condition Monitor
     |
     v
Diagnostic Engine
     |
     v
Severity Manager
     |
     +-------------------+
     |                   |
     v                   v
Driver Warning      Diagnostic Event
Manager             Manager
```

Configuration data supports the processing functions by providing parameter ranges, monitoring criteria, and severity criteria.

The architecture separates these responsibilities so that individual functions can be understood, implemented, changed, and verified independently.

---

## 3. Architectural Principles

The VehicleGuard architecture follows several principles intended to keep the system understandable and maintainable.

### 3.1 Separation of Responsibilities

Each architecture element has a defined primary responsibility.

Input reception, validation, monitoring, diagnostic evaluation, severity classification, warning generation, event generation, and configuration management are treated as separate system responsibilities.

This reduces unnecessary coupling between functions.

### 3.2 Validation Before Diagnostic Evaluation

Received vehicle data is validated before it is interpreted as representing an actual vehicle operating condition.

Invalid input data must remain distinguishable from valid data that represents an abnormal vehicle condition.

### 3.3 Configuration Separated from Processing Logic

Monitoring thresholds, supported input ranges, and severity criteria are treated as configuration data.

Diagnostic processing should therefore not depend on permanently embedded demonstration-specific threshold values.

### 3.4 Traceable Architecture

Architecture elements use unique identifiers.

These identifiers support traceability between:

```text
Stakeholder Need
        |
        v
System Requirement
        |
        v
Architecture Element
        |
        v
Implementation
        |
        v
Verification
```

### 3.5 Prototype Independence

The architecture describes VehicleGuard system responsibilities rather than a specific Python implementation.

The prototype is one implementation used to demonstrate and verify the architecture.

### 3.6 Controlled Scope

Architecture elements are introduced only when they support a defined VehicleGuard V1 responsibility.

Additional functionality should not be added without a corresponding engineering need or controlled project change.

---

## 4. System Boundary

VehicleGuard receives vehicle operating data from an external vehicle data source.

For the V1 prototype, this source is represented by the vehicle simulator.

The following vehicle information is currently included in the project scope:

- coolant temperature;
- battery voltage;
- oil pressure;
- engine RPM;
- brake condition;
- timestamp information associated with vehicle data.

VehicleGuard processes this information and produces two primary categories of output:

- driver warning information;
- diagnostic event information.

The following elements remain outside the VehicleGuard V1 system boundary:

- physical vehicle sensors;
- production vehicle ECUs;
- production CAN communication;
- real instrument cluster hardware;
- service center infrastructure;
- cloud backend services;
- production vehicle control functions.

VehicleGuard does not control vehicle actuators.

Its V1 responsibility is limited to monitoring, diagnostic evaluation, classification, and information generation.

---

## 5. Functional Architecture

VehicleGuard is decomposed into eight main architecture elements.

| ID | Architecture Element | Primary Responsibility |
|---|---|---|
| `COMP-INP-001` | Input Interface | Receive vehicle operating data and associate required timing information |
| `COMP-VAL-001` | Data Validation | Validate received data before diagnostic processing |
| `COMP-MON-001` | Condition Monitor | Evaluate validated parameters against configured operating conditions |
| `COMP-DIAG-001` | Diagnostic Engine | Detect and identify abnormal operating conditions |
| `COMP-SEV-001` | Severity Manager | Determine the severity of detected conditions |
| `COMP-WRN-001` | Driver Warning Manager | Generate driver-oriented warning information |
| `COMP-EVT-001` | Diagnostic Event Manager | Generate structured technical diagnostic events |
| `COMP-CFG-001` | Configuration Manager | Provide configuration data used by system processing |

These elements represent logical system responsibilities.

They do not necessarily require a one-to-one mapping to software files, classes, processes, or physical ECUs.

---

## 6. System Architecture

The high-level VehicleGuard V1 system architecture is shown below.

![VehicleGuard System Architecture](../diagrams/system-architecture.png)

<p align="center">
  <em>Figure 1 - VehicleGuard V1 System Architecture</em>
</p>

Vehicle data enters the system through the Input Interface and passes through the diagnostic processing chain.

The main processing sequence is:

```text
COMP-INP-001
      |
      v
COMP-VAL-001
      |
      v
COMP-MON-001
      |
      v
COMP-DIAG-001
      |
      v
COMP-SEV-001
      |
      +----------------+
      |                |
      v                v
COMP-WRN-001      COMP-EVT-001
```

`COMP-CFG-001` provides configuration information required by relevant processing elements.

The architecture supports evaluation of multiple monitored vehicle parameters within the same vehicle data sample.

---

## 7. Functional Decomposition

The functional decomposition of VehicleGuard V1 is shown below.

![VehicleGuard Functional Decomposition](../diagrams/functional-decomposition.png)

<p align="center">
  <em>Figure 2 - VehicleGuard V1 Functional Decomposition</em>
</p>

The functional decomposition describes how the overall VehicleGuard responsibility is divided into smaller system functions.

It is not intended to define the final software package structure.

The decomposition provides a functional basis for architecture allocation, interface definition, prototype implementation, and verification planning.

---

## 8. Architecture Element Definitions

### 8.1 COMP-INP-001 - Input Interface

**Purpose**

The Input Interface represents the entry point for vehicle operating data into VehicleGuard.

**Responsibilities**

The element is responsible for:

- receiving vehicle operating data from the defined external source;
- making supported vehicle parameters available for processing;
- receiving or associating timestamp information with vehicle data samples;
- passing received data to the validation function.

The Input Interface does not determine whether a vehicle condition is normal or abnormal.

Diagnostic interpretation begins only after the received data has been validated.

---

### 8.2 COMP-VAL-001 - Data Validation

**Purpose**

The Data Validation element determines whether received vehicle information is suitable for diagnostic evaluation.

**Responsibilities**

The element is responsible for:

- checking that required input parameters are present;
- checking whether received values use the expected data representation;
- checking numeric values against supported input ranges;
- identifying invalid input conditions;
- preventing invalid values from being interpreted as valid vehicle operating conditions.

A validation failure represents a data quality or input condition and must remain distinguishable from an abnormal vehicle operating condition.

---

### 8.3 COMP-MON-001 - Condition Monitor

**Purpose**

The Condition Monitor evaluates validated vehicle parameters against configured operating criteria.

**Responsibilities**

The element is responsible for:

- monitoring configured vehicle parameters;
- applying parameter-specific monitoring criteria;
- evaluating values against configured operating conditions;
- determining the current condition of each monitored parameter;
- supporting simultaneous monitoring of multiple parameters.

The Condition Monitor operates only on data that has passed the required validation checks.

---

### 8.4 COMP-DIAG-001 - Diagnostic Engine

**Purpose**

The Diagnostic Engine identifies abnormal conditions detected during parameter monitoring.

**Responsibilities**

The element is responsible for:

- detecting configured abnormal operating conditions;
- identifying the parameter associated with a detected condition;
- supporting multiple abnormal conditions within the same vehicle data sample;
- recognizing when a previously abnormal parameter returns to a normal condition;
- providing detected condition information for severity evaluation.

The Diagnostic Engine does not determine how a detected condition should be presented to the driver.

---

### 8.5 COMP-SEV-001 - Severity Manager

**Purpose**

The Severity Manager determines the significance of evaluated vehicle conditions.

**Responsibilities**

The element is responsible for assigning one of the supported condition levels:

- `NORMAL`;
- `INFO`;
- `WARNING`;
- `CRITICAL`.

Severity is determined using configured criteria associated with the monitored parameter and detected condition.

When multiple conditions are present, each condition is evaluated independently.

---

### 8.6 COMP-WRN-001 - Driver Warning Manager

**Purpose**

The Driver Warning Manager generates information intended for presentation to the driver.

**Responsibilities**

The element is responsible for:

- generating warning information for conditions requiring driver attention;
- identifying the affected vehicle parameter;
- including the applicable severity level;
- providing a driver-oriented description of the detected condition;
- avoiding active abnormal-condition warnings for parameters classified as `NORMAL`.

VehicleGuard V1 does not implement a production vehicle HMI.

The output of this element represents the warning information that could later be consumed by an HMI or another external system.

---

### 8.7 COMP-EVT-001 - Diagnostic Event Manager

**Purpose**

The Diagnostic Event Manager creates structured technical information about detected conditions.

**Responsibilities**

The element is responsible for generating diagnostic events containing relevant information such as:

- condition or fault identifier;
- affected vehicle parameter;
- observed value where available;
- severity level;
- associated timestamp.

The element also supports diagnostic information for invalid input conditions so that data problems remain distinguishable from actual abnormal vehicle operating conditions.

The generated information can be used by the prototype, verification activities, or future diagnostic interfaces.

---

### 8.8 COMP-CFG-001 - Configuration Manager

**Purpose**

The Configuration Manager provides configuration information used by VehicleGuard processing functions.

**Responsibilities**

The element is responsible for providing configuration data including:

- supported input ranges;
- monitoring thresholds;
- condition criteria;
- severity criteria;
- parameter-specific configuration.

The active configuration must be used consistently by the system during processing.

The V1 architecture does not require a specific configuration storage technology.

The prototype implementation may use a simple configuration file or equivalent structured representation.

---

## 9. Component Interaction

VehicleGuard follows a primarily sequential diagnostic processing flow.

A vehicle data sample is received by `COMP-INP-001` and transferred to `COMP-VAL-001`.

If the data is suitable for diagnostic processing, the validated information is evaluated by `COMP-MON-001`.

The resulting parameter condition is processed by `COMP-DIAG-001`, which identifies relevant abnormal conditions.

Detected conditions are passed to `COMP-SEV-001` for severity classification.

The classified information can then be used by:

- `COMP-WRN-001` to generate driver-oriented warning information;
- `COMP-EVT-001` to generate technical diagnostic event information.

Configuration information from `COMP-CFG-001` is used by the system elements that require configurable ranges, thresholds, or severity criteria.

Detailed interface structures will be defined separately in `05-interfaces.md`.

---

## 10. Architecture Interfaces

The architecture currently identifies the following logical interface relationships:

| Source | Destination | Information |
|---|---|---|
| Vehicle Data Source | `COMP-INP-001` | Vehicle operating data |
| `COMP-INP-001` | `COMP-VAL-001` | Received vehicle data |
| `COMP-VAL-001` | `COMP-MON-001` | Validated vehicle data |
| `COMP-MON-001` | `COMP-DIAG-001` | Evaluated parameter conditions |
| `COMP-DIAG-001` | `COMP-SEV-001` | Detected condition information |
| `COMP-SEV-001` | `COMP-WRN-001` | Classified condition information |
| `COMP-SEV-001` | `COMP-EVT-001` | Classified condition information |
| `COMP-CFG-001` | Processing Elements | Configuration data |
| `COMP-WRN-001` | External Consumer | Driver warning information |
| `COMP-EVT-001` | External Consumer | Diagnostic event information |

This table defines logical relationships only.

Data structures, units, value ranges, field definitions, and detailed interface contracts will be specified in `05-interfaces.md`.

---

## 11. Requirement Allocation

System requirements are allocated to architecture elements according to the element responsible for realizing the required behaviour.

### Input Interface

`COMP-INP-001` is the primary architecture element for:

- `SYS-INP-001`
- `SYS-INP-002`
- `SYS-INP-003`
- `SYS-INP-004`
- `SYS-INP-005`
- `SYS-INP-006`
- `SYS-INP-007`

### Data Validation

`COMP-VAL-001` is the primary architecture element for:

- `SYS-VAL-001`
- `SYS-VAL-002`
- `SYS-VAL-003`
- `SYS-VAL-004`
- `SYS-VAL-005`
- `SYS-VAL-006`

### Condition Monitor

`COMP-MON-001` is the primary architecture element for:

- `SYS-MON-001`
- `SYS-MON-002`
- `SYS-MON-003`
- `SYS-MON-004`
- `SYS-MON-005`
- `SYS-MON-006`

### Diagnostic Engine

`COMP-DIAG-001` is the primary architecture element for:

- `SYS-DIAG-001`
- `SYS-DIAG-002`
- `SYS-DIAG-003`
- `SYS-DIAG-004`
- `SYS-DIAG-005`

### Severity Manager

`COMP-SEV-001` is the primary architecture element for:

- `SYS-SEV-001`
- `SYS-SEV-002`
- `SYS-SEV-003`
- `SYS-SEV-004`
- `SYS-SEV-005`

### Driver Warning Manager

`COMP-WRN-001` is the primary architecture element for:

- `SYS-WRN-001`
- `SYS-WRN-002`
- `SYS-WRN-003`
- `SYS-WRN-004`
- `SYS-WRN-005`

### Diagnostic Event Manager

`COMP-EVT-001` is the primary architecture element for:

- `SYS-EVT-001`
- `SYS-EVT-002`
- `SYS-EVT-003`
- `SYS-EVT-004`
- `SYS-EVT-005`
- `SYS-EVT-006`
- `SYS-EVT-007`

### Configuration Manager

`COMP-CFG-001` is the primary architecture element for:

- `SYS-CFG-001`
- `SYS-CFG-002`
- `SYS-CFG-003`
- `SYS-CFG-004`
- `SYS-CFG-005`

---

## 12. Cross-Component Requirement Relationships

Primary allocation does not mean that a requirement can only affect one architecture element.

Some requirements depend on interactions between multiple elements.

Examples include:

| Requirement | Primary Element | Supporting Element |
|---|---|---|
| `SYS-VAL-006` | `COMP-VAL-001` | `COMP-MON-001` |
| `SYS-DIAG-004` | `COMP-DIAG-001` | `COMP-MON-001` |
| `SYS-DIAG-005` | `COMP-DIAG-001` | `COMP-MON-001` |
| `SYS-SEV-004` | `COMP-SEV-001` | `COMP-CFG-001` |
| `SYS-WRN-001` | `COMP-WRN-001` | `COMP-SEV-001` |
| `SYS-EVT-005` | `COMP-EVT-001` | `COMP-SEV-001` |
| `SYS-CFG-005` | `COMP-CFG-001` | Multiple processing elements |

These relationships are important for requirements traceability and later verification.

The structured traceability register will be maintained in `requirements/requirements.xlsx`.

---

## 13. Architectural Constraints

The VehicleGuard V1 architecture is subject to the following constraints.

### 13.1 Diagnostic-Only Responsibility

VehicleGuard does not directly control vehicle actuators.

The system observes vehicle information and generates diagnostic outputs.

### 13.2 Simulated Vehicle Environment

Vehicle data used by the prototype is generated by a simulator.

The prototype does not claim direct integration with a production vehicle network.

### 13.3 Configurable Demonstration Values

Thresholds used during prototype operation are demonstration configuration values.

They must not be presented as universally valid production automotive limits.

### 13.4 Invalid Data Separation

Invalid input data must remain distinguishable from abnormal vehicle operating conditions throughout diagnostic processing.

### 13.5 Requirement Traceability

Architecture behaviour should remain traceable to the system requirements defined in `03-system-requirements.md`.

### 13.6 Verification Support

Architecture elements should expose sufficient observable behaviour to allow requirement-based verification through the prototype.

---

## 14. Architecture Decisions

The following architecture decisions have been made for VehicleGuard V1.

### AD-001 - Sequential Diagnostic Processing

Vehicle data passes through defined processing stages rather than allowing every function to independently interpret raw input data.

**Reason**

This provides a clear separation between input reception, validation, monitoring, diagnostics, severity classification, and output generation.

### AD-002 - Validation Before Monitoring

Input validation is performed before diagnostic monitoring.

**Reason**

This prevents invalid data from being incorrectly interpreted as a real abnormal vehicle condition.

### AD-003 - Separate Severity Classification

Severity classification is separated from abnormal condition detection.

**Reason**

Detection determines what condition exists, while severity classification determines its significance.

Keeping these responsibilities separate improves traceability and allows severity criteria to be changed independently.

### AD-004 - Separate Driver and Diagnostic Outputs

Driver warning generation and diagnostic event generation are represented by separate architecture elements.

**Reason**

The two outputs serve different stakeholders and contain different levels of information.

Driver information should remain understandable without requiring interpretation of technical diagnostic data.

Diagnostic events may contain more detailed technical information.

### AD-005 - Centralized Configuration Responsibility

Configuration management is represented as a separate architecture responsibility.

**Reason**

Supported ranges, thresholds, and severity criteria should remain separate from the core diagnostic processing logic and should be consistently available to the functions that require them.

---

## 15. Architecture and Prototype Relationship

The VehicleGuard prototype will implement the responsibilities defined by this architecture.

However, architecture elements do not require a strict one-to-one relationship with Python files or classes.

For example:

```text
Architecture

COMP-DIAG-001
Diagnostic Engine

        |
        v

Prototype Implementation

one module
or
multiple functions/classes
```

The implementation structure may evolve as long as the defined architectural responsibilities and interfaces remain satisfied.

This distinction prevents software implementation choices from silently redefining the system architecture.

---

## 16. Current Limitations

The current architecture represents VehicleGuard V1 and intentionally excludes several production automotive concerns.

The architecture does not currently define:

- production CAN communication;
- AUTOSAR integration;
- ECU deployment;
- real sensor acquisition;
- functional safety mechanisms;
- cybersecurity mechanisms;
- persistent production diagnostic storage;
- cloud connectivity;
- remote diagnostics;
- production HMI implementation;
- vehicle actuator control;
- timing guarantees for real-time embedded execution.

These areas may be relevant to a production automotive system but are outside the current VehicleGuard V1 scope.

They should not be added to the architecture without a defined engineering need and corresponding project change.

---

## 17. Architecture Traceability

The architecture forms the next level of the VehicleGuard traceability chain:

```text
Stakeholder Need
        |
        v
System Requirement
        |
        v
Architecture Element
        |
        v
Implementation
        |
        v
Test Case
        |
        v
Verification Evidence
```

Architecture element identifiers such as `COMP-VAL-001` and `COMP-DIAG-001` will be referenced by later interface, implementation, and verification documentation.

This makes it possible to determine both:

- which architecture element is responsible for a requirement;
- which requirements justify the existence of an architecture element.

---

## 18. Architecture Baseline Status

The architecture defined in this document represents the initial VehicleGuard V1 system architecture.

The current architecture status is:

`Draft - Under Engineering Review`

The architecture will be reviewed during:

- detailed interface definition;
- prototype implementation;
- verification planning;
- risk analysis;
- requirements traceability review.

A significant architecture change should be evaluated for its impact on:

- system requirements;
- interfaces;
- implementation;
- test cases;
- project risks;
- requirements traceability.

Once the architecture and interfaces have been reviewed for consistency with the system requirements, the initial architecture baseline may be established.
