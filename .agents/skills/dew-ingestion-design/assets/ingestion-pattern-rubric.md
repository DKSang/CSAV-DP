
# Ingestion Pattern Rubric

## Pull API

Use when:
- source provides HTTP API
- data can be requested periodically
- API response can be saved as raw evidence

Risks:
- rate limits
- schema drift
- auth changes
- pagination

## File download / file drop

Use when:
- source publishes CSV/JSON/Parquet/etc.
- file versioning is possible
- raw file can be retained

Risks:
- manual updates
- file format changes
- unclear freshness

## Database query/export

Use when:
- source is a database or warehouse
- query access is available
- data is structured

Risks:
- source load
- query permissions
- schema changes

## CDC

Use when:
- change-level capture is required
- source supports CDC
- freshness and auditability justify complexity

Risks:
- operational complexity
- ordering issues
- replay complexity

## Stream/event ingestion

Use when:
- source is event-driven
- low-latency is required
- data is unbounded

Risks:
- much higher complexity
- ordering and exactly-once semantics
- monitoring burden

## Manual upload

Use when:
- source is human-provided
- automation is not possible yet
- learning/MVP accepts manual process

Risks:
- inconsistent format
- late delivery
- weak operational reliability