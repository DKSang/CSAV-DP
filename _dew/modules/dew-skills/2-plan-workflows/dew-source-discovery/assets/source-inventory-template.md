# Source Inventory Template

```markdown
---
title: "{Project Name} Source Inventory"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "2-plan-workflows"
decisionGates:
  GATE-07-source-access:
    status: pending
  GATE-08-source-trust:
    status: pending
evidence: []
assumptions: []
caveats:
  - "Sources listed here are candidates only until validated."
---

# Source Inventory: {Project Name}

## 0. Important Status Note

Sources in this document are candidates.

They are not accepted as P1/P2 until source validation produces evidence.

## 1. Source Summary

| Source ID | Source Name | Type | Expected Role | Candidate Status |
|---|---|---|---|---|
| SRC-001 | | API/File/DB/Stream/Web/Manual | | Candidate |

## 2. Source Details

## SRC-001 — {Source Name}

### Source Type

Choose one:

- API
- File
- Database
- Stream/Event
- Web page
- Manual upload
- Third-party dataset
- Internal system
- Derived rule

### Provider / Owner

### Access Method

Examples:
- public API
- authenticated API
- CSV download
- database query
- GitHub raw file
- web scrape
- manual export
- event stream

### Expected Business Role

### Related KPI(s)

| KPI ID | Dependency Type | Notes |
|---|---|---|
| KPI-001 | Required/Optional/Reference | |

### Expected Grain

One record is expected to represent:

### Expected Freshness

### Expected Fields

| Field | Expected Meaning | Related KPI | Required? |
|---|---|---|---|
| | | | Yes/No |

### Current Status

Candidate

### Validation Required

- Access check
- Sample extraction
- Schema snapshot
- Grain confirmation
- Freshness observation
- Profiling/DQ notes
- Source trust decision

### Assumptions

- [ASSUMPTION] ...

### Open Questions

## 3. KPI to Source Coverage

| KPI ID | KPI Name | Candidate Source(s) | Coverage Status |
|---|---|---|---|
| KPI-001 | | | Unknown |

## 4. Next Workflow

Recommended next:

`dew-source-assessment`