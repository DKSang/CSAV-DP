# Step 02 — Load Model and Source Context

## Mandatory Rules

- Load model, transformation, source, KPI, and trust context.
- Do not create generic DQ rules without target.

## Task

Extract DQ-relevant context.

## Extract

From model spec:
- datasets
- fields
- keys
- grain
- KPI mapping

From transformation design:
- transformation rules
- business rules
- grain changes
- caveats

From source validation:
- source DQ risks
- field coverage
- schema risks
- freshness risks

From PRD:
- trust expectation
- consumers
- serving mode

## Update

Update:
- data-quality-rules.md
- dq-rule-catalog.md

## Continue checkpoint

Ask:

`[C] Continue to DQ rule discovery`
