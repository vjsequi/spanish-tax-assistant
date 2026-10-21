# Delivery backlog

## Foundation completed 21 October 2026

- [x] Select a separate tax-project repository and carry the relevant source context with hashes.
- [x] Record the actual initial product decisions and retain the potential-reviewer dependency.
- [x] Prepare a draft requirements register, HLD/LLD, evaluation plan, security boundaries and staged delivery/operation plan.
- [x] Vendor only the inspected pinned Grill Me pair, with licence and a review receipt.
- [x] Add executable foundation/provenance checks, focused control tests and a CI workflow. See actual [verification](../process/verification.md).

## Visual evidence scope correction 21 October 2026

- [x] Record the owner's PDF-image/screenshot requirement and inspect the referenced native Oposiciones pipeline without executing it.
- [x] Update definition, requirements, HLD/LLD, extraction evaluation and security/telemetry plans. Retain [ADR 0003](../decisions/0003-visual-document-evidence.md) and the [source-specific lessons](../context/document-ingestion-lessons.md).
- [ ] Implement and test PDF rendering, standalone image intake, visual fact extraction and page/region evidence after the agreed feasibility/design gates. No such behaviour or comparative tax-quality result exists yet.

## TAX-001 Product discovery and feasibility design

Requirements: SCOPE-001, FACT-001, RULE-001, REVIEW-001, EVAL-001.

Continue the Grill Me interview. Confirm reviewer participation and representative PDF/image layouts and limits; inspect the full conditions for the two candidate deductions. Refine the definition and freeze the first rubric. Exit with a product definition the owner understands and a feasible review plan. Finding a potential reviewer alone does not close this slice.

## TAX-002 Representative source pack and independent labels

Depends on TAX-001. Author a small synthetic development pack covering the selected formats and conditions. Proposed case types are in [evaluation planning](../evaluation/plan.md); source files and expected answers are not authored yet. Expected answers stay in evals/expected and outside application input. Obtain independent source-derived review and preserve all unresolved treatments. Exit with actual reviewed labels and provenance.

## TAX-003 Reuse assessment and architecture selection

Depends on sufficient TAX-001 findings; can research alongside TAX-002. Assess a visual PDF/image path from the outset and compare it with embedded-text, OCR-assisted and hybrid paths on the same selected documents; assess reuse from invoice reconciliation. Resolve licences before adoption. Choose modules, persistence, provider interfaces and a bounded workflow. Record trade-offs and update HLD/LLD. Do not adopt an unverified full tax engine or portal automation merely to add capabilities.

## TAX-004 First deterministic vertical slice

Depends on TAX-001/002/003. Import supported synthetic PDFs/images, retain originals and versioned page/region evidence, support explicit manual fact confirmation and identify a simple discrepancy without inference. Do not substitute a text-only intake for the agreed visual path. A real vision-model extraction step belongs to separately authorised bounded inference. Add actual domain/security tests and observable failure paths. Demonstrate the output and inspect corrections with the owner.

## TAX-005 AI investigation and controlled comparison

Depends on the baseline and independently reviewed data. Add one bounded interpretation path, exact output validation and a separate scorer. Implement offline doubles first; fresh live authorisation must specify model/provider, calls, duration and money. Compare against the baseline and select complexity from observed failures. Harbor is a candidate adapter, not a substitute for tax labels.

## TAX-006 Shared review UI and recorded employer experience

Depends on actual supported outputs. Use preloaded synthetic cases, source/rule explanations and authentic reviewed recordings. Walk through the experience, inspect the implementation and iterate. Do not present browser state as an actual database commit or a precooked answer as new inference.

## TAX-007 CI release, hosted environments and operation

Depends on accepted product behaviour, security/domain gates and a verified cost/identity design. Package a reproducible artifact, deploy development, promote the same artifact to staging and production, exercise rollback/recovery and inspect redacted telemetry. Require actual authorisation before spend or exposure. Preserve recordings as a separate portfolio experience. Record actual bills, drills and defects; synthetic operation is distinct from external adoption.
