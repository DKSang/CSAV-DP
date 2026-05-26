# Step 02 — Load Storage and Ingestion Context

## Mandatory Rules

- Load storage targets and ingestion plans before transformation rules.
- Do not invent Bronze/Silver/Gold targets.
- Do not drop caveats.

## Task

Extract transformation-relevant context.

## Extract from storage design

- layer strategy
- Bronze targets
- Silver targets
- Gold expectations
- metadata requirements
- schema snapshot strategy
- quarantine targets

## Extract from ingestion design

- source ingestion pattern
- ingestion frequency
- schema evolution strategy
- idempotency assumptions
- replay/backfill limitations
- metadata fields

## Extract from KPI feasibility

- verified/caveated KPIs
- KPI formulas
- KPI grain
- required fields
- caveats

## Extract from source validation

- source grain
- source field coverage
- quality caveats
- freshness caveats

## Update documents

Update:
- transformation-design.md
- business-rule-catalog.md if known rules exist

## Update frontmatter

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-storage-ingestion-context
```

## Continue checkpoint

Ask:

`[C] Continue to grain transformation gate`
