---
title: CSAV-DP KPI Catalog
status: final
phase: "03-kpi-discovery"
created: 2026-05-26
gate:
  KPI-GATE-01-kpi-scope-and-primary-definitions: closed_after_source_mapping
source_brief: _dew-output/planning-artifacts/phase-01-project-brief/brief.md
business_discovery: _dew-output/planning-artifacts/phase-02-business-discovery/business-discovery.md
research_baseline: _dew-output/evidence-artifacts/research-baseline/spia-vietnam-report.md
feasibility_status: hypotheses_only
---

# CSAV-DP KPI Catalog

## 1. Purpose

This catalog defines the first set of candidate KPI, signal, advisory output, and data quality definitions for CSAV-DP.

All definitions in this catalog are **hypotheses only**. They are accepted for planning and source dependency mapping, but they are not yet feasible or verified.

No KPI in this document should be treated as implementation-ready until later validation confirms source availability, source fields, grain, geographic coverage, temporal coverage, quality rules, and advisory rule applicability.

## 2. Research Baseline

The KPI catalog is based on the accepted research baseline:

**SPIA Viet Nam Report: Global Ambitions, Sustainable Pathways**

The report is used as a domain anchor for climate-smart agriculture, CS-MAP, VHLSS measurement logic, risk/adaptation planning, province-level agricultural plans, and evidence standards.

## 3. KPI Group Priority

The KPI Discovery round covers four groups in priority order:

1. **Monitoring KPIs** — identify and rank climate/agricultural risk by location and time.
2. **Explanation signals** — explain which factors contribute to risk.
3. **Advisory outputs** — generate evidence-bounded recommendation categories/actions for the farmer-facing web app.
4. **Data quality KPIs** — measure freshness, completeness, traceability, and quality status of data and advisory outputs.

## 4. KPI-MON-001 — Climate-Agricultural Risk Level

### Classification

- **Type:** Monitoring KPI
- **Status:** Hypothesis — not verified
- **Primary consumer:** Data analyst
- **Downstream consumer:** Farmer/end user through web app

### Business Question

Which areas currently have the highest climate/agricultural risk over time?

### Decision Supported

Identify and rank locations that require monitoring, warning, or downstream advisory generation.

### Candidate Formula / Logic

Assign each location-season-scenario record to a categorical risk level:

```text
risk_level ∈ {no_or_minimal_risk, low_risk, medium_risk, high_risk}
```

The classification logic should follow validated CS-MAP/risk-map definitions where available, such as drought, salinity, flooding, rainfall, reservoir water level, or expected productivity-loss thresholds.

### Candidate Grain

```text
location × season × scenario_or_forecast_period × risk_type
```

Potential location levels:

- province;
- district if historical source uses it;
- ward/commune if available and compatible with the current administrative structure;
- mapped risk polygon if GIS data is available.

### Candidate Dimensions

- province;
- ward/commune or mapped polygon;
- region/agroecological region;
- season;
- crop;
- risk type;
- scenario/forecast condition;
- time period/year;
- source version.

### Required Fields — Candidate Only

- location identifier or geometry;
- season/cropping period;
- risk type;
- risk category or numeric threshold input;
- scenario or forecast condition;
- crop or farming system;
- source timestamp/version;
- quality/status fields.

### Caveat

This KPI must not be marked as feasible until source files, fields, geospatial grain, temporal grain, and risk-level definitions are validated.

## 5. SIG-EXP-001 — Risk Driver Type

### Classification

- **Type:** Explanation signal
- **Status:** Hypothesis — not verified
- **Primary consumer:** Data analyst
- **Downstream consumer:** CSAV-DP advisory generation system

### Business Question

Which factors contribute to risk, such as weather, seasonality, location, salinity, or other data?

### Decision Supported

Explain why a location-season-scenario record receives its risk level, so analysts can interpret dashboard results and the system can generate traceable advisory outputs.

### Candidate Formula / Logic

Assign one or more driver categories to each risk record:

```text
risk_driver_type ∈ {
  drought,
  salinity,
  flooding,
  rainfall_anomaly,
  reservoir_water_level,
  seasonal_mismatch,
  planting_date_mismatch,
  geographic_exposure,
  crop_or_farming_system_exposure,
  unknown_or_unclassified
}
```

A record may have multiple risk drivers if the validated source supports multi-driver classification.

### Candidate Grain

```text
location × season × scenario_or_forecast_period × risk_type × driver_type
```

This should align with `KPI-MON-001` where possible.

### Supporting Gold Mart Fields

- `risk_severity_score` — numeric score derived from risk category or thresholds, if valid.
- `risk_source_evidence` — source/rule that produced the risk driver assignment.
- `affected_crop` — crop or farming system affected.
- `affected_season` — cropping season or production window affected.
- `driver_confidence_status` — whether the driver is directly observed, rule-derived, inferred, or unknown.

### Required Fields — Candidate Only

- location identifier or geometry;
- season/cropping period;
- risk type;
- risk category or numeric risk input;
- driver indicator or source variable;
- crop/farming system;
- source reference/version;
- rule reference/version;
- quality/status fields.

### Caveat

This signal must not be marked as feasible until source fields and rule logic can distinguish actual risk drivers. If the source only provides a final risk category, `risk_driver_type` may need to be derived from source metadata or marked `unknown_or_unclassified`.

## 6. ADV-OUT-001 — Advisory Recommendation Category

### Classification

