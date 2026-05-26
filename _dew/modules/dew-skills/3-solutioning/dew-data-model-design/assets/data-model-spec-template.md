# Data Model Spec Template

```markdown
---
title: "{Project Name} Data Model Spec"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "3-solutioning"
stepsCompleted: []
decisionGates:
  GATE-24-modeling-grain:
    status: pending
  GATE-history-scd:
    status: pending
evidence: []
assumptions: []
caveats: []
---

# Data Model Spec: {Project Name}

## 0. Document Purpose

This document defines Silver and Gold model specifications.

It includes:
- model grain
- fields
- keys
- dimensions
- facts
- bridge tables
- history/SCD handling
- KPI mapping
- caveats

## 1. Input Context

| Input | Path | Status | Notes |
|---|---|---|---|
| Transformation Design | | Loaded/Missing | |
| Business Rule Catalog | | Loaded/Missing | |
| KPI Feasibility | | Loaded/Missing | |
| Data Product PRD | | Loaded/Missing | |
| Source Validation | | Loaded/Missing | |

## 2. Model Summary

| Model | Layer | Type | Grain | Consumer | Status |
|---|---|---|---|---|---|
| silver_x | Silver | Conformed table | | | proposed |
| gold_y | Gold | Fact/Mart | | | proposed |

## 3. Silver Models

## Model: silver_{name}

### Purpose

### Grain

One row represents:

### Input Dataset(s)

### Primary Key / Natural Key

### Fields

| Field | Type | Description | Source | Required? | DQ Rule |
|---|---|---|---|---|---|
| | | | | Yes/No | |

### Business Rules Applied

### Caveats

## 4. Gold Models

## Model: gold_{name}

### Purpose

### Consumer

### KPI(s)

### Grain

One row represents:

### Model Type

- fact table
- dimension table
- aggregate mart
- wide reporting table
- bridge table
- snapshot table

### Input Dataset(s)

### Keys

### Fields

| Field | Type | Description | Source/Rule | Related KPI | Required? |
|---|---|---|---|---|---|
| | | | | | |

### KPI Mapping

| KPI ID | KPI Name | Gold Field | Formula Rule | Feasibility Status |
|---|---|---|---|---|

### Caveats

## 5. Dimensions

| Dimension | Grain | Key | Purpose | Source |
|---|---|---|---|---|

## 6. Facts / Metrics

| Fact / Metric | Grain | Additive? | Formula | Related KPI |
|---|---|---|---|---|

## 7. Bridge Tables

| Bridge | Left Grain | Right Grain | Purpose | Caveat |
|---|---|---|---|---|

## 8. History / SCD Handling

| Entity | History Needed? | SCD Type | Reason | Caveat |
|---|---|---|---|---|

## 9. Open Questions

## 10. Handoff to DQ Design

DQ design must create rules for:
- primary keys
- required fields
- grain uniqueness
- accepted ranges
- referential integrity
- KPI plausibility
- bridge table consistency
```
