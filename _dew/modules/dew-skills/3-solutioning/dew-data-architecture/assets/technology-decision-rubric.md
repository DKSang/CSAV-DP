# Technology Decision Rubric

Technology choices must be justified by requirements and evidence.

Do not choose technology because it is trendy.

## Decision criteria

Evaluate each technology choice using:

- project scope
- user skill level
- data volume
- data variety
- freshness requirement
- source access pattern
- transformation complexity
- serving needs
- governance/security posture
- cost
- operational complexity
- portability
- local development speed
- deployment target
- team maintainability

## Required format

Every technology decision must include:

- selected option
- alternatives considered
- why selected
- why alternatives rejected
- evidence used
- risk
- reversibility
- revisit trigger

## Common decision areas

### Local development

Options:
- Python scripts
- notebooks
- DuckDB
- dbt-duckdb
- local Spark
- containerized dev environment

### Storage

Options:
- local files
- Parquet
- Delta
- warehouse tables
- lakehouse tables
- object storage

### Compute

Options:
- pandas
- Polars
- DuckDB
- Spark
- SQL warehouse
- cloud notebook runtime

### Orchestration

Options:
- manual run
- Makefile/task runner
- Airflow/Dagster/Prefect
- Fabric Data Pipeline
- cloud-native scheduler

### Transformation

Options:
- SQL
- dbt
- Python
- Spark
- hybrid

### Data quality

Options:
- custom tests
- dbt tests
- Great Expectations/Soda
- lightweight Python checks
- source contract tests

### Serving

Options:
- dashboard
- Gold mart
- API
- notebook/report
- web app feature
- ML feature table

## Reversibility guide

### Easy to reverse

- local folder structure
- naming conventions
- lightweight scripts
- dashboard layout

### Medium to reverse

- storage format
- transformation framework
- orchestration tool

### Hard to reverse

- cloud platform
- data model grain
- source integration pattern
- security model
- public API contract