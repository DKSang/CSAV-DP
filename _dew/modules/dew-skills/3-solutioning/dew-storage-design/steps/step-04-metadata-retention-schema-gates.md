# Step 04 — Metadata, Retention, and Schema Snapshot Gates

## Mandatory Rules

- Stop for user decisions.
- Metadata standard must match trust expectation.
- Raw retention must be explicit.
- Schema snapshot strategy must be explicit.
- If schema evolution direction is missing, trigger HALT-13.

## Gate 1 — Metadata Standard

Options:

A. Minimal metadata  
B. Operational metadata  
C. Full lineage metadata  
D. Custom project-specific metadata  

Ask user to choose.

## Gate 2 — Raw Retention

Options:

A. Keep all raw inputs  
B. Keep raw inputs for MVP period only  
C. Keep raw samples and schema snapshots only  
D. Keep raw externally and store references  
E. No raw retention with explicit caveat  

Ask user to choose.

## Gate 3 — Schema Snapshot Strategy

Options:

A. Snapshot schema every ingestion run  
B. Snapshot schema on source version/change  
C. Snapshot schema manually during validation only  
D. Use source contract tests and compare with baseline  
E. No schema snapshot with explicit caveat  

Ask user to choose.

## Record

Update:
- storage-design.md
- storage-decision-record.md
- .decision-log.md
- .learning-log.md if enabled

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-architecture-context
  - step-03-storage-layer-gate
  - step-04-metadata-retention-schema-gates