- **Type:** Advisory output
- **Status:** Hypothesis — not verified
- **Primary owner:** CSAV-DP system
- **Downstream consumer:** Farmer/end user through web app

### Business Question

What action recommendation should farmers in each area receive?

### Decision Supported

Generate a traceable, evidence-bounded advisory category for a location-season-risk record that can be consumed by the farmer-facing web app.

### Candidate Formula / Logic

Map validated risk context to a controlled recommendation category:

```text
advisory_recommendation_category ∈ {
  monitor_only,
  adjust_planting_date,
  shift_crop,
  change_cropping_pattern,
  avoid_rice_cultivation,
  change_irrigation_schedule,
  prepare_for_flooding,
  prepare_for_salinity,
  no_advisory_due_to_insufficient_evidence
}
```

The mapping should be rule-based and evidence-bounded:

```text
risk_level
+ risk_driver_type
+ affected_crop
+ affected_season
+ location/region
+ scenario_or_forecast_period
+ advisory_rule_version
+ data_quality_status
→ advisory_recommendation_category
```

### Candidate Grain

```text
location × season × scenario_or_forecast_period × crop_or_farming_system × risk_type
```

This should align with `KPI-MON-001` and `SIG-EXP-001` where possible.

### Supporting Gold Mart / Serving Fields

- `advisory_urgency_level` — low, medium, high, urgent, or unknown.
- `recommended_action_text` — human-readable recommendation text generated only after category/rule is clear.
- `advisory_eligibility_status` — eligible, insufficient_data, failed_quality_check, unsupported_location, unsupported_crop, no_rule_available.
- `advisory_rule_id` — identifier for the rule used.
- `advisory_rule_version` — version of the rule used.
- `advisory_confidence_status` — direct, rule-derived, inferred, insufficient evidence.
- `advisory_caveat` — limitation shown to analysts or web app users.

### Required Fields — Candidate Only

- location identifier or geometry;
- season/cropping period;
- crop/farming system;
- risk level;
- risk driver type;
- scenario or forecast condition;
- adaptation option or rule mapping;
- source reference/version;
- rule reference/version;
- data quality status;
- evidence/caveat fields.

### Caveat

This output must not generate final farmer-facing text until recommendation categories, rules, source dependencies, quality gates, and caveats are validated. If evidence is insufficient, the output should explicitly use `no_advisory_due_to_insufficient_evidence` or an ineligible status.

## 7. KPI-DQ-001 — Advisory Eligibility Status

### Classification

- **Type:** Data quality KPI / safety gate
- **Status:** Hypothesis — not verified
- **Primary owner:** CSAV-DP system
- **Downstream consumer:** Farmer-facing web app and analyst-facing QA checks

### Business Question

Is a location-season-risk record sufficiently complete, traceable, and rule-supported to generate or display an advisory output?

### Decision Supported

Prevent the system and web app from generating unsupported or low-quality advisory recommendations.

### Candidate Formula / Logic

Assign an eligibility status to each candidate advisory record:

```text
advisory_eligibility_status ∈ {
  eligible,
  insufficient_data,
  failed_quality_check,
  unsupported_location,
  unsupported_crop,
  unsupported_season,
  no_rule_available,
  stale_source_data,
  missing_lineage_or_evidence
}
```

A record should be `eligible` only if minimum conditions are satisfied:

```text
has_required_location
AND has_required_season
AND has_required_crop_or_farming_system
AND has_risk_level
AND has_risk_driver_or_valid_unknown_classification
AND has_source_reference
AND has_rule_reference
AND passes_minimum_quality_checks
AND source_freshness_is_acceptable
→ eligible
```

Otherwise, the record must be assigned the most specific ineligible status available.

### Candidate Grain

```text
location × season × scenario_or_forecast_period × crop_or_farming_system × risk_type × advisory_rule_version
```

This should align with `ADV-OUT-001` where possible.

### Supporting Gold Mart / Serving Fields

- `source_freshness_status` — fresh, stale, unknown.
- `risk_record_completeness_status` — complete, incomplete, unknown.
- `lineage_evidence_status` — complete, missing_source, missing_rule, missing_caveat.
- `quality_check_status` — pass, warn, fail.
- `dq_failure_reason` — structured reason for ineligible status.
- `advisory_caveat` — limitation shown to analysts/web users.

### Required Fields — Candidate Only

- location identifier or geometry;
- season/cropping period;
- crop/farming system;
- risk level;
- risk driver type or valid unknown classification;
- advisory rule id/version;
- source reference/version/timestamp;
- freshness threshold;
- quality check result;
- caveat/evidence fields.

### Caveat

This KPI is a safety gate. If this KPI cannot be computed for a record, the system should not produce a farmer-facing advisory for that record.

## 8. Gate Result

**KPI-GATE-01 — KPI Scope and Primary Definitions:** Accepted as hypotheses.

Accepted hypothesis definitions:

1. `KPI-MON-001` — Climate-Agricultural Risk Level.
2. `SIG-EXP-001` — Risk Driver Type.
3. `ADV-OUT-001` — Advisory Recommendation Category.
4. `KPI-DQ-001` — Advisory Eligibility Status.

## 9. Next Validation Requirement

The next phases must validate:

- source availability;
- source license;
- field existence;
- source grain;
- temporal coverage;
- geographic coverage;
- schema stability;
- quality rules;
- risk-level definitions;
- rule applicability;
- whether advisory output can be generated safely.
