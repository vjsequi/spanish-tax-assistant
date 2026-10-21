---
created: 2026-10-20
status: exploring
tags: [ai, portfolio, use-cases]
---

# AI Production Use Cases

The goal is to build and operate a useful AI application that Vicente understands well enough to explain end to end and rebuild from a clean environment. Originality is secondary to a clear business need, sound security, measurable quality, reliable operation and reproducibility. These are candidate directions; no replacement for the existing finance project has been selected.

## Candidate ideas

| Idea | Manageable first scope | Main dependency |
|---|---|---|
| [01 Niche Support Caseworker](01-niche-support-caseworker.md) | Investigate equipment-rental or repair requests using records and policies; prepare resolutions for approval | Access to an operator and representative cases |
| [02 Software Incident Investigator](02-software-incident-investigator.md) | Diagnose a defined set of failures in one owned AWS application | Useful telemetry and reproducible faults |
| [03 Invoice Exception Investigator](03-invoice-exception-investigator.md) | Compare invoices, purchase orders, delivery records and correspondence | Representative documents and a finance reviewer |
| [04 Security Evidence Assistant](04-security-evidence-assistant.md) | Answer customer security questionnaires with current supporting evidence | A reliable security evidence library and an accountable reviewer |
| [05 Property Maintenance Coordinator](05-property-maintenance-coordinator.md) | Clarify maintenance requests, detect duplicates and prepare work orders | A property manager who can validate routing and escalation |
| [06 Supplier Contract Reviewer](06-supplier-contract-reviewer.md) | Identify deviations from an explicit purchasing playbook | An approved playbook and review of ambiguous clauses |
| [07 Spanish Tax Preparation Assistant](07-spanish-tax-preparation-assistant.md) | Prepare evidence and a reviewed draft for one tax year, region and defined taxpayer profile | Independent validation by a qualified tax professional |

## Provisional recommendation

Without an external business partner, the software incident investigator is the strongest candidate for personal use and direct validation. With a willing operator, a niche support caseworker offers a clear business workflow and regular feedback. The invoice exception investigator is the strongest continuation of the finance direction and could reuse existing evidence, review, evaluation and telemetry components.

Broad tax preparation carries a larger domain-maintenance burden. A narrow tax assistant remains attractive if a tax professional can help establish trustworthy expected answers. Access to a real workflow should determine the final choice more strongly than novelty or agent count.

## What the established examples have in common

Messages, documents or logs contain incomplete information. The application combines them with structured records and policies, establishes what is known, asks about missing facts, and prepares an action. Routine cases can follow rules; ambiguous cases require interpretation.

**Receive a case → establish permissions → retrieve evidence → interpret or ask → validate → review and act → retain the outcome.**

| Business requirement | Engineering consequence |
|---|---|
| Keep customer records private | Enforce access in retrieval and tools; test cross-customer requests |
| Avoid duplicate actions | Durable state, idempotency and recovery checks |
| Handle changing policies and records | Version evidence and recheck relevant state before committing actions |
| Prevent costly unsupported decisions | Evaluate incorrect actions and unsupported claims as well as successes |
| Diagnose failures | Correlate retrievals, tool results, validation and handoffs without exposing sensitive evidence in routine logs |
| Reduce work | Measure completed cases, corrections, escalations and reviewer time |

Published customer stories establish that these workflow categories are used commercially. Reported savings are supplier/customer claims and do not predict results for a new implementation. Each idea note links its reference example and separates it from the proposed niche application.

## Comparing implementations

Start with a simple baseline: rules, deterministic retrieval and a fixed model call where needed. Compare it with a bounded tool-using agent. Add specialist delegation only when a specific failure suggests a benefit from independent tasks, context isolation or different permissions.

Use the same permitted evidence, task requirements and declared resource bounds. Measure task success, harmful actions, unsupported claims, useful clarification, reviewer effort, latency and known cost. Retain failures and skipped trials. Evaluate both outputs and resulting application state; polished explanations alone cannot establish correctness.

[Harbor](https://docs.harborframework.com/core-concepts) provides tasks, environments, agent integrations and verifiers for repeatable evaluations. [τ-bench](https://github.com/sierra-research/tau-bench) provides a relevant pattern for conversational support: policies, tools, simulated users and checks against the intended database state. These are candidate infrastructure and methodology choices; domain-specific expected answers and review remain necessary.

[Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) supplies context management, delegation and other harness capabilities on top of LangChain and LangGraph. A more elaborate harness must earn its operating and maintenance costs in the comparison.

## Evidence needed for completion

- [ ] Name the user, recurring problem, supported scope and useful outcome.
- [ ] Obtain representative cases and an accountable domain reviewer.
- [ ] Implement a deployed application with authentication, bounded permissions and review where actions have consequences.
- [ ] Reproduce the build, infrastructure and setup from a clean environment with pinned dependencies.
- [ ] Compare a simple baseline and the agent workflow on fixed, independently reviewed cases.
- [ ] Demonstrate timeout, duplicate-request, stale-data and recovery behaviour.
- [ ] Inspect an operational dashboard, exercise useful alerts and document a recovery drill or incident.
- [ ] Measure actual usage and reviewer effort; distinguish synthetic demonstrations, controlled drills and natural operational events.
- [ ] Walk through one case from evidence and permissions through tools, model calls, validation and final state.
- [ ] Reimplement a small core slice from the design, explaining the decisions and tests without relying on generated code as the explanation.
- [ ] Publish source, setup instructions and synthetic examples with suitable licences; keep customer records, secrets and raw private traces outside public artifacts.

A hosted application exercised with synthetic inputs establishes deployment and operation evidence. Business-use claims require actual use and feedback. Production quality includes ongoing maintenance, incident response and domain validation within the declared scope.

## Related work

- `Career Portfolio/00 Career Portfolio` (reference in the original vault)
- `Learning/00 Learning Home` (reference in the original vault)
