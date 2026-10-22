# ADR 0002 Stack and reuse assessment

**Status: proposed.** Python, typed interfaces, exact decimal money and OpenTelemetry are the initial engineering direction. The development tools are locked; application dependencies await the first feasibility slice.

**Partially selected, 22 October:** C001 uses the Python modular core, source/state protocols, exact Decimal arithmetic, existing pinned pypdf/Pillow/ReportLab packages, an external bounded Poppler renderer, atomic local JSON/file locking and a loopback-only standard-library HTTP adapter. These local choices are implemented and tested; they do not select the production HTTP server, database, cloud adapters, provider or agent framework. See [C001](../design/c001-working-slice.md). OpenTelemetry remains planned; implemented diagnostics currently cover local command counts/timing and audit events.

Use a visual PDF/image intake path in the first usable version, as clarified by the owner in [ADR 0003](0003-visual-document-evidence.md). Assess render/decoder and visual-extraction components against embedded-text, OCR-assisted and hybrid baselines. Docling remains a candidate rather than a prerequisite. Compare deterministic retrieval plus one interpretation call with bounded agent retrieval. LangGraph provides explicit workflow control; Deep Agents is a candidate if planning/context/delegation needs emerge. Harbor may run isolated tasks around our scorer. None is selected merely by inclusion here.

Use AEAT material for supported year/region and reviewed treatments. OpenFisca Core requires country rules and is not a complete Spanish-return engine by itself. hacienda-cli remains an integration reference pending its inconsistent licence declarations and specific shell/validation concerns; do not install or copy it yet. See the [retained research](../context/imports/predecessor/spanish-tax-exploration.md).

Evaluate PostgreSQL and private object storage against durable state, authorisation and low-idle deployment needs. Prefer AWS if it fits actual runtime and budget checks; preserve GCP as fallback. Local and cloud adapters share the core. Final selections need evidence and an updated ADR.
