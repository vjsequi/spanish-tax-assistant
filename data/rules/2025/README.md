# Retained 2025 rule references

The [catalog](catalog.json) selects public AEAT and BOE references; the [manifest](manifest.json) binds exact retained bytes, SHA-256, retrieval time, final URL and available HTTP metadata. Originals are unmodified. **Pinned does not mean independently reviewed, executable or approved for application use.** No taxpayer portal or private record was accessed.

Git attributes disable text normalisation/diff whitespace processing for retained originals and upstream licences, preserving source line endings and publisher whitespace. Verify hashes after checkout; do not format these original files to satisfy code-style checks.

Publishers: Agencia Estatal de Administración Tributaria (AEAT) and Agencia Estatal Boletín Oficial del Estado (BOE). Retained information is reused under their [AEAT conditions](https://sede.agenciatributaria.gob.es/Sede/gobierno-abierto/reutilizacion-informacion/condiciones-reutilizacion.html), [AEAT legal notice](https://sede.agenciatributaria.gob.es/Sede/condiciones-uso-sede-electronica/aviso-legal/utilizacion-informacion-contenida-web-aeat.html) and [BOE legal/reuse notice](https://www.boe.es/informacion/aviso_legal/). Those notices are also retained. Preserve source, update dates and reuse metadata; do not distort the material or imply publisher participation/endorsement. Government materials are not relicensed under the project's MIT software licence.

## Edition selection and applicability

The 2025 form is Annex I of Orden HAC/277/2026, published on 27 March 2026. Its publication year is not the return's tax year. The original BOE PDF includes unrelated annexes, which are retained intact but not selected as supported treatments.

For consolidated legislation, the catalog selects an actual BOE edition no later than 31 December 2025. The collector checks the returned `version-selected` marker. An unlisted date can otherwise silently return today's text. Initial wrong-date responses were rejected as 2025 editions and retained only in ignored local acquisition evidence.

An end-of-year edition is a reference point, not proof of complete legal applicability. Review commencement, accrual dates, transitional provisions and later retroactive changes against the 2025 manuals and original amending publications. BOE consolidated text is informational; official publications remain the legal references. The 2025 rent/childcare ambiguities remain review blockers.

## Reproduce and verify

Run from the repository root:

```sh
uv run --locked python -m scripts.pin_official_sources
```

This is offline verification. Explicit acquisition uses `--download` and optionally `--ca-file /path/to/trusted-ca.pem`; TLS verification stays enabled. The collector admits only selected HTTPS AEAT/BOE URLs, bounds source sizes and collection time, checks identities/selected editions and refuses silent replacement. It never follows instructions in source material, authenticates, imports a return or invokes a model.

Future updates need a new source-set version and independent review rather than overwriting a case's pinned rules.
