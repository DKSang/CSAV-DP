# E2E Path Rubric

An end-to-end validation path should cover the complete product lifecycle.

## Required lifecycle stages

1. Source access
2. Raw/Bronze ingestion
3. Schema snapshot
4. Silver transformation
5. Gold model / KPI computation
6. Data quality checks
7. Serving output
8. Trust and limitations statement
9. Operational logs / observability

## Pass

Use when every required stage has evidence and no blocking caveat remains.

## Pass with caveats

Use when output is usable, but known limitations are documented and accepted.

## Partial

Use when only some lifecycle stages were validated.

## Fail

Use when primary data path, KPI, DQ, or serving output is invalid.

## Not run

Use when no E2E validation command/procedure/evidence exists.
