# Bronze Silver Gold Rule Guide

## Bronze

Purpose:
- preserve ingested source data
- keep raw or near-raw state
- enable replay/debugging
- preserve source metadata

Typical rules:
- minimal parsing
- add ingestion metadata
- store raw response/file reference
- capture schema snapshot
- quarantine unreadable records

Avoid:
- business logic
- heavy cleansing
- KPI computation

## Silver

Purpose:
- clean and standardize data
- conform fields
- enforce basic quality
- prepare for modeling

Typical rules:
- cast types
- rename fields
- standardize units
- deduplicate
- validate required fields
- normalize codes
- join reference data
- apply source-level quality checks

Avoid:
- hiding major business assumptions
- mixing multiple KPI-specific aggregations too early

## Gold

Purpose:
- serve KPI/data product needs
- match consumer grain
- provide metrics or marts
- support dashboard/API/reporting

Typical rules:
- aggregate
- compute KPI
- join dimensions
- apply business rules
- expose friendly column names
- document caveats

Avoid:
- using unverified KPI logic
- changing grain silently
- mixing unrelated consumers in one table without reason
