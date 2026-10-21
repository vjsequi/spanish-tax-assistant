# Low level design

**Proposed interfaces, not implemented schemas.** Refine these after the representative formats and supported treatments are agreed.

## Core records

| Record | Required identity and state |
|---|---|
| Case | Authorised owner/workspace, tax year 2025, jurisdiction, profile, state and version |
| Source | Private immutable original, content hash, type, parser version and exact extraction spans |
| Fact | Typed value, unit/period, provenance, confirmation state and conflicting alternatives |
| Rule | Supported treatment, year/region, official source and version, prerequisites and exact calculation/rounding |
| Investigation | Input snapshot, workflow/model/prompt/schema versions, bounded attempts and outcome |
| Proposed change | Draft field, prior/new value, fact/rule references, calculation, source digest and pending status |
| Review event | Reviewer authority, exact proposal digest, decision, idempotency key, timestamp and new case version |

## Execution contract

1. Authorise the case and stage bounded supported documents. Parse in a resource-limited process; preserve originals privately and source spans. A parser process alone is not an OS sandbox.
2. Confirm facts or retain unresolved conflict. Evaluate scope from actual circumstances; unknown information is not false or zero.
3. Snapshot case/source/rule versions and enqueue durably. Claim with an opaque fence and bounded recovery policy.
4. Prepare authorised context, reserve provider work and execute outside a database transaction. Bound retrieval steps, output size, time, calls and money. Do not retry an uncertain charged request automatically.
5. Validate typed output, scope, source membership, quotations and exact deterministic treatments. Semantic support still needs evaluation and human review.
6. Recheck source/case versions and active-run authority before publishing a pending change. Changed evidence supersedes old work.
7. A separate review command validates current membership, versions and exact digest inside a transaction, then appends a review event. Model output cannot approve or submit a return.

Parse money from exact decimal text; use integer minor units and explicit Decimal arithmetic where rule rounding requires it. Select rounding stages per reviewed treatment, not a global rounding shortcut. No rule rates or tax thresholds are implemented in the bootstrap.

Diagnostic attributes are bounded operation/outcome/version categories. Protected traces may carry opaque correlation; routine telemetry never carries evidence, prompt/response text, taxpayer IDs or raw exception payloads. Durable audit and source provenance survive telemetry failure independently.
