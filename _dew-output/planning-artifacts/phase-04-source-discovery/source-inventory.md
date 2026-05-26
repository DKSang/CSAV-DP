---
title: CSAV-DP Candidate Source Inventory
status: candidate-only
phase: "04-source-discovery"
created: 2026-05-26
source_skill: dew-source-discovery
input_artifacts:
  - _dew-output/planning-artifacts/phase-01-project-brief/brief.md
  - _dew-output/planning-artifacts/phase-02-business-discovery/business-discovery.md
  - _dew-output/planning-artifacts/phase-03-kpi-discovery/kpi-catalog.md
  - _dew-output/planning-artifacts/phase-03-kpi-discovery/kpi-source-matrix.md
  - _dew-output/evidence-artifacts/research-baseline/spia-vietnam-report.md
---

# CSAV-DP Candidate Source Inventory

## 1. Purpose

This source inventory identifies candidate data sources for CSAV-DP KPI validation.

All sources are **candidate only**. No source is accepted, prioritized as P1, or considered implementation-ready in this phase.

This inventory exists because `dew-evidence-check` triggered `HALT-18` after KPI Discovery: KPI definitions exist, but source availability, access, fields, grain, and quality have not yet been validated.

## 2. Source Discovery Guardrails

- Candidate source does not mean accepted source.
- No source is marked P1 in this artifact.
- Access is not assumed to work.
- Schema stability is not assumed.
- Field existence is not assumed.
- KPI-source compatibility is not assumed.
- Advisory rules are not validated.

## 3. Candidate Source Inventory

| Source ID | Source Name | Source Type | Expected Business Role | Expected KPI Dependency | Access Method | Owner / Provider | Expected Grain | Expected Freshness | Status |
|---|---|---|---|---|---|---|---|---|---|
| `SRC-CAND-001` | SPIA Viet Nam Report | Research report / baseline document | Domain framing, evidence baseline, candidate risk/adaptation logic | All KPI hypotheses | Uploaded project file / repository evidence artifact | SPIA / CGIAR-related authors | Report-level; references national, regional, province, household, commune, and geospatial analyses | Static report, January 2025 version | Candidate baseline only |
| `SRC-CAND-002` | CS-MAP / Climate-Smart Mapping and Adaptation Planning risk maps | Geospatial risk maps / adaptation planning documents | Candidate source for risk levels, risk types, location-season-scenario mapping, and adaptation options | `KPI-MON-001`, `SIG-EXP-001`, `ADV-OUT-001`, `KPI-DQ-001` | To be discovered: PDFs, GIS files, online maps, DARD/MARD documents, or repository references | MARD/DARD/CGIAR-related CS-MAP initiatives | Province, district, commune, polygon, season, scenario, crop/risk type — exact grain unknown | Static or periodically updated planning artifacts; freshness unknown | Candidate |
| `SRC-CAND-003` | CS-MAP recommended adaptation options | Rule/adaptation option reference | Candidate baseline for advisory recommendation categories | `ADV-OUT-001`, `KPI-DQ-001` | Extract from CS-MAP documents/maps/plans if accessible | MARD/DARD/CS-MAP initiative | Location × season × risk level × adaptation option; exact grain unknown | Static/planning-cycle based; freshness unknown | Candidate |
| `SRC-CAND-004` | Province-level agricultural production plans | Policy/planning documents | Evidence of institutionalized risk/adaptation recommendations and production guidance | `KPI-MON-001`, `SIG-EXP-001`, `ADV-OUT-001` | Web search, official portals, DARD/Sub-Department documents, uploaded PDFs if available | Provincial DARD / Sub-Departments of Crop Production and Plant Protection | Province × year × crop season × recommendation text; exact structure unknown | Annual/seasonal | Candidate |
| `SRC-CAND-005` | Weather/climate API or dataset | API / time series dataset | Candidate source for weather, drought, rainfall anomaly, forecast period, and climate signals | `KPI-MON-001`, `SIG-EXP-001`, `ADV-OUT-001`, `KPI-DQ-001` | API access; likely public API candidate such as Open-Meteo, subject to assessment | Public weather/climate provider | Location × date/time × weather variable; exact spatial resolution depends on provider | Historical, forecast, daily/hourly depending on provider | Candidate |
| `SRC-CAND-006` | Salinity / flooding / reservoir / rainfall indicators | Sensor, API, report, or geospatial dataset | Candidate source for key risk drivers and severity inputs | `KPI-MON-001`, `SIG-EXP-001`, `ADV-OUT-001` | To be discovered from public agencies, hydrometeorological services, MARD/DARD, Mekong data portals, or reports | Provider unknown | Station, river segment, reservoir, province, district, polygon, date/season; exact grain unknown | Unknown | Candidate |
| `SRC-CAND-007` | Vietnam administrative geography dataset | Reference/master data | Location mapping, province/ward/commune hierarchy, region mapping, joining sources | All KPI definitions | Public dataset or GitHub repository; source to be selected | Provider unknown until assessed | Province, ward/commune, possibly legacy district; geometry availability unknown | Static but impacted by administrative changes | Candidate |
| `SRC-CAND-008` | Crop calendar / season definition source | Reference data | Define crop seasons, planting windows, affected crop/season context | `SIG-EXP-001`, `ADV-OUT-001`, `KPI-DQ-001` | FAO crop calendar, RiceAtlas, national crop calendars, or CS-MAP/province plan extraction | Provider unknown until assessed | Crop × region/province × season × planting/harvest window | Static or periodically updated | Candidate |
| `SRC-CAND-009` | VHLSS / SPIA measurement logic | Survey/methodology reference | Measurement design reference for adoption, reach, caveats, and evidence standards | Mainly research/evidence context; not direct MVP operational KPI unless data access is available | Uploaded report and possible GSO/SPIA repository if accessible | GSO / SPIA | Household, enumeration area, commune, province, region, year; exact accessible data unknown | Survey waves 2022–2024 in report | Candidate reference only |
| `SRC-CAND-010` | Rule catalog / advisory rule definitions | Project-created reference table | Versioned mapping from risk context to advisory recommendation category and eligibility logic | `ADV-OUT-001`, `KPI-DQ-001` | To be created by CSAV-DP after source assessment | CSAV-DP project | Rule ID × version × risk context × recommendation category | Versioned by project release | Candidate to be created |
| `SRC-CAND-011` | Data quality check results / pipeline metadata | Project-created metadata | Support eligibility, freshness, completeness, lineage, and quality gates | `KPI-DQ-001`, all advisory outputs | To be created by CSAV-DP during implementation | CSAV-DP project | Pipeline run × source × table × rule/check × result | Per pipeline run | Candidate to be created |

