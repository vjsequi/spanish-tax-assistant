# Evidence plan: justify the AI, workflow and operating cost

**Owner:** project owner. **Started:** 16 October 2026. **Status:** plan established; comparisons and release gates remain open.

Choose the least costly solution that meets the task's quality, security and operating requirements. Every material choice needs a question, alternatives, a bounded comparison and a dated decision. A more capable model or more elaborate workflow must earn its additional cost. Keeping rules or a simple pipeline is a valid result.

This applies the owner's AWS Generative AI Developer learning themes to this project. It is a project checklist, not a certification assessment or a claim to have completed the course. Here, validation means **financial/domain correctness and usefulness to a reviewer**; this is not a clinical application.

## How to check a box

A checked item below names a specific completed artifact or observation. It does not close its whole stage. Close a stage only when all its required items have dated evidence, code/data/configuration versions, an accountable reviewer and stated limitations. Distinguish implemented, locally tested, historically observed, human reviewed and cloud verified. Do not convert a missing measurement into zero or a planned test into a pass.

Use the decision record template (previous repository: `evaluation-results/decision-template.md`) for comparisons. Actual experiment artifacts stay in ignored private storage; only reviewed synthetic aggregates belong in Git. Existing release gates (previous repository: `release-readiness.md`) still govern publication and cloud exposure. This plan authorises no new model calls or cloud resources; live experiments require their own explicit provider, cost and resource bounds.

## 1. Scope the problem and the value hypothesis

**Decision:** which part of reconciliation is worth assisting, for whom, and what stays under human control?

- [x] Document the scoped problem and examples: EUR receipts, known customer/workspace, candidate invoices and supplied remittance evidence; AI interprets payment intent and proposes or asks. See the product brief (previous repository: `product-brief.md`) and AI walkthrough (previous repository: `ai-investigation.md`).
- [x] Define authority: AI cannot approve, reverse, forgive debt, change identity or obtain new permissions. A separate authorised reviewer commits exact financial commands.
- [x] Write the manual/assisted process map, baseline definitions and acceptance thresholds (previous repository: `scope-baseline-acceptance.md`), including intake, investigation, clarification, review, approval and exceptions. The owner confirmed the supported scope and targets on 16 October 2026.
- [x] Record the owner's acceptance of the scoped problem and desired benefit targets, with unsupported cases/fallbacks documented. This establishes owner agreement, not measured benefit or independent bookkeeper/user validation.
- [ ] Complete the per-experiment freeze of data, schedule/configuration and resource authorisation. The 17 October comparison protocol (previous repository: `comparison-plan-v1.md`) specifies the proposed case mix, phased schedule and agreed quality/time/latency arithmetic; final sources/labels and the phase-specific monetary authorisation remain open. An attractive demo alone is not business validation.

**Exit evidence:** a one-page scope/process map and signed-off hypotheses. Initial hypothesis: interpreting varied free text reduces investigation/review effort without increasing unsupported allocation suggestions. It remains a hypothesis.

## 2. Validate the data and evaluation framework

**Decision:** can the tests detect a useful improvement, a harmful regression and a misleading score?

- [x] Implement the isolated, versioned runner/scorer and seven-case development/held-out/adversarial manifest. Inputs and hidden labels are separate; the scorer runs after execution. See evaluation setup (previous repository: `evaluations.md`).
- [x] Retain the 6 October paired experiment (previous repository: `evaluation-results/2026-10-06.md`), including all 14 trials, exact checks, version hashes, resource bounds and unavailable monetary cost.
- [x] Complete assisted owner semantic review of the saved experiment, including all 14 conclusions/questions and eight claims. 17 October results (previous repository: `evaluation-results/2026-10-17-reviewed-summary.md`): AI-assisted 7/7 useful/supported, rules 3/7; all claims supported. Preserve four baseline usefulness failures and the distinction from independent expert review or new-model evidence.
- [x] Expand the source inventory with 30 authored development cases across ten families (previous repository: `../evals/comparison-v1/README.md`), including wording/cent variations, partial/split/overpayments, conflicts/missing intent, equal candidates, exclusions, unavailable targets and untrusted/quoted instructions. These are actual source files, not scored results or independently reviewed labels. Keep unsupported-input/intake boundary tests separate from supported investigation cases.
- [ ] Review independent source-derived labels, alternative valid outcomes and resolvability/security annotations, then integrate the expanded cases with the scorer. Keep intake and investigation datasets distinct and test the end-to-end path separately.
- [ ] Freeze new development and untouched final comparison splits by scenario/template family. Ground truth must depend only on evidence the application may see. Keep labels in the scorer; never load `evals/expected/` into model context or use public demo examples as fresh held-out cases.
- [ ] Check the test framework with deliberately wrong outputs, label/context leakage checks, tampered artifacts and missing/failed trials. Extend these existing software checks for every new variant and metric before trusting its results.

