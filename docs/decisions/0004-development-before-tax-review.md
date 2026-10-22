# ADR 0004 Develop a working product before professional tax QA

**Owner-directed, 22 October 2026.** The owner clarified: “The reviewer can only be engaged at the end of the process once we have something built and working.” They authorised continued official-source research and local downloads to make progress with available evidence.

## Decision

Professional review is final domain QA, not a prerequisite for development. Continue the approved product scope using retained, versioned official sources, explicit coverage limits and source-derived provisional rules. Build deterministic behaviour, visual evidence/review flows and offline AI interfaces before arranging professional feedback on a working product.

The first executable slice is C001: public synthetic visual sources, editable/confirmed facts, a provisional ordinary cash-salary/bank-interest calculation, comparison with supplied draft fields and export. This is an intermediate slice; multiple payers, in-kind benefits, children, pensions, donations, rent and childcare still need subsequent implementations. No first-release requirement is removed.

## Evidence and authority

- Official guidance and arithmetic-derived engineering tests are development evidence. Label them provisional; they are not independent case labels, professional sign-off or measured AI performance.
- Keep reviewed final expectations separate in `evals/expected`, outside application/model/development context. Do not invent reviewer identities, dates or decisions.
- A rule may execute in the explicit synthetic local development profile before professional QA. This does not set `approved_for_application` on the existing unreviewed rule register, authorise hosted private use or claim a validated tax result.
- Record uncertain interpretations and rounding assumptions. Missing facts and unsupported branches still block the affected result; they do not become zero. Keep authoritative source identity and version checks.
- The owner authorised public official-source research/downloads. Application inference remains zero; no new model/gateway calls, cloud provisioning, AEAT authentication/import/filing, private-reference access or reviewer contact follows from this decision.

## Completion and later QA

Develop and demonstrate supported flows, run engineering/domain/security regression tests and preserve their limitations. At final QA, the professional reviews the implemented rules, complete calculations, field mappings, source applicability and representative cases. Feedback creates tracked defects and new regressions before release claims based on tax validation. Owner product approval and professional tax QA remain separate.
