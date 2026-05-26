# Serving Mode Rubric

## Dashboard

Use when:
- users need visual monitoring
- metrics are consumed by analysts/business users
- interaction/filtering is important

Risk:
- users may over-trust metrics if limitations are hidden

## Gold data mart

Use when:
- analysts need queryable curated tables
- BI or downstream analysis consumes data
- semantic flexibility matters

Risk:
- requires documentation and metric contract

## API

Use when:
- application or external system needs programmatic access
- stable contract matters
- latency/availability requirements exist

Risk:
- versioning and access control become important

## Notebook/report

Use when:
- analysis is exploratory
- output is periodic or narrative
- trust level is lower

Risk:
- weak operationalization

## Web app feature

Use when:
- data product is embedded in end-user workflow
- recommendations/advisory are shown in app
- user experience matters

Risk:
- stronger product, security, and explanation requirements

## ML feature table

Use when:
- output feeds ML models
- point-in-time correctness matters
- training/serving consistency matters

Risk:
- feature leakage and historical correctness

## Reverse ETL

Use when:
- metrics/actions are sent back to operational systems
- downstream actions depend on data product

Risk:
- errors can affect operational users directly