**Exit evidence:** versioned case inventory, reviewed rubric, scorer regression results and a frozen experiment plan. The brief's roughly 30 development cases is a planning starting point, not a sufficient benchmark by itself. Choose final case/repetition counts from coverage, observed variability and the authorised budget. Previously inspected held-out cases become regression cases; new final claims need a new untouched set.

## 3. Establish security and financial safety gates

**Decision:** can untrusted documents, model output, users or retries cause unauthorised reads or financial effects?

- [x] Implement and locally test scoped evidence/tools, strict structured outputs, citation/source checks, exact cents, restricted worker privileges, stale-result rejection and transactional approval/reversal. See the security contract (previous repository: `design/genai-security.md`), LLD (previous repository: `design/lld.md`) and dated verification backlog (previous repository: `implementation-backlog.md`).
- [x] Record the 17 October threat/control/test matrix (previous repository: `design/security-control-matrix.md`) for direct/document prompt injection, cross-workspace access, fabricated citations, malicious files, unsafe rendering, credential leakage and resource exhaustion. It links current local evidence and explicit residual/cloud gaps. New variant or cloud changes still require relevant deterministic and real-PostgreSQL checks; the matrix does not close the security stage.
- [ ] For cloud exposure, implement trusted owner authentication, current workspace authorisation, separate environment/IAM/database roles, private evidence, secret handling and inference disable/limit controls. The loopback development identity must fail closed in cloud runtimes.
- [ ] Verify negative access, expiry/revocation, duplicate/stale commands, provider uncertainty and redaction in the actual deployed environment before exposure. Keep raw evidence/model text out of routine telemetry and public bundles.

**Exit evidence:** threat matrix with linked test results and residual risks. Financial/permission violations block a candidate regardless of speed, savings or average quality. No automated financial writes during evaluations. Zero observed critical failures is required in the defined suite; it does not prove zero risk outside it. Prompt filtering or an LLM judge cannot replace authorisation, transactions or human approval.

## 4. Compare workflow options

**Decision:** which steps improve outcomes or reduce total work enough to justify their complexity?

| Option | Purpose | Current evidence |
|---|---|---|
| Manual review without AI | Measure the work being assisted using the same permitted source records | Timed study not performed |
| Conservative rules | Cheapest automated baseline; confirmed exact references or safe clarification | Implemented; historical exact checks 4/7 |
| One model call without the rules bypass | Test whether invoking a model on every supported case adds value; retain the same evidence, validators and pending-only publication | Implemented locally 18 October; authored software checks only, no live comparison or demonstrated quality gain |
| Current rules-gated, one-call LangGraph workflow | Avoid inference where rules suffice; otherwise prepare scoped evidence, interpret once, validate and publish pending | Implemented; historical exact and assisted owner support/usefulness checks 7/7; broader comparison pending |
| A targeted extra step | Test a specific observed weakness, such as missing candidate evidence or unsupported interpretation | Not justified or implemented by this plan |

- [ ] Compare rules with the current workflow on the frozen data, using the same task policy, source records, independent grading and safety controls. Report proposal precision **and** coverage: asking on everything cannot win through apparent precision.
- [ ] Compare the one-call variant and current gated workflow with the same provider/model, schema, context and inference settings. Record only the intentional change, including the bypass policy. Do not compare an unsafe unconstrained prompt with a fully validated application and attribute the difference to orchestration.
- [ ] Separate **workflow policy** from **framework choice**. The current graph is a bounded sequence with a conditional rules branch and at most one model request, not a multi-agent system. A plain Python pipeline can implement the same policy. Assess that alternative through shared contract tests, inspectability, recovery integration and maintenance effort; identical policy/model outputs would not demonstrate an accuracy gain from LangGraph itself.
- [ ] Add retrieval, a second pass, a critic or another agent only if development error analysis identifies a problem that step could solve. Compare that one change with the simpler finalist; record measured benefit, new failure modes and added implementation/operating effort. A justified decision to stop adding steps closes this item.

**Exit evidence:** paired result table, regressions and a workflow/framework decision. A more complex option wins only if it meets all safety/quality requirements and its additional benefit clears the predeclared value threshold. The 6 October study compared rules with the gateway-enabled path; it did not compare frameworks or multiple workflow architectures.

