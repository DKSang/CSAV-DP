# Step 06 — Risk, Caveat, and Reversibility Review

## Mandatory Rules

- Do not hide Requirement Gate caveats.
- Do not convert caveats into solved problems.
- Every hard-to-reverse decision needs a revisit trigger.
- Every high-risk caveat needs owner or later skill responsibility.

## Task

Review risks, caveats, and reversibility.

## Caveat carryover

For each caveat from Requirement Gate:

| Caveat ID | Area | Description | Architecture Impact | Later Skill Responsible |
|---|---|---|---|---|

Assign later skill:
- dew-storage-design
- dew-ingestion-design
- dew-transformation-design
- dew-serving-design
- dew-governance-security-design
- dew-create-data-story

## Architecture risks

Record:

| Risk ID | Risk | Severity | Mitigation | Owner / Later Skill |
|---|---|---|---|---|

Risk areas:
- source access instability
- source schema drift
- grain mismatch
- freshness mismatch
- DQ uncertainty
- cost/complexity
- operational burden
- privacy/security
- platform lock-in
- local/cloud drift

## Reversibility

Record:

| Decision | Reversibility | Why | Revisit Trigger |
|---|---|---|---|

Classify:
- Easy
- Medium
- Hard

## Update documents

Update:
- `data-architecture.md`
- `architecture-caveat-carryover.md`
- `architecture-decision-record.md`

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-validated-context
  - step-03-lifecycle-architecture
  - step-04-architecture-pattern-gate
  - step-05-technology-decision-gate
  - step-06-risk-caveat-and-reversibility