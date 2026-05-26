# Step 05 — Trust, Grain, and Freshness Gates

## Mandatory Rules

- Stop for user decisions.
- Trust expectation must be explicitly selected.
- Grain must be approved or caveated.
- Freshness must be approved or caveated.
- Do not proceed to architecture readiness gate until these gates are resolved.

## Task

Resolve three core readiness gates:

1. Trust Expectation Gate
2. Grain Gate
3. Freshness Gate

---

## Gate 1 — Trust Expectation

Explain:

Trust expectation defines how much confidence downstream consumers can place in the data product.

Options:

A. Exploratory only  
B. Internal decision-support with documented limitations  
C. Trusted shared product with quality checks  
D. Production-grade with contracts and monitoring  

Recommend based on current artifacts.

Ask user to choose.

Do not continue until user chooses.

Update:

```yaml
decisionGates:
  GATE-05-trust-expectation:
    status: approved / approved-with-caveats