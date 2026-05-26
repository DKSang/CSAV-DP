# Monitoring and Alerting Rubric

## Minimal monitoring

Use when:
- learning/portfolio project
- manual runs
- low trust expectation

Monitor:
- run success/failure
- basic row counts
- obvious errors

## Internal monitoring

Use when:
- internal decision-support
- scheduled pipeline
- DQ matters

Monitor:
- source access
- schema drift
- freshness
- row counts
- critical DQ rules
- output availability

## Production monitoring

Use when:
- trusted shared or production-grade product
- multiple consumers
- SLA/contract exists

Monitor:
- pipeline runtime
- latency
- freshness SLA
- DQ SLA
- incident alerts
- access/security events
- cost/resource usage