## 5. Select and verify the model

**Decision:** which eligible service/model is sufficient at the lowest total task cost?

- [ ] Establish eligibility before benchmarking: supported service identity, regional/data handling requirements, output contract, context limits, availability, quotas and current pricing. Hosting in AWS does not itself require a particular model provider.
- [ ] Shortlist two eligible candidates initially: a lower-cost candidate and a stronger reference. Reuse the selected workflow and a common prompt/output contract where supported; label any provider-specific prompt tuning as a separate configuration comparison.
- [ ] Run a newly authorised, bounded paired comparison, including repeated trials for stochastic variation. Retain actual model IDs/aliases, revision precision, settings, prompt/schema hashes, timestamps and every attempted/failed/skipped/uncertain trial. Do not select the best of several responses after seeing scores.
- [ ] Select the least expensive candidate meeting the frozen quality/safety/latency requirements, or record that evidence is inconclusive and retain a provisional choice. Document what would trigger a change.

**Exit evidence:** model decision with actual service-adapter verification and cost provenance. The historical local gateway was chosen for development convenience and authentic capture; it is not a proven winner or a cloud identity. Subscription cost is unknown, not free. No Gemini, OpenAI, Bedrock or other new inference run is authorised by this checklist.

## 6. Measure performance and failure behaviour

**Decision:** does the complete application remain usable, inspectable and safe under its intended workload and failures?

- [x] Implement local structured redacted logs, OpenTelemetry correlation and API/job/graph/provider/database instrumentation; retain dated local trace and alert evidence. See observability (previous repository: `../observability/README.md`).
- [ ] Measure request-to-pending-result wall time, queue wait, provider time and human review/correction time separately. Distinguish local/cloud and warm/cold database/function paths. State sample size and conditions; seven toy cases cannot establish a reliable production p95.
- [ ] Exercise duplicates, lease expiry, stale snapshots, stored-response recovery, uncertain provider dispatch, telemetry outage and database/object restoration. Measure recovery time and remaining data gaps; do not infer recovery from retries alone.
- [ ] Test the intended concurrency/resource limits and cloud alerts, including actual notification and recovery. Verify that background work is durably dispatched and health/recovery polling does not defeat database auto-pause.

**Exit evidence:** measured timings, resource/usage observations, failure/recovery report and operational limits. Use deterministic failure injection for expensive or unsafe conditions; it verifies software behaviour, not model quality. Measure cloud cold activation separately from the API timeout rather than hiding it in an average.

## 7. Calculate value and choose the simplest adequate solution

**Decision:** does the quality/time benefit cover inference, infrastructure, human review and maintenance?

- [ ] Run a controlled manual-versus-assisted reviewer study after familiarisation. Use matched difficulty, counterbalanced order and fresh equivalent cases to reduce learning effects; record reviewer identity/experience, corrections, unresolved follow-up and active time. Owner self-review is useful pilot evidence, not independent user validation.
- [ ] Calculate the three primary measures below for each eligible finalist, with raw denominators, case slices and unknowns. Publish both task-quality and business-value limitations.
- [ ] Estimate monthly costs/value at the owner-demo workload and plausible later volumes separately. Include fixed/idle infrastructure, inference/retries/failures, human review/follow-up, maintenance and amortised implementation effort. Keep assumed wages, FX, tax and volume explicit.
- [ ] Record the selected option, rejected alternatives, remaining uncertainty and a reassessment trigger. If extra complexity does not pay for itself, retain the simpler option. If business value is unproven or negative at demo volume, describe learning/portfolio value separately from customer ROI.

### Primary measures and diagnostic checks

One trial is one scheduled case/variant/repetition ending in a proposed allocation, targeted question or justified unresolved outcome. This is not necessarily a paid invoice or a financially closed case.

| Primary measure | Definition and source | Decision and limitation |
|---|---|---|
| Correct, supported outcome rate | Trials passing independent exact checks **and actual human semantic review**, divided by all scheduled trials; report split/family and repeat counts from sealed evaluation/review artifacts. Failures, skipped trials and missing reviews are not successes. | Sets the quality floor. Appropriate questions can pass, but resolvable cases left unresolved fail the task rubric. Also report proposal precision and resolvable-case coverage to expose excessive abstention. Repeats of one family are not independent new cases. |
| Reviewer minutes per task | Total active review, correction and required clarification/follow-up minutes divided by all assigned tasks, alongside correctly reviewed completions and incomplete counts; use timed reviewer records. Report paired differences and spread. | Tests saved work. Include failed/abandoned tasks; a fast wrong answer is not a benefit. Report waiting/elapsed time separately, and do not impute missing follow-up or time. |
| Cost per correct, reviewed outcome | All observed variable run/retry/failure costs plus allocated hosting/operations and measured review labour, divided by correctly supported, reviewed outcomes. State allocation period, volume and price basis. If no successes or material cost is unknown, report undefined/unknown with known components. | Compares usable output cost. Show marginal and fully loaded costs separately: low demo volume makes fixed hosting dominate. Exact-only passes cannot supply this denominator. |

