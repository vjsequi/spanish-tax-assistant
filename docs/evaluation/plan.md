# Evaluation plan

Begin with the [prepared synthetic development pack](../../evals/review/reviewer-guide.md) and independently reviewed, source-derived expectations. Twenty cases now contain 110 source files/180 pages, including the 30-file/100-page benchmark. Eight initial cases are proposed for the first review round; the remaining twelve cover further conditions, ambiguity, visual variants, security and workload. No independent synthetic labels or review judgements have been obtained. Private reference material has not been inspected or copied. The following categories motivated the exposed development pack; they are not held-out reservations or proof of complete coverage.

| Proposed case | What the evaluation should distinguish |
|---|---|
| Consistent salary and withholding | Correct facts and no unnecessary amendment |
| Revised salary certificate | Version conflict handled without assuming which source wins |
| Missing bank-interest certificate | Useful request rather than invented amounts |
| Bank-interest/draft mismatch | Supported field comparison and exact difference |
| Childcare candidate with sufficient records | Full reviewed conditions and correct supported treatment |
| Childcare candidate with missing conditions | Specific question or referral |
| Rent candidate with sufficient records | Full reviewed conditions and correct supported treatment |
| Rent candidate with conflicting eligibility evidence | Conflict preserved and useful escalation |
| Foreign or complex income | Correct scope referral without silently dropping income |
| Malicious instructions or wrong-year rule | Permission boundary and year/region filtering remain effective |

Keep inputs under evals/inputs and expected answers under evals/expected. Only the independent scorer/reviewer receives expected answers. Models and application inputs must not read them. Source hashes, labels, alternative valid outcomes and security/resolvability annotations need review before freezing an experiment.

Compare checklist/rules, prepared retrieval plus a fixed model call, and bounded agent-directed retrieval. Hold evidence and declared tasks constant, and separate workflow policy, framework choice and model choice. Add agents only for an observed failure hypothesis. Use actual attempt/failed/skipped/completed denominators, pending human review, proposal precision/coverage and safe referral accounting.

Check individual facts, field changes, rule applicability and unsupported deductions/omissions as well as totals. Measure reviewer corrections and time. Classify failures into extraction, retrieval, outdated rules, missing/conflicting facts, reasoning, validation and recovery. Known cost, unavailable cost and reservations are different quantities.

The owner requires an independent complete calculation for fully covered cases. Validate each deterministic stage through the final payable/refundable balance against independently reviewed expectations; copied AEAT totals and cancelling field errors fail. Include multiple payers, benefits in kind, supported family branches and incomplete-coverage gates. This calculator is a separately evaluated foundation shared by the rules/AI variants, not LLM arithmetic. Evaluate evidence organisation, draft checking and supported deduction discovery separately and end to end. The approved [acceptance baseline](../product/acceptance.md) sets provisional targets: at least 95% required readable-fact extraction with correct evidence, automated processing within five minutes in at least 95% of attempts on the 30-file/100-page workload, and at least 20% less hands-on review time. They remain unmeasured; calculation and safety checks are blocking regardless of these percentages.

Select on development data, lock the candidate, then author and seal structurally separate final cases. An inspected demonstration is a regression example, not a fresh held-out result. Authored software responses verify plumbing only. Real provider comparisons need fresh explicit model/cost/call/time authorisation; current live allowance is zero.

## Document representation comparison

The owner selected visual PDF/image support from the outset. Separate this product requirement from a claim that a particular visual model is superior. Evaluate the same semantic documents as digital PDFs, image-only/scanned PDFs and screenshots. Include layout variants, ambiguous amount columns, decimal commas/signs, low resolution, rotation, cropped headers, footnotes, duplicate images and unreadable facts.

Compare (a) embedded text plus the fixed extractor on digital PDFs, (b) OCR plus that extractor on image-only inputs, (c) rendered-page/standalone-image interpretation, and optionally (d) a hybrid. A scan with no text layer must not become a deliberately empty text baseline. Keep source facts/labels identical across representations and retain preprocessing/model/prompt settings and actual resource use. Freeze extracted facts when comparing downstream workflows so retrieval-policy effects are not confused with intake differences.

Score exact fact/field values and their source/page/region support, missed issues, invented readings, useful clarification and time spent confirming/correcting values. Inspect monetary columns and individual treatments, not only totals. Measure preprocessing time, provider duration, image/page counts, known usage/cost and unknowns separately. The Oposiciones implementation and tests do not establish tax extraction quality. This comparison remains planned, with zero live allowance.
