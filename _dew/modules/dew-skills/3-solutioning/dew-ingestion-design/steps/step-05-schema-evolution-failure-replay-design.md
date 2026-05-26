# Step 05 — Schema Evolution, Failure Handling, Idempotency, Replay

## Mandatory Rules

- Schema evolution must be explicit.
- Failure handling must be explicit.
- Idempotency must be explicit.
- Replay/backfill must be explicit.
- If schema evolution is undefined, trigger HALT-13.

## Schema Evolution Gate

Options:

A. Strict schema contract  
B. Schema snapshot + drift detection  
C. Flexible rescued fields  
D. Manual review on change  
E. Source-specific strategy  

Ask user to choose.

## Failure handling

Define:
- retry
- backoff
- partial load behavior
- quarantine/dead-letter
- manual intervention
- alerting/logging

## Idempotency

Define:
- idempotency key
- duplicate detection
- rerun behavior
- run ID expectations

## Replay / Backfill

Define:
- whether raw data is retained
- whether source can be re-pulled
- backfill method
- replay limitations

## Update

Update:
- ingestion-design.md
- ingestion-decision-record.md
- ingestion-source-plan.md

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-source-and-storage-context
  - step-03-ingestion-pattern-gate
  - step-04-snapshot-incremental-and-frequency-gates
  - step-05-schema-evolution-failure-replay-design
decisionGates:
  GATE-11-schema-evolution:
    status: approved / approved-with-caveats