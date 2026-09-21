# Belarusian speech datasets

Dataset construction is a major part of the BE_TTS work, not merely an input to model training. Public resources cover raw audiobook inputs, segmented/aligned speech, checked TTS datasets, and corpus releases.

## Data pipeline

```text
source recordings / audiobooks
        ↓
segmentation + transcription
        ↓
ASR / text alignment
        ↓
speaker + audio-quality checks
        ↓
dataset QA
        ↓
checked/release dataset
        ↓
TTS training + evaluation
```

Large artifacts stay on Hugging Face/Kaggle. BE_TTS is the place for provenance, manifests, reusable processing code, tests and evaluation.

## Ministerskija aligned audiobooks

https://huggingface.co/collections/fosters/ministerskija

Published collection metadata reports:

- **35 books**
- **60,022 audio/text pairs**
- **260 hours of audio**
- ASR + Gemini alignment
- alignment confidence threshold **>= 0.95**

Raw input is kept as a separate collection:
https://huggingface.co/collections/fosters/ministerskija-input

Keeping raw and processed artifacts separate is important for reproducibility.

## Belarusian audio corpus

https://huggingface.co/datasets/fosters/be-bel-audio-corpus

Public dataset-card snapshot:

- **49,606 rows**
- **21.8 GB**
- approximately **87 h 38 m 32 s** across the three published constituent sets
- Apache-2.0

## Native audiobook speech

https://huggingface.co/collections/fosters/belarusian-audiobooks-native

The collection describes:

- native sample rate;
- mono audio;
- chunks up to 30 seconds;
- audio, text, duration and aligned transcription fields.

The account contains many book-specific repositories. Repository count therefore must not be presented as the number of independent corpus families.

## Curated checked TTS datasets

https://huggingface.co/collections/archivartaunik/belarusian-tts-datasets

The collection is explicitly curated for Belarusian TTS and includes checked resources such as:

- `Jevanhielle_Zyhamont_outChecked`
- `Jevanhielle_Zyhamont0_10_Checked`
- `output5Checked`
- `output4Checked`
- `Melez_Tryvozhnae_Schasce_testpartChecked`
- `output3Checked`
- `by-bel-korpus-audio-set-1Checked`
- `dataset-knihiChecked`

Example:
https://huggingface.co/datasets/archivartaunik/output4Checked

Its public card identifies a Belarusian audio+text TTS dataset in Parquet format, currently 360 rows, with MIT declared on that artifact.

Licenses differ across datasets. `Checked` describes a project stage, not a universal legal or quality status.

## Dataset tooling

The broader public ecosystem also contains tools/Spaces for:

- raw-audio → structured HF dataset conversion;
- audio chunk classification for music/defects;
- speaker identification;
- TTS dataset validation;
- SRT/audio → dataset cutting.

That matters for OSS maintenance: dataset quality is treated as an engineering pipeline rather than a collection of opaque files.

## Relationship to XTTS

The XTTS training history contains explicit dataset-composition branches: `2datasets`, `3Dataset`, `Knihi`, `modelCorpus`, denoised data, small/big-data variants and later stress-aware work.

See [XTTSV2.md](XTTSV2.md).

## Provenance policy

For every dataset promoted through BE_TTS, the manifest should eventually record:

- canonical source and creator;
- license / permission and redistribution status;
- speaker or recording rights where applicable;
- transformations and alignment method;
- model-generated vs human-reviewed text/labels;
- quality thresholds and known limitations;
- immutable Hugging Face/Kaggle revision;
- which model checkpoints used the dataset.

## Next steps

1. Add dataset-stage labels: `raw`, `aligned`, `checked`, `release`.
2. Validate provenance metadata in CI.
3. Publish small redistributable fixtures for tests.
4. Add duplicate, speaker, duration and audio-quality statistics.
5. Link every recommended model checkpoint to exact dataset revisions.
