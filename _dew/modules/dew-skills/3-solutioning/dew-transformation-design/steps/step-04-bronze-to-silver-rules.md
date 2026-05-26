# Step 04 — Bronze to Silver Rules

## Mandatory Rules

- Bronze to Silver rules must be source-specific.
- Do not apply KPI-specific aggregation too early unless approved.
- Metadata preservation must follow storage design.
- DQ handoff must be explicit.

## Task

Define Bronze → Silver transformation rules.

## For each source

Record:

| Rule ID | Source | Input Bronze | Output Silver | Rule Type | Description | Required? |
|---|---|---|---|---|---|---|

Rule types:
- rename
- cast
- standardize
- clean
- deduplicate
- filter
- derive
- join reference
- validate
- quarantine

## Required sections

For each Silver output:
- purpose
- grain
- input Bronze dataset
- output fields
- metadata fields
- transformation rules
- DQ handoff
- caveats

## Update documents

Update:
- transformation-design.md
- business-rule-catalog.md if business rules exist

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-storage-ingestion-context
  - step-03-grain-transformation-gate
  - step-04-bronze-to-silver-rules
```

## Continue checkpoint

Ask:

`[C] Continue to Silver to Gold rules`
