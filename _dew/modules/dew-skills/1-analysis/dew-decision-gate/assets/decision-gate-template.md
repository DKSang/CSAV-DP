# DECISION GATE: {Gate ID} — {Gate Name}

## Gate Type

Soft Halt / Hard Halt / Safety Halt / Readiness Halt

## Phase

{Phase name}

## Trigger

This gate is triggered when:
- ...

## Why this matters

Explain why this decision affects the project.

Connect the explanation to the data engineering lifecycle:
- Generation / Source Systems:
- Storage:
- Ingestion:
- Transformation:
- Serving:
- Undercurrents:

## Learning explanation

Use this section when `learning_mode = true`.

Explain:
- concept definition
- practical example
- common mistake
- what can go wrong downstream
- what evidence is needed

## Current evidence

| Evidence | Status | Path / Reference |
|---|---|---|
| Artifact | Available / Missing | |
| Sample | Available / Missing | |
| Schema | Available / Missing | |
| Validation | Available / Missing | |
| User decision | Available / Missing | |

## Missing evidence

- ...

## Options

### A. {Option A}

Description:

Pros:
- ...

Cons:
- ...

Choose this when:
- ...

### B. {Option B}

Description:

Pros:
- ...

Cons:
- ...

Choose this when:
- ...

### C. {Option C}

Description:

Pros:
- ...

Cons:
- ...

Choose this when:
- ...

### D. {Option D}

Description:

Pros:
- ...

Cons:
- ...

Choose this when:
- ...

## Recommendation

Recommended option: {A/B/C/D}

Reason:
- ...

## Trade-off summary

| Option | Pros | Cons | Risk | Downstream Impact |
|---|---|---|---|---|
| A | | | | |
| B | | | | |
| C | | | | |
| D | | | | |

## Required user decision

Please choose one:

- A
- B
- C
- D
- R = revise options
- E = explain more
- U = use recommendation

## Resume rule

The agent must stop here.

The agent must not continue until the user explicitly selects an option or says “use recommendation”.

## Decision log update required

After the user chooses, append an entry to `.decision-log.md`.

## Learning log update required

After the user chooses, append a short note to `.learning-log.md` when learning mode is enabled.