# Grain Transformation Rubric

## Preserve grain

Use when:
- output dataset should keep source grain
- no aggregation or bridge is needed
- downstream model expects same grain

Risk:
- may not match KPI grain

## Aggregate grain

Use when:
- KPI or serving layer needs coarser grain
- source grain is lower-level than target

Examples:
- station-hour → station-day
- transaction → customer-day
- ward-day → province-month

Risk:
- aggregation rules must be explicit

## Join / enrich grain

Use when:
- source needs dimension/context enrichment
- lookup/mapping is required

Risk:
- duplicate joins can change grain

## Bridge grain

Use when:
- source grain and target grain are different entities
- mapping table is needed

Examples:
- station → ward
- product → category
- device → location

Risk:
- bridge assumptions can dominate KPI meaning

## Explode grain

Use when:
- nested/list data must become row-level records

Risk:
- row counts increase
- duplicates possible

## Filter grain

Use when:
- only subset is relevant to KPI/product

Risk:
- filtering criteria must be auditable
