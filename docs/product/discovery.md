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

These are product decisions, not evidence of an implemented workflow. Packet formats were settled in the following round; exact media adapters and safe limits remain engineering work.

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

## Relief coverage and saved cases 21 October 2026

| Decision | Actual owner answer and interpretation |
|---|---|
| Other reliefs | “Include more relief types initially” — broaden the proposed standard employment expenses, union/mandatory professional fees and individual pension-contribution coverage; exact additions still need to be named |
| Regional deductions | “Yes, include reviewed branches of both” — both habitual-home rent and childcare/conciliation are first-complete-release requirements for independently validated branches; complex/unresolved branches remain explicit referrals |
| Retention | “Yes, save cases until I delete them” — persist between sessions; deletion covers documents and derived records, with a tested backup-retention policy before hosted private use |

The earlier “investigate both” decision is now a commitment to include validated branches of both in the first complete release. It is not a finding that the conditions or calculations are validated.

## Additional reliefs, workload and pilot targets 21 October 2026

| Decision | Actual owner answer and accepted meaning |
|---|---|
| Additional reliefs | “donations and employer pension contributions” — add both to the proposed standard employment expenses, evidenced union/mandatory professional fees and individual pension contributions |
| Workload | “Yes, about 30 files and 100 pages” — representative benchmark including PDFs and screenshots; safe technical limits still need testing |
| Value | “Yes, use 20% as the initial pilot goal” — at least 20% less hands-on review time than a comparable manual workflow, subject to blocking calculation/safety checks |
| Processing time | “Yes, use the five-minute pilot target” — at most five minutes of automated processing in at least 95% of attempts; progress/resume, exclude human pauses and measure cold activation separately |
| Extraction | “Yes, use 95% as the initial extraction target” — at least 95% of required readable facts correctly extracted and linked before confirmation; missing readable facts count as failures |

These are future targets, not measurements, provider authorisation or evidence of implemented tax behaviour. The [acceptance baseline](acceptance.md) makes their measurement boundaries and blocking checks explicit.

## Consolidated confirmation — product baseline 1.0

Asked whether the consolidated definition and acceptance baseline matched the intended product, including complete calculation, selected branches and pilot targets, while exact tax rules, independent labels and release evidence remained outstanding.

Actual owner answer: **“Yes, freeze this product baseline.”** The product interview is closed for baseline 1.0, approved 21 October 2026. The [definition](definition.md) and [acceptance baseline](acceptance.md) are the approved direction for detailed requirements and design, not a validated legal specification or implemented release. No further owner preference is silently pending in this interview; the named source/reviewer/engineering work remains explicit.

## Remaining decision tree

```text
Confirmed: profile/year, visual evidence, review packet/manual submission
├── Confirmed: optional initial draft, fact confirmation, Spanish product
├── Confirmed: individual returns, multiple employers, explicit partial coverage
│   └── Draft representation, supported fields and scope/unknown screens
├── Confirmed: Spanish PDF/optional JSON, guided workflow, all three value areas
│   └── Packet example and first employer walkthrough remain design/review work
├── Confirmed: complete deterministic calculation within supported profile
│   └── Source/rule/field specification and independent comparison evidence pending
├── Confirmed: owner-only application, professional review by export
├── Local/private validation context stays outside Git; synthetic review pending
│   └── Treatment coverage and a preliminary field-level review rubric
│       └── Synthetic pack → independent labels → experimental freeze
└── Confirmed: saved cases until deletion, 30 files/100 pages and pilot targets
    └── Baseline measurement, tested limits and release evidence pending
```

Both deductions are now committed to the first complete release for independently validated branches. Their full conditions and source discrepancies still need professional review before implementation. Establish facts from official sources; ask the owner about preferences and trade-offs. Engineering should propose tested media/resource limits and representative layouts, rather than ask the owner to choose decoder internals. Security constraints and the zero inference allowance remain in force.

The next slice is detailed source/rule/field specification and legal feasibility, followed by the independently reviewed source pack and architecture alignment. Draft requirement details, labels and tax behaviour are not validated by product approval. If source review changes the supported product branches, reopen that specific decision, retain the owner answer and version the baseline explicitly. Live inference, cloud and AEAT authority remain unchanged.

## Development sequencing correction - 22 October 2026

The owner explicitly instructed that the tax professional can be engaged only at the end, once there is a built, working product, and authorised further official-source research/local downloads. Development is to proceed with the best available AEAT/BOE evidence and provisional engineering tests. Professional feedback becomes final QA and iteration, not an implementation prerequisite. Product scope remains baseline 1.0. No live inference, private-reference access, cloud provisioning or AEAT account/filing operation is authorised by this sequencing change. See [ADR 0004](../decisions/0004-development-before-tax-review.md).
