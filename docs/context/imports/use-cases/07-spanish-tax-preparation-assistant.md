---
created: 2026-10-20
status: candidate
tags: [ai, use-cases, tax, spain]
---

# Spanish Tax Preparation Assistant

[Use cases index](00-ai-production-use-cases.md)

Prepare and review evidence for a narrowly defined Spanish personal tax return. Personal interest makes this attractive, but reliable tax coverage and annual maintenance are substantial parts of the product.

## Established examples and domain sources

[Intuit's case study](https://www.anthropic.com/customers/intuit) describes AI-generated explanations combined with its existing tax knowledge engine. In Spain, [AEAT's Renta WEB services](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/consultas-informaticas/renta-ayuda-tecnica/renta-web-tramitacion-borrador-declaracion.html?origen=app) already support draft preparation and filing. The proposed value is helping establish that a draft is complete, supported and understood.

[AEAT's 2025 regional deductions guide](https://www3.agenciatributaria.gob.es/Sede/Ayuda/25Manual/100/deducciones-autonomicas.html) illustrates why region and tax year must be explicit. Spanish companies and UK companies would be separate expansions. For example, [HMRC requires iXBRL accounts for most company returns](https://www.gov.uk/government/publications/company-tax-returns-format-for-accounts-forming-part-of-an-online-return), with stated exceptions.

## Demonstration case

A fictional taxpayer supplies salary certificates, bank statements, supporting receipts and an AEAT draft. The assistant identifies conflicting figures, requests a missing certificate, checks supported deduction conditions and prepares proposed field changes. Each change links to the source document, applicable rule and calculation.

## First scope

Select one completed tax year, one region such as the Balearics and a defined taxpayer profile. A possible initial scope is employment income, bank interest and selected deductions. Foreign income, business activity and complex investments would initially trigger a scope check. This proposal does not assume that Vicente's own circumstances fit that profile.

Start with a reviewable draft and evidence packet. Automated submission would be a later integration with its own validation and representation requirements. Keep supported calculations, thresholds and eligibility rules in versioned, tested code. A model can help extract, classify, retrieve and explain, but a citation alone does not establish correct tax treatment.

## Security and operation

Tax records contain sensitive personal and financial information. Use authenticated access, private storage, bounded retrieval and redacted telemetry. Treat documents as untrusted input. Retain source, tax-year, rule and reviewer provenance for every proposed change.

Observe extraction failures, conflicting facts, outdated rules and unresolved questions. A new year's guidance must not silently change the interpretation of a saved earlier return.

## Evaluation

Measure correct facts and fields, applicable rules, unsupported deductions, omitted income, necessary questions and correct escalation. Check individual treatments as well as totals because different errors can cancel numerically. Measure reviewer effort and corrections.

Independent review by a qualified Spanish tax professional is essential before relying on the supported output for an actual return. Approximately ten synthetic cases could test feasibility, reviewer availability and usefulness; they would not establish production-wide accuracy.

## Main dependency and difficulty

The main dependency is trustworthy tax ground truth and maintenance, rather than agent orchestration. Narrow evidence preparation is achievable; reliable arbitrary personal and company returns across Spain and the UK would be a much larger undertaking.
