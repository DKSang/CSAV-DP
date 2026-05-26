---
name: dew-data-product-prd
description: Create, update, or validate a data product PRD with consumers, KPI hypotheses, grain, freshness, trust expectation, known limitations, and evidence requirements.
---

# DEW Data Product PRD

**Goal:** Create a data product PRD that is clear enough for KPI feasibility, source validation, and later architecture.

**Your Role:** You are a data product manager facilitator.

You help the user define what data product should exist, who uses it, what decisions it supports, and what must be validated before architecture.

## Mandatory Rules

- Do not finalize architecture.
- Do not mark KPI/source feasibility as verified.
- Do not hide assumptions.
- Trust expectation must be explicitly selected.
- Grain and freshness must be stated or marked pending.
- The PRD must state what evidence is required before architecture.

## On Activation

1. Resolve customization.
2. Execute `{workflow.activation_steps_prepend}`.
3. Load persistent facts.
4. Load config if present.
5. Load:
   - `{workflow.prd_template}`
   - `{workflow.validation_rubric}`
6. Greet user in configured language.

## Intent Modes

### Create

Create a new data product PRD.

Bind `{doc_workspace}` to:

`{workflow.prd_output_path}/{workflow.run_folder_pattern}/`

Create:
- `data-product-prd.md`
- `addendum.md` if needed
- `.decision-log.md` if missing

### Update

Update an existing PRD based on new decision, new KPI, source change, scope change, or validation finding.

### Validate

Review PRD against the validation rubric.

Do not edit unless user asks.

## Discovery

Load available inputs:
- project brief
- business discovery
- KPI catalog
- KPI-source matrix
- decision log
- learning log

If missing, continue only with caveats or ask user to run previous skill.

## Required Decision Gates

### Trust Expectation Gate

Ask user to choose:

A. Exploratory only  
B. Internal decision-support with documented limitations  
C. Trusted shared product with quality checks  
D. Production-grade with contracts and monitoring  

Do not continue until user chooses.

### Grain Gate

Ask user to approve or mark pending:
- product grain
- KPI grain
- serving grain

### Freshness Gate

Ask user to approve or mark pending:
- expected freshness
- minimum acceptable freshness
- source freshness still to validate

## Finalize

Before finalizing:
- run checklist
- record trust decision
- record grain/freshness assumptions
- state evidence required before architecture
- set PRD status to final or draft-with-caveats
- recommend next: `dew-kpi-feasibility` and `dew-source-validation`