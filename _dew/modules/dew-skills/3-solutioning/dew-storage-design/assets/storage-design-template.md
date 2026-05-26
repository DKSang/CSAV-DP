# Storage Design Template

```markdown
---
title: "{Project Name} Storage Design"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "3-solutioning"
stepsCompleted: []
decisionGates:
  GATE-15-storage-layer:
    status: pending
  GATE-storage-metadata-standard:
    status: pending
  GATE-storage-retention:
    status: pending
evidence: []
assumptions: []
caveats: []
---

# Storage Design: {Project Name}

## 0. Document Purpose

This document defines the storage design for the project.

It translates architecture-level storage intent into concrete storage layers, metadata standards, retention expectations, schema snapshot strategy, and source-to-storage mapping.

## 1. Input Context

| Input | Path | Status | Notes |
|---|---|---|---|
| Data Architecture | | Loaded/Missing | |
| Architecture Decisions | | Loaded/Missing | |
| Architecture Caveats | | Loaded/Missing | |
| Source Validation | | Loaded/Missing | |
| KPI Feasibility | | Loaded/Missing | |
| Evidence Index | | Loaded/Missing | |

## 2. Architecture Carryover

### Selected Architecture Pattern

### Storage Technology Direction

### Caveats Carried Forward

| Caveat ID | Area | Description | Storage Impact |
|---|---|---|---|

## 3. Storage Layer Strategy

Choose one:

A. Minimal raw + curated outputs  
B. Bronze/Silver/Gold medallion  
C. Warehouse staging + marts  
D. Lakehouse tables with medallion convention  
E. Local-first files with promotion path  

Selected:

Rationale:

## 4. Layer Responsibilities

| Layer | Purpose | Data Shape | Mutability | Consumers | Owner |
|---|---|---|---|---|---|
| Raw / Bronze | | | Append-only/Mutable | | |
| Silver | | | | | |
| Gold | | | | | |
| Evidence | | | | | |
| Metadata | | | | | |
| Quarantine / Error | | | | | |

## 5. Raw / Bronze Design

### Purpose

### Accepted Data Forms

- original API response
- original file
- extracted rows
- raw JSON
- raw CSV
- raw Parquet
- manual upload copy

### Raw Retention

Choose one:

A. Keep all raw inputs  
B. Keep raw inputs for MVP period only  
C. Keep raw samples and schema snapshots only  
D. Keep raw externally and store references  
E. No raw retention, with explicit caveat  

Selected:

### Raw Immutability

### Source File / API Response Preservation

### Caveats

## 6. Silver Design

### Purpose

### Cleaning / Standardization Scope

### Conformance Scope

### Metadata Required

### DQ Expectations

### Caveats

## 7. Gold Design

### Purpose

### KPI / Serving Alignment

### Grain

### Consumers

### Caveats

## 8. Metadata Standard

Required metadata fields:

| Field | Layer | Purpose | Required? |
|---|---|---|---|
| dew_source_system | Bronze/Silver/Gold | Source ID | Yes |
| dew_source_file_path | Bronze/Silver | Raw source traceability | Yes |
| dew_ingestion_timestamp | Bronze | Ingestion time | Optional/Required |
| dew_silver_timestamp | Silver | Silver processing time | Optional/Required |
| dew_silver_run_id | Silver | Processing run ID | Optional/Required |
| dew_dq_status | Silver/Gold | DQ result status | Optional/Required |

Selected metadata standard:

## 9. Schema Snapshot Strategy

| Source ID | Schema Snapshot Location | Frequency | Drift Handling |
|---|---|---|---|
| SRC-001 | | | |

## 10. Partitioning / Organization

### Folder / Table Organization

### Partitioning Direction

### Naming Convention

### Environment Separation

## 11. Source-to-Storage Mapping

| Source ID | Source Name | Raw/Bronze Target | Silver Target | Gold Dependency | Caveat |
|---|---|---|---|---|---|
| SRC-001 | | | | | |

## 12. Evidence and Audit Storage

### Evidence Artifacts

### Validation Results

### Decision Logs

### Learning Logs

## 13. Open Questions

## 14. Handoff to Ingestion Design

Key storage decisions ingestion must follow:

- target raw/bronze location:
- metadata requirements:
- schema snapshot expectations:
- quarantine/error location:
- retention rules:
- idempotency implications: