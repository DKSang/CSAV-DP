# DQ Severity Rubric

## Critical

Use when:
- failure invalidates primary KPI
- failure creates unsafe/misleading decision
- privacy/security issue exists
- grain uniqueness fails for Gold model

Default action:
- fail pipeline
- do not serve data

## High

Use when:
- required field missing
- key uniqueness fails
- critical range invalid
- source freshness misses requirement

Default action:
- fail or quarantine
- user review required

## Medium

Use when:
- non-critical field has quality issue
- sample coverage incomplete
- partial missingness affects caveat

Default action:
- warn and document caveat

## Low

Use when:
- documentation/naming/minor issue
- does not affect KPI or decision

Default action:
- log only
