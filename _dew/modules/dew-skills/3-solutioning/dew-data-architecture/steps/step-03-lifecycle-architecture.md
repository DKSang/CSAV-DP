
# Step 03 — Lifecycle Architecture

## Mandatory Rules

- Use data engineering lifecycle structure.
- Do not over-design detailed storage/ingestion/transformation here.
- Architecture-level decisions only.
- Detailed designs belong to later skills.

## Task

Create lifecycle-level architecture.

## Lifecycle sections

### 1. Generation / Source Systems

For each P1/P2 source, summarize:
- source type
- role
- access method
- grain
- freshness
- schema stability
- validation status
- caveats

### 2. Storage

Define high-level intent:
- raw/bronze purpose
- silver purpose
- gold purpose
- metadata expectations
- evidence retention

Do not finalize detailed storage layout yet.

### 3. Ingestion

Define high-level intent:
- batch/streaming direction
- snapshot/incremental direction
- replay/backfill expectation
- schema drift direction
- failure handling expectation

Do not finalize detailed ingestion spec yet.

### 4. Transformation

Define high-level intent:
- KPI computation layer
- grain transformation
- bridge/mapping needs
- conformance logic
- DQ responsibility

### 5. Serving

Define high-level intent:
- serving mode
- consumer
- freshness
- trust statement
- limitations

### 6. Undercurrents

Summarize:
- security
- privacy
- data management
- DataOps
- orchestration
- software engineering
- observability
- cost

## Update documents

Update `data-architecture.md`.

## Update frontmatter

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-validated-context
  - step-03-lifecycle-architecture