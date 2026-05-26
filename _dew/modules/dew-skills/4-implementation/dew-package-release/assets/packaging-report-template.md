# Packaging Report Template

```markdown
---
title: "DEW Package Release Report"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "4-implementation"
stepsCompleted: []
decisionGates:
  GATE-32-package-release:
    status: pending
packageVersion:
  status: pending
---

# DEW Package Release Report

## 0. Purpose

This report prepares the DEW skill module for release.

## 1. QA Input

| QA Artifact | Path | Status | Notes |
|---|---|---|---|
| Skill QA Report | | | |
| Module Catalog Audit | | | |

## 2. Package Scope

### Included

### Excluded

### Optional

## 3. Package Version

Version:

Version type:
- initial
- patch
- minor
- major
- pre-release

## 4. Release Caveats

| Caveat | Severity | Accepted? | Notes |
|---|---|---|---|

## 5. Package Contents

| Path | Included? | Notes |
|---|---|---|
| src/dew-skills/module.yaml | | |
| src/dew-skills/module-help.csv | | |
| src/dew-skills/1-analysis | | |
| src/dew-skills/2-plan-workflows | | |
| src/dew-skills/3-solutioning | | |
| src/dew-skills/4-implementation | | |

## 6. Release Risks

| Risk | Severity | Mitigation |
|---|---|---|

## 7. Release Package Checklist

See:

`release-package-checklist.md`

## 8. Final Release Notes

See:

`final-release-notes.md`

## 9. Package Release Gate

A. Package release approved  
B. Package release approved with caveats  
C. Fix required before package release  
D. Block package release  

User decision:

## 10. Handoff to Installation Guide
```
