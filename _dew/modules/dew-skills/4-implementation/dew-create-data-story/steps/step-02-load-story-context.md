# Step 02 — Load Story Context

## Mandatory Rules

- Load all design artifacts relevant to the story.
- Do not invent missing implementation context.
- If context is missing, trigger HALT-17.

## Task

Create story context pack.

## Extract based on story layer

### Foundation story

Load:
- data architecture
- dataops runbook
- governance/security
- implementation conventions

### Source access / ingestion story

Load:
- source validation
- storage design
- ingestion design
- source contract tests
- evidence index

### Transformation story

Load:
- transformation design
- data model spec
- DQ rules
- ingestion outputs

### Gold/KPI story

Load:
- KPI feasibility
- transformation design
- data model spec
- KPI-to-model mapping
- DQ rules

### Serving story

Load:
- serving design
- metric contract
- trust limitations
- governance/access

### DataOps story

Load:
- dataops runbook
- observability plan
- operational readiness report

## Create

Create:

`{workflow.story_context_output_path}/{story_id}-context.md`

## Continue checkpoint

Ask:

`[C] Continue to create story`
