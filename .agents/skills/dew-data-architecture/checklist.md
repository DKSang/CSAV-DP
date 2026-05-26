# Data Architecture Checklist

## Required inputs

- [ ] Requirement Gate Report loaded.
- [ ] Architecture readiness is approved or approved-with-caveats.
- [ ] Data Product PRD loaded.
- [ ] KPI Feasibility Report loaded.
- [ ] Source Validation Report loaded.
- [ ] Evidence Index loaded or missing evidence recorded.
- [ ] Decision Log loaded or initialized.
- [ ] Learning Log loaded or initialized.

## Validated context

- [ ] Business decision captured.
- [ ] Data consumer captured.
- [ ] Trust expectation captured.
- [ ] MVP scope captured.
- [ ] Non-goals captured.
- [ ] Caveats carried over.

## Lifecycle architecture

- [ ] Source/generation architecture summarized.
- [ ] Storage intent summarized.
- [ ] Ingestion intent summarized.
- [ ] Transformation intent summarized.
- [ ] Serving intent summarized.
- [ ] Undercurrents summarized.

## Architecture decisions

- [ ] Architecture pattern options compared.
- [ ] User approved selected architecture pattern.
- [ ] Technology decision options compared.
- [ ] User approved technology direction.
- [ ] ADRs created.
- [ ] Rejected alternatives documented.
- [ ] Reversibility documented.
- [ ] Revisit triggers documented.

## Caveats and risks

- [ ] Requirement Gate caveats carried over.
- [ ] Architecture risks documented.
- [ ] Caveat owners / later skills assigned.
- [ ] No caveat hidden or silently removed.

## Finalization

- [ ] data-architecture.md completed.
- [ ] architecture-decision-record.md completed.
- [ ] architecture-caveat-carryover.md completed.
- [ ] Decision log updated.
- [ ] Learning log updated if learning mode is enabled.
- [ ] Next skills identified.
- [ ] No unresolved hard HALT remains.

## Failure conditions

Fail this workflow if:
- Requirement Gate is missing.
- Requirement Gate is blocked.
- Architecture proceeds without user approval.
- Unvalidated KPI/source assumptions become architecture facts.
- Technology is selected without trade-off explanation.
- Caveats from Requirement Gate are dropped.