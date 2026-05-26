# Step 04 — Source Sample and Schema Snapshot

## Mandatory Rules

- Do not assume schema.
- Do not assume required fields exist.
- Do not promote to P1 if sample or schema is missing.
- If evidence is missing, trigger `HALT-18 — No Validation Evidence`.

## Task

Capture or document source sample and schema snapshot.

## Required evidence

For each validation-first source:

- source sample
- schema snapshot or field list
- required KPI field mapping

## Sample evidence

Record:
- sample path
- captured date
- row count if applicable
- format
- time range if applicable
- coverage notes

## Schema evidence

Record:
- schema path
- field names
- field types if available
- nullable/required if known
- example values
- related KPI fields

## Field mapping

| KPI Required Field | Source Field | Available? | Evidence | Notes |
|---|---|---|---|---|

## Missing field handling

If required field is missing:

A. Find substitute field  
B. Modify KPI formula  
C. Defer KPI  
D. Reject source for this KPI  

Ask user if the missing field affects primary KPI.

## Update report

Update:
- source-validation-report.md
- evidence index if evidence exists

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-source-context
  - step-03-access-check
  - step-04-sample-and-schema