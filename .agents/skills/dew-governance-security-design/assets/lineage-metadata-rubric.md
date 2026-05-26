# Lineage Metadata Rubric

## Minimal lineage

Use when:
- learning/portfolio project
- few sources
- low trust expectation

Minimum:
- source file/path
- source system
- run timestamp
- transformation note

## Operational lineage

Use when:
- internal decision-support
- recurring pipeline
- DQ evidence matters

Minimum:
- source system
- source object/file
- ingestion run ID
- transform run ID
- schema version
- DQ status
- evidence path

## Full audit lineage

Use when:
- trusted shared product
- compliance/auditability needed
- multiple consumers

Minimum:
- source version
- ingestion job/run
- transformation job/run
- DQ rules/results
- metric version
- access decision
- caveat version
- owner approval
