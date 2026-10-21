# Initial product definition

**Version 1.0, owner approved 21 October 2026.** The owner confirmed “Yes, freeze this product baseline.” The [acceptance baseline](acceptance.md) records the selected targets and blocking gates. This approves the product direction for detailed requirements and design; legal conditions, rule/field specification and independent validation remain outstanding.

## User and useful outcome

An individual preparing their Spanish personal income-tax return needs to organise evidence, establish that a draft agrees with their records and find applicable supported deductions. The owner wants all three in one journey, including an independent complete tax/refund calculation for the covered profile. The application helps them find missing or conflicting facts, understand calculated results and proposed corrections, and review an evidence packet before manual submission in Renta WEB. Measure evidence organisation, draft checking and deduction discovery separately as well as overall review effort and safety against the selected pilot targets below.

The first supported profile is a common-regime resident employee in the Balearics, for tax year 2025, making an individual return with employment income, bank interest and selected deductions. Salary certificates from multiple employers are supported in the product scope, with each payer retained separately and combined supported fields checked. Additional treatments still require validated rules. The owner explicitly confirmed this bounded profile, year and review-packet deliverable. Independently validated branches of childcare/conciliation and habitual-home rent are both required in the first complete release; their conditions and implementation are not validated yet. The profile is a product boundary, not a claim about the owner's personal eligibility.

The first employment branches are ordinary salary and documented benefits in kind. Refer severance, arrears and other unvalidated special treatments. Support people without dependants and straightforward cases with children, including the applicable family minima and credits. Shared custody, disability and dependent ascendants need later separately validated branches. Exact conditions must replace “straightforward” in the executable coverage screen. Initially calculate ordinary annual returns; formal corrections of already-filed returns are outside the first release.

Initial relief coverage includes standard employment expenses, evidenced union/mandatory professional fees, individual pension contributions, donations and employer pension contributions. Prior-year carryforwards and other unvalidated reliefs remain screened, explicit coverage gaps rather than assumed zeros. Exact eligibility, attribution, ordering, caps and interactions need independently reviewed rules.

## First complete journey

1. Open a synthetic demonstration case, or later create a private authenticated case for the supported profile.
2. Supply salary certificates, bank-interest records, receipts, screenshots and other relevant documents. An AEAT draft is optional at the start: without one, organise the evidence and identify missing information. PDF pages, including scans, and standalone images are first-class visual evidence; manually supplied information is recorded with its own provenance.
3. Confirm the extracted facts used in proposals beside their source images. Permit batch confirmation of clear facts; resolve conflicts individually. Model confidence cannot confirm a fact.
4. Inspect missing information and candidate deductions using official material filtered to 2025 and the Balearics. Calculate the complete tax/refund independently when all required supported facts are confirmed. Once a draft is supplied, compare its fields and inspect discrepancies. Without draft values, do not invent a prior value or present a draft-field change as ready.
5. Inspect each proposed field change, supporting evidence, rule and deterministic calculation. Ask a specific question or refer unsupported circumstances.
6. Accept, correct or defer changes; export a review packet. The person handles the official submission.

The first interface and review packet will be in Spanish. Technical documentation for employers remains in English. The owner selected a readable PDF as the main deliverable and an optional structured JSON export. Include coverage limits, confirmed facts, proposed changes, evidence references, calculations and unresolved questions. The concrete packet layout remains open.

The primary interaction is a guided case workflow through evidence, fact confirmation, findings, proposed changes and export. Contextual questions belong to the active case and its supported scope.

Initially only the owner logs into the application. They export a packet for professional review and manage any sharing themselves; shared cases and professional logins are outside the first release. Evaluation judgements remain separate from the owner's in-app decisions.

Private reference material and derived taxpayer details must remain local and private. Availability and scope details belong in ignored local discovery notes. No reference source files or review evidence have been inspected. Private context is not a public example or permission to send private content to an application provider. Synthetic review can be arranged later; reviewer qualifications, remit and independently checked synthetic judgements remain dependencies.

## Document evidence

The owner prefers PDF page images based on experience with the Oposiciones pipeline, and explicitly includes screenshots and varied information sources. Preserve both original bytes and visual page evidence from the first usable version. Digital PDFs must remain usable through the visual path even when an embedded text layer exists; scanned PDFs and screenshots must not depend on such a layer.

