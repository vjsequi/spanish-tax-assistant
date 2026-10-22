# Evaluation data boundary

**22 October process update:** professional tax review happens at final QA of the working product, under [ADR 0004](../docs/decisions/0004-development-before-tax-review.md). Implementation and source-derived engineering regressions proceed before then. Numeric assertions in application tests are explicitly provisional software-author expectations, not independently reviewed labels. The expected-answer isolation boundary remains unchanged.

Twenty wholly synthetic development cases are prepared under inputs/: 110 source files and 180 pages, including C018 with 30 files/100 pages. Inputs include digital PDFs, an image-only PDF, PNG/JPEG screenshots, partial supplied draft extracts and deliberate ambiguity/attack cases. See the [manifest](inputs/manifest.json), [review instructions](review/reviewer-guide.md) and [evaluation plan](../docs/evaluation/plan.md). No independent tax labels, inference outputs or quality results exist.

Put publishable synthetic development sources in inputs/. Hidden source-derived expectations belong in expected/ and are read only by a separate scorer/reviewer. Preserve split/source/configuration provenance and actual human judgements. Do not send expected/ to a model, runtime input loader, public bundle or trace. A later sealed final pack must be structurally separate from inspected development cases.

Authoring/ contains exposed construction inputs, not expected tax solutions. Review/ contains requests and a blank template, not completed judgements. The pack verifier enforces the narrow case-input schema and checks every retained file hash; it cannot establish semantic correctness, adequate coverage or real-world layout diversity. These fixtures must not be reported as independent held-out performance evidence.
