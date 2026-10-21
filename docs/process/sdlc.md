# Development lifecycle

Use short vertical slices and feedback at each stage. The repository maintains evidence rather than treating a written plan as completed delivery.

| Stage | Work and inspectable output | Exit evidence |
|---|---|---|
| Define | Grill Me discovery, product definition, user journey, assumptions and boundaries | Owner-confirmed scope and useful outcome; open dependencies named |
| Specify | Traceable requirements, representative data and independent expected answers | Reviewed acceptance criteria and a frozen evaluation rubric |
| Design | Reuse comparison, HLD/LLD, threat model, interfaces and ADRs | Supported trade-offs and a small implementation slice |
| Develop | Deterministic baseline, then bounded AI where useful | Passing behaviour/security/recovery tests and reproducible builds |
| Inspect and evaluate | Demonstrate a case, review outputs and execution evidence, compare options | Actual human judgements, full denominators, costs and limits |
| Iterate | Classify failures and update only justified requirements/design/code | Regression evidence and a recorded decision |
| Integrate | Pull request checks, dependency/skill/source verification, build artifact | Actual CI result for the commit and retained artifact identity |
| Deploy | Authorised development → staging → production promotion | Environment-specific identity/storage checks, smoke tests and rollback evidence |
| Operate | Observe latency/failures/queues/cost, exercise recovery and review rule changes | Actual dashboards, useful alerts, drill/incident records and versioned maintenance |

For a slice, maintain requirement → decision/design → implementation → test/evaluation → reviewer judgement → release/operation links. A model report cannot approve its own result. Keep application audit records distinct from telemetry.

The initial CI validates the repository foundation and its control tests. Additional checks arrive with the actual application. No deployment workflow is supplied as an empty success: cloud adapters, identity and IaC must be designed and implemented before deployment can execute.

Use docs/process/status.json for stage state and docs/process/verification.md for actual verification. Do not add dates, users, production usage or measurements that have not happened.
