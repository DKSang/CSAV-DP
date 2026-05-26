# Source Contract Test Template

```markdown
---
title: "Source Contract Test — {Source ID}"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
relatedSource: "{Source ID}"
evidenceType: "source-contract-test"
---

# Source Contract Test: {Source ID} — {Source Name}

## Purpose

Define minimal expectations this source must satisfy before it can support architecture and ingestion design.

## Test Scope

- sample-level
- schema-level
- field-level
- freshness-level
- grain-level

## Tests

| Test ID | Test Name | Expectation | Required? | Related KPI |
|---|---|---|---|---|
| SCT-001 | Required fields exist | Fields X, Y, Z exist | Yes | KPI-001 |
| SCT-002 | Row count non-zero | Row count > 0 | Yes | |
| SCT-003 | Time field exists | Time/date column exists | Yes/No | |
| SCT-004 | Grain keys exist | Grain keys present | Yes/No | |
| SCT-005 | Critical fields not null | Null rate below threshold | Yes/No | |
| SCT-006 | Schema drift check | Current schema compared to snapshot | Yes | |

## Caveats

## Expected Result Status

- pass
- pass-with-caveats
- fail
- blocked
- not-run