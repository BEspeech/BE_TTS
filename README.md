# BE_TTS

**Open infrastructure for Belarusian speech and language technology.**

BE_TTS is the public engineering hub for reusable tools, evaluation suites, dataset metadata, and model integration around Belarusian text-to-speech (TTS) and speech/NLP research.

The broader public project already spans Hugging Face and Kaggle. This repository is being developed as the stable place for source code, tests, evaluation protocols, contribution workflows, and release documentation.

## Focus areas

- **Homograph and stress disambiguation** for context-dependent Belarusian pronunciation.
- **Text normalization and phonemization** for TTS pipelines.
- **Belarusian TTS** models, inference integrations, and public demos.
- **Speech corpora** alignment, segmentation, metadata, and quality assurance.
- **Evaluation** for pronunciation, homographs, speech quality, and regression testing.
- **Reusable OSS tooling** for researchers and developers working with Belarusian.

## Why this matters

Belarusian remains comparatively under-resourced in modern speech and NLP tooling. Pronunciation ambiguity is especially important for TTS: the same written homograph may require different stress or pronunciation depending on context.

Our goal is to make the work reusable beyond a single model by publishing common interfaces, evaluation assets, dataset metadata, and reproducible tooling.

## Public ecosystem snapshot

Snapshot date: **2026-09-21**. Counts below refer to public artifact repositories shown on the corresponding profiles; they are not counts of unique underlying corpora.

| Public profile | Public footprint | Representative work |
| --- | ---: | --- |
| [fosters on Hugging Face](https://huggingface.co/fosters) | 251 dataset repos · 3 models · 5 Spaces · 4 collections | Belarusian homograph disambiguation, phonemization, XTTS, aligned speech/audiobook corpora |
| [archivartaunik on Hugging Face](https://huggingface.co/archivartaunik) | 439 dataset repos · 59 models · 28 Spaces · 2 collections | Belarusian TTS datasets, XTTS/OmniVoice checkpoints, TTS + stress demos |
| [wisekinder on Kaggle](https://www.kaggle.com/wisekinder) | Public profile; selected artifacts indexed below | Earlier XTTS/TTS experiments and datasets |
| [siarheys on Kaggle](https://www.kaggle.com/siarheys) | Public profile; aggregate metrics pending verification | Additional project research artifacts |

Representative public resources include:

- [Belarusian contextual homograph model](https://huggingface.co/fosters/homograph-bel-xlm-roberta-base)
- [Belarusian audio corpus](https://huggingface.co/datasets/fosters/be-bel-audio-corpus)
- [Belarusian Audiobooks (native) collection](https://huggingface.co/collections/fosters/belarusian-audiobooks-native)
- [Ministerskija aligned audiobook collection](https://huggingface.co/collections/fosters/ministerskija)
- [Belarusian TTS Datasets collection](https://huggingface.co/collections/archivartaunik/belarusian-tts-datasets)
- [BeTTSNaciski: Belarusian TTS + stress demo](https://huggingface.co/spaces/archivartaunik/BeTTSNaciski)
- [Bextts: Belarusian TTS demo](https://huggingface.co/spaces/archivartaunik/Bextts)
- [XTTSv2-BY on Kaggle](https://www.kaggle.com/datasets/wisekinder/xttsv2-by)

See [docs/ECOSYSTEM.md](docs/ECOSYSTEM.md) for a more detailed, date-stamped inventory and quality notes.

## Repository status

This repository is currently being bootstrapped as the project's public engineering and maintenance hub.

Planned source layout:

```text
BE_TTS/
├── src/                  # reusable library / pipeline code
├── evals/                # homograph, pronunciation and TTS evaluations
├── tests/                # regression and unit tests
├── examples/             # minimal reproducible examples
├── data/
│   └── manifests/        # metadata and provenance; not large binaries
└── docs/                 # ecosystem, methodology and release documentation
```

Large datasets and model weights will remain on appropriate public artifact platforms such as Hugging Face and Kaggle rather than being committed directly to Git.

## Roadmap

See [docs/ROADMAP.md](docs/ROADMAP.md). Immediate priorities are:

1. publish a machine-readable public resource manifest with license/provenance metadata;
2. move reusable homograph, pronunciation, and TTS evaluation code into this repository;
3. add reproducible examples and automated tests;
4. establish CI and release-quality checks;
5. document stable interfaces between text normalization, stress resolution, phonemization, and TTS.

## Data and model provenance

External datasets and models retain their own licenses and usage conditions. Some research artifacts are experimental or under active provenance/license review; do not assume the repository's MIT license applies to external data or model weights.

New data contributions must document source, license/permission, preprocessing, and any relevant speaker or recording rights. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Contributing

Contributions are welcome, especially around:

- Belarusian linguistic edge cases and homographs;
- pronunciation/stress test cases;
- phonemization and normalization;
- dataset QA and provenance tooling;
- reproducible TTS evaluation;
- documentation and examples.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

Source code and documentation committed to this repository are licensed under the [MIT License](LICENSE), unless a file explicitly states otherwise.

External datasets, model weights, recordings, and other linked artifacts may use different licenses.
