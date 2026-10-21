# Spanish Personal Tax Project Exploration

**Recorded 21 October 2026. Status: candidate for the next portfolio project.** The owner recovered the 20 October use-case notes and asked to assess a shift from invoice reconciliation to a useful Spanish personal-tax application. The saved analysis supports a narrowly scoped evidence and draft-review assistant. A replacement project, new repository and tax implementation have not been selected.

## Recovered baseline

The source notes are in the owner's Obsidian `Work Vault/Use Cases` folder:

- `00 AI Production Use Cases.md`, created 20 October, status `exploring`.
- `07 Spanish Tax Preparation Assistant.md`, created 20 October, status `candidate`.

The index compares seven directions: niche support, software incidents, invoice exceptions, security evidence, property maintenance, supplier contracts and Spanish personal tax. It favours incident investigation without a business partner, support with an available operator, and invoice exceptions for continuity with existing finance work. Tax is attractive for personal usefulness, conditional on trustworthy domain review and annual maintenance. It records no final selection.

The shared pattern is receiving a case, establishing permissions, retrieving evidence and policies, interpreting or asking, validating, obtaining review and retaining the outcome. The owner's goal includes understanding and explaining the implementation, reproducible setup, measured quality and useful operation. Originality and agent count are secondary to those outcomes.

Source SHA-256 values at recovery:

- Index: `1ef5f40b20fbccf41de3109ea4f8949051df7070d8fabe16c1e89fe6a153e386`.
- Tax note: `92446f809f72576c533cb21cb29a8612313f5ca6e2edc98a0264d4bb6280742a`.

## Proposed product and first scope

Help an individual understand whether a Spanish personal income-tax draft is complete and supported by their documents. Produce discrepancies, focused questions and proposed field changes, each linked to evidence, the applicable rule and any calculation. The proposed value is less work gathering and checking information before a person reviews the return.

The recovered note suggests one completed tax year, one region such as the Balearics, and a defined taxpayer profile covering employment income, bank interest and selected deductions. A concrete feasibility candidate is **tax year 2025, Balearics, common-regime resident employees**, subject to owner selection and tax-professional review. Residence and supported circumstances must be established from facts; the owner's location does not establish their tax profile.

Start with document imports and a reviewable evidence packet. Foreign income, business activity, complex investments and unsupported regimes require a scope decision. Companies, other countries and automated filing are later expansions. An unresolved tax treatment should remain a question or referral. Coverage should grow by independently validated treatment, not by allowing an LLM to improvise more answers.

## User cases and shared capabilities

| User case | Useful result | Engineering capability |
|---|---|---|
| Establish whether the documents are sufficient | A specific missing-document or missing-fact request | Structured extraction, completeness rules and conversation state |
| Compare certificates and statements with a draft | Supported differences with document and field references | Document understanding, normalisation, exact comparisons and provenance |
| Check a selected deduction | Supported eligibility, missing conditions or escalation | Retrieval filtered by tax year and region, rule checks and useful clarification |
| Explain a proposed field change | A trace from source fact through rule and calculation to the changed field | Typed tools, deterministic calculation and evidence-grounded explanation |
| Review and export the preparation work | An accepted version and an inspectable review packet | Human authority, immutable versions, private storage and reproducible export |

A demonstration could contain two certificates with conflicting withholding figures and an incompletely supported deduction. The assistant would establish the document versions, ask which certificate is authoritative when necessary, retrieve the relevant supported rule, and show the resulting proposed changes. This is a proposed synthetic case, not an actual taxpayer result or an evaluation label.

AI would assist extraction, document classification, evidence retrieval, question selection and explanation. Versioned code would implement supported calculations and eligibility conditions. Citation identity alone cannot prove that a tax interpretation is correct.

## Reuse candidates checked on 21 October

**Existing project.** Reuse the patterns for source provenance, scoped tools, structured output, durable jobs, source freshness, separate human authority, isolated evaluation and redacted OpenTelemetry. Review module boundaries before extracting code: the current financial model, datasets and scorer are tied to invoice reconciliation. Its test counts and historical model results do not measure tax accuracy. See current comparison implementation (previous repository: `../comparison-implementation.md`) and local observability (previous repository: `../../observability/README.md`).

