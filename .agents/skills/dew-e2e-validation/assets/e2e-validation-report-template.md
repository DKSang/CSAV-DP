# E2E Validation Report Template

```markdown
---
title: "{Project Name} E2E Validation Report"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "4-implementation"
stepsCompleted: []
decisionGates:
  GATE-25-e2e-validation:
    status: pending
evidence: []
assumptions: []
caveats: []
---

# E2E Validation Report: {Project Name}

## 0. Document Purpose

This report validates the implemented data product end-to-end.

It checks the full path:

Source → Raw/Bronze → Silver → Gold → DQ → Serving → Trust/Limitations → Operational Evidence

## 1. Input Artifacts

| Artifact | Path | Loaded? | Notes |
|---|---|---|---|
| Sprint Status | | Yes/No | |
| Story Validation Reports | | Yes/No | |
| Completion Notes | | Yes/No | |
| Evidence Index | | Yes/No | |
| DataOps Runbook | | Yes/No | |
| Serving Spec | | Yes/No | |
| DQ Rules | | Yes/No | |
| Data Model Spec | | Yes/No | |

## 2. E2E Validation Path

| Stage | Expected Output | Evidence | Status |
|---|---|---|---|
| Source access | | | pass/fail/partial |
| Bronze ingestion | | | pass/fail/partial |
| Schema snapshot | | | pass/fail/partial |
| Silver transformation | | | pass/fail/partial |
| Gold model / KPI | | | pass/fail/partial |
| DQ rules | | | pass/fail/partial |
| Serving output | | | pass/fail/partial |
| Trust/limitations | | | pass/fail/partial |
| Observability/logs | | | pass/fail/partial |

## 3. Story Completion Coverage

| Story ID | Status | Validation Report | Completion Notes | Evidence |
|---|---|---|---|---|
| 1.1 | done | | | |

## 4. E2E Test / Review Summary

### Validation Method

A. Run E2E command  
B. Review existing story evidence  
C. Manual walkthrough  
D. Hybrid  

Selected:

### Command / Procedure

```bash
# command or manual procedure
```

### Result

* pass
* pass-with-caveats
* fail
* partial
* not-run

## 5. Data Output Validation

| Output | Expected | Observed | Evidence | Status |
| ------ | -------- | -------- | -------- | ------ |

## 6. KPI / Metric Validation

| KPI | Gold Field | Expected Grain | Observed Output | Status |
| --- | ---------- | -------------- | --------------- | ------ |

## 7. DQ Validation

| DQ Rule | Expected Action | Evidence | Result |
| ------- | --------------- | -------- | ------ |

## 8. Serving Validation

| Serving Asset | Expected | Observed | Evidence | Status |
| ------------- | -------- | -------- | -------- | ------ |

## 9. Operational Validation

| Requirement | Expected | Evidence | Status |
| ----------- | -------- | -------- | ------ |

## 10. Findings

| Severity                 | Finding | Impact | Required Action |
| ------------------------ | ------- | ------ | --------------- |
| Critical/High/Medium/Low |         |        |                 |

## 11. E2E Validation Gate

A. E2E pass
B. E2E pass with caveats
C. Return to implementation
D. Block release

User decision:

## 12. Handoff to Final Evidence Review
```
