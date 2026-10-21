# Product discovery decisions

Use the reviewed [Grill Me entry point](../../.agents/skills/grill-me/SKILL.md) and its [Grilling dependency](../../.agents/skills/grilling/SKILL.md). The installed revision works in rounds of independent questions. User answers settle decisions; new questions depend on those answers. Facts come from research, not invented owner preferences.

## Confirmed on 21 October 2026

| Decision | Actual owner answer |
|---|---|
| Skill identity | “Yes, Matt Pocock’s grill-me” |
| First profile | “Yes, start with that bounded profile” — Balearics employee, salary, bank interest and selected deductions |
| Reviewer availability | “I have a potential reviewer” — potential contact, not confirmed engagement or qualification evidence |
| Tax year | “Yes, start with tax year 2025” |
| Deliverable | “Yes, a review packet with proposed field changes” — manual Renta WEB submission |
| Deductions to investigate | “Investigate both candidates” — childcare/conciliation and habitual-home rent |

## Document evidence clarification 21 October 2026

The owner did not accept restricting the first pack to text PDFs. Their answer explicitly included “certificates, receipts, screenshots, any source of information” and explained a preference for an image when working with PDFs. They pointed to their Oposiciones repositories as relevant experience.

Recorded decision: visual PDF/page evidence, scanned/image-only PDFs and standalone images/screenshots are in the initial product direction. Embedded-text extraction and OCR can assist and be evaluated, while confirmed facts remain required. Broad document sources do not expand the agreed tax profile. Inspection of the native ConceptLock reference confirms page-image rendering/attachment and page/clip provenance, not a measured tax-quality advantage. See [retained lessons](../context/document-ingestion-lessons.md).

## Workflow, confirmation and language 21 October 2026

| Decision | Actual owner answer and accepted recommendation |
|---|---|
| Starting without a draft | “Yes, allow starting without a draft” — organise evidence and missing information first; compare and propose draft-field changes once a draft is supplied |
| Fact confirmation | “Yes, confirm facts before proposing changes” — show source images, allow batch confirmation of clear facts, resolve conflicts individually; model confidence is not confirmation |
| Language | “Yes, Spanish product and English technical docs” — Spanish interface and review packet, English technical documentation |

These are product decisions, not evidence of an implemented workflow. Draft intake representation and packet formats remain open.

## Return branches and partial coverage 21 October 2026

| Decision | Actual owner answer and accepted recommendation |
|---|---|
| Return type | “Yes, individual returns first” — joint returns outside initial coverage; household information still collected when required by a supported deduction |
| Multiple employers | “Yes, support multiple employers” — retain each payer separately, check combined supported fields; additional treatments need validated rules |
| Partial coverage | “Yes, allow a clearly labelled partial review” — list unsupported items prominently, allow an incomplete packet and never imply that the whole return has been checked |

A partial review must retain dependencies: if unsupported income or an unknown circumstance could change a proposed treatment, that treatment remains unresolved until the needed facts are established. The owner's answer is not authority to ignore other income, infer a zero or approve an affected deduction.

## Packet, interaction and useful outcome 21 October 2026

| Decision | Actual owner answer and interpretation |
|---|---|
| Packet format | “Yes, Spanish PDF plus optional JSON” — coverage limits, confirmed facts, proposed changes, evidence references, calculations and unresolved questions |
| Interaction | “Yes, guided workflow with contextual questions” — add evidence, confirm facts, inspect findings, review changes and export |
| Main value | “couldn't we include all 3?” — include organising evidence, checking the draft and finding applicable supported deductions in the same journey; do not force an exclusive value choice |

Measure the three activities separately alongside end-to-end review effort and safety. Including deduction discovery does not approve unreviewed treatments or extend the agreed tax scope. No numerical value result or target was accepted in this round.

## Complete calculation, private reference and reviewer access 21 October 2026

