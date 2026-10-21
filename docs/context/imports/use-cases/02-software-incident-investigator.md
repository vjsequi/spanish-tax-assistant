---
created: 2026-10-20
status: candidate
tags: [ai, use-cases, operations, aws]
---

# Software Incident Investigator

[Use cases index](00-ai-production-use-cases.md)

Investigate failures in one owned application using bounded telemetry, deployment records, configuration and source context. This is the strongest candidate for personal operation and validation without an external business partner.

## Established example

Sentry's Seer investigates errors using telemetry and source code and supports a workflow toward proposed fixes. The [Sentry case study](https://claude.com/customers/sentry) illustrates the commercial pattern. A first portfolio version would cover a much smaller application and failure catalogue.

## Demonstration case

Document imports begin failing after a deployment. The investigator checks the failure timeline, recent configuration changes, storage access, parser errors and database connectivity. It produces supported hypotheses, identifies missing evidence and recommends the next diagnostic step.

## First scope

Support one application and one cloud architecture. Begin with a defined set of failures such as a revoked storage permission, a database connection failure, a parser regression and a downstream timeout. Use read-only diagnostic tools with explicit scope and execution limits. Keep remediation under separate approval.

## Security and operation

Use least-privilege diagnostic identities. Remove secrets and sensitive payloads from model context and routine logs. Treat source comments and log content as untrusted input. Scope investigation to the selected application and environment.

The investigator must remain diagnosable when its own dependencies fail. Bound retries, retain partial results and report unavailable telemetry. An incident alert should not cause unlimited duplicate investigations or model spending.

## Evaluation

Create controlled faults with known causes and independently specify expected observations and acceptable conclusions. Measure diagnosis correctness, evidence support, useful next steps, unsafe recommendations, time to a useful diagnosis and cost. Include ambiguous cases where the correct response is to request more evidence.

Separate controlled drills from naturally occurring incidents. Avoid leaking the injected fault label into the investigator's context. Compare fixed diagnostic checks plus model synthesis against an agent choosing bounded diagnostic tools.

## Main dependency

Useful instrumentation and reproducible failures. Vicente can be the real operator, but broader business-value claims would need additional usage evidence. Keep initial scope to diagnosis so that automatic code modification and deployment do not become prerequisites.
