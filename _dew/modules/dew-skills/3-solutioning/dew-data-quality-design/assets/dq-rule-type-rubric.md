# DQ Rule Type Rubric

## not_null

Use for required fields.

## unique

Use for primary keys and grain checks.

## accepted_range

Use for numeric values with valid domain.

## accepted_values

Use for categorical fields.

## referential_integrity

Use when foreign key/dimension relationship must hold.

## freshness

Use when source/product freshness matters.

## schema_contract

Use for expected columns/types/schema drift.

## row_count_anomaly

Use to detect unexpected row volume changes.

## duplicate_check

Use when duplicate records affect metrics.

## valid_geography

Use for region/province/ward/station consistency.

## valid_time_window

Use for date/time range and completeness.

## business_rule_consistency

Use for domain-specific logic or KPI assumptions.

## KPI_plausibility

Use for final metric output sanity checks.
