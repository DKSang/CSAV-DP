# Observability Plan Template

```markdown
# Observability Plan

## Purpose

Define what the project must monitor.

## Monitoring Table

| Monitor ID | Area | Signal | Threshold | Severity | Action |
|---|---|---|---|---|---|
| MON-001 | Source access | API call success | fail | High | alert/retry |
| MON-002 | Freshness | latest data date | > expected lag | High | warn/fail |
| MON-003 | DQ | critical DQ fail | > 0 | Critical | fail pipeline |
| MON-004 | Row count | row count anomaly | threshold | Medium | warn |
| MON-005 | Schema | schema drift | changed | High | block/review |

## Log Requirements

Each run should log:
- run ID
- start/end time
- source
- row counts
- schema version
- DQ result
- errors
- output paths

## Alerting

| Alert | Trigger | Recipient | Action |
|---|---|---|---|

## Evidence Outputs

| Evidence | Path | Produced By |
|---|---|---|
| ingestion run log | | |
| DQ result | | |
| freshness report | | |
| schema drift report | | |
```
