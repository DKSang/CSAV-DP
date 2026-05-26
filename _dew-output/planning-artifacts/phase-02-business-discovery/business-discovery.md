---
title: CSAV-DP Business Discovery
status: final
phase: "02-business-discovery"
created: 2026-05-26
gate:
  BD-GATE-01-business-decision-context: closed
source_brief: _dew-output/planning-artifacts/phase-01-project-brief/brief.md
trust_expectation: trusted_shared_product_with_quality_checks
---

# CSAV-DP Business Discovery

## 1. Purpose

This artifact refines the business decision context for CSAV-DP after the Project Brief scope gate was closed.

The goal is to clarify who uses the data product, what decision or question it supports, what action follows from the answer, and what level of trust should guide the next phases.

## 2. Input Context

CSAV-DP is a portfolio data engineering project about climate-smart agriculture in Vietnam. The MVP prioritizes a Gold data mart as the core data product for analysts, then serves risk monitoring and advisory-style information through dashboard and web app features.

The Project Brief gate is already closed. This Business Discovery artifact refines the decision workflow inside that approved scope.

## 3. Consumer Map

| Consumer | Role | Decision / Need | Frequency | Output Needed |
|---|---|---|---|---|
| Data analyst | Primary analytical consumer | Identify and explain agricultural/climate risk areas | Recurring, likely daily/weekly/monthly depending on source freshness | Gold marts, risk indicators, dashboard/report-ready outputs, quality evidence |
| Farmer / end user | Downstream product consumer | Understand simplified risk/advisory information for their area | When web app is used or refreshed | Web app feature consuming system-generated advisory records or recommendation categories |
| CSAV-DP system | Advisory generation owner | Transform validated risk signals into advisory content | On data refresh / scheduled run | Evidence-bounded advisory outputs generated from rules/logic, not manual analyst work |

## 4. Primary Consumer Decision

The primary analytical consumer is the **data analyst**.

The farmer/end user is the downstream product consumer. This means the system must eventually serve farmer-facing advisory information, but the data foundation must first be reliable enough for analyst-facing risk monitoring and dashboard/report outputs.

## 5. Analyst Workflow

The analyst workflow is:

1. Use the Gold data mart and dashboard/report outputs.
2. Analyze risk areas by province/ward/region/time.
3. Compare areas to identify locations needing attention.
4. Interpret risk drivers using documented factors and caveats.
5. Use dashboard/report outputs for monitoring and communication.

The analyst should **not** be responsible for manually creating farmer-facing recommendation content every time new data arrives. That would create a bottleneck and slow down the web app workflow.

## 6. Advisory Generation Workflow

Farmer-facing recommendation content is owned by the **CSAV-DP system**, not by manual analyst processing.

The intended flow is:

```text
Gold data mart
+ validated risk/advisory logic
+ versioned rule/threshold definitions
+ data quality and evidence metadata
→ advisory records / recommendation categories
→ farmer-facing web app feature
```

The web app should consume documented, reproducible, evidence-bounded advisory outputs. It should not wait for a data analyst to manually prepare recommendations after every data refresh.

## 7. Core Business Questions

The data product should answer four layered questions:

### Core monitoring questions

1. Which areas currently have the highest climate/agricultural risk over time?
2. Which areas should be prioritized for warning or intervention first?

### Explanation question

3. Which factors contribute to risk, such as weather, seasonality, location, salinity, or other data?

### System-generated advisory question

4. What action recommendation should farmers in each area receive?

The first two questions are the core MVP monitoring questions. The third explains why an area is risky. The fourth is system-generated advisory output and must remain evidence-bounded.

## 8. Action After Answer

The workflow produces two serving outputs:

1. **Analyst-facing output:** dashboard/report for monitoring, comparison, and explanation of risk areas.
2. **Farmer-facing output:** web app feature that consumes system-generated advisory records or recommendation categories.

The farmer-facing output depends on validated Gold marts, rules, thresholds, caveats, and quality checks.

## 9. Trust Expectation

The selected trust expectation is:

**Trusted shared product with quality checks.**

This means the product should include:

- data quality checks;
- documented assumptions;
- source caveats;
- lineage or traceability;
- reproducible evidence artifacts;
- versioned risk/advisory rules where applicable;
- clear distinction between monitoring insight and advisory recommendation.

This does **not** mean production-grade contracts, full SLAs, operational monitoring, or guaranteed farmer advice.

## 10. Business Decision Gate Result

**BD-GATE-01 — Business Decision Context:** Closed.

The decision context is clear enough to continue.

Closed business context:

The primary analytical consumer is the data analyst. The downstream product consumer is the farmer/end user. The analyst uses the product to analyze risk areas and create or consume dashboard/report outputs. The system, not the analyst, owns farmer-facing advisory generation from validated Gold marts, evidence-bounded rules, and quality-checked risk logic. The product should behave like a trusted shared analytical product with quality checks, but it is not production-grade.

## 11. Implications for Next Phases

The next workflow should not jump directly to architecture. It should first define the risk/advisory questions and candidate metrics clearly enough to guide source assessment and Gold mart design.

Recommended next steps:

1. `dew-kpi-discovery` — define monitoring, explanation, and advisory output candidates.
2. `dew-evidence-check` — separate assumptions from evidence.
3. Source inventory and assessment — validate source availability, quality, grain, freshness, and licensing.
4. Only after source evidence should ingestion/storage/serving architecture be finalized.
