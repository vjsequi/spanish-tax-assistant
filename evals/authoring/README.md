# Synthetic source authoring

`cases.json` is the explicit source specification for twenty software-authored development cases. It contains invented document content and construction metadata, **not independent expected answers**. It is outside the application/model input boundary.

Regenerate draft inputs from the repository root:

```sh
uv run --locked python -m scripts.build_review_cases
uv run --locked python -m scripts.check_tax_pack
```

The builder uses pinned ReportLab/pypdf/Pillow development dependencies and system Poppler `pdftoppm` for controlled image/scan variants. It makes no network/model calls and uses no private reference. Generated sources are marked synthetic and bind into `evals/inputs/manifest.json`; the guide, request and blank review template are separate. Do not regenerate an independently reviewed source pack in place: new sources require a new dataset version/location and fresh hash-bound review.

Expected answers remain exclusively for the independent scorer/reviewer under `evals/expected`. This authoring file, source-extraction values, actual inference and independent tax review are distinct evidence categories.
