# Low level design

**Proposed interfaces, not implemented schemas.** Refine these after the representative formats and supported treatments are agreed.

## Core records

| Record | Required identity and state |
|---|---|
| Case | Authorised owner/workspace, tax year 2025, jurisdiction, profile, state and version |
| Source | Private immutable original, content hash, detected media type, parser/decoder version and admission result |
| Page image | Source hash, physical page index, image hash, dimensions, renderer version/configuration and any rotation/crop transform |
| Evidence anchor | Source/page-image identity and valid region or whole-page reference; text spans when available, with coordinate convention and transform mapping |
| Fact | Visible transcription and normalised typed value, unit/period, text/image anchors, legibility and confirmation state, and conflicting alternatives |
| Rule | Supported treatment, year/region, official source and version, prerequisites and exact calculation/rounding |
| Investigation | Input snapshot, workflow/model/prompt/schema versions, bounded attempts and outcome |
| Proposed change | Draft field, prior/new value, fact/rule references, calculation, source digest and pending status |
| Review event | Reviewer authority, exact proposal digest, decision, idempotency key, timestamp and new case version |

## Execution contract

1. Authorise the case and stage bounded PDFs/images. Detect and admit formats, preserve original bytes/hash, render PDF pages or decode standalone images with size/page/pixel/time limits, and retain versioned derivatives. Image-only PDFs need no embedded text. Run decoding/rendering in an appropriately isolated resource-limited process; a child process alone is not an OS sandbox.
2. Propose facts from visual evidence; retain readable transcriptions, normalised values and valid image/page/region anchors. Auxiliary text/OCR may assist. Confirm facts or retain illegibility/unresolved conflict. Evaluate scope from actual circumstances; unknown information is not false or zero.
3. Snapshot case/source/rule versions and enqueue durably. Claim with an opaque fence and bounded recovery policy.
4. Prepare authorised context, reserve provider work and execute outside a database transaction. Bound retrieval steps, output size, time, calls and money. Do not retry an uncertain charged request automatically.
5. Validate typed output, scope, source and rendered-image membership, page/coordinate bounds, available text quotations and exact deterministic treatments. An image reference or matching OCR text does not independently prove the model read a figure correctly. Semantic support still needs evaluation and human review.
6. Recheck source/case versions and active-run authority before publishing a pending change. Changed evidence supersedes old work.
7. A separate review command validates current membership, versions and exact digest inside a transaction, then appends a review event. Model output cannot approve or submit a return.

Parse money from exact decimal text; use integer minor units and explicit Decimal arithmetic where rule rounding requires it. Select rounding stages per reviewed treatment, not a global rounding shortcut. No rule rates or tax thresholds are implemented in the bootstrap.

Diagnostic attributes are bounded operation/outcome/version categories. Protected traces may carry opaque correlation; routine telemetry never carries evidence, prompt/response text, taxpayer IDs or raw exception payloads. Durable audit and source provenance survive telemetry failure independently.

## Rendering and visual provenance

Bind a cached derivative to original content hash plus renderer/configuration/transform identity. Do not reuse an image solely because a filename already exists. Use a declared physical-page convention and coordinate origin; store dimensions and map crops/rotation back to the retained page. If precise localisation is unavailable, cite the whole page explicitly instead of inventing a bounding box.

Keep the full page available when requesting a detail crop so column headers, footnotes and period/context are not lost. Record missing/cropped dates, unreadable digits, decimal separators, signs, totals and duplicate screenshots as uncertainty. Provider-side downscaling and changed render settings need explicit image/configuration provenance. No amount or field is accepted solely from model confidence.
