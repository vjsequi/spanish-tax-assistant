# ADR 0002 Stack and reuse assessment

**Status: proposed.** Python, typed interfaces, exact decimal money and OpenTelemetry are the initial engineering direction. The development tools are locked; application dependencies await the first feasibility slice.

Assess simple text/table extraction before Docling/OCR. Compare deterministic retrieval plus one interpretation call with bounded agent retrieval. LangGraph provides explicit workflow control; Deep Agents is a candidate if planning/context/delegation needs emerge. Harbor may run isolated tasks around our scorer. None is selected merely by inclusion here.

Use AEAT material for supported year/region and reviewed treatments. OpenFisca Core requires country rules and is not a complete Spanish-return engine by itself. hacienda-cli remains an integration reference pending its inconsistent licence declarations and specific shell/validation concerns; do not install or copy it yet. See the [retained research](../context/imports/predecessor/spanish-tax-exploration.md).

Evaluate PostgreSQL and private object storage against durable state, authorisation and low-idle deployment needs. Prefer AWS if it fits actual runtime and budget checks; preserve GCP as fallback. Local and cloud adapters share the core. Final selections need evidence and an updated ADR.
