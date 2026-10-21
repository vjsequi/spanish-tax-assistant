# Verification evidence

## Repository foundation 21 October 2026

Executed locally with CPython 3.14.8, uv 0.8.4, Ruff 0.16.10 and mypy 1.20.2:

- `uv lock` resolved the six development packages plus the project; no runtime dependencies.
- `uv sync --locked` installed the locked development tools in an isolated environment.
- `uv export --locked --offline --only-dev --format requirements-txt --no-emit-project --no-header --quiet --output-file requirements-dev.txt` produced hash-locked CI requirements.
- `python scripts/check_repository.py` verified 45 Markdown files, 12 imported context sources, four reviewed skill files, 15 draft requirements and disabled live defaults.
- `ruff check .` and `ruff format --check .` passed.
- `mypy` passed for four source files.
- `python -m unittest discover -s tests -v` passed seven control tests, including mutated sources, path escape, symlink bypass, inference/default type changes and unexpected skill files.
- Compared installed skill Git blob hashes with the pinned upstream tree before recording the review receipt.

The same source checks and control tests run again in the final repository after copying, followed by staged Git whitespace validation and an initial local commit. GitHub Actions is configured but has not run remotely. These results establish local repository controls only. No application/tax extraction, tax calculation, model inference, independent tax review, cloud deployment or operation is claimed.

Initial helper execution needed an existing CA bundle for TLS; verification remained enabled. The dependency cache and intermediate virtual environment are outside the new source tree and are not copied into Git.

## Visual evidence discovery update 21 October 2026

Read the Oposiciones native ConceptLock source/design/tests and recorded source hashes and evidence limits. Updated product/discovery, requirements, proposed designs, evaluation/security/operation plans and the working handoff. No renderer, vision provider, tax extraction or quality comparison was executed. The repository checker passed for 47 Markdown files, twelve imported sources, four reviewed skill files and fifteen draft requirements; all seven existing repository-control tests passed. Lint/format checks also passed. These are documentation/control checks, not PDF rendering, visual-model or tax-domain tests.

## First source push and hosted CI 21 October 2026

At the owner's explicit request, verified GitHub authentication and the existing public `vjsequi/spanish-tax-assistant` destination, connected `origin`, fast-forwarded local `main` to the committed visual-evidence work and ran `git push --set-upstream origin main`. No force push or visibility change was needed. The working tree was clean before publication; the repository checker passed before the push.

