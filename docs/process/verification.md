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
