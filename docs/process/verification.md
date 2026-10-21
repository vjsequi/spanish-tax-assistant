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
