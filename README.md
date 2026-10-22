# Spanish Tax Assistant

An evidence workbench for reviewing a Spanish personal income-tax draft: establish the facts, find missing or conflicting information, and explain proposed field changes before a person files in Renta WEB.

**Current stage: first working synthetic slice, 22 October 2026.** C001 now runs locally through source-page inspection, editable/confirmed facts, a provisional deterministic calculation, supplied-draft comparison and Spanish PDF/JSON export. Professional tax QA is scheduled for the end of development, as the owner directed. The wider product, AI extraction and cloud deployment remain unfinished; no independently validated tax accuracy is claimed.

The source-derived specification retains fifteen original references, seventeen calculation stages, 108 field mappings and 25 candidate rules. Four additional AEAT guidance pages support C001 development. Twenty synthetic cases remain available for later branch expansion/review; nine recorded tax questions remain open. See the [working slice and limits](docs/design/c001-working-slice.md) and [review sequencing decision](docs/decisions/0004-development-before-tax-review.md).

**Initial intake direction, confirmed 21 October:** PDFs, including scanned/image-only PDFs, and standalone images/screenshots are first-class evidence. Preserve original files and page images and confirm extracted facts. The first slice renders the fixed C001 PDFs for visual/manual review, with a narrow digital-template prefill explicitly labelled as such. General PDF/image admission, vision-model extraction and comparative intake evaluation remain pending. See [the visual-evidence decision](docs/decisions/0003-visual-document-evidence.md).

**Further product decisions:** individual returns, multiple employers, optional AEAT draft at case start, confirmed facts before proposals, Spanish interface/packet and English technical documentation. A partial review must expose its coverage gaps and unresolved dependencies. See [discovery](docs/product/discovery.md) for actual answers; implementation and detailed acceptance remain pending.

The agreed product also needs an **independent complete tax/refund calculation for fully covered cases**, alongside the evidence-backed PDF/optional JSON packet. Only the owner initially logs in; professional review is through exported packets. Private reference material stays local and is not part of the public repository or its quality evidence.

## Start here

1. [Product definition](docs/product/definition.md) and [acceptance baseline](docs/product/acceptance.md) — user, outcome, scope, owner-selected pilot targets and blocking release checks.
2. [Discovery decisions](docs/product/discovery.md) — actual owner answers and remaining questions.
3. [Requirements](docs/requirements/README.md) and [backlog](docs/product/backlog.md) — traceable behaviour and delivery slices.
4. [SDLC](docs/process/sdlc.md) — define, design, implement, inspect, evaluate, iterate, release and operate.
5. [HLD](docs/design/hld.md) and [LLD](docs/design/lld.md) — proposed design and open choices.
6. [Evaluation plan](docs/evaluation/plan.md), [threat model](docs/security/threat-model.md) and [operations](docs/operations/runbook.md).
7. [Working handoff](docs/context/handoff.md), [glossary](GLOSSARY.md) and [agent instructions](AGENTS.md).

### Detailed requirements and review pack

Read the [2025 tax specification and calculation graph](docs/requirements/tax-2025.md), then the [independent review instructions](evals/review/reviewer-guide.md). The [reference set](data/rules/2025/README.md) retains exact AEAT/BOE bytes and selected consolidation editions. The [synthetic input manifest](evals/inputs/manifest.json) binds 20 cases, 110 files and 180 pages; C018 is the 30-file/100-page workload. The [Spanish review guide](output/pdf/tax-2025-review-guide.pdf) inventories every case. These exposed development cases have no independent answers yet and are not a held-out test set.

The recovered use-case notes and relevant predecessor evidence are inside [context imports](docs/context/imports/README.md), with original and imported hashes in the [source manifest](docs/context/source-manifest.json). No Obsidian vault or old checkout is required to continue here.

## Work locally

Python 3.14 is the development baseline. The local adapter uses pinned pypdf, Pillow and ReportLab plus an existing Poppler `pdftoppm` executable. Model calls remain disabled.

```sh
uv sync --locked
PYTHONPATH=src uv run --locked python -m renta_assistant --port 8020
```

Open [the local workbench](http://127.0.0.1:8020/). Start with the source images, confirm the fictional facts and coverage, then save/calculate. Incomplete confirmations produce a partial review. The current calculator supports only the documented C001 branch; this is a loopback-only synthetic development server, with no uploads or hosted private access. State persists under ignored `.runtime/workbench`.

Run the checks:

```sh
uv sync --locked
uv run --locked python scripts/check_repository.py
uv run --locked python -m scripts.check_tax_pack
uv run --locked python -m scripts.pin_development_guidance
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
PYTHONPATH=src uv run --locked python -m unittest discover -s tests -v
```

The documentation/provenance checker also runs with `python3 scripts/check_repository.py`. Tax-pack/source checks verify hashes, declared editions, stage/field links and input isolation. The tests additionally exercise provisional arithmetic, application commands, local state and HTTP boundaries. Source-derived numeric assertions are authored engineering evidence pending final professional QA; they are not independent labels or measured tax accuracy. CI runs the same checks.

To create the shareable review ZIP locally, run `uv run --locked python -m scripts.package_tax_review`. It packages an explicit public/synthetic inventory, including the retained references and blank answer template, into `output/review/tax-2025-review-pack.zip`. Regenerating source fixtures additionally requires Poppler; see [authoring](evals/authoring/README.md). Do not regenerate a reviewed version in place. Source collection is explicit and bounded; the source tool verifies offline by default.

## Working agreements

- Keep supported tax treatments in versioned, tested rules. Use AI to help extract, retrieve, ask and explain.
- Preserve exact money and the rounding required by each supported rule. An authentic quotation alone does not prove a correct treatment.
- Use only synthetic data in the public development tree. Private tax documents, credentials, sessions, prompts and traces belong in ignored private storage.
- Live model allowance is zero. New calls require provider/model, cost, call and time limits. Cloud spend and AEAT portal operations require specific authorisation.
- The repository contains only the reviewed, pinned `grill-me` and `grilling` skills from Matt Pocock. See [skill review](docs/security/skill-review.md). Invoke `/grill-me` explicitly; the interview develops the product decisions before implementation.

AWS is the preferred cloud candidate, with GCP as fallback. Development, staging and production are planned environments; none is provisioned. Earlier budget targets of under EUR 10 idle and about EUR 40 during active development are carried as planning targets across environments, not measured tax-product costs.
