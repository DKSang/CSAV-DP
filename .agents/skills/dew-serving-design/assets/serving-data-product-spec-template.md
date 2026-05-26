# Serving Data Product Spec Template

```markdown
---
title: "{Project Name} Serving Data Product Spec"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "3-solutioning"
stepsCompleted: []
decisionGates:
  GATE-20-serving-mode:
    status: pending
  GATE-serving-trust-limitations:
    status: pending
evidence: []
assumptions: []
caveats: []
---

# Serving Data Product Spec: {Project Name}

## 0. Document Purpose

This document defines how the data product is served to users or downstream systems.

It covers:
- serving mode
- data consumer experience
- metric contracts
- trust statement
- known limitations
- freshness
- access expectations
- feedback loop

## 1. Input Context

| Input | Path | Status | Notes |
|---|---|---|---|
| Data Product PRD | | Loaded/Missing | |
| Data Model Spec | | Loaded/Missing | |
| KPI to Model Mapping | | Loaded/Missing | |
| DQ Rules | | Loaded/Missing | |
| Business Rule Catalog | | Loaded/Missing | |
| Evidence Index | | Loaded/Missing | |

## 2. Data Product Summary

### Product Name

### Product Type

### Consumers

| Consumer ID | Consumer | Role | Decision Supported | Serving Need |
|---|---|---|---|---|

### Decisions Supported

## 3. Serving Mode

Choose one or more:

A. Dashboard  
B. Gold data mart  
C. API  
D. Notebook/report  
E. Web app feature  
F. ML feature table  
G. Reverse ETL output  

Selected:

## 4. Served Assets

| Asset ID | Asset Name | Type | Source Model | Consumer | Status |
|---|---|---|---|---|---|
| SERV-001 | | dashboard/mart/API/report | gold_x | | proposed |

## 5. Metric Serving Contracts

See:

`metric-serving-contract.md`

## 6. Freshness and Availability

| Asset | Expected Freshness | Source Freshness | Ingestion Frequency | Caveat |
|---|---|---|---|---|

## 7. Trust and Limitations Statement

See:

`trust-and-limitations-statement.md`

## 8. Consumer Experience

### User Journey

### Filters / Dimensions

### Drill-downs

### Alerts / Recommendations

### Export / API Access

### Documentation Shown to User

## 9. Self-Service Policy

A. No self-service; curated outputs only  
B. Limited self-service with documented metrics  
C. Full semantic/metric layer  
D. API-first contract  

Selected:

## 10. Feedback Loop

How consumers report:
- metric issue
- missing data
- freshness problem
- wrong business logic
- new KPI request

## 11. Handoff to Governance/Security

Governance must review:
- access control
- privacy posture
- metric exposure
- documentation ownership
- auditability
```
