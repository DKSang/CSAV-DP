# Source Validation Checklist

## Required inputs

- [ ] Source inventory loaded.
- [ ] Source scorecard loaded.
- [ ] KPI catalog loaded or context provided.
- [ ] KPI-source matrix loaded or reconstructed.
- [ ] Data product PRD loaded or context provided.

## Access evidence

- [ ] Access method documented.
- [ ] Access check completed or blocked reason documented.
- [ ] Access evidence path recorded.
- [ ] HALT-05 triggered if access unverified for P1 candidate.

## Sample evidence

- [ ] Source sample exists or missing reason documented.
- [ ] Sample path recorded.
- [ ] Sample metadata recorded.
- [ ] Sample caveats documented.

## Schema evidence

- [ ] Schema snapshot exists or missing reason documented.
- [ ] Fields listed.
- [ ] Required KPI fields mapped.
- [ ] Schema evolution recommendation documented.

## Grain and freshness

- [ ] Source grain assessed.
- [ ] Target KPI/product grain compared.
- [ ] Freshness requirement compared with observed freshness.
- [ ] Grain/freshness caveats documented.

## Quality/profile

- [ ] Basic profile completed or missing reason documented.
- [ ] Nulls/duplicates/ranges reviewed where applicable.
- [ ] Quality risk assigned.

## Decision

- [ ] Recommended source status assigned.
- [ ] User approves final status.
- [ ] Decision log updated.
- [ ] Learning log updated if learning mode is enabled.
- [ ] Evidence index updated.
- [ ] No source promoted to P1 without access/sample/schema evidence.