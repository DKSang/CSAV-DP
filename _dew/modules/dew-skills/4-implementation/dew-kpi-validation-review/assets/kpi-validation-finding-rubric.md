# KPI Validation Finding Rubric

## High severity

Use when:
- required field is missing
- formula cannot be implemented
- grain is incompatible
- sample output is invalid
- KPI is primary and still hypothesis only
- evidence is missing

Impact:
- blocks architecture unless user approves caveated continuation or defers KPI

## Medium severity

Use when:
- field meaning is uncertain
- sample is too small
- source coverage is partial
- freshness is unknown
- output is plausible but not fully validated

Impact:
- can proceed with caveats if user approves

## Low severity

Use when:
- naming issue exists
- documentation needs clarification
- minor caveat exists
- evidence path needs indexing

Impact:
- does not block but must be documented