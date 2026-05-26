# KPI Feasibility Status Rubric

## Status: Verified on sample

Use when:
- required fields are available in sample
- field meanings are plausible
- grain is compatible or transformation is clear
- sample computation was executed
- sample output was reviewed
- caveats are documented

This does not mean production-ready.

## Status: Feasible with caveats

Use when:
- KPI can likely be computed
- some limitations exist
- user approves caveated continuation
- downstream artifacts will preserve caveats

Examples:
- sample is small
- source freshness is uncertain
- field meaning needs owner confirmation
- source coverage is partial

## Status: Hypothesis only

Use when:
- KPI is defined
- but field availability or sample computation has not been proven

This status blocks architecture for primary KPI unless user explicitly approves caveated continuation.

## Status: Deferred

Use when:
- KPI is useful
- but not needed for MVP
- or source is not currently available
- or validation cost is too high for now

## Status: Rejected

Use when:
- KPI cannot be computed from available data
- formula is not meaningful
- grain is incompatible
- required source does not exist
- user decides not to pursue it