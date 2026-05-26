# Step 02 — Load Design Artifacts

## Mandatory Rules

- Load all designs before creating epics.
- Do not invent implementation scope.
- Carry caveats forward.

## Task

Extract implementation context.

## Extract

From storage:
- layers
- source-to-storage mapping
- metadata requirements

From ingestion:
- source plans
- schema evolution
- idempotency
- replay/backfill

From transformation:
- Bronze→Silver rules
- Silver→Gold rules
- business rules

From model:
- Silver/Gold models
- KPI-to-model mapping
- bridge/history needs

From DQ:
- DQ rules
- severity/action
- evidence requirements

From serving:
- serving mode
- metric contract
- trust statement

From governance:
- access/privacy/lineage requirements

From DataOps:
- monitoring
- runbook
- operational mode

## Update

Update:
- epics.md
- story-map.md

## Continue checkpoint

Ask:

`[C] Continue to build epic map`
