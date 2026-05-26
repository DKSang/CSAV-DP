# Step 02 — Load Source and Storage Context

## Mandatory Rules

- Load source validation and storage mapping before choosing ingestion patterns.
- Do not invent source access behavior.
- Do not invent storage targets.

## Task

Extract ingestion-relevant context.

## Extract from source validation

For each source:
- source ID
- source type
- access method
- validation status
- source grain
- freshness
- schema stability
- DQ risk
- caveats

## Extract from storage design

For each source:
- raw/bronze target
- schema snapshot target
- quarantine target
- metadata requirements
- retention rule

## Update documents

Update:
- ingestion-design.md
- ingestion-source-plan.md

## Update frontmatter

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-source-and-storage-context