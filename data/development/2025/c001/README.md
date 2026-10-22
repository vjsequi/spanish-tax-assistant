# Supplementary guidance for provisional C001 development

Four additional public AEAT 2025 guidance pages are retained with hashes in [the manifest](manifest.json), selected by [the catalog](catalog.json). They cover the employment calculation scheme, state/regional liability method, Balearic minima and the distinct 2025 employment credit. The original fifteen-reference review set remains unchanged.

The owner authorised development before professional QA on 22 October 2026; see [ADR 0004](../../../../docs/decisions/0004-development-before-tax-review.md). The first local synthetic calculation uses the existing source-derived rule parameters and this additive reference set. It is provisional, with professional review deferred to final QA. Neither pinning nor software-authored regression assertions constitutes independent validation.

Publisher: Agencia Estatal de Administración Tributaria. The [retained AEAT reuse/legal notices](../../../../data/rules/2025/README.md) apply. Originals remain unmodified, with source URL, retrieval/update metadata and SHA-256 retained; no endorsement or new licence is implied.

Run `uv run --locked python -m scripts.pin_development_guidance` to verify offline. Acquisition is explicit with `--download` and uses the bounded official-host collector. This script never authenticates to AEAT, imports a return or invokes a model.
