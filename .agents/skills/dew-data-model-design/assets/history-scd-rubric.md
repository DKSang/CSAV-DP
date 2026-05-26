# History and SCD Rubric

## No history

Use when:
- entity attributes are static or not important historically
- MVP does not require point-in-time analysis

## Type 1 overwrite

Use when:
- only current state matters
- historical changes are not important

## Type 2 history

Use when:
- historical attribute changes affect analysis
- point-in-time correctness matters

## Snapshot history

Use when:
- periodic state is useful
- source provides snapshots
- changes are hard to track event-by-event

## Event history

Use when:
- source provides events
- full sequence matters

## Rule

Do not choose SCD/history pattern silently.

History handling affects storage, transformation, DQ, and serving semantics.
