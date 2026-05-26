# Ingestion Design Checklist

## Required inputs

- [ ] Data architecture loaded.
- [ ] Storage design loaded.
- [ ] Source-to-storage mapping loaded.
- [ ] Source validation report loaded.
- [ ] Source contract test results loaded or caveat recorded.
- [ ] Evidence index loaded or caveat recorded.

## Ingestion pattern

- [ ] Ingestion pattern selected by source.
- [ ] Batch vs streaming decision made.
- [ ] Snapshot vs incremental decision made.
- [ ] Frequency mapped to freshness requirement.
- [ ] User approved key ingestion decisions.

## Source-specific plans

- [ ] Each P1 source has ingestion source plan.
- [ ] Raw/Bronze target specified.
- [ ] Metadata requirements specified.
- [ ] Schema snapshot target specified.
- [ ] Quarantine/error handling specified.
- [ ] Idempotency strategy specified.
- [ ] Replay/backfill strategy specified.

## Schema and failure handling

- [ ] Schema evolution strategy selected.
- [ ] Failure handling strategy defined.
- [ ] Retry/backoff behavior defined if relevant.
- [ ] Partial load behavior defined.
- [ ] Evidence/logging requirements defined.

## Finalization

- [ ] ingestion-design.md completed.
- [ ] ingestion-decision-record.md completed.
- [ ] ingestion-source-plan.md completed.
- [ ] Decision log updated.
- [ ] Learning log updated if learning mode is enabled.
- [ ] No unresolved HALT-12 remains.
- [ ] No unresolved HALT-13 remains.