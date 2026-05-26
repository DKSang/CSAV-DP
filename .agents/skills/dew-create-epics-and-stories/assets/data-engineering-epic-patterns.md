# Data Engineering Epic Patterns

## EPIC-01 — Foundation and Project Setup

Typical stories:
- initialize repo/project structure
- create config management
- create evidence folder structure
- create logging conventions
- create README/run guide

## EPIC-02 — Source Access and Bronze Ingestion

Typical stories:
- implement source access
- implement raw download/API response capture
- implement Bronze write
- capture schema snapshot
- capture ingestion run log

## EPIC-03 — Source Contract and DQ Prechecks

Typical stories:
- implement required field checks
- implement schema drift check
- implement row count check
- implement freshness check

## EPIC-04 — Silver Transformation

Typical stories:
- implement source-specific cleaning
- cast/rename fields
- standardize units/codes
- deduplicate
- add metadata
- quarantine invalid records

## EPIC-05 — Gold Modeling and KPI Computation

Typical stories:
- implement Gold fact/mart
- implement KPI formula
- implement bridge table
- implement aggregate table
- validate sample KPI output

## EPIC-06 — Data Quality Evidence

Typical stories:
- implement DQ rule catalog
- implement critical DQ tests
- write DQ result artifacts
- fail/quarantine/warn policy

## EPIC-07 — Serving Data Product

Typical stories:
- create dashboard/mart/API/report
- expose metric contract
- add freshness display
- show limitations/caveats

## EPIC-08 — Governance Documentation

Typical stories:
- document lineage
- document access control
- document trust statement
- document owners/stewards

## EPIC-09 — DataOps and Observability

Typical stories:
- implement run logs
- create observability plan artifacts
- create incident/backfill runbook
- add CI/test commands
