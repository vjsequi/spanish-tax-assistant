---
created: 2026-10-20
status: candidate
tags: [ai, use-cases, finance]
---

# Invoice Exception Investigator

[Use cases index](00-ai-production-use-cases.md)

Investigate differences between supplier invoices, purchase orders, delivery records and correspondence. This extends the finance direction from incoming-payment matching into evidence gathering and exception review.

## Established example

[Rossum's customer stories](https://rossum.ai/customer-stories/) describe invoice automation at Wolt, Adyen, Eurowag and other businesses. [Rossum's purchase-order matching documentation](https://knowledge-base.rossum.ai/help/docs/two-way-po-matching-with-custom-function) describes comparing captured invoice data with purchase-order records. These establish adjacent document-processing workflows; the investigation proposed here would require its own validation.

## Demonstration case

An invoice charges for ten units. The delivery record confirms eight, and an email says the remaining two were cancelled. The investigator gathers the records, identifies the discrepancy, calculates the amount in question and prepares a review packet or a specific clarification request.

## First scope

Choose one currency, one business profile and a few exception types: quantity differences, price differences, duplicate invoices and missing delivery evidence. Preserve exact decimal parsing and integer monetary units where appropriate. Keep financial postings and supplier communication behind explicit review.

## Security and operation

Restrict tools to authorised supplier and workspace evidence. Uploaded documents may contain malicious instructions. Recheck source versions and balances before any approved action; repeated jobs must not create repeated financial effects.

Observe extraction failures, missing records, stale proposals, queue age and review handoffs. Retain immutable source provenance separately from redacted diagnostic telemetry.

## Evaluation

Check extracted facts, exact discrepancy amounts, evidence support, alternative valid outcomes and appropriate clarification. Include conflicting emails, revised orders, duplicates, fabricated references and changed source records. Measure finance-review effort and correction rates.

Compare prepared retrieval plus one interpretation call with bounded agent-directed investigation. Ground truth needs a reviewer familiar with the supported purchasing process.

## Relationship to existing work

The invoice-reconciliation project already provides relevant patterns for evidence, scoped access, exact money, review, durable jobs, evaluation and telemetry. Purchasing documents and supplier-side accounting introduce new domain requirements; reuse should follow explicit interfaces rather than assuming the existing financial model covers them.
