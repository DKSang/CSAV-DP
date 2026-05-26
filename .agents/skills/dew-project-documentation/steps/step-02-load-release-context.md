# Step 02 — Load Release Context

## Mandatory Rules

- Load release, serving, model, DQ, governance, and DataOps context.
- Do not invent documentation content.

## Task

Extract documentation context.

## Extract

From release:
- release type
- included scope
- excluded scope
- caveats
- risks

From serving:
- users
- outputs
- metrics
- freshness
- trust limitations

From model:
- datasets
- fields
- grain
- KPI mapping

From DQ:
- rules
- severity
- actions
- evidence

From DataOps:
- run schedule
- monitoring
- run commands
- incident/backfill notes

## Update

Update all documentation files.

## Continue checkpoint

Ask:

`[C] Continue to create user-facing docs`
