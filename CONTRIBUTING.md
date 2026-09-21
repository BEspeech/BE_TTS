# Contributing to BE_TTS

Thank you for helping improve open Belarusian speech and language tooling.

## Useful contribution areas

We especially welcome contributions to:

- homograph and stress disambiguation;
- pronunciation test cases;
- Belarusian text normalization and phonemization;
- TTS evaluation and regression tests;
- dataset validation and metadata tooling;
- reproducible examples and documentation;
- public resource indexing and provenance checks.

## Before opening a pull request

Keep changes focused and reproducible. For code changes, include tests or a minimal example where practical.

Do not commit large model weights, audio corpora, archives, or generated datasets directly to this repository. Store large public artifacts on an appropriate platform such as Hugging Face and link them through a manifest or documentation.

## Data provenance requirements

Any contribution that introduces or references data should document, where applicable:

- original source and canonical URL;
- creator/publisher;
- license or explicit permission;
- whether redistribution is permitted;
- recording/speaker rights where relevant;
- preprocessing or transformations;
- language/orthography assumptions;
- known quality limitations.

Do not contribute private, confidential, or personally identifying material without a clear lawful basis and explicit permission.

## Models and generated annotations

For model-generated or LLM-assisted labels, record:

- the generator/model when known;
- prompt or labeling methodology when publishable;
- confidence/filtering rules;
- human review status;
- evaluation limitations.

Generated labels should not be presented as gold annotations unless they have been independently verified.

## Pull request checklist

A PR should make it easy to answer:

1. What problem does this solve?
2. What public artifact or workflow does it affect?
3. How was it validated?
4. Are licensing/provenance requirements satisfied?
5. Does it change a public interface or evaluation result?

When evaluation metrics are reported, include the exact dataset/split and enough detail to reproduce them.

## Development direction

The initial repository structure is intentionally lightweight while reusable code and evaluation assets are consolidated from existing public research work.

See [docs/ROADMAP.md](docs/ROADMAP.md) for current priorities.
