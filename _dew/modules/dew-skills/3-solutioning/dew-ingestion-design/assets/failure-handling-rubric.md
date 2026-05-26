# Failure Handling Rubric

## Retry

Use for:
- transient network errors
- temporary API failures
- database timeouts

## Backoff

Use for:
- rate-limited APIs
- overloaded sources

## Quarantine

Use for:
- malformed records
- invalid schema
- records failing critical DQ checks

## Dead-letter

Use for:
- event/message ingestion
- records that cannot be processed

## Partial load handling

Define whether partial loads:
- fail whole run
- load valid records and quarantine invalid records
- require manual approval

## Idempotency

Every ingestion design must explain:
- what happens if the same run is executed twice
- how duplicate files/API pages/records are handled
- how reruns are detected

## Replay / Backfill

Every ingestion design must explain:
- whether raw data is retained
- whether historical source data can be re-requested
- how to rerun ingestion safely