## 4. KPI Coverage Check

| KPI / Signal / Output | Candidate Source Coverage | Coverage Status |
|---|---|---|
| `KPI-MON-001` Climate-Agricultural Risk Level | `SRC-CAND-002`, `SRC-CAND-004`, `SRC-CAND-005`, `SRC-CAND-006`, `SRC-CAND-007`, `SRC-CAND-001` | Candidate source exists |
| `SIG-EXP-001` Risk Driver Type | `SRC-CAND-002`, `SRC-CAND-004`, `SRC-CAND-005`, `SRC-CAND-006`, `SRC-CAND-008`, `SRC-CAND-007`, `SRC-CAND-001` | Candidate source exists |
| `ADV-OUT-001` Advisory Recommendation Category | `SRC-CAND-003`, `SRC-CAND-002`, `SRC-CAND-004`, `SRC-CAND-008`, `SRC-CAND-010`, `SRC-CAND-001` | Candidate source exists |
| `KPI-DQ-001` Advisory Eligibility Status | `SRC-CAND-010`, `SRC-CAND-011`, source metadata from all selected sources | Candidate source exists, but project-created evidence is missing |

No `HALT-04 — Source Not Identified` is triggered because every primary KPI has at least one candidate source.

## 5. Critical Unknowns

The following must be validated before any source is accepted:

- actual access path;
- license and reuse rights;
- schema and file format;
- field existence;
- geographic grain;
- temporal grain;
- crop/season compatibility;
- administrative geography compatibility after Vietnam administrative changes;
- source freshness;
- source stability;
- data quality profile;
- lineage metadata;
- rule provenance;
- advisory safety constraints.

## 6. Recommended Assessment Order

Recommended first assessment batch:

1. `SRC-CAND-002` — CS-MAP / climate-smart risk maps.
2. `SRC-CAND-003` — CS-MAP recommended adaptation options.
3. `SRC-CAND-007` — Vietnam administrative geography dataset.
4. `SRC-CAND-005` — weather/climate API or dataset.
5. `SRC-CAND-006` — salinity/flooding/reservoir/rainfall indicators.
6. `SRC-CAND-008` — crop calendar / season definitions.
7. `SRC-CAND-010` — project rule catalog.
8. `SRC-CAND-011` — project DQ metadata/check results.

Province-level agricultural plans and VHLSS/SPIA measurement logic should remain important supporting sources, but they may be harder to operationalize as automated MVP inputs.

## 7. Gate Status

**SRC-DISC-GATE-01 — Candidate Source Coverage:** Ready for review.

This source inventory is complete at the candidate discovery level, but no source is accepted or implementation-ready.

## 8. Next Workflow Recommendation

Recommended next workflow:

**`dew-source-assessment`**

The next phase should assess candidate source access, licensing, field/grain fit, quality risks, and feasibility before implementation or architecture design.
