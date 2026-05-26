# Ingestion Design Template

```markdown
---
title: "{Project Name} Ingestion Design"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "3-solutioning"
stepsCompleted: []
decisionGates:
  GATE-16-ingestion-pattern:
    status: pending
  GATE-17-batch-vs-streaming:
    status: pending
  GATE-ingestion-snapshot-incremental:
    status: pending
  GATE-11-schema-evolution:
    status: pending
evidence: []
assumptions: []
caveats: []
---

# Ingestion Design: {Project Name}

## 0. Document Purpose

This document defines how validated/caveated sources are ingested into the approved storage design.

It covers:
- source extraction pattern
- batch vs streaming
- snapshot vs incremental
- frequency
- schema evolution
- failure handling
- idempotency
- replay/backfill
- logging/evidence requirements

## 1. Input Context

| Input | Path | Status | Notes |
|---|---|---|---|
| Data Architecture | | Loaded/Missing | |
| Storage Design | | Loaded/Missing | |
| Source-to-Storage Mapping | | Loaded/Missing | |
| Source Validation Report | | Loaded/Missing | |
| Source Contract Tests | | Loaded/Missing | |
| Evidence Index | | Loaded/Missing | |

## 2. Architecture and Storage Carryover

### Architecture Pattern

### Storage Targets

### Caveats

| Caveat ID | Area | Description | Ingestion Impact |
|---|---|---|---|

## 3. Source Ingestion Summary

| Source ID | Source Name | Source Type | Access Pattern | Target | Recommended Ingestion Pattern |
|---|---|---|---|---|---|
| SRC-001 | | API/File/DB | | | |

## 4. Ingestion Pattern Decision

Options:

A. Pull API  
B. File download / file drop  
C. Database query/export  
D. CDC  
E. Stream/event ingestion  
F. Manual upload  

Selected by source:

## 5. Batch vs Streaming Decision

Options:

A. Batch  
B. Micro-batch  
C. Streaming  
D. Event-driven  
E. Manual/on-demand  

Selected:

Rationale:

## 6. Snapshot vs Incremental Decision

Options:

A. Full snapshot  
B. Incremental by timestamp  
C. Incremental by cursor/token  
D. Append-only events  
E. Manual versioned files  
F. Hybrid  

Selected by source:

## 7. Ingestion Frequency

| Source ID | Required Freshness | Source Freshness | Ingestion Frequency | Caveat |
|---|---|---|---|---|
| SRC-001 | | | | |

## 8. Schema Evolution Strategy

Options:

A. Strict schema contract  
B. Schema snapshot + drift detection  
C. Flexible rescued fields  
D. Manual review on change  
E. Source-specific strategy  

Selected by source:

## 9. Idempotency and Deduplication

### Idempotency Key

### Natural Key / Business Key

### File/API response uniqueness

### Duplicate handling

## 10. Failure Handling

### Retry

### Backoff

### Dead-letter / quarantine

### Partial load handling

### Alerting

### Manual recovery

## 11. Replay and Backfill

### Replay Strategy

### Backfill Strategy

### Raw Dependency

### Limitations

## 12. Logging and Evidence

Required logs:
- ingestion run log
- source access log
- schema snapshot
- row count summary
- error/quarantine report
- DQ precheck report

## 13. Source-Specific Ingestion Plans

## SRC-001 — {Source Name}

### Source Type

### Access Pattern

### Target Raw/Bronze Location

### Ingestion Pattern

### Frequency

### Snapshot/Incremental Strategy

### Required Metadata

### Schema Evolution Strategy

### Failure Handling

### Idempotency

### Replay/Backfill

### Caveats

## 14. Handoff to Transformation Design

Transformation must know:
- raw/bronze target
- metadata fields
- schema caveats
- source grain
- ingestion frequency
- idempotency/deduplication assumptions
- DQ precheck results