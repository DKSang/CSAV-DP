# Release Readiness Report Template

```markdown
---
title: "{Project Name} Release Readiness Report"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "4-implementation"
stepsCompleted: []
decisionGates:
  GATE-27-release-readiness:
    status: pending
evidence: []
assumptions: []
caveats: []
releaseDecision:
  status: pending
---

# Release Readiness Report: {Project Name}

## 0. Document Purpose

This report decides whether the data product is ready for release.

## 1. Release Candidate Summary

### Product Name

### Release Version

### Release Type

A. Learning / demo release  
B. Internal MVP release  
C. Internal decision-support release  
D. Trusted shared release  
E. Production release  

Selected:

## 2. Input Readiness

| Input | Status | Notes |
|---|---|---|
| E2E Validation | pass/pass-with-caveats/fail/missing | |
| Final Evidence Review | complete/caveated/incomplete | |
| Sprint Status | done/partial/blocked | |
| DQ Status | pass/caveated/fail | |
| Serving Status | ready/caveated/missing | |
| Trust Statement | ready/caveated/missing | |
| Governance/Security | ready/caveated/missing | |
| DataOps Runbook | ready/caveated/missing | |
| Learning Capture | complete/incomplete | |

## 3. Release Scope

### Included

### Excluded

### Deferred

## 4. Release Caveats

| Caveat ID | Area | Description | User-Facing? | Release Impact |
|---|---|---|---|---|

## 5. Release Risks

| Risk ID | Severity | Risk | Mitigation | Release Impact |
|---|---|---|---|---|

## 6. Rollback / Recovery

### Rollback Trigger

### Recovery Path

### Backfill / Replay Notes

### Communication Notes

## 7. Release Checklist

See:

`release-checklist.md`

## 8. Release Notes

See:

`release-notes.md`

## 9. Release Readiness Gate

A. Release  
B. Release with caveats  
C. Do not release; return to implementation  
D. Do not release; return to design  
E. Archive as learning/demo only  

User decision:

## 10. Handoff to Documentation / Learning / Pattern Extraction

Next:

`dew-project-documentation`
```
