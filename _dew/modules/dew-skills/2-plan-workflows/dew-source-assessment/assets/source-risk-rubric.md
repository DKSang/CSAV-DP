# Source Risk Rubric

## Access Risk

High when:
- authentication unknown
- source may be blocked
- manual access only
- rate limit or licensing unclear

Medium when:
- access method known but untested

Low when:
- access method is simple and likely testable

## Field Coverage Risk

High when:
- required KPI fields are not clearly present

Medium when:
- fields may exist but names/meaning are uncertain

Low when:
- fields are documented and map cleanly to KPI needs

## Grain Risk

High when:
- source grain is unknown or likely incompatible

Medium when:
- source requires aggregation, bridge, or mapping

Low when:
- source grain matches KPI/product grain

## Freshness Risk

High when:
- update frequency is unknown or slower than product requirement

Medium when:
- likely sufficient but not verified

Low when:
- source update pattern is documented and fits requirement

## Schema Stability Risk

High when:
- no contract, docs, versioning, or stable structure

Medium when:
- schema stable historically but no formal contract

Low when:
- schema is documented/versioned/contracted

## Privacy/Security Risk

High when:
- PII/sensitive/regulated data may exist

Medium when:
- internal or restricted data exists

Low when:
- public non-sensitive data