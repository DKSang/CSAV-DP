# Architecture Pattern Rubric

## Local-first

Use when:
- project is learning/portfolio/internal prototype
- data volume is small to medium
- fast iteration matters
- local DuckDB/Python/dbt style workflow is useful
- cloud deployment can come later

Pros:
- fast feedback
- low cost
- easy experimentation
- good for learning

Cons:
- not production-grade by default
- limited built-in orchestration
- may need migration path to cloud/lakehouse

## Warehouse-first

Use when:
- structured analytics is the core use case
- sources fit relational modeling
- BI/dashboard is main serving layer
- team prefers SQL-centric development

Pros:
- strong analytics patterns
- mature governance and BI integration

Cons:
- less flexible for files/unstructured data
- may be costly at scale
- streaming and ML feature use cases may need extra components

## Lakehouse

Use when:
- data includes files, semi-structured data, large datasets
- bronze/silver/gold layering is needed
- batch and scalable transformations are expected
- future ML/AI workloads may appear

Pros:
- flexible storage
- supports medallion patterns
- scalable
- good for mixed workloads

Cons:
- more architecture complexity
- requires stronger governance
- may be overkill for small learning projects

## Hybrid

Use when:
- local-first development is desired
- cloud/lakehouse or warehouse is target deployment
- project needs fast iteration and production path

Pros:
- balances learning speed and deployment realism
- supports local validation and cloud implementation

Cons:
- requires clear environment boundaries
- more documentation needed
- potential drift between local and cloud

## Streaming-first

Use when:
- source is event-driven
- low latency is required
- data is unbounded
- freshness requirement cannot be met by batch

Pros:
- low latency
- event-native design

Cons:
- much more operational complexity
- harder debugging/replay
- not appropriate unless freshness requires it

## Application-integrated

Use when:
- data product is embedded in a web/app workflow
- serving layer is API or app feature
- operational UX matters

Pros:
- directly useful to end users
- supports action-oriented workflows

Cons:
- requires stronger API, auth, and product engineering discipline