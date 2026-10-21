---
created: 2026-10-20
status: candidate
tags: [ai, use-cases, security]
---

# Security Evidence Assistant

[Use cases index](00-ai-production-use-cases.md)

Help a small software company answer customer security questionnaires using current policies, technical evidence and approved previous responses. The business need is to reduce repeated research while keeping answers accurate and reviewable.

## Established example

[Vanta's Questionnaire Automation](https://www.vanta.com/products/questionnaire-automation) drafts responses from security documentation and previous questionnaires and includes review and approval workflows. Its [implementation guidance](https://help.vanta.com/en/articles/11488356-vanta-questionnaire-automation-implementation-guide) describes completing a real questionnaire through that workflow.

## Demonstration case

A customer asks whether backups are encrypted, restoration is tested and data remains in a specified region. The assistant finds the relevant policy and implementation evidence, identifies an outdated restore-test record and drafts separate supported answers and open questions.

## First scope

Support a defined questionnaire format and a curated evidence library for one product. Return an answer, citations, evidence date and unresolved issues for each question. An accountable person approves the export. A documented intention must remain distinct from evidence that a control is implemented and operating.

## Security and operation

Security documents can expose sensitive infrastructure details. Enforce document access and export permissions. Treat questionnaire wording as untrusted input and prevent it from expanding retrieval permissions. Keep approval history and evidence versions.

Track indexing failures, stale sources, unanswered questions and reviewer changes. Reusing an old answer must not hide changes to the current product or environment.

## Evaluation

Measure answer support, correct product/environment scope, evidence freshness, omissions and unsupported positive claims. Include a policy that conflicts with configuration, expired evidence, an unknown control and a question attempting to retrieve secrets. Measure review time and material corrections.

The output supports a security review; it does not establish certification or compliance by itself.

## Main dependency

A maintained evidence library and a reviewer who can distinguish a policy statement from an operating control. The project's own security evidence could provide initial cases, while customer-value claims would need actual questionnaire usage.