[Hosted run 39582623574](https://github.com/vjsequi/spanish-tax-assistant/actions/runs/39582623574) completed successfully for commit `bafff1ed7884659125628e923fb5477211633cf4`. GitHub Actions installed hash-locked development tools and passed repository/provenance checks, lint/format, strict types and the seven repository-control tests. Verified with `gh run view 39582623574 --repo vjsequi/spanish-tax-assistant --json status,conclusion,jobs,url,headSha`. This establishes hosted foundation CI only; application implementation, domain evaluation and deployment remain unstarted.

## Continued product interview 21 October 2026

Recorded the owner's actual interview answers, updated the definition and draft requirements, and retained unanswered questions and dependencies. No application behaviour, tax labels or provider calls were added. During this update, `.venv/bin/python scripts/check_repository.py`, `.venv/bin/ruff check .`, `.venv/bin/ruff format --check .`, `.venv/bin/mypy`, `.venv/bin/python -m unittest discover -s tests -v` and `git diff --check` passed. The tests remain the seven foundation controls. The repository checker was rerun after later documentation/register edits; the latest output is retained in the tool execution record. Proposed review-pack sizes are planning recommendations, not authored cases or independent labels.

The interview checkpoint `d904930dc1068606fe8e4904680877adc3b3a3bf` was committed and pushed. [Hosted run 39585351247](https://github.com/vjsequi/spanish-tax-assistant/actions/runs/39585351247) passed; verified with `gh run list --repo vjsequi/spanish-tax-assistant --branch main --limit 2 --json databaseId,headSha,status,conclusion,url`. Private discovery answers were saved only under an already-ignored local directory, with directory/file permissions restricted to the owner; no reference case files or labels were opened or staged. Subsequent consolidation passed the checker with 50 Markdown files, 27 draft requirements, twelve imported sources and four reviewed skill files, plus `git diff --check`. The selected 30-file/100-page workload and 95%/five-minute/20% targets have not been executed.

The owner then explicitly froze product baseline 1.0. Recorded the exact confirmation and approval metadata while leaving detailed requirement entries as drafts pending legal/field specification. Reran all six local README-equivalent checks using the locked `.venv` tools: repository/provenance (50 Markdown files/27 requirements), Ruff lint/format, strict mypy (four source files), all seven repository-control tests and Git whitespace validation passed. `git ls-files .private` returned no tracked paths. This validates the consolidated repository foundation, not the selected tax/AI/performance targets.

## Detailed specification and synthetic review preparation 21 October 2026

At the owner's explicit request, collected fifteen public static AEAT/BOE references (not taxpayer portal downloads) with bounded `python -m scripts.pin_official_sources --download`, then verified the retained hashes offline. The initial Python trust store rejected TLS; retry used the existing trusted CA bundle through `--ca-file`, with verification enabled. Unlisted BOE date queries silently selected later text: retained the five rejected responses locally, selected actual listed editions and checked the response's selected-version marker. No tax-review approval is inferred from hash verification.

Added pinned development-only ReportLab 4.4.9, pypdf 6.10.0 and Pillow 12.3.0 using `uv add --dev ... --no-build`. The AEAT manuals require AES support in pypdf; installed its documented crypto extra with `uv --cache-dir .runtime/uv-cache add --dev 'pypdf[crypto]==6.10.0' --no-build`. Cryptography 50.0.2, cffi 2.1.1 and pycparser 3.11 are locked transitive development dependencies. Inspected installed package licence metadata and retained nine distributed notice/licence files with hashes. Refreshed CI requirements using `uv --cache-dir .runtime/uv-cache export --locked --offline --only-dev --format requirements-txt --no-emit-project --no-header --quiet --output-file requirements-dev.txt`.

Static reference inspection used `pdfinfo` and `pdftotext -layout`. Poppler reported embedded-font warnings for the AEAT manuals; text extraction alone is not visual/legal validation. The field checker initially found plain extraction merged adjacent 1123/1122 labels. Confirmed both visually on original form physical page 62 and with layout extraction, then added a token-preserving fallback rather than accepting arbitrary digit substrings. The retained form has 87 physical pages. Manual parts 1/2 have 1,448/634 pages; the printed updates are 20 May/30 September 2026. Their original bytes remain unchanged.

Authored `2025-dev-0.1` using `.venv/bin/python -m scripts.build_review_cases`: twenty cases, 110 source files, 180 source pages and one 23-page Spanish review guide. C018 has exactly thirty files/one hundred pages. Sources include 107 PDFs, two PNGs and one JPEG; C016's PDF is checked to have no embedded text. Five synthetic partial draft excerpts contain supplied comparison values, not expected tax truth. No expected tax answers were generated. The input manifest binds authoring data, generator, official source-set hash and Python/document-tool versions. Local Poppler is `pdftoppm version 23.05.0`; the external renderer is recorded, not a cross-platform byte-reproducibility guarantee.

Visual QA: rendered all 23 guide pages and all 180 source pages with Poppler into ignored `.runtime/visual-qa`, inspected three guide contact sheets and twelve source sheets, then inspected the guide cover, family declaration and benefits-in-kind certificate at higher resolution. Also inspected the original form's rent annex at higher resolution. No clipping, overlap, missing glyphs or unintended blank pages were observed in the authored documents; C017's blur is deliberate and its readable-fact labels remain pending independent review. Some local Poppler runs printed Fontconfig cache warnings but produced the inspected pages. This is layout QA, not tax/fact correctness or real-institution layout coverage.

Final local README-equivalent checks used the locked `.venv` executables:

- `python scripts/check_repository.py`: 53 Markdown files, 27 requirements, twelve imported sources and four reviewed skill files; expected-answer Markdown is now excluded from traversal.
- `python -m scripts.check_tax_pack`: fifteen retained references, seventeen stages, 108 field/page memberships, 25 unapproved rule contracts, nine open questions, twenty cases, 110 files/180 pages and nine licence receipts.
- `ruff check .`, `ruff format --check .` and strict `mypy`: passed (nine source files checked by mypy).
- `python -m unittest discover -s tests -v`: eighteen control tests passed, including source/edition/page mutation, hostile URLs, exact-number policy, input contamination/path escape, export inventory isolation, expected-area exclusion and reviewed-pack regeneration refusal.
- `python -m scripts.package_tax_review`: created a focused public/synthetic ZIP with internal hash receipts. Checked every archive member/hash, ZIP integrity, absence of private/expected/authoring paths and byte equality across two builds in this environment.
- `git diff --check` / staged equivalent: passed for authored text. Initial staged checks flagged publisher whitespace/CRLF and PDF serialization whitespace. Added byte-preserving Git attributes for originals/licences and binary attributes for PDFs/images instead of modifying them, then rechecked staged text and original-byte hashes. Tracked private/runtime paths are absent; the pre-existing expected-area README is documentation, with no independent labels authored or inspected.

These are source/specification/fixture controls and layout checks. No application extraction, tax engine, model/gateway inference, independent tax review, private-reference inspection, performance/value experiment, AEAT authentication/import/filing or cloud application deployment occurred. All nine tax questions and exact rounding/applicability approval remain open. The change was committed and pushed as `d8d42e3143f6a9011ea134ea5e722d629f4dfb87`. [Hosted run 39627799064](https://github.com/vjsequi/spanish-tax-assistant/actions/runs/39627799064) completed successfully on Ubuntu: hash-locked tool installation, repository/provenance and tax-pack integrity, lint/format, strict types and eighteen control tests. Verified with `gh run view 39627799064 --repo vjsequi/spanish-tax-assistant --json status,conclusion,jobs,headSha,url`. A subsequent documentation-only checkpoint records that run; the reference and fixture identities are unchanged.
