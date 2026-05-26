# Data Lifecycle Architecture Guide

DEW architecture follows the data engineering lifecycle.

## 1. Generation / Source Systems

Architecture must record:
- source type
- access method
- ownership/provider
- grain
- freshness
- schema stability
- source trust status
- caveats

Do not design ingestion until source validation is clear.

## 2. Storage

Architecture should decide at high level:
- raw/bronze retention
- silver conformance purpose
- gold serving purpose
- metadata expectations
- evidence retention
- file/table direction

Detailed storage design belongs to `dew-storage-design`.

## 3. Ingestion

Architecture should decide at high level:
- batch vs streaming direction
- snapshot vs incremental direction
- replay/backfill expectation
- schema drift direction
- failure handling expectation

Detailed ingestion design belongs to `dew-ingestion-design`.

## 4. Transformation

Architecture should decide at high level:
- where KPI computation happens
- grain transformation points
- business rule ownership
- bridge/mapping needs
- DQ responsibilities

Detailed transformation design belongs to `dew-transformation-design`.

## 5. Serving

Architecture should decide at high level:
- serving mode
- consumer
- freshness
- trust statement
- limitations

Detailed serving design belongs to `dew-serving-design`.

## 6. Undercurrents

Architecture must not forget:
- security
- privacy
- data management
- DataOps
- orchestration
- software engineering
- observability
- cost / FinOps