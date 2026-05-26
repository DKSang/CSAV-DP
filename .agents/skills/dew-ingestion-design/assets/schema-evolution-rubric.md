# Schema Evolution Rubric

## Strict schema contract

Use when:
- source schema must not change silently
- production trust is high
- breaking changes should fail fast

Behavior:
- fail ingestion on unexpected schema
- require review before accepting changes

## Schema snapshot + drift detection

Use when:
- source is external
- no formal contract exists
- changes must be detected and logged

Behavior:
- capture schema snapshot
- compare to previous snapshot
- warn or fail depending on severity

## Flexible rescued fields

Use when:
- semi-structured data may contain extra fields
- you want to avoid hard failure for non-critical changes

Behavior:
- expected fields validated
- unexpected fields captured separately

## Manual review on change

Use when:
- source updates are infrequent
- project is learning/MVP
- manual approval is acceptable

Behavior:
- detect change
- stop or warn
- user reviews before proceeding