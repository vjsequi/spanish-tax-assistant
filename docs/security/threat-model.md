# Initial threat model

Protect taxpayer records, case authority, source/rule provenance, review decisions, service credentials and provider budgets. These controls are design requirements; deployed verification remains future work.

| Threat | Required control and meaningful evidence |
|---|---|
| Document prompt injection | Treat content as data; bounded scoped tools; adversarial tests against authority changes |
| Cross-taxpayer access | Trusted identity and workspace checks in every read/tool/command; negative access tests |
| Wrong year or region | Versioned corpus/rules with explicit applicability and wrong-context test cases |
| Fabricated facts or deductions | Typed source-linked facts, deterministic treatment checks, semantic and independent review |
| Stale or duplicate review | Source/version digest checks, transactional authority, idempotency and append-only events |
| Malicious PDFs/images/XML | Detect actual type; bound compressed/decoded size, page/pixel count, CPU/memory/time; isolate parsers/decoders, reject unsafe active content/external entities and avoid shell interpolation |
| Exfiltration in logs or tools | Private stores, no arbitrary egress/tools, redacted telemetry and secret/session exclusions |
| Runaway inference or uncertain retry | Explicit authorisation, durable attempt limits, timeout and conservative uncertainty recovery |
| Supply-chain skill changes | Reviewed pinned minimal files, licence/hash receipt, no automatic updates or installer hooks |

Authentication is required before any real-data hosted access. Public examples are synthetic and recorded. Portal sessions and filing capabilities are outside the first release. A future adapter needs its own authority and verification; the cloud must never start with a loopback-only development identity.

Independent tax review is a domain gate. Schema-valid XML, citation identity and a plausible total do not establish a correct return.

## Implemented development controls

The public-reference collector allowlists HTTPS AEAT/BOE hosts, checks redirect destinations and exact selected BOE editions, bounds acquisition and verifies retained hashes offline. Tests cover silent fallback to a newer consolidation, hostile URLs, source drift and mapped-field page drift. The review exporter selects manifest-listed public/synthetic files rather than recursively publishing a directory; private, expected-answer and authoring paths are prohibited. Case metadata is narrowly checked for answer-key contamination and path escape, and document checks skip the expected-answer area entirely. These development controls do not establish runtime intake isolation, application permissions, semantic tax correctness or resistance to a live model attack.

## Visual evidence

Prompt injection can appear in a screenshot or page image as well as text. Preserve the document-as-data boundary across visual adapters and tool calls. An official-looking logo or screenshot does not authenticate a source. Keep legibility, source authority, extracted facts and tax interpretation as distinct review concerns.

Retain originals privately; safe derivatives should not leak unrelated metadata or content through model requests, public exports or diagnostics. Do not log image bytes, base64, image URLs, local paths, filenames, embedded identifiers or OCR transcripts. Cropping must preserve mapping to the full retained source and avoid silently removing conditions. Test malformed/truncated files, oversized images and repeated submissions without contacting a provider.
