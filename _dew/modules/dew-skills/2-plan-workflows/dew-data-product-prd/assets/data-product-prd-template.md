# Data Product PRD Template

```markdown
---
title: "{Project Name} Data Product PRD"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "2-plan-workflows"
decisionGates:
  GATE-05-trust-expectation:
    status: pending
  GATE-04-kpi-grain:
    status: pending
evidence: []
assumptions: []
caveats:
  - "KPI and source feasibility must be validated before architecture."
---

# Data Product PRD: {Project Name}

## 0. Document Purpose

This PRD defines the data product requirements.

It does not prove KPI or source feasibility. Those must be validated in later workflows.

## 1. Vision

## 2. Data Consumers

| Consumer ID | Consumer | Role | Decision Supported | Output Needed |
|---|---|---|---|---|
| CON-001 | | | | |

## 3. Decisions Supported

## 4. Data Product Type

Choose one or more:

- Dashboard
- Gold data mart
- API
- ML feature table
- Report
- Notebook
- Web app feature
- Reverse ETL output

## 5. KPI Hypotheses

| KPI ID | KPI Name | Formula Summary | Grain | Feasibility Status |
|---|---|---|---|---|
| KPI-001 | | | | Hypothesis |

## 6. Product Grain

One row / one observation represents:

## 7. Freshness Requirement

Expected freshness:

Minimum acceptable freshness:

Freshness validation status:

## 8. Trust Expectation

Choose one:

A. Exploratory only  
B. Internal decision-support with documented limitations  
C. Trusted shared product with quality checks  
D. Production-grade with contracts and monitoring  

Selected:

## 9. Candidate Sources

| Source ID | Source Name | Source Type | Role | Validation Status |
|---|---|---|---|---|
| SRC-001 | | API/File/DB | Required/Optional | Candidate |

## 10. Data Quality Expectations

Initial expectations only. Final DQ rules come later.

- Completeness:
- Uniqueness:
- Valid ranges:
- Freshness:
- Referential integrity:
- Business rule consistency:

## 11. Known Limitations

## 12. Non-Goals

## 13. Evidence Required Before Architecture

Architecture cannot be finalized until:

- primary KPI feasibility is validated or caveated
- P1 sources are access-verified
- source sample/schema evidence exists
- grain is approved
- trust expectation is approved
- freshness expectation is approved

## 14. Open Questions

## 15. Assumptions Index

## 16. Next Workflows

Required next:
- `dew-kpi-feasibility`
- `dew-source-validation`