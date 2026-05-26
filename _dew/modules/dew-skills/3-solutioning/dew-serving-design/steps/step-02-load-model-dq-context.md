# Step 02 — Load Model and DQ Context

## Mandatory Rules

- Load Gold models, KPI mapping, DQ rules, and caveats before serving mode.
- Do not expose metrics without contract context.

## Task

Extract serving context.

## Extract

From PRD:
- consumers
- decisions supported
- product type
- trust expectation

From model spec:
- Gold models
- dimensions
- facts
- grain
- KPI mapping

From DQ design:
- DQ rules
- DQ gate policy
- critical caveats

From transformation:
- business rules
- metric calculation caveats

## Update

Update:
- serving-data-product-spec.md
- metric-serving-contract.md
- trust-and-limitations-statement.md

## Continue checkpoint

Ask:

`[C] Continue to serving mode gate`
