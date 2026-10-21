# Delivery backlog

## Foundation completed 21 October 2026

- [x] Select a separate tax-project repository and carry the relevant source context with hashes.
- [x] Record the actual initial product decisions and retain the potential-reviewer dependency.
- [x] Prepare a draft requirements register, HLD/LLD, evaluation plan, security boundaries and staged delivery/operation plan.
- [x] Vendor only the inspected pinned Grill Me pair, with licence and a review receipt.
- [x] Add executable foundation/provenance checks, focused control tests and a CI workflow. See actual [verification](../process/verification.md).
- [x] Push the committed foundation to the owner's existing public GitHub repository and verify the first hosted foundation CI run.

## Visual evidence scope correction 21 October 2026

- [x] Record the owner's PDF-image/screenshot requirement and inspect the referenced native Oposiciones pipeline without executing it.
- [x] Update definition, requirements, HLD/LLD, extraction evaluation and security/telemetry plans. Retain [ADR 0003](../decisions/0003-visual-document-evidence.md) and the [source-specific lessons](../context/document-ingestion-lessons.md).
- [ ] Implement and test PDF rendering, standalone image intake, visual fact extraction and page/region evidence after the agreed feasibility/design gates. No such behaviour or comparative tax-quality result exists yet.

## Product baseline completed 21 October 2026

- [x] Complete the Grill Me product interview and record actual owner answers, excluding private context from Git.
- [x] Obtain explicit shared-understanding confirmation: “Yes, freeze this product baseline.”
- [x] Freeze product/acceptance baseline 1.0 and trace 27 draft detailed requirements, including complete calculation and selected pilot targets.
- [ ] Complete tax-rule feasibility, exact conditions/field mapping and independent validation. Product approval does not close these gates.

## TAX-001 Detailed requirements and legal feasibility

Requirements: SCOPE-001, FACT-001, RULE-001, CALC-001, REVIEW-001, EVAL-001.

The consolidated [definition](definition.md) and [acceptance baseline](acceptance.md) are owner-approved at version 1.0; see [discovery](discovery.md) for the actual confirmation. Specify explicit calculation/deduction conditions, source versions, input/output field mapping and representative layouts with tested engineering limits. The [deduction research](../context/deduction-feasibility.md) and [complete-calculation chain](../context/calculation-feasibility.md) identify source/reviewer work. TAX-002 resolves source-derived label ambiguities before an experimental rubric/case freeze. Exit with a feasible rule/coverage specification and concrete independent review plan. Private validation context stays in ignored local notes, not public quality evidence.

## TAX-002 Representative source pack and independent labels

Depends on TAX-001. Author a small synthetic development pack covering the selected formats, complete-calculation branches and conditions. Proposed case types are in [evaluation planning](../evaluation/plan.md); source files and expected answers are not authored yet. Expected answers stay in evals/expected and outside application input. Obtain independent source-derived review and preserve all unresolved treatments. Separately plan local-only private-reference handling; never copy taxpayer details into public inputs/labels. Exit with actual reviewed labels and provenance.

## TAX-003 Reuse assessment and architecture selection

Depends on sufficient TAX-001 findings; can research alongside TAX-002. Assess a visual PDF/image path from the outset and compare it with embedded-text, OCR-assisted and hybrid paths on the same selected documents; assess reuse from invoice reconciliation. Resolve licences before adoption. Choose modules, persistence, provider interfaces and a bounded workflow. Record trade-offs and update HLD/LLD. Do not adopt an unverified full tax engine or portal automation merely to add capabilities.

## TAX-004 First deterministic vertical slice

Depends on TAX-001/002/003. Import supported synthetic PDFs/images, retain originals and versioned page/region evidence, support explicit manual fact confirmation and identify a simple discrepancy without inference. Do not substitute a text-only intake for the agreed visual path. A real vision-model extraction step belongs to separately authorised bounded inference. Add actual domain/security tests and observable failure paths. Demonstrate the output and inspect corrections with the owner.

This first slice is an intermediate milestone. Further deterministic slices must implement the independently complete tax/refund calculation, intermediate-field checks and safe incomplete-coverage gates required by CALC-001 before the agreed first complete release. A discrepancy demonstration alone does not fulfil that release requirement.

## TAX-005 AI investigation and controlled comparison

Depends on the baseline and independently reviewed data. Add one bounded interpretation path, exact output validation and a separate scorer. Implement offline doubles first; fresh live authorisation must specify model/provider, calls, duration and money. Compare against the baseline and select complexity from observed failures. Harbor is a candidate adapter, not a substitute for tax labels.

## TAX-006 Shared review UI and recorded employer experience

Depends on actual supported outputs. Use preloaded synthetic cases, source/rule explanations and authentic reviewed recordings. Walk through the experience, inspect the implementation and iterate. Do not present browser state as an actual database commit or a precooked answer as new inference.

## TAX-007 CI release, hosted environments and operation

Depends on accepted product behaviour, security/domain gates and a verified cost/identity design. Package a reproducible artifact, deploy development, promote the same artifact to staging and production, exercise rollback/recovery and inspect redacted telemetry. Require actual authorisation before spend or exposure. Preserve recordings as a separate portfolio experience. Record actual bills, drills and defects; synthetic operation is distinct from external adoption.
