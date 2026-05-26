# Source Type Guide

## API

Use when data is fetched through HTTP or SDK.

Validation evidence:
- API call log
- sample response
- schema snapshot
- rate limit/auth notes

## File

Use when data comes from CSV, JSON, Excel, Parquet, GeoJSON, etc.

Validation evidence:
- downloaded file
- file metadata
- schema/header snapshot
- sample rows

## Database

Use when data comes from OLTP, OLAP, warehouse, lakehouse, or queryable system.

Validation evidence:
- connection/query log
- schema/table description
- sample query result

## Stream/Event

Use when data is unbounded or event-driven.

Validation evidence:
- event sample
- topic/stream schema
- ordering/time semantics
- retention/TTL notes

## Web Page

Use when data is embedded in public pages.

Validation evidence:
- page URL
- extraction method
- HTML/table sample
- update pattern notes

## Manual Upload

Use when user or operator supplies files manually.

Validation evidence:
- sample file
- upload process
- owner
- expected schedule

## Third-party Dataset

Use when data comes from external curated datasets.

Validation evidence:
- dataset metadata
- license/terms
- schema
- sample
- update frequency

## Derived Rule

Use when a source is a business rule, threshold, ontology, or mapping.

Validation evidence:
- rule definition
- owner
- version/change log
- test cases