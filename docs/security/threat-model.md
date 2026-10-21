# Initial threat model

Protect taxpayer records, case authority, source/rule provenance, review decisions, service credentials and provider budgets. These controls are design requirements; deployed verification remains future work.

| Threat | Required control and meaningful evidence |
|---|---|
| Document prompt injection | Treat content as data; bounded scoped tools; adversarial tests against authority changes |
| Cross-taxpayer access | Trusted identity and workspace checks in every read/tool/command; negative access tests |
| Wrong year or region | Versioned corpus/rules with explicit applicability and wrong-context test cases |
| Fabricated facts or deductions | Typed source-linked facts, deterministic treatment checks, semantic and independent review |
| Stale or duplicate review | Source/version digest checks, transactional authority, idempotency and append-only events |
| Malicious files/XML | Type/size/page/time limits, isolated parsing, no external entities, no arbitrary shell interpolation |
| Exfiltration in logs or tools | Private stores, no arbitrary egress/tools, redacted telemetry and secret/session exclusions |
| Runaway inference or uncertain retry | Explicit authorisation, durable attempt limits, timeout and conservative uncertainty recovery |
| Supply-chain skill changes | Reviewed pinned minimal files, licence/hash receipt, no automatic updates or installer hooks |

Authentication is required before any real-data hosted access. Public examples are synthetic and recorded. Portal sessions and filing capabilities are outside the first release. A future adapter needs its own authority and verification; the cloud must never start with a loopback-only development identity.

Independent tax review is a domain gate. Schema-valid XML, citation identity and a plausible total do not establish a correct return.
