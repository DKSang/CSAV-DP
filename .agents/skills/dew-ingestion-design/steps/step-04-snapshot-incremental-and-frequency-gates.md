# Step 04 — Snapshot, Incremental, and Frequency Gates

## Mandatory Rules

- Stop for user decisions.
- Snapshot/incremental choice must be source-specific.
- Ingestion frequency must be tied to freshness requirement.
- Do not assume streaming unless freshness requires it.

## Gate 1 — Batch vs Streaming

Options:

A. Batch  
B. Micro-batch  
C. Streaming  
D. Event-driven  
E. Manual/on-demand  

Ask user to choose.

## Gate 2 — Snapshot vs Incremental

Options:

A. Full snapshot  
B. Incremental by timestamp  
C. Incremental by cursor/token  
D. Append-only events  
E. Manual versioned files  
F. Hybrid  

Ask user to choose per source if needed.

## Gate 3 — Frequency

For each source:

| Source ID | Required Freshness | Observed Freshness | Recommended Frequency | User Decision |
|---|---|---|---|---|

## Record

Update:
- ingestion-design.md
- ingestion-decision-record.md
- ingestion-source-plan.md
- .decision-log.md

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-source-and-storage-context
  - step-03-ingestion-pattern-gate
  - step-04-snapshot-incremental-and-frequency-gates