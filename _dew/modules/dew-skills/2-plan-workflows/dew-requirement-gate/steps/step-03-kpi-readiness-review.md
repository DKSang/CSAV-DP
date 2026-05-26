# Step 03 — KPI Readiness Review

## Mandatory Rules

- Do not mark a KPI ready without feasibility status.
- Primary KPI cannot remain `Hypothesis only` unless user explicitly accepts caveated continuation or defers it.
- Missing KPI evidence must trigger `HALT-03` or `HALT-18`.

## Task

Review whether KPI requirements are ready for architecture.

## For each primary KPI

Review:

| KPI ID | KPI Name | Feasibility Status | Evidence | Caveat | Architecture Impact |
|---|---|---|---|---|---|

## Allowed KPI readiness statuses

- Ready
- Ready with caveats
- Blocked
- Deferred
- Rejected

## Decision cases

### Ready

Use when:
- KPI is verified on sample
- or feasible with caveats approved

### Ready with caveats

Use when:
- sample validation exists but limitations remain
- user accepts caveats
- downstream impact is clear

### Blocked

Use when:
- KPI is hypothesis only
- required fields unresolved
- formula/grain unclear
- sample computation missing

### Deferred

Use when:
- KPI removed from MVP by user decision

### Rejected

Use when:
- KPI is invalid or not feasible

## If primary KPI is blocked

Trigger:

`HALT-03 — KPI Feasibility Not Proven`

Options:
A. Return to KPI feasibility  
B. Continue with caveat  
C. Defer KPI  
D. Reduce MVP scope  

## Update report

Update KPI Readiness section.

Update caveat register if caveats exist.

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-validated-context
  - step-03-kpi-readiness-review