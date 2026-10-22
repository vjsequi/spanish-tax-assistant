# Tests

Run `PYTHONPATH=src uv run --locked python -m unittest discover -s tests -v`. The suite includes foundation/source-pack controls and provisional C001 arithmetic, field components, input/coverage gates, local persistence/idempotency/stale-writer checks, source drift, PDF export and actual loopback HTTP boundary tests.

The C001 numeric assertions are source-derived software-author expectations pending professional QA, distinct from isolated independent labels. These tests do not establish real-world tax accuracy, AI extraction performance, full profile coverage, hosted security or production readiness. The HTTP test binds a local ephemeral port; restricted execution environments may require local-socket permission.
