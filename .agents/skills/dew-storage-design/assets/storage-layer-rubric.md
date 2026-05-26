# Storage Layer Rubric

## Minimal raw + curated outputs

Use when:
- project is small
- learning/portfolio scope
- source count is low
- speed matters more than full medallion rigor

Risk:
- weaker governance
- harder lineage if not disciplined

## Bronze/Silver/Gold medallion

Use when:
- source validation evidence exists
- transformations need clear separation
- DQ and lineage matter
- project is internal decision-support or more serious

Risk:
- more files/tables
- more design overhead

## Warehouse staging + marts

Use when:
- structured data dominates
- SQL analytics is primary
- serving is BI or data mart

Risk:
- less flexible for raw files/semi-structured data

## Lakehouse tables with medallion convention

Use when:
- cloud/lakehouse architecture is chosen
- scalable storage is needed
- bronze/silver/gold should be table-based

Risk:
- higher operational complexity

## Local-first files with promotion path

Use when:
- project needs fast local iteration
- later deployment may target Fabric/cloud/lakehouse
- DuckDB/Parquet/dbt-style development is preferred

Risk:
- local/cloud drift if conventions are weak