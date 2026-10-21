# Working handoff

## Current objective

On 21 October 2026 the owner authorised a separate Spanish personal-tax repository with the context needed for complete AI-assisted development and a staged SDLC. Product discovery uses the explicitly confirmed Matt Pocock Grill Me skill.

Confirmed: 2025; Balearics resident employee; employment income, bank interest and selected deductions; independent complete tax/refund calculation for covered cases; evidence-backed review packet with proposed field changes; manual official submission. Validated branches of childcare/conciliation and habitual-home rent are first-complete-release requirements. Independent synthetic review remains planned, with no labels or judgements obtained.

On the subsequent input-format answer, the owner explicitly included screenshots and broader source documents and preferred PDF images, citing Oposiciones experience. Visual digital/scanned PDF and image evidence are initial requirements, with text/OCR as supporting paths; do not revert to a text-PDF-only start. See [ADR 0003](../decisions/0003-visual-document-evidence.md) and [the inspected pipeline lessons](document-ingestion-lessons.md).

The repository foundation and initial product/design/evaluation/security/delivery documents are prepared. Application implementation, labels, inference and hosted operation remain unstarted. The [discovery record](../product/discovery.md) contains actual answers; the [backlog](../product/backlog.md) names the next slice. Continue TAX-001 before dependent product implementation.

Further owner answers confirmed optional draft intake at case start, confirmation of facts before proposals (batch clear facts, resolve conflicts individually), a guided Spanish interface and PDF/optional JSON packet, English technical documentation, individual returns, multiple employers and clearly labelled partial reviews. Unknown dependencies still block affected treatments. The owner wants evidence organisation, draft checking and supported deduction discovery in the same journey. Definition and draft requirements reflect these answers. HLD/LLD remain architecture hypotheses needing alignment with approved baseline 1.0 and the detailed rule specification. The discovery record retains actual answers and the closed decision tree; do not infer preferences from older draft design prose.

The owner then required an **independent complete tax/refund calculation** within the agreed 2025 profile, superseding the initial proposed field-review-only calculation boundary. Plan deterministic intermediate and final calculations, with no whole-return result for unsupported/incomplete cases. Only the owner initially logs in; professional review uses exported packets. Private validation context is retained in ignored local discovery notes; no reference source files/review labels have been inspected. Private reference material and derived details remain local and out of Git, cloud and external application providers. Synthetic review is still pending.

Initial branches are ordinary salary/documented benefits in kind, straightforward families with children or no dependants, and ordinary annual returns. The owner requires reviewed branches of both rent and childcare, plus standard employment expenses, evidenced union/mandatory professional fees, individual/employer pension contributions and donations. Saved cases persist until explicit deletion. Pilot targets: about 30 files/100 pages, at least 95% correct pre-confirmation readable-fact extraction plus evidence, five minutes of automated processing in at least 95% of attempts and at least 20% less hands-on review time. These are targets, not results. The owner confirmed **“Yes, freeze this product baseline”**, approving definition/acceptance baseline 1.0 on 21 October 2026. Product discovery is closed for that baseline; detailed requirement entries remain drafts pending legal specification and verification design.

**Next work:** complete the source/rule/field map and operational coverage checklist for the full calculation, pin official 2025 material, resolve the recorded deduction ambiguities through independent review, then prepare reviewed synthetic cases and align HLD/LLD. TAX-001 legal feasibility remains open. Do not restart the interview or substitute field-only review for the agreed full calculation. No new inference, provisioning or AEAT action was authorised by freezing the baseline.

The committed foundation and visual-evidence work are pushed to public [vjsequi/spanish-tax-assistant](https://github.com/vjsequi/spanish-tax-assistant), branch `main`. Hosted foundation CI passed for `bafff1ed7884659125628e923fb5477211633cf4`; see [verification](../process/verification.md). This is not application, tax-quality or deployment evidence.

## Self-contained context

The [import inventory](imports/README.md) contains the recovered 20 October use-case notes and relevant predecessor evidence planning/research, with source and imported hashes. Historical links to absent vault/old-repository documents are rendered as source references rather than broken dependencies. Prior invoice tests and model results establish no tax quality. No runtime, credentials, hidden labels or private taxpayer records were imported.

The predecessor remains at `/Users/sequiv/Repositories/GHVJ/invoice-reconciliation` for optional code assessment. Its reported persistent PostgreSQL storage exhaustion is not a dependency of this new foundation. Do not copy private runtime data or prune existing projects.

## Workflow and authority

Use .agents/skills/grill-me and its grilling dependency at the reviewed pinned revision; updates need inspection. The SDLC keeps definition → requirements → design → development → review/evaluation → iteration → CI → deployment → operations traceable. Product discovery closed at owner-approved baseline 1.0. Detailed legal/field specification and verification design remain open; a future scope change needs an explicit versioned decision.

Initial live-model allowance is zero; no cloud or AEAT operations are authorised. The first public employer experience will use preloaded synthetic results. A hosted private owner application is a later milestone with trusted identity, private storage, environment isolation and actual deployment/operation evidence. Keep provider budgets and publication separate from design work.
