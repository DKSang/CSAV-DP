# Dev HALT Rubric

Trigger HALT when:

## New dependency required

Examples:
- new library not approved
- new service needed
- new cloud resource needed
- new source credential needed

Recommended HALT:
`HALT-17 — Implementation Not Ready`

## Missing config/secrets/source path

Recommended HALT:
`HALT-17 — Implementation Not Ready`

## Story conflicts with design

Examples:
- story says KPI formula A but model design says formula B
- source path differs from ingestion design
- DQ severity conflicts with DQ policy

Recommended HALT:
Return to design or story revision.

## Validation fails repeatedly

If validation fails three times, stop and document:
- attempts
- error
- suspected cause
- required decision

## Evidence cannot be produced

Recommended HALT:
`HALT-18 — No Validation Evidence`
