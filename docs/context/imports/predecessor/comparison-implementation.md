# Local workflow comparison implementation

**Implemented 18 October 2026.** C2 and version-2 evaluation/scoring now support a local comparison of B1 rules, C1 rules-gated investigation and C2 one-call investigation. Local software verification uses explicitly authored responses; no new model inference or cloud deployment is included. The 17 October protocol (previous repository: `comparison-plan-v1.md`) and its preparation receipt remain dated preparation records.

## One application with two investigation policies

The shared workflow (previous repository: `../backend/reconciliation/investigation/workflow.py`) keeps the same five LangGraph nodes, prompt, model context, output schema, source validation, security assessment and transactional pending-result publication. C1 retains the existing `bounded-investigation-v1` policy and default manifest shape. C2 records `workflow_variant: c2-one-call` and `policy_version: bounded-one-call-v1`.

C2 runs the existing rules checks but discards a successful matching shortcut on supported cases. It therefore calls the supplied adapter once on an exact-reference case where C1 needs no call. Mandatory missing-customer, already-allocated and no-candidate guards remain effective. The database can reject missing identity before graph execution. C2 requires an adapter, a one-call manifest and a non-rules provider; it cannot silently become a rules fallback.

Both policies commit the source-bound security assessment before inference. Calls occur outside database transactions; validators check structured output, exact cents, IDs and quotes. Publication rechecks the active run/source snapshot. A concurrent duplicate cannot obtain a second reservation or cancel the first call; a committed response is reused after recovery. Run identity binds the full manifest, so C1 and C2 cannot share an idempotency key with different policies. Neither policy approves allocations or changes financial authority. No SQL migration was changed or added in this slice.

## Executable format and isolation

The contracts (previous repository: `../backend/reconciliation/evaluation/contracts.py`) retain strict schema-version-1 plans, observations and labels for historical runs. Schema version 2 adds:

- Separate trial `variant` and `provider` fields. B1 uses `rules`; C1/C2 share either `authored-test-double` or `codex-gateway` in a complete comparison block. Provider grouping cannot substitute for workflow grouping.
- Balanced case/repetition/variant blocks, unique schedule keys, contiguous equal repetitions and deterministic family interleaving/variant rotation. Exact schedules are retained before dispatch.
- `comparison-authored` plans with zero live calls and zero live monetary reservations. The built-in authored adapter (previous repository: `../backend/reconciliation/evaluation/doubles.py`) handles machine-form confirmation or asks a canned question. It reads no labels, files, credentials or network and makes no model inference. Its stored generations are labelled `authored_test_double`, with usage billing `authored_no_inference`, even when the output looks plausible. Shared attempt records exercise the real reservation/recovery code; they do not represent a paid provider request.
- Worker observations with separate worker and coordinator/dispatch timings. These include local subprocess conditions and do not verify API queue latency, warm-cloud performance or cold activation.
- Scorer-only v2 labels with explicit `resolvable` and `requires_safe_action` booleans. Resolvability must agree with allowed proposal alternatives. These annotations never enter application/model context.

The coordinator (previous repository: `../backend/reconciliation/evaluation/runner.py`) reuses the existing source allowlist, hashes, per-trial isolated workspaces, durable pre-dispatch reservations and real financial-effect checks. The worker (previous repository: `../backend/reconciliation/evaluation/worker.py`) receives only its restricted PostgreSQL role. Authored comparison children receive no HOME/CODEX_HOME login locations or provider credentials and never construct a gateway. The audit guard denies label reads and imports of both scorer modules; it is not an OS sandbox. Isolation remaps opaque runtime IDs across workspaces while preserving source facts. Exact request equality across policies is also tested on one unchanged snapshot.

Live comparison wiring is available for a future explicitly authorised gateway experiment, but it is disabled by default. It requires the live opt-in, resource bounds and a dataset declaring v2 label annotations. The scorer also checks the actual label version. A missing opt-in or annotation declaration fails before creating the run directory or dispatching work. Explicit source/model/prompt/schema/lock identities are checked; configuration or policy drift cannot be silently relabelled as C2. Unknown live dispatch stops subsequent trials, and financial-effect violations stop the comparison; remaining scheduled trials are retained as skipped. This implementation is not permission to run it live.

## Independent scoring and reports

The shared scorer (previous repository: `../backend/reconciliation/evaluation/scorer.py`) retains v1 exact/citation/review logic. The v2 accounting module (previous repository: `../backend/reconciliation/evaluation/comparison_scoring.py`) adds variant-level, provider-level, family and case summaries; direct C2-versus-C1 comparisons; paired changes versus B1; and per-case repetition/action variability. Original labels, observations, reports and completed human-review records are unchanged.

