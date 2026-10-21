# Independent review request: synthetic 2025 development pack

**Pending review.** The [input manifest](../inputs/manifest.json) contains twenty wholly authored synthetic cases, 110 source files and 180 source pages. C018 alone has thirty documents/one hundred pages. PDFs, PNG/JPEG images, an image-only PDF and a deliberately degraded image exercise the visual direction; none establishes measured extraction quality. No private reference material was used.

The [PDF guide](../../output/pdf/tax-2025-review-guide.pdf) inventories every case without supplying its calculated answer. The first review wave is **C001, C002, C003, C004, C008, C010, C011, C012**. Review the remaining variations afterwards; the benchmark needs semantic review before it can count as quality evidence. These are exposed development/regression cases, not held-out final tests.

## Materials and roles

- [Rule/source requirements](../../docs/requirements/tax-2025.md), [retained reference set](../../data/rules/2025/README.md), [field map](../../data/rules/2025/aeat-fields.json) and [open questions](../../data/rules/2025/review-questions.json).
- [Review request](review-request.json): input/source hashes, wave, construction intent and pending status. Construction intent describes software-authored variations, not independent tax truth.
- [Blank answer template](answer-template.json): no expected values, decisions or reviewer details have been prefilled.
- Authoring instructions/data live outside case inputs under `evals/authoring`. Application/model context may receive the selected case's documents and legitimate case context only; it must not receive construction metadata, review templates/requests or expected answers.

The owner shares the package and arranges review themselves. No message, invitation or publication to a professional is performed by this repository workflow. Reviewer participation, competence and judgements must be recorded when actually obtained; no account/collaboration feature is implied.

## Review procedure

1. Verify source editions, original amendment applicability and unresolved rule questions. Pinning is not legal sign-off. Resolve a material ambiguity or retain it as blocking the affected branch.
2. Inspect original visual documents. Transcribe relevant values and their page/image support; distinguish gross income, net cash, withholding, payments on account, period, source version and ownership. Describe actual illegibility rather than guess a digit.
3. Check completeness, contradictory/replaced sources and unsupported circumstances. Missing material facts must not become zero or false. State useful questions and valid alternatives.
4. Independently derive the supported calculation: each intermediate field/stage, national/regional treatment, exact rounding and final result when completeness permits. Validate individual fields even if totals happen to agree.
5. Check each proposed field mapping and repeated person/payer/annex context against the retained form. A synthetic partial draft is an unverified comparison source, not the expected answer. The package deliberately supplies no complete draft tax total.
6. Record evidence-linked facts, field/stage expectations, permitted questions/alternatives, safety/scope outcomes, unresolved conditions, source hashes and input hash. Review negative, incomplete and attack-containing inputs as well as ordinary cases.
7. Complete reviewer identity/competence, actual date and sign-off only after review. A software-authored answer, schema-valid record or owner's product approval is not independent validation.

Use the blank template in a separate review workspace. Approved synthetic labels belong under `evals/expected` for the separate scorer/reviewer; do not paste them into application prompts, source documents or case metadata. Private reference files and labels remain local and outside this synthetic/public pack. The implementation/model context must never read expected-answer files.

## Coverage and limits

| Variation group | Authored material for review |
|---|---|
| Ordinary / multiple payers | Cash income, Social Security, union/professional fees, annual allowance and duplicate aggregation risks |
| Benefits/pensions | In-kind valuation, payments on account/recovery, genuine employer versus employee amounts and corroborating certificates |
| Income boundaries | Low employment income; distinct Article-20 reduction and 2025 liability credit; gross/net bank interest |
| Version/missing evidence | Issuer-declared replacement and missing certificate/amount |
| Regional benefits | Rent conditions, unknown household/property facts, educational services, other claimants and maternity/advance interactions |
| Donations | Multiple entities, history, classification and regional third-sector claim |
| Scope/security | Prior losses; embedded instructions; supplied other-year/region note; visual representation/legibility variations |
| Workload | C018 is exactly thirty files/one hundred pages, including meaningful monthly statements, education details and corroborating annual records; this is not a latency result |

All identifiers/entities/transactions are fictional and marked synthetic. No valid taxpayer identifier, real IBAN/address or real employer/customer record is intended. These simplified layouts are authored approximations, not validated coverage of real institutions or authentic AEAT forms. A production parser must not treat synthetic document markers as proof of authenticity.

C016 pairs C001's first three source documents for representation testing only; C001's partial draft has no C016 counterpart. Compare matched source extraction separately from downstream tasks. C017's legibility labels require actual visual review; the author's pre-blur text is not a validated readable-fact denominator.

The final evaluation pack must be newly authored, independently reviewed and structurally separate after candidate selection. Report complete planned/attempted/failed/skipped/pending-review denominators. Do not advertise pilot percentages, tax correctness or reviewer-time savings from this preparation work.
