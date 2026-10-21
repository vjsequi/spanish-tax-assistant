# Third party notices

The original project code is MIT licensed. Retain upstream notices for imported software and check individual model/data licences before adoption.

The pinned `.agents/skills/grill-me` and `.agents/skills/grilling` files come from Matt Pocock's MIT-licensed `mattpocock/skills` repository. The [upstream licence](third_party/licenses/matt-pocock-skills.txt), [review receipt](docs/security/skill-review.md) and [hash manifest](docs/security/skill-manifest.json) are included.

Recovered owner-authored use-case notes and predecessor project context are retained with provenance in docs/context/source-manifest.json. External sources linked by those notes are references; their code, datasets or models have not been incorporated. No hacienda-cli, Docling, OpenFisca or Harbor application dependency is installed.

## Official reference material

Unmodified AEAT/BOE documents in `data/rules/2025/originals` are attributed to their publishers in the [catalog and byte manifest](data/rules/2025/README.md), with URLs, retrieval dates, available update dates and exact selected editions. Retained AEAT reuse/legal notices and BOE reuse notice govern those materials; they are not covered by the project's MIT software licence. Preserve attribution and reuse metadata, avoid distortion and do not imply publisher endorsement. The project-authored field/rule transcriptions are clearly marked drafts pending independent tax review.

## Development document tools

ReportLab 4.4.9 (BSD), pypdf 6.10.0 (BSD-3-Clause) and Pillow 12.3.0 (MIT-CMU) generate and inspect synthetic documents. The pypdf crypto extra supports reading the public AEAT manuals' AES encryption: cryptography 50.0.2 (Apache-2.0 OR BSD-3-Clause), cffi 2.1.1 (MIT-0) and pycparser 3.11 (BSD-3-Clause). ReportLab also uses charset-normalizer 3.5.2 (MIT). Versions and wheel hashes are locked; distributed package notices, including bundled-component notices where supplied, are retained in the [licence manifest](third_party/development-licences.json). This is an upstream metadata/licence review, not a vulnerability or production dependency audit.

Local Poppler `pdftoppm`/`pdftotext`/`pdfinfo` executables render/inspect PDFs during authoring and visual QA. They are external development tools, not vendored or linked into the application or review bundle. CI verifies the retained fixtures without running Poppler. No new application runtime dependency or model/provider is installed by these development tools.