Hard guardrails are **financial/access integrity** and **the frozen operating envelope** (latency, resource and cost bounds). Diagnostic slices include unsupported-proposal rate, appropriate-clarification rate, citation support, errors, model calls/tokens and warm/cold latency. Use these to explain the three outcomes rather than manufacture one weighted score that lets low cost offset a safety failure.

Targets are not measured results. Anchors include the exact financial/access contracts, bounded execution limits and the owner's aggregate **under EUR 10/month idle / about EUR 40/month active** planning budget. The owner confirmed scope-and-criteria-v1 (previous repository: `scope-baseline-acceptance.md`) on 16 October: at least 90% supported correct outcomes on the new finite comparison set, zero unsafe/unsupported proposals, at least 20% less reviewer effort, 30-second warm results for at least 95% of declared pilot trials and a 120-second cold activation bound. Freeze the case mix/schedule and experiment resource limits separately. A no-provider timing pilot can inform an explicitly versioned amendment; seven cases cannot establish general accuracy.

For a fixed monthly task volume `N`, define `t` as average active human minutes per assigned task (including corrections/follow-up), `h` as EUR/hour, `v` as variable non-labour EUR/task and `F` as fixed monthly hosting/operations EUR:

```text
Monthly capacity value = N × (t_baseline − t_candidate) / 60 × h
Monthly incremental operating cost = (F_candidate − F_baseline) + N × (v_candidate − v_baseline)
Monthly net value = monthly capacity value − monthly incremental operating cost − added maintenance EUR/month
```

For build payback, divide incremental build cost by positive monthly net value; if the latter is zero/negative, no payback is established. Show low/base/high assumptions and the volume where value changes sign. Saved staff capacity is not automatically cash saved. Avoided financial-error loss needs observed error frequency/severity and stays a separate sensitivity estimate until supported. Do not double-count review labour in both `v` and `t`. The cost-per-correct-outcome KPI includes labour; `v` in this value formula excludes it.

**Exit evidence:** complete scorecard and decision record with estimates separated from observed timings, spend and outcomes. The AWS study (previous repository: `design/aws-deployment.md`) supplies a reproducible hosting estimate, not a bill or a measured ROI.

## 8. Prove deployment, operation and improvement

**Decision:** can the selected release run safely in its real environment, and which claims does that evidence support?

- [x] Retain the AWS regional cost/compatibility study and local component probes. These support a proposed design, not a deployed system.
- [ ] Implement/review the missing cloud adapters and per-stage deployment definitions; keep the shared domain/application/LangGraph implementation and migration history.
- [ ] Under explicit access/spend authorisation, verify development and staging, promote the same tested image to protected production, and retain identity/isolation, real synthetic journey, release/rollback, alert, restore, cold-start and bill/usage evidence. Follow the AWS deployment gates (previous repository: `design/aws-deployment.md`) and release plan (previous repository: `release-readiness.md`).
- [ ] Re-evaluate when model/prompt/data/policy changes or observed failures justify it. Record one evidence-led improvement and regressions, or a reasoned decision to make no change. Ordinary CI remains provider-free; live experiments are separately bounded.
- [ ] If later claiming customer benefit/adoption, obtain actual consenting user/problem validation and observed use with before/after outcomes. A real owner-operated cloud demo supports deployment/operation experience; it does not supply customer impact or commercial production history.
- [ ] Complete semantic/public-inventory review and owner acceptance before publishing the separate recorded employer experience. Explain the measured choice, rejected options and limitations; visitors trigger no backend/model calls.

**Exit evidence:** dated release/operations record plus an honest claim register. Keep “designed”, “implemented locally”, “deployed”, “used by the owner” and “benefited external users” separate.

## Comparison discipline

