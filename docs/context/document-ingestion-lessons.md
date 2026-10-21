# Oposiciones document ingestion lessons

**Read-only inspection, 21 October 2026.** The owner identified their Oposiciones work as relevant PDF-image experience. Pulpo Oposiciones links the independently versioned question-generator and UI repositories. This assessment inspected the native ConceptLock source/design/tests in `multiple_question_generator_with_adk`; no private PDF corpus, runtime output or provider workflow was used.

## Observed pattern

- The inspected native path defaults to vision concept extraction and has text alternatives. PyMuPDF renders physical pages to PNG files, with a native default of 144 DPI. That setting is a reference, not a tax-document resolution decision.
- Section extraction can combine page images with bounded text previews; concept extraction attaches full-page images for the section. Image manifests identify pages/clips and prompts describe section boundaries. These are full pages with prompted boundaries, not geometric region crops.
- Support metadata is model-attributed. Unit tests cover rendering, image attachment and contracts; some use authored/fake image bytes. The inspected comparator is normalized exact-string overlap, not a measured OCR/financial-field accuracy study.
- The native render helper reuses an existing page filename and attaches pages without the tax product's required source/configuration cache identity and explicit page/pixel/provider budgets. Review these boundaries before reuse.
- Current repository instructions designate a different paired-worktree route for future fresh modules. The inspected native runner is a pattern reference, not authority to start that pipeline.

## Transfer to the tax assistant

Preserve rendered visual evidence, allow scanned/image-only documents and standalone screenshots, bind extracted facts to source/page evidence, and carry necessary visual context between stages. Add exact region/transform provenance, explicit legibility/manual confirmation, resource bounds and tax-specific field evaluation. Do not copy syllabus-generation retry policies or its source-authority policy into financial/tax decisions. A supplied document can support a claimed fact without establishing current law or eligibility.

No implementation or comparative tax-quality claim follows from this inspection. The [ADR](../decisions/0003-visual-document-evidence.md) and [evaluation plan](../evaluation/plan.md) govern the proposed adaptation.

## Inspected source identities

The following paths are relative to `multiple_question_generator_with_adk`. Hashes identify inspected working-copy bytes; they are references, not imported runtime dependencies.

- `scripts/run_conceptlock_syllabus.py` — relevant lines 2716, 2859, 2969, 3164. Rendering, image/text routing and native defaults. SHA-256: `bd01f88cb514f400edd8bcfb4e7fa5ac3448304f55a04776a9885164631ee32a`.
- `conceptlock/pdf_image_concept_proof.py` — relevant lines 24, 126. Image manifest, page/clip support and boundary prompt. SHA-256: `522e6c70e291cbb8fe3e038877aa3d7ebf5bd2b5daa81d59c78719f2cada1477`.
- `tests/test_conceptlock_enaire_runner.py` — relevant lines 1295, 1313. Rendering/attachment software tests, not domain quality. SHA-256: `5bd1172595d7772023eb1c25e787c2dff8f2f232778d210fdeaad2c43354b1b5`.
- `tests/test_pdf_image_concept_proof.py` — relevant lines 96. Authored normalized-string-overlap comparator test. SHA-256: `186622e094332e1d8e6df12f680d81b3a40da5145659c7e07a166728df8a9829`.
- `docs/conceptlock_pipeline.md` — relevant lines 3. Current fresh-module route takes precedence over the native reference. SHA-256: `017a3e6eac8f20c87ea994145dbe55d013e9c62b87f8498bba955b125038b125`.
