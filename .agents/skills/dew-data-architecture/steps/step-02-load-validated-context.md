# Step 02 — Load Validated Context

## Mandatory Rules

- Load all validated/caveated context before architecture design.
- Do not treat assumptions as facts.
- Do not drop caveats from Requirement Gate.
- If evidence is missing for a key claim, label it as caveated or blocked.

## Task

Load validated context for architecture.

## Input discovery

Search for:

- `{planning_artifacts}/**/requirement-gate-report.md`
- `{planning_artifacts}/**/architecture-readiness-matrix.md`
- `{planning_artifacts}/**/caveat-register.md`
- `{planning_artifacts}/**/data-product-prd.md`
- `{planning_artifacts}/**/kpi-feasibility-report.md`
- `{planning_artifacts}/**/source-validation-report.md`
- `{evidence_artifacts}/**/validation-evidence-index.md`
- `{planning_artifacts}/**/.decision-log.md`
- `{learning_artifacts}/**/.learning-log.md`

## Extract

### From Requirement Gate

- final gate decision
- trust expectation
- grain decision
- freshness decision
- accepted caveats
- architecture readiness status

### From KPI Feasibility

- primary KPI statuses
- KPI caveats
- grain implications
- required fields
- sample computation evidence

### From Source Validation

- P1/P2 sources
- source access evidence
- schema evidence
- source grain
- source freshness
- source DQ/profile notes
- source caveats

### From PRD

- data consumers
- data product type
- decisions supported
- MVP scope
- non-goals

## Update documents

Update:

- `data-architecture.md`
- `architecture-caveat-carryover.md`

## Update frontmatter

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-validated-context