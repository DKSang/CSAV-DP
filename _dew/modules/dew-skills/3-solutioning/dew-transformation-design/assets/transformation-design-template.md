# Transformation Design Template

```markdown
---
title: "{Project Name} Transformation Design"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "3-solutioning"
stepsCompleted: []
decisionGates:
  GATE-19-transformation-rule:
    status: pending
  GATE-transformation-grain:
    status: pending
evidence: []
assumptions: []
caveats: []
---

# Transformation Design: {Project Name}

## 0. Document Purpose

This document defines transformation rules from raw/bronze data into Silver and Gold datasets.

It covers:
- Bronze → Silver rules
- Silver → Gold rules
- grain changes
- business rules
- KPI computation logic
- caveats
- DQ handoff

## 1. Input Context

| Input | Path | Status | Notes |
|---|---|---|---|
| Storage Design | | Loaded/Missing | |
| Ingestion Design | | Loaded/Missing | |
| KPI Feasibility | | Loaded/Missing | |
| Source Validation | | Loaded/Missing | |
| Data Product PRD | | Loaded/Missing | |
| Evidence Index | | Loaded/Missing | |

## 2. Caveat Carryover

| Caveat ID | Source | Description | Transformation Impact |
|---|---|---|---|

## 3. Source-to-Transformation Summary

| Source ID | Bronze Target | Source Grain | Silver Target | Gold Dependency | Caveat |
|---|---|---|---|---|---|

## 4. Grain Transformation Design

| Input Dataset | Input Grain | Output Dataset | Output Grain | Transformation Type | Decision |
|---|---|---|---|---|---|
| | | | | Preserve/Aggregate/Join/Bridge/Explode/Filter | |

## 5. Bronze to Silver Rules

## Source / Dataset: {name}

### Input

### Output

### Purpose

### Transformation Rules

| Rule ID | Rule Type | Description | Required? | Caveat |
|---|---|---|---|---|
| TR-001 | rename/cast/clean/filter/deduplicate/join/derive | | Yes/No | |

### Metadata Rules

### Error / Quarantine Rules

### DQ Handoff

## 6. Silver to Gold Rules

## Gold Dataset: {name}

### Purpose

### Consumer

### KPI(s)

### Grain

### Input Silver Dataset(s)

### Transformation Rules

| Rule ID | Rule Type | Description | Related KPI | Required? |
|---|---|---|---|---|
| TRG-001 | aggregate/join/calculate/filter/pivot | | KPI-001 | Yes |

### KPI Formula Mapping

| KPI ID | KPI Formula | Gold Field | Computation Rule |
|---|---|---|---|

### Caveats

## 7. Business Rule Catalog Link

See:

`business-rule-catalog.md`

## 8. DQ Rule Handoff

Transformation requires DQ checks for:
- input completeness
- schema conformity
- grain uniqueness
- valid ranges
- referential integrity
- KPI plausibility
- freshness
- business rule consistency

Detailed DQ design:

`dew-data-quality-design`

## 9. Open Questions

## 10. Handoff to Data Model Design

Data model design must use:
- final Silver outputs
- final Gold outputs
- approved grain decisions
- business rules
- KPI mapping
- caveats
```
