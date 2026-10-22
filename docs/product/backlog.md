# Delivery backlog

## Active slice: TAX-004.1 C001 working product, 22 October 2026

The owner moved the professional reviewer to final QA of the working product; see [ADR 0004](../decisions/0004-development-before-tax-review.md). Earlier review-before-implementation prerequisites below are superseded. Official-source provisional development, engineering tests and synthetic demonstrations proceed now. Independent validation remains unclaimed.

- [x] Retain four additional AEAT guidance pages without replacing the original review source set.
- [x] Implement exact provisional C001 calculation, stage/field worksheet and explicit unsupported/unknown gates.
- [x] Implement visual source inspection, editable/confirmed facts and manual coverage declarations.
- [x] Save/resume local state, reject stale/conflicting writes and compare only confirmed supplied draft fields.
- [x] Export Spanish provisional/partial PDF and JSON packets; retain source/rule versions and audit history.
- [x] Verify partial-save/resume, confirmed calculation, stage expansion and PDF download in the real local UI; render/inspect the six-page packet.
- [x] Verify [hosted CI](https://github.com/vjsequi/spanish-tax-assistant/actions/runs/39750638547) for `1e57ebabd2d111516c7e58431ff5a4a43cf7a4b9`: source/fixture/guidance integrity, lint/format, strict types and 35 engineering tests.

Next: multiple employers and low-income employment branches, then family/relief and required regional deduction branches. Implement the AI/visual adapter and separate engineering evaluator while keeping live inference disabled until bounded authorisation. Arrange the tax professional once the product is working across the agreed scope; their feedback drives final QA fixes.

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

## Detailed specification and source pack prepared 21 October 2026

- [x] Retain fifteen public official references with exact bytes, hashes, metadata and checked BOE selected editions.
- [x] Prepare the source-derived draft: seventeen calculation stages, 108 contextual AEAT fields and 25 rule contracts, linked to the requirement register.
- [x] Record nine unresolved tax-review questions; keep every rule unapproved for application use.
- [x] Author twenty wholly synthetic development cases: 110 source files/180 pages, including the 30-file/100-page workload and visual/security variations.
- [x] Prepare a Spanish review guide, hash-bound requests and a blank independent-answer template; provide a reproducible offline review ZIP.
- [x] Align proposed HLD/LLD with complete calculation, coverage gates and optional draft comparison.
- [ ] Obtain independent rule/applicability/rounding review and source-linked fact, field, stage and stopping-outcome labels. The pack contains no completed judgements.
- [ ] Freeze independently reviewed rules/cases/rubric for final tax validation. Provisional deterministic implementation and engineering comparisons proceed before professional QA under ADR 0004.

## TAX-001 Detailed requirements and legal feasibility

Requirements: SCOPE-001, FACT-001, RULE-001, CALC-001, REVIEW-001, EVAL-001.

The consolidated [definition](definition.md) and [acceptance baseline](acceptance.md) are owner-approved at version 1.0. The [detailed requirements](../requirements/tax-2025.md) map pinned sources, stages, fields and candidate rule contracts. Continue source-derived predicates/rounding specifications alongside implementation. The [nine review questions](../../data/rules/2025/review-questions.json) remain open for final professional QA; unresolved material branches are explicit rather than assumed. Full independent applicability/label review happens under TAX-002 at the end, without blocking provisional engineering. Private reference material remains local and outside this pack.

## TAX-002 Representative source pack and independent labels

Depends on TAX-001. The [synthetic review pack](../../evals/review/reviewer-guide.md) is prepared: twenty cases, with eight proposed for the first professional review round. Source documents and version-bound pending requests exist; independent expected answers and judgements do not. Obtain source-derived labels in the separate scorer/reviewer boundary, record ambiguities/alternatives and review benchmark semantics. Expected answers stay in evals/expected and outside application input. Author a separate sealed final pack later. Exit with actual reviewed labels and provenance; never copy taxpayer details into public inputs/labels.

## TAX-003 Reuse assessment and architecture selection

Depends on sufficient TAX-001 findings; can research alongside TAX-002. Assess a visual PDF/image path from the outset and compare it with embedded-text, OCR-assisted and hybrid paths on the same selected documents; assess reuse from invoice reconciliation. Resolve licences before adoption. Choose modules, persistence, provider interfaces and a bounded workflow. Record trade-offs and update HLD/LLD. Do not adopt an unverified full tax engine or portal automation merely to add capabilities.

## TAX-004 First deterministic vertical slice

Proceed with source-derived feasibility/design under ADR 0004; independent TAX-002 labels are a final QA dependency. C001 now supplies the first provisional local slice; see [its implementation boundary](../design/c001-working-slice.md). Continue general PDF/image admission and visual/AI extraction without substituting a text-only product. A real vision-model step needs separately authorised bounded inference. Add domain/security/recovery tests and observable failure paths for each new branch, then demonstrate and iterate.

This first slice is an intermediate milestone. Further deterministic slices must implement the independently complete tax/refund calculation, intermediate-field checks and safe incomplete-coverage gates required by CALC-001 before the agreed first complete release. A discrepancy demonstration alone does not fulfil that release requirement.

## TAX-005 AI investigation and controlled comparison

Depends on a working deterministic baseline and source-derived development cases. Implement offline interpretation contracts, exact output validation and an isolated provisional scorer now; independent tax labels arrive during final QA. Fresh live authorisation must specify model/provider, calls, duration and money. Compare options using appropriately labelled engineering evidence, then repeat relevant evaluation against reviewed labels. Harbor remains a candidate adapter, not a substitute for tax labels.

## TAX-006 Shared review UI and recorded employer experience

Depends on actual supported outputs. Use preloaded synthetic cases, source/rule explanations and authentic reviewed recordings. Walk through the experience, inspect the implementation and iterate. Do not present browser state as an actual database commit or a precooked answer as new inference.

## TAX-007 CI release, hosted environments and operation

Depends on accepted product behaviour, security/domain gates and a verified cost/identity design. Package a reproducible artifact, deploy development, promote the same artifact to staging and production, exercise rollback/recovery and inspect redacted telemetry. Require actual authorisation before spend or exposure. Preserve recordings as a separate portfolio experience. Record actual bills, drills and defects; synthetic operation is distinct from external adoption.
