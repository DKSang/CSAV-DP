# Step 05 — Silver to Gold Rules

## Mandatory Rules

- Do not create Gold rule for unresolved KPI unless user approved caveat.
- KPI formula must map to Gold fields.
- Gold grain must be explicit.
- Caveats must be preserved.

## Task

Define Silver → Gold transformation rules.

## For each Gold output

Record:
- dataset name
- consumer
- KPI(s)
- grain
- input Silver datasets
- transformation rules
- KPI formula mapping
- caveats

## Required KPI mapping

| KPI ID | Formula | Input Fields | Gold Field | Rule ID | Feasibility Status |
|---|---|---|---|---|---|

## If KPI is not verified/caveated

Options:
A. Exclude KPI from Gold  
B. Include as caveated metric  
C. Return to KPI feasibility  
D. Replace KPI  

Ask user if primary KPI is affected.

## Update documents

Update:
- transformation-design.md
- business-rule-catalog.md
- transformation-decision-record.md if decisions occur

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-storage-ingestion-context
  - step-03-grain-transformation-gate
  - step-04-bronze-to-silver-rules
  - step-05-silver-to-gold-rules
```

## Continue checkpoint

Ask:

`[C] Continue to business rule gate`