Visual interpretation produces proposed facts with page/region references, readable transcriptions and normalised typed values for confirmation. Extracted text and OCR can support search or serve as comparison paths. Blurred, cropped, conflicting or ambiguous content triggers a targeted question or request for better evidence. A model's transcription is a proposal to check, not proof of authenticity or correct tax treatment.

The first media adapters target PDFs and common image formats such as PNG/JPEG, with exact formats and resource limits tested in feasibility. Intake is extensible to other formats and information sources; acceptance of a document does not expand the supported tax regime or treatments. See [ADR 0003](../decisions/0003-visual-document-evidence.md).

## Product boundaries

The owner explicitly requires an independent complete tax/refund calculation within the agreed profile. Develop a versioned deterministic engine covering the required intermediate calculations, applicable national/regional rules, deductions, withholding and final balance. Research and independently review its exact branches before implementation. Supplied AEAT totals are comparison evidence, not a substitute for the calculation. A case without a draft can still be calculated if all required supported facts are confirmed.

Joint returns, foreign income, business activity, complex investment disposals, other regimes/regions/years and corporate taxes require explicit scope referral until separately supported. Household facts required by a supported individual-return treatment still need to be established. A selected bank-interest context does not imply support for all investment taxation. Automated AEAT access, XML import, signature and filing are later integrations.

The owner accepts a partial review when other circumstances are unsupported. List those items and coverage gaps prominently in the interface and exported packet. Review only fields whose required facts are established, and leave any affected treatment unresolved if unsupported income or other unknown circumstances could change it. Do not supply an independently validated whole-return total for an incompletely covered case. Never imply that the complete return was checked or silently discard unsupported income.

The public employer experience uses synthetic preloaded examples without uploads or sign-in. Any real-data hosted owner workspace requires authentication and private access. A production-like deployment is a later measured milestone, with development/staging/production and a fresh cost assessment.

Private saved cases persist between sessions until the owner explicitly deletes them. Deletion covers originals and derived records. Design and test backup-retention/deletion behaviour before hosted private use; do not imply that deleting an active case instantly removes every backup copy. Local-only reference policy remains stricter than a future general hosted workspace.

## Why AI and what stays deterministic

Use AI for varied document understanding, choosing bounded evidence retrieval, resolving language ambiguity through questions, and explaining supported facts. Calculations, eligibility conditions, year/region filtering, permissions, source freshness and review authority remain explicit versioned code. A model's confidence or an authentic quote alone does not establish correct tax treatment.

## Initial acceptance criteria to refine

- Supported fields link to exact text spans or original/derived image, page and region evidence; missing, illegible and conflicting facts remain visible. A visual source needs a reviewable image anchor even when no searchable text exists.
- A case can begin without an AEAT draft and report evidence readiness. Draft-field proposals require supplied draft values and the confirmed facts they use. Batch confirmation records the exact facts and versions confirmed; an unresolved conflict cannot be hidden in a batch.
- Each proposed change identifies applicable year/region, rule version, evidence and calculation. Unsupported claims or deductions block acceptance.
- For a fully covered case, independently calculate the complete tax/refund and expose the intermediate values. Validate fields and stages as well as the final total; cancelling errors do not pass. A copied draft total or partial sum does not satisfy this requirement.
- Unknown conditions cause useful questions or referral. Repeating work does not duplicate a committed review decision, and changed evidence invalidates stale proposals.
- Multiple-payer records retain their own evidence and periods; duplicate/revised records cannot be added twice. Partial reviews expose unsupported items and block affected treatments when required facts are unknown.
- Independent tax review checks individual fields and treatments as well as totals. No tax-quality result exists at bootstrap.
- Compare checklist/rules, prepared retrieval plus one call and bounded agent retrieval on frozen reviewed cases. Measure harmful errors, missed issues, useful questions, reviewer corrections/time, latency and known cost.
- Demonstrate permissions, recovery, redaction and reproducible delivery in each environment before claiming hosted operation.

The owner selected a benchmark of about 30 files/100 pages, at least 95% correct pre-confirmation extraction with correct evidence, at least 95% of attempts within five minutes of automated processing (human pauses excluded, cold starts measured separately), and at least 20% less hands-on review time than a comparable manual workflow. These are future pilot targets. The [acceptance baseline](acceptance.md) defines denominators and blocking gates; the final experimental rubric/case freeze still needs independent labels. The invoice project's results are historical context, not transferred tax evidence.
