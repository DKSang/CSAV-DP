# Data Product PRD Validation Rubric

## Consumer and Decision Readiness

- Does the PRD identify data consumers?
- Does it identify the decisions supported?
- Does each KPI map to a decision?
- Does it define the data product type?

## Data Product Readiness

- Does it state product grain?
- Does it state freshness requirement?
- Does it state trust expectation?
- Does it identify candidate sources?

## Evidence Discipline

- Does it avoid marking KPI feasibility as verified?
- Does it avoid marking sources as accepted without validation?
- Does it list evidence required before architecture?
- Does it clearly label assumptions and caveats?

## Failure Conditions

The PRD fails if:
- it jumps to architecture
- it claims source/KPI feasibility without evidence
- trust expectation is missing
- grain is missing with no pending decision
- freshness is missing with no pending decision
- consumers are vague
- KPIs do not map to decisions