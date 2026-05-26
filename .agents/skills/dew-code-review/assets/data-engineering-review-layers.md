# Data Engineering Review Layers

## Acceptance Auditor

Check:
- each AC
- implementation task completion
- validation approach
- story DoD

## Source/Schema Hunter

Check:
- source path/API matches design
- schema fields not invented
- source contract respected
- schema drift handling included

## Grain Auditor

Check:
- model/output grain matches design
- joins do not duplicate rows unexpectedly
- aggregation rules are explicit

## KPI Auditor

Check:
- KPI formula matches approved formula
- KPI fields map correctly
- output sample is plausible

## DQ Auditor

Check:
- required DQ rules implemented
- severity/action behavior respected
- DQ evidence exists

## Lineage/Metadata Auditor

Check:
- required metadata fields
- source traceability
- run IDs/timestamps
- evidence paths

## Operational Auditor

Check:
- logging
- idempotency
- failure handling
- replay/backfill notes
- run instructions

## Caveat Auditor

Check:
- caveats from story/design are preserved
- user-facing limitations not removed
