# Evaluation plan

Begin with a small synthetic development pack and independently reviewed, source-derived expectations. A potential tax reviewer exists, but no case labels or review judgements have been obtained. No tax cases are authored in the bootstrap. The following are **proposed case types**, not a dataset or held-out reservations.

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

Select on development data, lock the candidate, then author and seal structurally separate final cases. An inspected demonstration is a regression example, not a fresh held-out result. Authored software responses verify plumbing only. Real provider comparisons need fresh explicit model/cost/call/time authorisation; current live allowance is zero.
