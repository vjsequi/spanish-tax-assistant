# Initial product definition

**Version 0.1, 21 October 2026.** This draft incorporates actual owner decisions. Detailed deduction coverage, UI and release acceptance remain under discovery.

## User and useful outcome

An individual preparing their Spanish personal income-tax return needs to establish that a draft agrees with their records and that proposed treatments have support. The first application helps them find missing or conflicting facts, understand proposed corrections and review an evidence packet before manual submission in Renta WEB.

The first supported profile is a common-regime resident employee in the Balearics, for tax year 2025, with employment income, bank interest and selected deductions. The owner explicitly confirmed this bounded profile, year and review-packet deliverable. Childcare/conciliation expenses and habitual-home rent are approved for investigation as feasibility candidates; their conditions and implementation are not validated yet. The profile is a product boundary, not a claim about the owner's personal eligibility.

## First complete journey

1. Open a synthetic demonstration case, or later create a private authenticated case for the supported profile.
2. Supply salary certificates, bank-interest records, relevant receipts and an AEAT draft through supported local formats.
3. Review extracted facts and resolve conflicting versions or missing documents.
4. Inspect discrepancies and candidate deductions using official material filtered to 2025 and the Balearics.
5. Inspect each proposed field change, supporting evidence, rule and deterministic calculation. Ask a specific question or refer unsupported circumstances.
6. Accept, correct or defer changes; export a review packet. The person handles the official submission.

A potential qualified reviewer has been identified by the owner. Their availability, remit and independent case judgements remain to confirm.

## Product boundaries

Start with evidence and field review, rather than requiring a complete return-calculation engine. Totals may be compared with supplied draft values or validated supported calculations. A complete tax bill must not be implied when only selected fields are covered.

Foreign income, business activity, complex investment disposals, other regimes/regions/years and corporate taxes require explicit scope referral until separately supported. A selected bank-interest context does not imply support for all investment taxation. Automated AEAT access, XML import, signature and filing are later integrations.

The public employer experience uses synthetic preloaded examples without uploads or sign-in. Any real-data hosted owner workspace requires authentication and private access. A production-like deployment is a later measured milestone, with development/staging/production and a fresh cost assessment.

## Why AI and what stays deterministic

Use AI for varied document understanding, choosing bounded evidence retrieval, resolving language ambiguity through questions, and explaining supported facts. Calculations, eligibility conditions, year/region filtering, permissions, source freshness and review authority remain explicit versioned code. A model's confidence or an authentic quote alone does not establish correct tax treatment.

## Initial acceptance criteria to refine

- Supported fields link to exact source spans; missing and conflicting facts remain visible.
- Each proposed change identifies applicable year/region, rule version, evidence and calculation. Unsupported claims or deductions block acceptance.
- Unknown conditions cause useful questions or referral. Repeating work does not duplicate a committed review decision, and changed evidence invalidates stale proposals.
- Independent tax review checks individual fields and treatments as well as totals. No tax-quality result exists at bootstrap.
- Compare checklist/rules, prepared retrieval plus one call and bounded agent retrieval on frozen reviewed cases. Measure harmful errors, missed issues, useful questions, reviewer corrections/time, latency and known cost.
- Demonstrate permissions, recovery, redaction and reproducible delivery in each environment before claiming hosted operation.

Numerical quality, timing and value targets will be frozen with a reviewed rubric and experiment plan. The invoice project's seven-case results and targets are historical context, not transferred tax evidence.
