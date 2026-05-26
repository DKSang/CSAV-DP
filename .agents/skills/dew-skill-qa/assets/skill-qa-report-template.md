# Skill QA Report Template

```markdown
---
title: "DEW Skill QA Report"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "4-implementation"
stepsCompleted: []
decisionGates:
  GATE-31-skill-qa:
    status: pending
findings: []
---

# DEW Skill QA Report

## 0. Purpose

This report audits the DEW skill pack before release.

## 1. QA Scope

| Area | Included? | Notes |
|---|---|---|
| module.yaml | Yes/No | |
| module-help.csv | Yes/No | |
| skill folders | Yes/No | |
| SKILL.md files | Yes/No | |
| customize.toml files | Yes/No | |
| assets | Yes/No | |
| steps | Yes/No | |
| checklists | Yes/No | |
| cross-skill links | Yes/No | |
| HALT/gate consistency | Yes/No | |

## 2. Summary

Recommended decision:

- pass
- pass-with-caveats
- request-fixes
- block-release

## 3. Module Structure Review

## 4. Module Catalog Review

See:

`module-catalog-audit.md`

## 5. Skill Structure Review

| Skill | Folder Exists | SKILL.md | customize.toml | assets | steps | checklist | Status |
|---|---|---|---|---|---|---|---|

## 6. Cross-Link Review

| Skill | preceded-by | followed-by | Valid? | Finding |
|---|---|---|---|---|

## 7. Gate / HALT Review

| Gate / HALT | Used In | Defined? | Consistent? | Finding |
|---|---|---|---|---|

## 8. Findings

| Severity | Area | Finding | Required Action |
|---|---|---|---|
| Critical/High/Medium/Low | | | |

## 9. Final QA Gate

A. QA passed  
B. QA passed with caveats  
C. Fix required before package  
D. Block release  

User decision:

## 10. Handoff to Package Release
```
