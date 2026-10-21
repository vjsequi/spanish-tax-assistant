---
created: 2026-10-20
status: candidate
tags: [ai, use-cases, procurement]
---

# Supplier Contract Reviewer

[Use cases index](00-ai-production-use-cases.md)

Compare supplier agreements with an explicit purchasing playbook and prepare a cited list of deviations. The intended user is a procurement reviewer who repeatedly checks similar documents.

## Established example

[Icertis and Microsoft's case study](https://www.microsoft.com/en/customers/story/1723797353687211986-icertis-professional-services-azure-openai) describes generative AI in contract intelligence across commercial functions. A smaller application could focus on identifying deviations from a single organisation's approved requirements.

## Demonstration case

A supplier agreement proposes automatic renewal, a different notice period and payment terms outside the purchasing policy. The reviewer assistant finds the clauses, identifies an amendment that changes one of them and prepares a comparison with exact references.

## First scope

Support one agreement type and a short, explicit playbook covering items such as payment terms, renewal, notice and required documentation. Return clause locations, applicable playbook rules and uncertainties. Negotiation, legal interpretation and acceptance stay with the authorised reviewer.

## Security and operation

Contracts contain confidential commercial information. Enforce document permissions and treat instructions embedded in agreements as untrusted. Track document and playbook versions so the report cannot silently refer to superseded terms.

Retain partial results when parsing fails and distinguish an absent clause from an unreadable document. Observe unsupported formats, retrieval gaps and review turnaround.

## Evaluation

Check clause retrieval, amendment handling, deviation classification, citation correctness and meaningful abstention. Include clauses split across pages, conflicting versions, ambiguous wording and missing provisions. Measure missed deviations, false alarms and review effort.

## Main dependency

An approved playbook and a reviewer able to resolve ambiguity. A contract summary alone would provide weaker evidence of business value than an evaluated deviation-review workflow.