1. Freeze the question, variants, primary measure, quality floor, minimum useful improvement, safety gates, case mix and resource limits **before** seeing final outcomes. An incomplete threshold or budget means the experiment is not ready.
2. Change one factor at a time: workflow policy with model held fixed; model with workflow held fixed. If both change, attribute findings to the whole configuration. Start with normalised records to isolate intent interpretation, then include reviewed document intake in a separate end-to-end comparison.
3. Use the same authorised evidence and financial validators in every automated arm. Pair results by case, counterbalance execution/reviewer order and record concurrency/cache conditions. Split development tuning from final comparison; do not repeatedly tune against the final set.
4. Use several repetitions for stochastic candidates where affordable; predeclare counts and report every repetition, not best-of output. Report case-level gains/regressions, counts and uncertainty. Cluster any uncertainty analysis by case/family; repeated prompts do not multiply independent evidence. Small samples support scoped engineering decisions, not population guarantees.
5. Have a real reviewer grade semantic support with the rubric and sealed response hashes; blind the variant when practical. Record reviewer disagreements and resolution. Any future model judge must first be calibrated against human judgements and reported separately.
6. Stop on critical access/financial failures, exhausted bounds, uncertain dispatch or missing provenance. Do not silently re-call a model to repair the report. Record skipped work and the stop reason; expand the experiment only with a new plan and authorisation.
7. Select the cheapest eligible option meeting the predeclared requirements. When differences are too small/uncertain to justify change, retain the simpler adequate candidate and state the uncertainty. Keep rejected experiments and re-evaluation triggers.

The existing evaluator supports the historical rules/gateway comparison and explicit semantic-review records. It does **not** yet implement every proposed workflow/model variant, reviewer timing study or value calculation. Add and test only the infrastructure needed for the next comparison; this document is not an executed benchmark.

## Immediate work and existing evidence

The owner has confirmed stage 1's scope/acceptance targets (previous repository: `scope-baseline-acceptance.md`), completed saved-response review and the SEC-01 repair. The comparison protocol (previous repository: `comparison-plan-v1.md`), 30 development source cases, twenty empty final reservations, security matrix and balanced timing templates are prepared. C2 and version-2 evaluator/scorer support (previous repository: `comparison-implementation.md`) were implemented locally on 18 October with authored-response checks and no live inference. Next review independent source-derived development labels and freeze the labelled manifest, actual configurations and schedule; service-model eligibility remains open. Select on development data before authoring/sealing final confirmation. Live execution follows only after exact resource bounds are separately authorised. Cloud adapter work can proceed alongside preparation; its exposure gates remain independent.

| Evidence available on 16 October | What it supports | What it cannot establish |
|---|---|---|
| Local software verification (previous repository: `implementation-backlog.md`) | Tested exact-money, permission, job/recovery and frontend boundaries within the dated scope | General model accuracy, cloud security or business value |
| 6 October exact checks, reviewed 17 October (previous repository: `evaluation-results/2026-10-17-reviewed-summary.md`) | AI-assisted exact/human checks 7/7; rules exact 4/7, human usefulness 3/7; all eight claims supported; no observed financial effects | Independent expert validation, model/framework superiority, business savings or general accuracy |
| Local telemetry evidence (previous repository: `../observability/README.md`) | Instrumentation, inspected correlation/redaction and defined local alert exercises | Deployed alert delivery, production latency or reliability |
| AWS regional study (previous repository: `design/aws-deployment.md`) | Explicit cost scenarios and local runtime/database compatibility probes | Actual AWS behaviour, monthly bill or cost cap |
| Recorded preview (previous repository: `recorded-demo.md`) | Inspectable shared UI and authentic captured outcomes | Live visitor execution, owner acceptance or reviewed publication |

## AWS learning alignment and sources

The checklist follows the lifecycle themes the owner named. AWS's [Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html) covers scoping through continuous improvement and quality, security, performance and cost. This plan turns those themes into project-specific evidence gates; it does not claim a one-to-one verified mapping to every lesson in the private course.

- Stages 1–2 and repeated comparison: [periodic functional evaluation](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops01-bp01.html), including diverse cases, task metrics and ground truth.
- Stages 4–5 and 7: [right-size model selection](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost01-bp01.html), selecting sufficient capability against workload requirements and cost.
- Stage 3: [secure prompt inputs](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec04-bp02.html), applied here alongside independent permission, transaction and review controls.
- Stages 6 and 8: [monitor operational health](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops02.html), with our actual cloud verification still pending.

External guidance was checked on 16 October 2026. Repository reports control implementation/result claims. These recommendations require no new framework, model judge, vector database, model training or additional agent unless the evidence justifies it.
