# Metadata Standard Rubric

## Minimal metadata

Use when:
- project is learning/portfolio
- source count is low
- traceability needs are simple

Typical fields:
- dew_source_system
- dew_source_file_path
- dew_processing_timestamp
- dew_dq_status

## Operational metadata

Use when:
- ingestion and transformation runs must be traced
- reruns/backfills are expected

Typical fields:
- dew_source_system
- dew_source_file_path
- dew_ingestion_timestamp
- dew_ingestion_run_id
- dew_silver_timestamp
- dew_silver_run_id
- dew_dq_status

## Full lineage metadata

Use when:
- multiple sources
- multiple consumers
- auditability matters
- production-like workflow

Typical fields:
- source system
- source object
- source file path
- source extraction timestamp
- ingestion run ID
- transform run ID
- batch ID
- schema version
- DQ status
- record hash
- lineage ID

## Rule

Metadata choice must match trust expectation.

Exploratory projects can use minimal metadata.

Internal decision-support should use at least operational metadata for key tables.

Trusted shared products need stronger lineage and DQ metadata.