# Code Review Report Template

```markdown
---
title: "Code Review — {Story ID}"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "4-implementation"
storyId: "{Story ID}"
---

# Code Review: {Story ID} — {Story Title}

## 1. Review Summary

Recommended decision:

- approve
- approve-with-caveats
- request-changes
- block

## 2. Story Reviewed

Story path:

Status:

## 3. Files Reviewed

| Path | Purpose | Finding |
|---|---|---|

## 4. Acceptance Criteria Audit

| AC | Status | Evidence | Notes |
|---|---|---|---|
| AC-1 | pass/fail/partial | | |

## 5. Data Engineering Review

| Layer | Status | Finding |
|---|---|---|
| Source access | | |
| Ingestion | | |
| Storage | | |
| Transformation | | |
| Model grain | | |
| DQ | | |
| Serving | | |
| Governance/Security | | |
| DataOps | | |

## 6. Evidence Review

| Required Evidence | Present? | Path | Valid? |
|---|---|---|---|
| | Yes/No | | Yes/No |

## 7. Findings

| Severity | Finding | Impact | Required Action |
|---|---|---|---|
| Critical/High/Medium/Low | | | |

## 8. Decision

A. Approve  
B. Approve with caveats  
C. Request changes  
D. Block  

User/reviewer decision:

## 9. Required Follow-up
```
