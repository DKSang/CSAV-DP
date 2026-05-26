# DataOps Runbook Template

```markdown
---
title: "{Project Name} DataOps Runbook"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "3-solutioning"
stepsCompleted: []
decisionGates:
  GATE-22-operational-readiness:
    status: pending
evidence: []
assumptions: []
caveats: []
---

# DataOps Runbook: {Project Name}

## 0. Document Purpose

This runbook defines how the data product is operated.

It covers:
- operational readiness
- run schedule
- monitoring
- alerting
- incident handling
- replay/backfill
- change process
- environments
- CI/CD handoff

## 1. Input Context

| Input | Path | Status |
|---|---|---|
| Storage Design | | |
| Ingestion Design | | |
| Transformation Design | | |
| Data Model Spec | | |
| DQ Rules | | |
| Serving Spec | | |
| Governance Review | | |

## 2. Operational Mode

Choose one:

A. Manual / learning mode  
B. Scheduled internal pipeline  
C. Monitored internal data product  
D. SLA-backed production pipeline  

Selected:

## 3. Run Schedule

| Pipeline / Asset | Frequency | Trigger | Owner | Notes |
|---|---|---|---|---|

## 4. Operational Dependencies

| Dependency | Type | Failure Impact | Mitigation |
|---|---|---|---|

## 5. Monitoring Summary

See:

`observability-plan.md`

## 6. Incident Handling

### Incident Types

- source access failure
- schema drift
- DQ failure
- freshness miss
- transformation failure
- serving failure
- security/access incident

### Incident Process

## 7. Replay / Backfill

## 8. Change Process

Change types:
- source schema change
- business rule change
- KPI definition change
- DQ rule change
- serving contract change
- access policy change

## 9. Environment Strategy

- local
- dev
- test
- prod
- cloud workspace
- notebook/runtime
- CI runner

## 10. CI/CD Handoff

## 11. Open Operational Risks

## 12. Handoff to Epics and Stories

Implementation stories must include:
- operational evidence
- DQ evidence
- logs
- runbook updates
- incident/backfill notes
```
