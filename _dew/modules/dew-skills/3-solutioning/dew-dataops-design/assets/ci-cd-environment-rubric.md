# CI/CD and Environment Rubric

## Manual / learning mode

Use when:
- project is still exploratory
- no recurring schedule
- user runs scripts/notebooks manually

## Lightweight CI

Use when:
- code is versioned
- tests should run before merge
- DQ/source contract tests exist

## Full deployment pipeline

Use when:
- cloud workspace or production-like environment exists
- multiple environments are needed
- deployment should be controlled

## Environment strategy

Common stages:
- local
- dev
- test
- prod

Minimum for DEW:
- document where code runs
- document where data lives
- document how configs/secrets are managed
- document how evidence is generated
