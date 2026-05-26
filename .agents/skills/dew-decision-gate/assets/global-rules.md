# DEW Global Rules

## Core Rule 1 — Agent may recommend, but must not decide

The agent may analyze, explain, compare options, and recommend one option.

The agent must not silently make project-shaping decisions for the user.

Project-shaping decisions include:
- project scope
- business objective
- data consumer
- KPI definition
- KPI grain
- KPI feasibility
- source acceptance
- source priority
- trust expectation
- freshness
- architecture pattern
- technology choice
- storage layer
- ingestion pattern
- schema evolution
- transformation rule
- data quality rule
- serving mode
- privacy/security posture
- implementation readiness
- learning closure

For every project-shaping decision, the agent must:
1. Stop.
2. Explain the concept briefly.
3. Show current evidence.
4. Present options.
5. Recommend one option.
6. Explain trade-offs.
7. Ask the user to choose.
8. Wait for explicit user confirmation.
9. Record the decision in `.decision-log.md`.

The agent may recommend, but must not decide.

## Core Rule 2 — No phase is done without evidence

A phase is not complete just because an artifact was written.

A DEW phase is complete only when it has:
- artifact
- validation evidence
- decision log entry
- learning note
- next-phase readiness statement

Planning artifacts are not evidence.

Evidence may include:
- successful API call log
- downloaded source sample
- schema snapshot
- profiling report
- executable SQL/Python notebook
- source contract test
- data quality test result
- sample KPI output
- validation report
- user-approved decision log entry

If evidence is missing, the agent must trigger a HALT.

## Core Rule 3 — No architecture before KPI/source validation

The agent must not create final architecture, storage, ingestion, transformation, or serving designs until:
- primary KPI feasibility is verified or explicitly caveated
- P1 sources are access-verified
- source sample/schema evidence exists
- grain is approved by the user
- trust expectation is approved by the user
- freshness expectation is approved by the user

If these are missing, trigger:

`HALT-10 — Architecture Before Validation`

## Core Rule 4 — Decision gates are mandatory learning points

Every critical decision must pass through a Decision Gate.

At each Decision Gate, the agent must:
- explain why the decision matters
- connect the decision to the data engineering lifecycle
- show current evidence
- present options
- recommend one option
- explain trade-offs
- ask the user to choose
- wait for explicit confirmation
- record the final decision

## Core Rule 5 — Preserve uncertainty

If something is unknown, the agent must label it as:
- Unknown
- Assumption
- Needs validation
- Deferred
- Rejected
- Use with caveats

The agent must not convert assumptions into facts.