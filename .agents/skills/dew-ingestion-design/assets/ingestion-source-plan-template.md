### `assets/ingestion-source-plan-template.md`

```markdown
# Ingestion Source Plan Template

```markdown
# Ingestion Source Plan

## Source

Source ID:

Source Name:

Validation Status:

## Access

Access method:

Access evidence:

## Target

Raw/Bronze target:

Schema snapshot target:

Quarantine target:

## Pattern

Ingestion pattern:

Batch/streaming:

Snapshot/incremental:

Frequency:

## Metadata

Required metadata fields:

## Schema Evolution

Strategy:

Drift detection:

Breaking change behavior:

## Failure Handling

Retry:

Backoff:

Dead-letter/quarantine:

Manual intervention:

## Idempotency

Idempotency key:

Deduplication logic:

## Replay / Backfill

Replay possible?

Backfill possible?

Requirements:

## Evidence to Produce During Implementation

- run log
- row count summary
- schema snapshot
- access log
- error report