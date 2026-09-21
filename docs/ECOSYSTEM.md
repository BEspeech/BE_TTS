# Belarusian Speech/NLP Ecosystem

This document is a date-stamped inventory of public work connected to the BE_TTS effort. It exists so that the GitHub repository can act as an engineering hub while large datasets, model checkpoints, and demos remain on platforms designed for those artifacts.

**Snapshot date:** 2026-09-21

Metrics are snapshots and may change. Hugging Face profile counts below count public artifact repositories, not unique underlying corpora. Similar intermediate, source, processed, and checked variants may all appear separately.

## Aggregate public Hugging Face footprint

Across the two public Hugging Face profiles included in this project inventory:

- **690 dataset repositories** (251 + 439)
- **62 model repositories** (3 + 59)
- **33 Spaces** (5 + 28)
- **6 collections** (4 + 2)

These totals are useful as evidence of sustained public work, but they should not be interpreted as 690 independent datasets or 62 production-ready models.

## fosters

Profile: https://huggingface.co/fosters

Public profile snapshot:

- 251 dataset repositories
- 3 model repositories
- 5 Spaces
- 4 collections

### Contextual homograph disambiguation

Model: https://huggingface.co/fosters/homograph-bel-xlm-roberta-base

The model resolves the stress variant of an exact Belarusian homograph occurrence from sentence context and is designed to run before phonemization in a Belarusian TTS pipeline.

Published model-card details include:

- XLM-R base backbone
- 102,029 training contexts
- 1,941 homographs represented in the training split
- 2,896 observed stress variants
- preliminary gold-validation macro-F1: 0.901211
- gold validation size: 275 contexts / 28 homographs

The model card explicitly warns that the gold validation set is narrow and that the score must not be treated as a broad estimate across all trained homographs.

Most training labels are silver/model-generated rather than human-reviewed. The linked training dataset/model currently uses a provisional `license: other` while provenance and licensing are being reviewed. This should remain visible rather than being hidden in downstream documentation.

### Belarusian audio corpus

Dataset: https://huggingface.co/datasets/fosters/be-bel-audio-corpus

Public dataset-card snapshot:

- 49,606 rows
- 21.8 GB
- Apache-2.0
- 60 downloads in the preceding month at snapshot time
- three constituent sets with durations:
  - 13:42:04
  - 37:05:34
  - 36:50:54

Combined duration: approximately **87 h 38 m 32 s**.

### Ministerskija aligned audiobooks

Collection: https://huggingface.co/collections/fosters/ministerskija

Collection description:

- 35 books
- 60,022 audio/text pairs
- 260 hours of audio
- ASR + Gemini alignment
- confidence threshold >= 0.95

Raw-input collection:
https://huggingface.co/collections/fosters/ministerskija-input

### Belarusian Audiobooks (native)

Collection: https://huggingface.co/collections/fosters/belarusian-audiobooks-native

The collection describes native-sample-rate mono Belarusian audiobook speech split into chunks up to 30 seconds with audio, text, duration, and aligned transcriptions.

### Public tooling / demos

The profile currently lists five Spaces, including:

- Belhophonemizer — Belarusian text to IPA phonemes
- Chunk Classifier
- Speaker Identifier
- Dataset Converter
- Audio Classification

These are relevant to an end-to-end data/TTS maintenance story because they cover preprocessing, QA, speaker analysis, and phonemization rather than only model checkpoints.

## archivartaunik

Profile: https://huggingface.co/archivartaunik

Public profile snapshot:

- 439 dataset repositories
- 59 model repositories
- 28 Spaces
- 2 collections
- recent Space activity visible on the public profile at snapshot time

### Belarusian TTS datasets

Collection:
https://huggingface.co/collections/archivartaunik/belarusian-tts-datasets

The collection is explicitly described as curated Belarusian datasets for TTS and currently contains checked dataset variants.

### TTS models

Representative public checkpoints include:

- https://huggingface.co/archivartaunik/omnivoice-finetune-be-5500
- https://huggingface.co/archivartaunik/omnivoice-finetune-be-4000
- https://huggingface.co/archivartaunik/BE_XTTS_V3_18kBigDat
- https://huggingface.co/archivartaunik/BE_XTTS_V2_20_Naciski

The OmniVoice 5500 checkpoint is a 0.6B-parameter Belarusian TTS model. Its public card records training/evaluation details including eval loss 3.4399 at step 5500 and A100 80 GB training hardware. It uses `license: other`, so downstream reuse must follow the artifact's own terms.

### Public TTS demos

- BeTTSNaciski — https://huggingface.co/spaces/archivartaunik/BeTTSNaciski
- Bextts — https://huggingface.co/spaces/archivartaunik/Bextts

At snapshot time both were running public Spaces; the profile showed 7 likes for BeTTSNaciski and 18 likes for Bextts.

## Kaggle: wisekinder

Profile: https://www.kaggle.com/wisekinder

Kaggle's profile-level aggregate metadata is not reliably exposed to the public crawler used for this snapshot, so this document does **not** invent a total dataset/notebook/download count.

Two directly indexed public artifacts are:

### XTTSv2-BY

https://www.kaggle.com/datasets/wisekinder/xttsv2-by

Snapshot:

- Apache 2.0
- 17.86 GB
- 7,132 files
- 540 views
- 21 downloads
- 23 views / 4 downloads in the preceding 30 days

The artifact includes XTTS training code/checkpoints and related files.

### [STT] XTTSv2 tune on audio data set

https://www.kaggle.com/models/wisekinder/stt-xttsv2-tune-on-audio-data-set

Snapshot:

- created 2024-11-09
- Apache 2.0
- 19.04 GB
- 245 views
- 80 downloads

The public model card is sparse, so it should be presented as evidence of earlier public experimentation rather than as a flagship documented release.

## Kaggle: siarheys

Profile: https://www.kaggle.com/siarheys

The public profile is part of the project inventory, but the profile page and profile-level activity were not reliably retrievable through the crawler on the snapshot date. No aggregate metric is claimed here until it can be verified from a stable public artifact page or Kaggle API export.

## Quality and provenance priorities

The public footprint is substantial, but the strongest OSS story is not raw artifact count. The GitHub hub should improve the parts reviewers and downstream users need for reproducibility:

1. canonical resource manifest;
2. explicit license/provenance per artifact;
3. distinction between source, intermediate, checked, and release-ready datasets;
4. distinction between gold and model-generated annotations;
5. versioned evaluation sets;
6. reproducible baseline code;
7. CI for data metadata, links, tests, and release checks.

This is also the main reason BE_TTS exists as a GitHub engineering hub rather than attempting to copy every large artifact into Git.
