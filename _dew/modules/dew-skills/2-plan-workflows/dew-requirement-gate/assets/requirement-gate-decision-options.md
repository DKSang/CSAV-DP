# Requirement Gate Decision Options

## A. Proceed to architecture

Use when:
- KPI readiness is sufficient
- source readiness is sufficient
- trust, grain, and freshness are approved
- caveats are minor or none
- evidence is indexed

Meaning:
Architecture can begin normally.

## B. Proceed to architecture with caveats

Use when:
- some evidence is partial
- risks are understood
- user accepts caveats
- downstream impact is documented

Meaning:
Architecture can begin, but must carry caveats explicitly.

Required:
- caveat register updated
- decision log updated
- architecture artifact must include caveats

## C. Return to KPI validation

Use when:
- primary KPI is still hypothesis only
- required fields are unverified
- formula or grain is unclear
- sample computation is missing

Meaning:
Do not start architecture.

Recommended workflows:
- dew-kpi-feasibility
- dew-kpi-prototype
- dew-kpi-validation-review

## D. Return to source validation

Use when:
- P1 source access is unverified
- sample/schema is missing
- source grain/freshness is unknown
- source trust is not established

Meaning:
Do not start architecture.

Recommended workflows:
- dew-source-validation
- dew-source-access-check
- dew-source-sampler
- dew-source-contract-test

## E. Reduce MVP scope

Use when:
- current MVP depends on unresolved KPI/source
- simpler scope can proceed safely
- user prefers progress over full scope

Meaning:
Update PRD/KPI/source scope before architecture.