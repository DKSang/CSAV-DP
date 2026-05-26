# Step 07 — DataOps, Security, and Governance Undercurrents

## Mandatory Rules

- Architecture must include undercurrents.
- Do not leave security/privacy as afterthoughts.
- Do not design full governance here; capture architecture-level responsibilities and defer details.

## Task

Review FDE-style undercurrents at architecture level.

## Undercurrent review

### Security

Record:
- data sensitivity
- access control direction
- secrets handling
- network/auth assumptions
- encryption direction if relevant

### Privacy

Record:
- PII/sensitive data status
- privacy posture
- minimization expectation
- retention caveats

### Data Management

Record:
- metadata expectations
- lineage expectations
- ownership
- catalog/documentation needs

### DataOps

Record:
- orchestration direction
- CI/CD direction
- environment strategy
- deployment path

### Observability

Record:
- logging
- monitoring
- alerting
- data quality checks
- freshness checks

### Software Engineering

Record:
- repo structure direction
- testing approach
- code review expectation
- modularity
- configuration management

### Cost / FinOps

Record:
- cost risks
- local-first cost advantage if applicable
- cloud cost triggers
- scaling thresholds

## Update document

Update:
- `data-architecture.md`

Update frontmatter:

```yaml
stepsCompleted:
  - step-01-init
  - step-02-load-validated-context
  - step-03-lifecycle-architecture
  - step-04-architecture-pattern-gate
  - step-05-technology-decision-gate
  - step-06-risk-caveat-and-reversibility
  - step-07-dataops-security-governance-undercurrents