**AEAT reference services.** [Renta WEB](https://sede.agenciatributaria.gob.es/Sede/Renta.html) supplies the existing preparation context. [Renta WEB Open](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/renta-ayuda-tecnica/renta-web-open.html) can simulate a return without authentication and produce a preview, but cannot file it. Selected, manually checked synthetic scenarios could provide a calculation cross-check; the simulator is not an established automated API or an independent judgement of document completeness. AEAT also [documents importing a return from an external XML file](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/renta-ayuda-tecnica/presentar-declaracion-mediante-fichero-generado-externo.html). Format validation and correct tax treatment require separate checks.

**Spanish portal integration reference.** [hacienda-cli](https://github.com/jatorre/hacienda-cli/tree/353671652116c0b93e7d7e9fe2a5092fd9576203) documents downloading tax data/draft artifacts, local XML checks and browser-based import. It does not supply a complete tax engine. Its README reports dependence on a live headed browser and changing AEAT screens. At that pinned revision, [README](https://github.com/jatorre/hacienda-cli/blob/353671652116c0b93e7d7e9fe2a5092fd9576203/README.md) and [package metadata](https://github.com/jatorre/hacienda-cli/blob/353671652116c0b93e7d7e9fe2a5092fd9576203/package.json) declare AGPL-3.0-or-later while [LICENSE](https://github.com/jatorre/hacienda-cli/blob/353671652116c0b93e7d7e9fe2a5092fd9576203/LICENSE) contains MIT. Resolve that inconsistency before copying or distributing it. Inspection of the [CLI entry point](https://github.com/jatorre/hacienda-cli/blob/353671652116c0b93e7d7e9fe2a5092fd9576203/src/index.ts) also found shell-interpolated filenames and an upload path that continues after local schema-check failure. Treat it as a candidate for further audit and hardening; no execution or portal behaviour was verified.

**Document processing.** [Docling](https://github.com/docling-project/docling) supports structured PDF/table extraction and OCR with local execution. Its code is MIT licensed; model licences are separate. It is a candidate to compare with simpler extraction on the selected documents, with CPU, memory and startup costs included.

**Calculation components.** [OpenFisca Core](https://github.com/openfisca/openfisca-core) supplies a tax-benefit modelling engine whose tax rules come from country packages; it is not by itself a complete Spanish return implementation. The [spanish-tax-calculators README](https://github.com/luxeon/spanish-tax-calculators) describes narrower JavaScript calculations, and [irpf_spain](https://github.com/srponze/irpf_spain) targets broker transactions. These remain research candidates. A coverage, provenance, licence and test review would precede reuse; none has been selected as the supported IRPF engine.

## Evaluation and operation

The recovered note calls for approximately ten synthetic feasibility cases and an independent qualified Spanish tax reviewer. These would test scope, expected answers and usefulness; broader accuracy needs a separate frozen evaluation. Review individual facts and treatments as well as the total: different errors can cancel numerically.

Compare a checklist/rules baseline, deterministic retrieval plus a fixed model call, and a bounded agent choosing permitted retrieval tools. Keep the same permitted evidence, declared tasks and explicit resource bounds. Specialist delegation would follow a demonstrated failure that benefits from separate context, independent tasks or different permissions. Harbor is a candidate execution adapter; the domain rubric and human review remain necessary. Framework choice and workflow policy should be evaluated separately.

Measure fact/field correctness, omitted income, unsupported deductions, applicability of year/region rules, necessary questions, escalation and reviewer corrections/time. Traces should explain retrieval, tool outcomes, validation failures, conflicts, source changes, timeout and recovery. Default logs and metrics must exclude taxpayer identities, documents and model text. Source evidence and authoritative review records belong in protected application storage.

A hosted version would need trusted authentication, private per-case access, source and rule versioning, retention/deletion controls, bounded inference and deployed recovery/redaction checks. A publicly accessible portfolio would use synthetic examples. Existing AWS budget targets and development/staging/production aspirations can inform a fresh cost study; they do not establish this product's operating cost or authorise provisioning or inference.

## Decision before creating a repository

The tax assistant is a credible flagship candidate because it adds useful document review, contextual retrieval, rule versioning and measurable human assistance. Its main uncertainty is reliable tax coverage and access to an accountable reviewer. More agents cannot resolve that dependency.

Next settle the taxpayer profile and first supported treatments, obtain reviewer availability, and assess a small synthetic document pack and an existing-code shortlist. If that feasibility review succeeds and the owner selects the tax direction, create a separate repository carrying the scope, source inventory, reuse/licence decisions, architecture and evaluation plan. Preserve invoice reconciliation as inspectable prior work and extract shared components deliberately. Until then, this is exploration alongside the existing project's evidence plan (previous repository: `../evidence-plan.md`), not a replacement implementation backlog.