Reports include:

- Exact success and human-supported success over **all scheduled trials**, including failures, unknowns and skips. Pending human judgements remain pending and contribute no success.
- Supported correctness on resolvable cases, proposal precision and resolvable proposal/supported coverage. An implementation that asks on everything cannot win through empty proposal precision.
- Known incorrect/unsupported proposals, pending proposal reviews, safe-action support, financial violations and unknown financial safety. Numerical 90% quality arithmetic cannot offset a safety failure.
- Authored generations separately from observed real-provider attempts and conservative call reservations. Known cost and unavailable cost remain distinct; a reservation is not a bill and observed attempts are not guaranteed upstream request/retry counts.
- Local worker/dispatch measurements with their scope stated. No production p95, reviewer saving, cloud operation, model/framework superiority or cheapest-model decision is inferred.

Version-1 labels can support an authored software smoke run with resolvability explicitly marked `legacy-alternatives-derived`. Real comparison evidence requires the new source-derived annotations and actual trial/hash-bound human reviews. No new development labels or final-test sources were authored by this implementation.

An authored report always has release status `authored-test-double-no-model-quality-evidence`; it cannot become a model-quality or release pass. A future live three-variant run is labelled a development comparison, not final confirmation. Finalist-only schedules, other service-model adapters, independent annotations, frozen final inputs and controlled human timing remain separate prerequisites for the full protocol.

## Local authored comparison commands

Use a healthy local PostgreSQL instance with migrations and separate API/worker roles from local setup (previous repository: `local-development.md`). The existing default database reported disk exhaustion during this change; verification used a separate bounded temporary PostgreSQL instance in memory. Existing data was not pruned. Resolve that storage issue before using the normal persistent setup.

Choose fresh artifact paths for every run. Plans/results are immutable and refuse overwrite. From the repository root, with configured local `.env`:

```sh
uv run --locked recon-eval plan \
  --dataset evals --mode comparison-authored --max-seconds 180 \
  --output .runtime/evals/c2-authored-plan.json

uv run --locked --env-file .env recon-eval run \
  --dataset evals --plan .runtime/evals/c2-authored-plan.json \
  --output .runtime/evals/c2-authored-run

uv run --locked recon-eval score \
  --dataset evals --run .runtime/evals/c2-authored-run \
  --output .runtime/evals/c2-authored-scores.json

uv run --locked recon-eval report \
  --scores .runtime/evals/c2-authored-scores.json
```

This uses the old seven-case regression inputs, schedules 21 software trials and consumes zero provider calls. The current thirty-case source-only pack has no reviewed labels/labelled dataset manifest and cannot yet replace `--dataset evals`. The broad `protocol.json` is still a planning artifact, not an executable v2 plan. Do not add `--allow-live` to this authored command.

## Verification and remaining evidence

Tests cover exact-reference C1 bypass/C2 call counts, identical model requests on an unchanged snapshot, duplicate/replayed calls, manifest conflicts, late clarification, invalid amounts/foreign IDs/quotes, provider uncertainty, mandatory scope guards, restricted identities, isolated authored execution and independent scoring. Accounting tests cover pending/rejected reviews, empty proposal precision, resolvable coverage, failed/skipped denominators, policy/transport provenance, strict annotations and finite telemetry labels. Historical interrupted-artifact handling remains regression tested. See the dated backlog verification (previous repository: `implementation-backlog.md`) for final counts and environment details.

Inspect the real PostgreSQL C2/comparison tests (previous repository: `../tests/integration/test_one_call_comparison.py`), strict schedule/annotation tests (previous repository: `../tests/unit/test_comparison_contracts.py`) and independent accounting mutations (previous repository: `../tests/unit/test_comparison_scoring.py`). Authored review booleans in unit fixtures are test data, not new owner judgements on model outputs.

Variant labels are a fixed three-value allowlist in spans/logs/metric attributes. Local/GCP collector privacy policies retain that bounded label while continuing to strip evidence, raw exception text and span-event payloads. GCP delivery remains unverified. Mermaid artifacts describe the same graph; regenerating them invokes no workflow node or model.

Next review independent development labels, extend the labelled manifest/scorer annotations and freeze an actual development schedule. Service-provider/model eligibility and pricing, final confirmation sources, human timing, static-demo review and cloud deployment remain open. The new local software checks do not close those evidence gates.
