---
title: CSAV-DP Source Assessment Scorecard
status: preliminary-assessment
phase: "05-source-assessment"
created: 2026-05-26
source_skill: dew-source-assessment
input_source_inventory: _dew-output/planning-artifacts/phase-04-source-discovery/source-inventory.md
result: no_source_accepted_yet
---

# CSAV-DP Source Assessment Scorecard

## 1. Purpose

This scorecard assesses candidate sources for KPI relevance, access risk, ownership clarity, expected field coverage, grain compatibility, freshness, schema stability, privacy/security risk, license/terms risk, operational reliability, and validation effort.

This is a **preliminary assessment only**. No source is accepted, marked P1, or considered implementation-ready in this phase.

## 2. Assessment Guardrails

- Do not promote source to P1 without validation evidence.
- Do not assume access works.
- Do not assume schema is stable.
- Do not assume source grain matches KPI grain.
- Do not hide source caveats.
- If source trust is unclear, trigger `HALT-06 — Source Trust Not Established`.

## 3. Priority Labels

| Priority | Meaning |
|---|---|
| Validate first | Strong KPI relevance and likely useful for MVP validation; still not accepted |
| Validate later | Useful but not first validation batch |
| Exploration only | Useful for framing/research but weak as operational data |
| Reject early | Not suitable enough to continue |
| Blocked | Cannot assess until access/provider/license/source path is clarified |

## 4. Source Scorecard

| Source ID | Source | KPI Relevance | Access Risk | Owner / Provider Clarity | Expected Field Coverage | Expected Grain Compatibility | Expected Freshness | Schema Stability Risk | Privacy / Security Risk | License / Terms Risk | Operational Reliability | Validation Effort | Priority | Key Caveat |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|
| `SRC-CAND-001` | SPIA Viet Nam Report | High for framing; low for direct operations | Low | Clear | Conceptual / report-level | Not operational grain | Static | Low | Low | Medium | High as baseline, not live data | Low | Exploration only | Accepted as research baseline, not operational source |
| `SRC-CAND-002` | CS-MAP risk maps | Very high | High | Medium | Potentially high | Unknown until files/GIS inspected | Unknown / planning-cycle | Medium | Low | Medium to high | Unknown | High | Validate first | Core source for risk/advisory logic, but access path and machine-readable format are not established |
| `SRC-CAND-003` | CS-MAP recommended adaptation options | Very high | High | Medium | Potentially high | Unknown | Static/planning-cycle | Medium | Low | Medium to high | Unknown | High | Validate first | Needed for advisory categories, but rule extraction/provenance must be validated |
| `SRC-CAND-004` | Province-level agricultural production plans | Medium to high | High | Medium | Medium | Province/year/season text; exact structure unknown | Annual/seasonal | High | Low | Medium | Medium | High | Validate later | Useful evidence of institutional recommendations but likely hard to automate early |
| `SRC-CAND-005` | Weather/climate API or dataset | High | Low to medium | High if Open-Meteo or similar public provider is chosen | High for weather variables | Point/grid × time; must map to admin units | Daily/hourly/forecast possible | Medium | Low | Low to medium depending provider | Medium to high | Medium | Validate first | Good candidate for operational weather signals; must validate terms, attribution, coverage, rate limits, and API schema |
| `SRC-CAND-006` | Salinity/flooding/reservoir/rainfall indicators | Very high for MRD/risk drivers | High | Low to medium | Potentially high | Station/river/reservoir/polygon grain unknown | Unknown | High | Low | Medium to high | Unknown | High | Blocked | `HALT-06`: source trust not established until provider/access path is identified |
| `SRC-CAND-007` | Vietnam administrative geography dataset | Very high | Medium | Medium | High if selected dataset has geometry and codes | Must handle new admin structure and legacy district references | Static but politically/currently sensitive | Medium | Low | Medium | Medium | Medium | Validate first | Need official/current admin structure and stable keys; historical district compatibility is a risk |
| `SRC-CAND-008` | Crop calendar / season definition source | High | Medium | Medium | Medium to high | Crop × region/province × season; exact grain depends source | Static/periodic | Medium | Low | Low to medium | Medium | Medium | Validate first | Needed for season/crop context; source selection and regional fit must be validated |
| `SRC-CAND-009` | VHLSS / SPIA measurement logic | Medium | High for raw data, low for report logic | High | High in report, raw fields unknown | Household/EA/commune/province/year if data accessible | Survey waves | Medium | Medium to high if raw microdata | High | Low for report, unknown for raw data | High | Exploration only | Good measurement reference; not assumed available as operational source |
| `SRC-CAND-010` | Rule catalog / advisory rule definitions | Very high | Low because project-created | High | High if designed well | Can be designed to match Gold grain | Versioned by project | Low if governed | Low | Low | High if tested | Medium | Validate first | Must be created with provenance; cannot be treated as evidence until rules are validated |
| `SRC-CAND-011` | DQ check results / pipeline metadata | Very high for safety gate | Low because project-created | High | High if designed well | Can be designed to match pipeline/Gold grain | Per run | Low if governed | Low | Low | High if automated | Medium | Validate first | Must be implemented and tested before advisory eligibility can be computed |

## 5. Validation Priority Grouping

### Validate First

1. `SRC-CAND-002` — CS-MAP risk maps.
2. `SRC-CAND-003` — CS-MAP recommended adaptation options.
3. `SRC-CAND-005` — Weather/climate API or dataset.
4. `SRC-CAND-007` — Vietnam administrative geography dataset.
5. `SRC-CAND-008` — Crop calendar / season definition source.
6. `SRC-CAND-010` — Rule catalog / advisory rule definitions.
7. `SRC-CAND-011` — DQ check results / pipeline metadata.

### Validate Later

1. `SRC-CAND-004` — Province-level agricultural production plans.

### Exploration Only

1. `SRC-CAND-001` — SPIA Viet Nam Report.
2. `SRC-CAND-009` — VHLSS / SPIA measurement logic.

### Blocked

1. `SRC-CAND-006` — Salinity/flooding/reservoir/rainfall indicators.

## 6. HALT-06 — Source Trust Not Established

`SRC-CAND-006` triggers `HALT-06 — Source Trust Not Established` because the candidate group is important but no specific provider, access path, license, field schema, or coverage evidence has been established.

This does not reject the source category. It means the project must identify a concrete provider or dataset before it can be assessed properly.

Potential provider categories to investigate later:

- official hydrometeorological agency sources;
- MARD/DARD reports or datasets;
- Mekong Delta salinity monitoring portals;
- reservoir/water-level datasets;
- trusted research or open-data repositories.

## 7. Source Assessment Result

No source is accepted yet.

The best next validation batch should focus on:

1. actual access path;
2. license/terms;
3. sample extraction;
4. schema/field profiling;
5. grain compatibility;
6. temporal and geographic coverage;
7. source caveats;
8. integration feasibility for KPI validation.

## 8. Recommended Next Workflow

Recommended next workflow:

**`dew-source-validation`**

If the project wants implementation-level evidence, use targeted implementation skills after source validation planning:

- `dew-source-access-check`;
- `dew-source-sampler`;
- profiling/field validation workflow;
- DQ/rule catalog workflow.

## 9. Decision

**Decision:** Preliminary source assessment completed.

**Status:** Ready for user review.

**Date:** 2026-05-26
