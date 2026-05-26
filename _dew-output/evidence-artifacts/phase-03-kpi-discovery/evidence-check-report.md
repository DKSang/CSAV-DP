---
title: Phase 03 KPI Discovery Evidence Check Report
status: halt-18-missing-validation-evidence
phase: "03-kpi-discovery"
created: 2026-05-26
target_artifacts:
  - _dew-output/planning-artifacts/phase-03-kpi-discovery/kpi-catalog.md
  - _dew-output/planning-artifacts/phase-03-kpi-discovery/kpi-source-matrix.md
skill: dew-evidence-check
halt: HALT-18-missing-evidence
---

# Phase 03 — KPI Discovery Evidence Check Report

## 1. Purpose

This evidence check evaluates whether Phase 03 KPI Discovery can be considered evidence-complete.

Per DEW Evidence Check rules:

- planning artifacts are not evidence;
- a phase is not done without evidence;
- missing evidence triggers `HALT-18`;
- caveated continuation requires explicit user approval.

## 2. Target Phase

| Item | Value |
|---|---|
| Phase | Phase 03 — KPI Discovery |
| Target artifact | `kpi-catalog.md` |
| Supporting artifact | `kpi-source-matrix.md` |
| Decision log | `.decision-log.md` |
| Research baseline | `spia-vietnam-report.md` |

## 3. Required Gates

| Gate | Status | Notes |
|---|---|---|
| KPI-GATE-01 — KPI Scope and Primary Definitions | Closed | KPI definitions accepted as hypotheses only |
| Source dependency mapping | Completed at candidate level | Candidate dependencies only, not verified |
| KPI feasibility validation | Missing | Not part of KPI Discovery; required later |
| Source field/grain validation | Missing | Required before implementation |
| Rule/advisory validation | Missing | Required before farmer-facing advisory |

## 4. Evidence Classification

| Requirement | Status | Evidence Path | Notes |
|---|---|---|---|
| Business context exists | Available | `_dew-output/planning-artifacts/phase-02-business-discovery/business-discovery.md` | Business decision context is available and closed |
| KPI catalog exists | Available | `_dew-output/planning-artifacts/phase-03-kpi-discovery/kpi-catalog.md` | Planning artifact only; definitions are hypotheses |
| KPI source matrix exists | Available | `_dew-output/planning-artifacts/phase-03-kpi-discovery/kpi-source-matrix.md` | Candidate mapping only; sources are not verified |
| Research baseline exists | Available | `_dew-output/evidence-artifacts/research-baseline/spia-vietnam-report.md` | Accepted as domain/evidence baseline, not operational data |
| Source availability evidence | Missing | Not available | Need source inventory and access check |
| Source license evidence | Missing | Not available | Need license/access review for each source |
| Source field existence evidence | Missing | Not available | Need sample extraction and profiling |
| Source grain compatibility evidence | Missing | Not available | Need geography/time/crop grain validation |
| CS-MAP/risk map file evidence | Missing | Not available | Need actual source files or URLs and sample inspection |
| Province-level plan evidence | Missing | Not available | Need source list, plan files, and parsing/profile notes |
| Weather/climate source evidence | Missing | Not available | Need selected API/dataset and sample response/profile |
| Salinity/flooding/reservoir data evidence | Missing | Not available | Need selected source and coverage check |
| Administrative geography evidence | Missing | Not available | Need selected admin geography dataset and grain mapping |
| Crop calendar/season source evidence | Missing | Not available | Need selected source and season definitions |
| Rule catalog evidence | Missing | Not available | Need versioned advisory rules and rule provenance |
| Data quality check evidence | Missing | Not available | Need DQ rules and test results |
| Advisory safety evidence | Missing | Not available | Need eligibility logic validation and caveat review |

## 5. Evidence Result

**Result:** `HALT-18 — Missing validation evidence`

Phase 03 has strong planning artifacts, but it is not evidence-complete for implementation.

The KPI definitions are valid as **hypotheses**, but not validated as feasible KPIs.

## 6. What Is Safe to Continue With

It is safe to continue to the next planning/validation workflow if the continuation is explicitly caveated:

- KPI definitions remain hypotheses.
- Source dependencies remain candidate only.
- No architecture or implementation should treat these KPIs as feasible yet.
- No farmer-facing advisory output should be produced until source, rule, DQ, and safety evidence exists.

## 7. Missing Evidence to Produce Next

The next evidence-producing work should include:

1. Source inventory for CS-MAP, province agricultural plans, weather/climate, salinity/flooding/reservoir, admin geography, crop calendar, and rule sources.
2. Source license/access review.
3. Source sample extraction.
4. Field profiling.
5. Grain compatibility check.
6. Geographic and temporal coverage check.
7. Initial rule catalog draft with provenance.
8. Advisory eligibility validation logic.
9. DQ checks and quality evidence.

## 8. Decision Required

Because evidence is missing, the user must choose one:

A. Produce missing evidence next.  
B. Continue with caveat.  
C. Reduce scope.  
D. Return to previous phase.

## 9. Recommendation

Recommended decision: **A. Produce missing evidence next.**

The best next workflow is a source inventory / evidence workflow focused on validating the candidate source dependencies before architecture or implementation.
