---
title: CSAV-DP KPI Source Matrix
status: final
phase: "03-kpi-discovery"
created: 2026-05-26
source_kpi_catalog: _dew-output/planning-artifacts/phase-03-kpi-discovery/kpi-catalog.md
feasibility_status: candidate_dependencies_only
---

# CSAV-DP KPI Source Matrix

## 1. Purpose

This matrix maps candidate KPI definitions to candidate source dependencies.

All source dependencies are **candidate only**. Availability, licensing, fields, grain, quality, and operational suitability are not verified in this phase.

## 2. Source Dependency Summary

| Candidate Source | Role in KPI Discovery | Verification Status |
|---|---|---|
| SPIA Viet Nam Report | Research baseline, domain framing, candidate risk/adaptation logic | Accepted as research baseline, not implementation data |
| CS-MAP / climate-smart risk maps | Candidate source for risk level, risk type, location/season/scenario mapping, adaptation options | Not verified |
| CS-MAP recommended adaptation options | Candidate rule baseline for advisory categories | Not verified |
| Province-level agricultural plans | Candidate source for institutionalized recommendations and adaptation plan signals | Not verified |
| VHLSS / SPIA measurement logic | Candidate reference for measurement design, adoption context, caveats | Not verified as direct project data source |
| Weather/climate forecast or historical climate source | Candidate source for drought, rainfall, weather anomaly, forecast-period signals | Not verified |
| Salinity/flooding/reservoir/rainfall indicators | Candidate source for risk drivers and severity inputs | Not verified |
| Crop calendar or season definition source | Candidate source for crop/season context and advisory windows | Not verified |
| Vietnam administrative geography dataset | Candidate source for province/ward/commune/region mapping | Not verified |
| Source metadata from ingestion pipeline | Candidate source for freshness, lineage, version, and quality metadata | Not created yet |
| Rule catalog / advisory rule definitions | Candidate source for advisory rule ID/version and eligibility logic | Not created yet |
| Data quality check results | Candidate source for advisory eligibility and safety gate | Not created yet |

## 3. KPI-to-Source Matrix

| KPI / Signal / Output | Candidate Source Dependencies | Required Validation |
|---|---|---|
| `KPI-MON-001` Climate-Agricultural Risk Level | CS-MAP risk maps; province-level agricultural plans; weather/climate source; salinity/flooding/reservoir/rainfall indicators; Vietnam administrative geography; SPIA report as baseline | Confirm source availability, license, geography grain, temporal grain, risk-level definitions, field existence, risk category mapping, source versioning |
| `SIG-EXP-001` Risk Driver Type | CS-MAP risk maps; province-level agricultural plans; weather/climate source; salinity/flooding/reservoir/rainfall indicators; crop calendar/season source; Vietnam administrative geography; SPIA report as baseline | Confirm drivers can be distinguished from source fields or rule metadata; validate multi-driver logic; define unknown/unclassified handling |
| `ADV-OUT-001` Advisory Recommendation Category | CS-MAP adaptation options; CS-MAP risk maps; province-level agricultural plans; crop calendar/season source; weather/climate and salinity/flooding/reservoir/rainfall sources; Vietnam administrative geography; rule catalog; SPIA report as baseline | Confirm recommendation categories match validated adaptation options; define rule mapping; define unsupported cases; validate caveats and web-app-safe output logic |
| `KPI-DQ-001` Advisory Eligibility Status | Ingestion metadata; source freshness metadata; data quality check results; rule catalog; lineage metadata; CS-MAP/province plan/weather/admin geography sources | Confirm required metadata exists; define freshness thresholds; define minimum completeness; define pass/warn/fail checks; define failure reason hierarchy |

## 4. Field Dependency Matrix

| Field / Concept | Needed By | Candidate Source | Status |
|---|---|---|---|
| `location_id` / geometry | All KPIs | CS-MAP, admin geography, source data | Candidate |
| `province` / `region` | All KPIs | Admin geography, SPIA regional framing | Candidate |
| `ward_or_commune` | All KPIs if fine grain used | Admin geography, CS-MAP if available | Candidate |
| `season` / `cropping_period` | All KPIs | CS-MAP, crop calendar, province plans | Candidate |
| `scenario_or_forecast_period` | Monitoring, explanation, advisory | CS-MAP, weather/climate source | Candidate |
| `risk_type` | Monitoring, explanation, advisory | CS-MAP, weather/climate/salinity/flooding sources | Candidate |
| `risk_level` | Monitoring, advisory, DQ | CS-MAP, derived rules | Candidate |
| `risk_driver_type` | Explanation, advisory, DQ | CS-MAP metadata, source variables, rule logic | Candidate |
| `risk_severity_score` | Explanation/dashboard ranking | Derived from risk category or thresholds | Candidate |
| `affected_crop` | Explanation, advisory, DQ | CS-MAP, crop calendar, province plans | Candidate |
| `affected_season` | Explanation, advisory, DQ | CS-MAP, crop calendar, province plans | Candidate |
| `advisory_recommendation_category` | Web app output | Rule catalog from validated adaptation options | Candidate |
| `advisory_urgency_level` | Web app/dashboard | Derived rule logic | Candidate |
| `recommended_action_text` | Web app display | Derived from category/rule only after validation | Candidate |
| `advisory_eligibility_status` | DQ safety gate | DQ rules, lineage, source metadata, rule catalog | Candidate |
| `source_reference` / `source_version` | All KPIs | Ingestion metadata, source registry | Candidate |
| `rule_id` / `rule_version` | Advisory, DQ | Rule catalog | Candidate |
| `quality_check_status` | DQ, advisory safety | DQ framework | Candidate |
| `advisory_caveat` | Advisory/web app | Rule catalog, source caveats, evidence artifacts | Candidate |

## 5. Validation Gates Required Next

Before any KPI is considered feasible, the project must pass later validation gates for:

1. Source discovery and inventory.
2. Source license/access review.
3. Source sample extraction.
4. Field profiling.
5. Grain compatibility check.
6. Geography compatibility check.
7. Temporal coverage check.
8. Data quality profiling.
9. Rule catalog design.
10. Advisory safety review.

## 6. Decision

**Decision:** Source dependency mapping is complete at candidate level.

**Status:** Candidate only — not verified.

**Date:** 2026-05-26
