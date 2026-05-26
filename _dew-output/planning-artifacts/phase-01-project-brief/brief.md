---
title: CSAV-DP Project Brief
status: final
phase: "01-project-brief"
created: 2026-05-26
gate:
  GATE-00-project-scope: closed
project_type: portfolio
---

# CSAV-DP Project Brief

## 1. Project Purpose

CSAV-DP is a portfolio data engineering project focused on climate-smart agriculture in Vietnam. The project will build an end-to-end data product that integrates climate, agriculture, geography, and administrative data into reliable analytics-ready layers.

The MVP prioritizes risk monitoring for agriculture and prepares a path toward evidence-bounded advisory-style action recommendations.

## 2. Target Users / Consumers

The MVP has two confirmed user groups:

1. **Data analyst** — the primary technical consumer. Analysts need clean, documented, analysis-ready Gold data marts, KPIs, risk metrics, and data quality evidence.
2. **Farmer / end user / customer** — the primary domain/end consumer. Farmers or end users need simplified risk/advisory information, likely served later through dashboard or web app features.

For implementation order, the project should first make the data reliable for analysts, while keeping farmer-facing advisory use cases as a design constraint.

## 3. Decision / Action Supported

The product supports two confirmed decision/action directions:

1. **Monitor risk** — the core MVP capability. Users should be able to monitor climate/agricultural risk by location and time.
2. **Recommend an action** — the advisory direction. The product should eventually provide simple action recommendations for farmers or decision-makers.

Action recommendation must remain evidence-bounded. The MVP must not present recommendations as production-grade agricultural advice until source quality, business rules, domain thresholds, and limitations are validated.

## 4. Expected Data Product

The confirmed MVP data product types are:

1. **Gold data mart** — the core data product and foundation for analytics, KPI/risk modeling, quality checks, and traceability.
2. **Dashboard** — an analyst-facing serving layer for risk monitoring, comparison, and explanation.
3. **Web app feature** — a farmer/end-user-facing feature for simplified risk or advisory information.

Implementation priority:

1. Gold data mart first.
2. Dashboard second.
3. Web app feature third.

This order prevents the project from jumping into UI before the data, grain, KPIs, and advisory logic are validated.

## 5. Project Type

The confirmed project type is **Portfolio project**.

This means CSAV-DP should be strong enough to demonstrate end-to-end data engineering capability, including:

- clear business and user purpose;
- evidence-driven source assessment;
- Bronze/Silver/Gold modeling;
- documented KPI/risk logic;
- data quality checks;
- reproducible implementation artifacts;
- visible serving layer through dashboard and/or web app.

The project does not need production-grade SLAs, full monitoring, or guaranteed advisory reliability in the MVP.

## 6. MVP Scope

The MVP should focus on a narrow but complete end-to-end slice:

- climate-smart agriculture in Vietnam;
- risk monitoring by location and time;
- Gold data mart as the core deliverable;
- dashboard and web app feature as serving layers;
- advisory-style recommendations treated as hypotheses until validated;
- evidence artifacts for sources, assumptions, data quality, and limitations.

## 7. Non-Goals

The MVP will not attempt to:

- build a production-grade farmer advisory platform;
- guarantee real-time or operational recommendations;
- cover every crop, risk, and province from the start;
- treat unvalidated public data as authoritative;
- prioritize UI before data foundations;
- build ML before source quality and business rules are understood.

## 8. Learning Objectives

The project should demonstrate and teach:

- data engineering workflow from project brief to serving layer;
- evidence-driven source discovery and assessment;
- Bronze/Silver/Gold lakehouse thinking;
- Gold mart design for analytics and advisory use cases;
- KPI/risk metric definition;
- data quality and lineage practices;
- phase-gated implementation using DEW;
- separation between assumptions, evidence, and production claims.

## 9. Initial KPI Hypotheses

Initial KPI/risk directions are hypotheses only:

- agricultural climate risk score by location/time;
- weather exposure indicators;
- crop/risk window indicators;
- advisory status or recommended action category;
- data freshness and completeness by source;
- data quality status by pipeline run.

These must be validated in later phases.

## 10. Initial Source Hypotheses

Potential source groups to investigate later:

- weather/climate APIs;
- Vietnam administrative geography datasets;
- agricultural statistics datasets;
- crop calendar or crop atlas data;
- hydrology/salinity station data if available;
- domain rules or threshold references for advisory logic.

No source is accepted as final until it passes source inventory and evidence review.

## 11. Assumptions and Limitations

Current assumptions:

- Vietnam climate-smart agriculture remains the domain focus.
- Risk monitoring is the primary MVP capability.
- Advisory recommendation is a design direction, not a production claim.
- Analysts are the first implementation consumer.
- Farmer-facing use cases influence the design but may be served after the Gold mart is reliable.

Current limitations:

- Specific crops, regions, KPIs, sources, and grains are not yet finalized.
- Architecture is not finalized.
- Data quality is unknown until source assessment is completed.

## 12. Evidence Required Before Architecture

Before architecture design is finalized, the project needs:

- confirmed MVP domain slice such as crop, risk type, geography, and time grain;
- candidate source inventory;
- source access and licensing notes;
- sample extraction from priority sources;
- profiling evidence for schema, completeness, duplicates, keys, and temporal coverage;
- first KPI/risk/advisory rule candidate;
- documented caveats and limitations.

## 13. Next Workflow Recommendation

Recommended next DEW workflow:

1. **dew-business-discovery** — refine the business/user problem within the closed project scope.
2. **dew-kpi-discovery** — define the first risk/KPI/advisory question.
3. **dew-evidence-check** — separate assumptions from evidence.
4. **source inventory / assessment** — validate candidate sources before architecture.

## 14. Gate Status

**GATE-00 — Project Scope:** Closed.

Closed scope:

CSAV-DP is a portfolio data engineering project about climate-smart agriculture in Vietnam. The MVP prioritizes a Gold data mart as the core data product for analysts, then serves risk monitoring and advisory-style information through a dashboard and web app feature for farmers/end users. Risk monitoring is the primary capability. Action recommendation is included as an advisory direction but must remain evidence-bounded and non-production-grade until validated.
