# DEW Project Brief Template

```markdown
---
title: "{Project Name} Project Brief"
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
workflow: dew
phase: "1-analysis"
stepsCompleted: []
decisionGates:
  GATE-00-project-scope:
    status: pending
evidence: []
assumptions: []
caveats: []
---

# Project Brief: {Project Name}

## 0. Document Purpose

This brief defines the initial scope, purpose, users, learning goals, and evidence requirements for the data engineering project.

## 1. Project Summary

[What is this project?]

## 2. Project Type

Choose one:

- A. Learning / exploration
- B. Portfolio project
- C. Internal decision-support
- D. Production-grade

Decision:

## 3. Target Users / Data Consumers

Who will use the output?

- Analyst
- Business user
- Data scientist
- Application
- Farmer / field user
- External user
- Other

## 4. Decision Supported

What decision should this data product help users make?

## 5. Expected Data Product

Possible outputs:

- Dashboard
- Gold data mart
- API
- ML feature table
- Report
- Notebook
- Reverse ETL output
- Web app feature

## 6. MVP Scope

### In Scope

- ...

### Out of Scope

- ...

## 7. Learning Objectives

What should the user learn while building this project?

- Source assessment
- KPI feasibility
- Ingestion
- Storage design
- Transformation/modeling
- Serving layer
- Data quality
- Governance/DataOps

## 8. Initial KPI Hypotheses

Important: These are hypotheses, not verified KPIs.

| KPI ID | KPI Name | Business Question | Candidate Grain | Status |
|---|---|---|---|---|
| KPI-001 | | | | Hypothesis |

## 9. Initial Source Hypotheses

Important: These sources are not accepted until validated.

| Source ID | Source Name | Source Type | Access Method | Status |
|---|---|---|---|---|
| SRC-001 | | API/File/DB/Stream | | Candidate |

## 10. Assumptions

- [ASSUMPTION] ...

## 11. Known Unknowns

- ...

## 12. Evidence Required Before Architecture

Before final architecture, DEW requires:

- KPI feasibility evidence
- source access evidence
- source sample/schema evidence
- grain decision
- trust expectation decision
- freshness decision

## 13. Next Recommended Workflow

Recommended next skill:

`dew-business-discovery`