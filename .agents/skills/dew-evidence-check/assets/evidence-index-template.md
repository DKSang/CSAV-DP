---
title: "Validation Evidence Index"
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
workflow: dew
---

# Validation Evidence Index

This file indexes all validation evidence produced by the DEW workflow.

A phase cannot be marked complete unless required evidence is listed here.

## Evidence Table

| Evidence ID | Phase | Type | Description | Path | Status | Related Decision |
|---|---|---|---|---|---|---|
| EVD-0001 | | | | | missing/available/validated/stale/invalid | |

## Evidence Types

- api-call-log
- source-sample
- schema-snapshot
- profiling-report
- kpi-sample-query
- kpi-sample-output
- notebook
- source-contract-test
- data-quality-test
- pipeline-test
- review-report
- user-decision
- caveat-approval

## Evidence Entry Template

```markdown
## EVD-{number} — {Evidence Name}

Date:
Phase:
Type:
Description:
Path:
Status:
Produced by:
Related source:
Related KPI:
Related decision:
Validation summary:
Caveats: