# Incident and Backfill Rubric

## Incident process must define

- how incident is detected
- who is notified
- how severity is classified
- how data serving is paused or caveated
- how fix is verified
- how incident is documented

## Backfill process must define

- source of truth for historical data
- raw data availability
- date range selection
- idempotency behavior
- downstream recomputation
- DQ validation after backfill
- serving refresh after backfill

## Severity

### Critical

Data product is misleading, unsafe, or unavailable for primary consumer.

### High

Core KPI/source/DQ/freshness issue affects decisions.

### Medium

Partial issue with caveated impact.

### Low

Minor documentation or non-critical issue.
