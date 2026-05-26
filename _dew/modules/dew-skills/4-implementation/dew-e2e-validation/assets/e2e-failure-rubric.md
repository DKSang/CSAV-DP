# E2E Failure Rubric

## Critical

Blocks release.

Examples:
- primary source cannot be accessed
- Bronze/Silver/Gold output missing
- primary KPI wrong or missing
- critical DQ rule fails
- serving output missing
- trust limitations missing for user-facing product

## High

Usually blocks release unless user explicitly accepts caveat.

Examples:
- partial source coverage
- freshness evidence missing
- schema snapshot missing
- DQ evidence incomplete

## Medium

Can release with caveat.

Examples:
- non-critical metric missing
- documentation incomplete
- minor operational evidence weak

## Low

Does not block.

Examples:
- naming issue
- formatting issue
- non-critical note
