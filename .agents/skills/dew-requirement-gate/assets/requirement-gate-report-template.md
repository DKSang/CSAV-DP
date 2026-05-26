# Requirement Gate Report Template

```markdown
---
title: "{Project Name} Requirement Gate Report"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "2-plan-workflows"
stepsCompleted: []
decisionGates:
  GATE-05-trust-expectation:
    status: pending
  GATE-04-kpi-grain:
    status: pending
  GATE-10-source-freshness:
    status: pending
  GATE-12-architecture-readiness:
    status: pending
evidence: []
assumptions: []
caveats: []
architectureReadiness:
  status: pending
---

# Requirement Gate Report: {Project Name}

## 0. Document Purpose

This report decides whether the project is ready to proceed to data architecture.

This document does not create architecture.

It reviews:
- business readiness
- KPI readiness
- source readiness
- trust expectation
- grain
- freshness
- caveats
- MVP scope
- architecture readiness

## 1. Input Artifacts

| Artifact | Path | Loaded? | Status | Notes |
|---|---|---|---|---|
| Project Brief | | Yes/No | | |
| Business Discovery | | Yes/No | | |
| Data Product PRD | | Yes/No | | |
| KPI Catalog | | Yes/No | | |
| KPI Feasibility Report | | Yes/No | | |
| Source Inventory | | Yes/No | | |
| Source Scorecard | | Yes/No | | |
| Source Validation Report | | Yes/No | | |
| Evidence Index | | Yes/No | | |
| Decision Log | | Yes/No | | |
| Learning Log | | Yes/No | | |

## 2. Executive Readiness Summary

| Area | Status | Blocker? | Notes |
|---|---|---|---|
| Business decision | Ready / Caveated / Blocked | Yes/No | |
| Data consumer | Ready / Caveated / Blocked | Yes/No | |
| KPI feasibility | Ready / Caveated / Blocked | Yes/No | |
| Source validation | Ready / Caveated / Blocked | Yes/No | |
| Trust expectation | Ready / Caveated / Blocked | Yes/No | |
| Grain | Ready / Caveated / Blocked | Yes/No | |
| Freshness | Ready / Caveated / Blocked | Yes/No | |
| Evidence index | Ready / Caveated / Blocked | Yes/No | |
| Caveats accepted | Ready / Caveated / Blocked | Yes/No | |

## 3. Business Readiness

### Data Consumer

### Decision Supported

### Data Product Type

### Status

- Ready
- Ready with caveats
- Blocked

### Notes

## 4. KPI Readiness

| KPI ID | KPI Name | Priority | Feasibility Status | Evidence | Architecture Impact |
|---|---|---|---|---|---|
| KPI-001 | | Primary/Secondary | | | |

### KPI Blockers

- ...

### KPI Caveats

- ...

### KPI Decision Needed

A. Accept KPI readiness  
B. Accept KPI readiness with caveats  
C. Return to KPI validation  
D. Defer KPI  
E. Reduce MVP scope  

## 5. Source Readiness

| Source ID | Source Name | Related KPI | Validation Status | Evidence | Architecture Impact |
|---|---|---|---|---|---|
| SRC-001 | | | P1/P2/Exploration/Rejected/Blocked | | |

### Source Blockers

- ...

### Source Caveats

- ...

### Source Decision Needed

A. Accept source readiness  
B. Accept source readiness with caveats  
C. Return to source validation  
D. Defer source  
E. Reduce MVP scope  

## 6. Trust Expectation Gate

Choose one:

A. Exploratory only  
B. Internal decision-support with documented limitations  
C. Trusted shared product with quality checks  
D. Production-grade with contracts and monitoring  

Selected:

Rationale:

Evidence / context:

Downstream impact:
- architecture:
- DQ:
- serving:
- monitoring:
- documentation:

## 7. Grain Gate

### Product Grain

One row / observation represents:

### KPI Grain(s)

| KPI ID | Grain | Status | Notes |
|---|---|---|---|

### Source Grain(s)

| Source ID | Grain | Compatibility | Notes |
|---|---|---|---|

### Grain Decision

A. Grain is consistent enough for architecture  
B. Grain is consistent with caveats  
C. Requires bridge/mapping design  
D. Return to KPI/source validation  
E. Reduce MVP scope  

Selected:

## 8. Freshness Gate

### Required Freshness

### Observed Source Freshness

| Source ID | Required | Observed | Status | Notes |
|---|---|---|---|---|

### Freshness Decision

A. Freshness is sufficient  
B. Freshness is acceptable with caveats  
C. Freshness is insufficient; redesign requirement  
D. Return to source validation  
E. Reduce MVP scope  

Selected:

## 9. Caveat Register

| Caveat ID | Area | Description | Severity | Accepted? | Downstream Impact |
|---|---|---|---|---|---|
| CAV-001 | KPI/Source/Trust/Grain/Freshness | | High/Medium/Low | Yes/No | |

## 10. Architecture Readiness Matrix

| Requirement | Status | Evidence | Decision |
|---|---|---|---|
| Primary KPI feasible or caveated | | | |
| P1 source validated or caveated | | | |
| Trust expectation approved | | | |
| Grain approved | | | |
| Freshness approved | | | |
| Caveats accepted | | | |
| Evidence indexed | | | |

## 11. Final Requirement Gate Decision

Choose one:

A. Proceed to architecture  
B. Proceed to architecture with caveats  
C. Return to KPI validation  
D. Return to source validation  
E. Reduce MVP scope  

Selected:

Reason:

## 12. Decision Log Entries

## 13. Learning Notes

## 14. Next Workflow

If approved:

`dew-data-architecture`

If not approved:

- `dew-kpi-feasibility`
- `dew-kpi-prototype`
- `dew-kpi-validation-review`
- `dew-source-validation`
- `dew-source-access-check`
- `dew-source-sampler`
- `dew-source-contract-test`