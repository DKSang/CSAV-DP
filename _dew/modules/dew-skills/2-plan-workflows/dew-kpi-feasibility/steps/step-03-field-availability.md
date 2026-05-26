# Step 03 — Field Availability Analysis

## Mandatory Rules

- Do not assume required fields exist.
- Do not assume candidate source field names are correct.
- If no sample/schema/source evidence exists, mark field availability as Unknown.
- Unknown field availability blocks KPI verification.

## Task

Assess whether required KPI fields are available in candidate sources.

## For each KPI

Create a field availability table:

| Required Field | Business Meaning | Candidate Source | Candidate Source Field | Available? | Evidence |
|---|---|---|---|---|---|

## Evidence types allowed

- source sample
- schema snapshot
- field dictionary
- API response
- CSV header
- database schema
- notebook inspection
- documented source specification

## Classification

Field availability must be one of:

- Yes
- No
- Unknown
- Partial
- Substitute available

## Missing field handling

If a required field is missing:

Options:
A. Find substitute field  
B. Modify KPI formula  
C. Defer KPI  
D. Reject KPI  

Ask user if the field is critical.

## Update files

Update:

- `field-availability.md`
- `kpi-feasibility-report.md`

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-kpi-context
  - step-03-field-availability