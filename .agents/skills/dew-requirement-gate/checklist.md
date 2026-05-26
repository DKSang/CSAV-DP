# Requirement Gate Checklist

## Required input artifacts

- [ ] Project brief loaded or context provided.
- [ ] Business discovery loaded or context provided.
- [ ] Data product PRD loaded or context provided.
- [ ] KPI catalog loaded.
- [ ] KPI feasibility report loaded.
- [ ] Source inventory loaded.
- [ ] Source validation report loaded.
- [ ] Evidence index loaded or missing evidence recorded.
- [ ] Decision log loaded or initialized.
- [ ] Learning log loaded or initialized.

## Business readiness

- [ ] Data consumer is clear.
- [ ] Business decision is clear.
- [ ] Data product type is clear.
- [ ] MVP scope is clear.

## KPI readiness

- [ ] Primary KPIs identified.
- [ ] Primary KPIs have feasibility status.
- [ ] Primary KPIs are not silently treated as verified.
- [ ] KPI caveats are listed.
- [ ] KPI blockers are listed.
- [ ] User has approved KPI readiness or return path.

## Source readiness

- [ ] P1/P2 candidates identified.
- [ ] P1 sources have access/sample/schema evidence or caveat.
- [ ] Source caveats are listed.
- [ ] Source blockers are listed.
- [ ] User has approved source readiness or return path.

## Trust, grain, freshness

- [ ] Trust expectation selected.
- [ ] Product/KPI grain approved or caveated.
- [ ] Source grain compatibility reviewed.
- [ ] Freshness requirement reviewed.
- [ ] Observed source freshness reviewed or caveated.
- [ ] Schema evolution direction known or caveated.

## Caveat handling

- [ ] Caveat register created.
- [ ] High severity caveats are explicitly approved or block the gate.
- [ ] Downstream impact documented.
- [ ] Revisit triggers defined.

## Architecture readiness

- [ ] Architecture readiness matrix completed.
- [ ] Final gate decision selected by user.
- [ ] Decision log updated.
- [ ] Learning log updated if learning mode is enabled.
- [ ] Evidence index referenced.
- [ ] No unresolved hard HALT remains.

## Failure conditions

Fail this gate if:
- architecture readiness is approved without user choice
- primary KPI is unresolved with no caveat
- P1 source is unresolved with no caveat
- trust expectation is missing
- grain is undefined
- freshness is material and unknown
- evidence is missing and not caveated
- caveats are hidden