| Decision | Actual owner answer and interpretation |
|---|---|
| Complete calculation | “Include an independent complete tax/refund calculation” — replaces the earlier proposed field-review-only calculation boundary; add a deterministic full calculation for covered cases |
| Review evidence | Private context is retained only in ignored local discovery notes. Synthetic review can be arranged later; no synthetic labels or review judgements have been obtained. |
| Initial access question | “I don't understand the question” — no answer was inferred; clarified whether the professional needs an application login |
| Clarified access | “Yes, only I log in; use exported review packets” — one owner initially, professional review through owner-managed exports |
| Complete-calculation profile | “Yes, complete calculation within that profile” — 2025 Balearics individual employment/bank-interest scope and supported deductions; unsupported cases may receive a partial review but no independently validated whole-return total |
| Private reference context | Scope details remain in ignored local discovery notes; no reference source files or review evidence have been inspected. |

Private reference material and derived taxpayer information must stay on the laptop, outside Git, cloud, public examples, external application providers and routine telemetry. Private discovery answers are deliberately omitted from this public record. No file path, figures or reviewer labels were requested or opened. A local gateway is not evidence that downstream processing stays local. Later reference use needs an explicit handling plan; private context is not public quality evidence.

The owner's full-calculation requirement supersedes the initial draft's suggestion to stop at field review. Manual Renta WEB submission remains confirmed. Scope the complete deterministic calculation through its intermediate values and supported branches; never substitute a partial calculation or a copied AEAT total. Detailed branch coverage, review rubric and implementation are still pending.

## Initial calculation branches 21 October 2026

| Decision | Actual owner answer and accepted recommendation |
|---|---|
| Employment | “Yes, salary and documented benefits in kind first” — multiple employers supported; severance, arrears and other unvalidated special treatments referred |
| Family | “Yes, include straightforward cases with children” — support people without dependants and parents in straightforward arrangements, with applicable family minima/credits; shared custody, disability and dependent ascendants are later validated branches |
| Return status | “Yes, ordinary annual returns first” — formal corrections of filed returns are outside the first release |

“Straightforward” is not an executable rule. Turn it into explicit supported conditions, evidence and negative cases during specification; unknown family facts cannot default to inapplicable. The [calculation-chain research](../context/calculation-feasibility.md) identifies the stages and facts to validate.

## Current frontier — asked, awaiting answers

18. **Common reliefs:** recommend standard employment expenses, evidenced union/mandatory professional fees and individual pension contributions; other unvalidated reliefs/history trigger referral.
19. **Regional deductions:** recommend reviewed branches of both rent and childcare for the first complete release, with exact conditions and explicit unresolved/referral branches.
20. **Retention:** recommend persisting private cases across sessions until explicit deletion, with tested hosted backup retention before private hosted use.

No answer is assumed. Further decisions concern representative workload and acceptance targets. The [deduction feasibility brief](../context/deduction-feasibility.md) records official-source ambiguities for the professional, not choices the owner must resolve from memory. Visual intake is already settled.

## Remaining decision tree

```text
Confirmed: profile/year, visual evidence, review packet/manual submission
├── Confirmed: optional initial draft, fact confirmation, Spanish product
├── Confirmed: individual returns, multiple employers, explicit partial coverage
│   └── Draft representation, supported fields and scope/unknown screens
├── Confirmed: Spanish PDF/optional JSON, guided workflow, all three value areas
│   └── Packet example, quantitative targets and first employer walkthrough
├── Confirmed: complete deterministic calculation within supported profile
│   └── Pending: full calculation chain, branch coverage and comparison rubric
├── Confirmed: owner-only application, professional review by export
├── Local/private validation context stays outside Git; synthetic review pending
│   └── Treatment coverage and a preliminary field-level review rubric
│       └── Synthetic pack → independent labels → experimental freeze
└── Pending: intended private-use milestone and retention needs
    └── Representative workload, measured baseline and release thresholds
```

Investigating the two deductions does not yet commit both to the first usable release. Research their full conditions before asking for that coverage decision. Establish facts from official sources; ask the owner about preferences and trade-offs. Engineering should propose tested media/resource limits and representative layouts, rather than ask the owner to choose decoder internals. Security constraints and the zero inference allowance remain in force.

The repository is ready for discovery work. Product discovery is not declared complete, and draft requirements are not an approved specification. Record future questions, exact answers, changed assumptions and their affected requirements here. Close the interview with the owner's shared-understanding confirmation before implementing the dependent product design.
