# Spanish Tax Assistant

An evidence workbench for reviewing a Spanish personal income-tax draft: establish the facts, find missing or conflicting information, and explain proposed field changes before a person files in Renta WEB.

**Current stage: product discovery and repository foundation, 21 October 2026.** The owner selected a first scope: tax year **2025**, a **Balearics resident employee**, employment income, bank interest and selected deductions. Childcare/conciliation and habitual-home rent are the first deduction research candidates. The first deliverable is a review packet with evidence and proposed field changes. Independent tax review is still to arrange; a potential reviewer exists. Tax extraction, calculations, AI investigation and deployment are not implemented.

## Start here

1. [Product definition](docs/product/definition.md) — user, outcome, scope and initial acceptance criteria.
2. [Discovery decisions](docs/product/discovery.md) — actual owner answers and remaining questions.
3. [Requirements](docs/requirements/README.md) and [backlog](docs/product/backlog.md) — traceable behaviour and delivery slices.
4. [SDLC](docs/process/sdlc.md) — define, design, implement, inspect, evaluate, iterate, release and operate.
5. [HLD](docs/design/hld.md) and [LLD](docs/design/lld.md) — proposed design and open choices.
6. [Evaluation plan](docs/evaluation/plan.md), [threat model](docs/security/threat-model.md) and [operations](docs/operations/runbook.md).
7. [Working handoff](docs/context/handoff.md), [glossary](GLOSSARY.md) and [agent instructions](AGENTS.md).

The recovered use-case notes and relevant predecessor evidence are inside [context imports](docs/context/imports/README.md), with original and imported hashes in the [source manifest](docs/context/source-manifest.json). No Obsidian vault or old checkout is required to continue here.

## Work locally

Python 3.14 is the initial development baseline. The application has no runtime dependencies yet. Development tools are version-locked.

```sh
uv sync --locked
uv run --locked python scripts/check_repository.py
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
uv run --locked python -m unittest discover -s tests -v
```

The documentation/provenance checker also runs with `python3 scripts/check_repository.py` without installing tools. It checks repository consistency, imported hashes and disabled live-operation defaults; it does not evaluate tax correctness. CI runs these same foundation checks. Hosted CI execution and cloud deployment need their own evidence.

## Working agreements

- Keep supported tax treatments in versioned, tested rules. Use AI to help extract, retrieve, ask and explain.
- Preserve exact money and the rounding required by each supported rule. An authentic quotation alone does not prove a correct treatment.
- Use only synthetic data in the public development tree. Private tax documents, credentials, sessions, prompts and traces belong in ignored private storage.
- Live model allowance is zero. New calls require provider/model, cost, call and time limits. Cloud spend and AEAT portal operations require specific authorisation.
- The repository contains only the reviewed, pinned `grill-me` and `grilling` skills from Matt Pocock. See [skill review](docs/security/skill-review.md). Invoke `/grill-me` explicitly; the interview develops the product decisions before implementation.

AWS is the preferred cloud candidate, with GCP as fallback. Development, staging and production are planned environments; none is provisioned. Earlier budget targets of under EUR 10 idle and about EUR 40 during active development are carried as planning targets across environments, not measured tax-product costs.
