# Step 03 — DQ Rule Discovery

## Mandatory Rules

- Every DQ rule must link to dataset/field/key/KPI or source.
- Do not create vague rules like “check data quality”.
- Each critical dataset needs at least grain/key check.

## Task

Discover candidate DQ rules.

## Rule categories

- source-level
- ingestion/Bronze
- Silver
- Gold/KPI
- serving

## Required rule types

Consider:
- not_null
- unique
- accepted_range
- accepted_values
- referential_integrity
- freshness
- schema_contract
- row_count_anomaly
- duplicate_check
- valid_geography
- valid_time_window
- business_rule_consistency
- KPI_plausibility

## Required table

| Rule ID | Layer | Dataset | Field/Key | Rule Type | Related KPI | Reason |
|---|---|---|---|---|---|---|

## Update

Update:
- data-quality-rules.md
- dq-rule-catalog.md

## Continue checkpoint

Ask:

`[C] Continue to DQ rule gate`
