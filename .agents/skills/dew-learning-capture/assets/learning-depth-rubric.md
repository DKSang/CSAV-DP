# Learning Depth Rubric

## Shallow

The lesson only says what was done.

Example:
- I created ingestion.

## Medium

The lesson explains why it was done.

Example:
- I used batch ingestion because the source freshness requirement did not require streaming.

## Deep

The lesson connects decision, trade-off, evidence, and future reuse.

Example:
- I chose snapshot ingestion because the source did not provide reliable incremental cursor. This increased storage/reprocessing cost but made replay simpler. Next time I should validate whether the source has update timestamps before committing to snapshot.
