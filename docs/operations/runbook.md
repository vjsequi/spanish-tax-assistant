# Operation and release plan

All hosted environments are **unprovisioned**. The current executable surface is repository validation and its local control tests. Run the README commands to inspect that foundation. There is no application service, database migration, cloud endpoint or deployment command yet.

## Intended environments and promotion

Development uses synthetic data and explicit operator budgets. Staging exercises release controls and reviewer scenarios. Production would serve an authenticated owner within supported scope. Keep identities, storage, secrets and rule/corpus versions separate; promote the same immutable application artifact after environment-specific checks.

Implement CI artifact retention and SBOM/dependency/source provenance with application packaging. Add deployable AWS definitions only after identity, supported service-model access, private storage and durable dispatch are designed and locally tested. Promotion needs permission/access tests, tax/evaluation gates, cost bounds, actual smoke tests and rollback/recovery evidence. A failed release must not silently update rules for an existing review.

AWS is preferred if equivalent controls fit the budget; GCP is fallback. Reassess costs for the actual tax workload, including document parsing, model use, storage/backups, telemetry and all environments. Under EUR 10 idle/about EUR 40 active are inherited planning targets, not provisioning permission or a provider guarantee.

## Observability and maintenance

Instrument admission, PDF rendering/image decoding, visual-extraction attempts, auxiliary text/OCR, illegible facts, conflicts, retrieval, validation, pending review, queue age, timeout and recovery using OpenTelemetry. Measure bounded page/image/pixel volume and processing time alongside known provider usage/cost; keep source-specific identities out of metric labels. Separate actual costs from reservations and unknown usage. Bounded labels and redaction protect sensitive text; audit records remain authoritative.

Exercise useful alerts and recovery drills before claiming operation. Define backup/restore, deletion/retention, dependency updates, annual tax-rule updates and rollback. Record actual deployment IDs, artifact hashes, bills, drills and incidents here or linked evidence. Synthetic drills are different from naturally occurring incidents or external adoption.
