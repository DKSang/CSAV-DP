# Dependency Mapping Rubric

## Hard dependency

A story cannot start until another story is done.

Examples:
- Silver transform depends on Bronze ingestion.
- Gold KPI depends on Silver model.
- Serving dashboard depends on Gold model.
- DQ rule execution depends on target dataset.

## Soft dependency

A story can start with caveats, but must be revisited.

Examples:
- documentation can start before final code paths exist.
- dashboard wireframe can start before final Gold model.

## Evidence dependency

A story depends on validation evidence.

Examples:
- KPI computation story needs KPI feasibility evidence.
- source ingestion story needs source access evidence.
- DQ implementation story needs DQ rule catalog.

## User decision dependency

A story depends on an approved decision gate.

Examples:
- serving story depends on serving mode decision.
- privacy/access story depends on privacy posture decision.
