# Belarusian XTTS research lineage

BE_TTS is not a one-off XTTS fine-tune. The public Hugging Face history shows a sustained training program around Coqui XTTS v2, with **40+ XTTS-labelled model/checkpoint repositories** spanning late 2024 through later stress-aware and larger-data experiments.

These are experiment/checkpoint repositories, not 40 independent architectures.

## What was explored

The public lineage includes multiple experiment families:

- dataset-composition variants such as `Model_big`, `Model_all`, `2datasets`, `modelCorpus`, `Knihi`, second/third-dataset series, small-data and big-data branches;
- long checkpoint sequences labelled 30/35/40/46/47/48/53/55/60/70/75/80/82/85/90 epochs;
- an explicit `48EP_denoized` branch;
- later `V3` / new-DVAE / small-vs-big-data experiments;
- stress-aware `Naciski` branches;
- public inference demos, including standard, streaming, and stress-aware synthesis.

Representative inventory:
https://huggingface.co/archivartaunik/models

## Representative XTTS checkpoints

### Belarusian_TTS_V2_Final

https://huggingface.co/archivartaunik/Belarusian_TTS_V2_Final

Public artifact contents include the XTTS model, DVAE and mel statistics, tokenizer/config, training script, TensorBoard data, and a reference voice sample.

A public discussion on this model in January 2025 identified stress placement as a quality gap and connected further improvement to collecting a more diverse dataset. Later `Naciski` checkpoints make stress-aware synthesis a visible follow-up line.

### Stress-aware XTTS

- https://huggingface.co/archivartaunik/BE_XTTS_V2_10_Naciski
- https://huggingface.co/archivartaunik/BE_XTTS_V2_20_Naciski

The public `10_Naciski` artifact includes a best-model checkpoint, base XTTS files, tokenizer, training code and TensorBoard log. This line connects acoustic TTS work directly to the homograph/stress subsystem documented in [HOMOGRAPHS.md](HOMOGRAPHS.md).

### Larger-data / later XTTS branch

- https://huggingface.co/archivartaunik/BE_XTTS_V3_12kBigDataset
- https://huggingface.co/archivartaunik/BE_XTTS_V3_18kBigDat

The published `BE_XTTS_V3_18kBigDat` config records a concrete run with:

- 8 epochs;
- batch size 8, eval batch size 16;
- AdamW at learning rate `9e-6`;
- MultiStepLR;
- 22.05 kHz input/DVAE audio and 24 kHz output;
- evaluation enabled with a 1% split capped at 256 examples;
- Belarusian (`be`) explicitly present in the model language list.

The training script uses XTTS transfer learning and accepts multiple dataset metadata inputs, making corpus composition part of the reproducible training interface.

## Why the history matters

The checkpoint sequence documents iterative work on several independent axes:

1. **Corpus composition** — book-oriented, corpus-oriented, two-/three-dataset, small/big-data variants.
2. **Training duration / checkpoint selection** — many staged epoch-labelled checkpoints.
3. **Audio quality** — including an explicit denoised-data branch.
4. **Pronunciation and stress** — dedicated `Naciski` experiments.
5. **Model-side changes** — later V3/new-DVAE branches.

Checkpoint names are historical experiment labels, not a guarantee that every run is directly comparable. A major BE_TTS goal is to normalize this history into reproducible experiment manifests.

## Public demos

- Bextts — https://huggingface.co/spaces/archivartaunik/Bextts
- BexttsStream — https://huggingface.co/spaces/archivartaunik/BexttsStream
- BeTTSNaciski — https://huggingface.co/spaces/archivartaunik/BeTTSNaciski

## Reproducibility work planned in BE_TTS

For the most important checkpoints, we want to publish a canonical experiment record containing:

- exact base checkpoint and model revision;
- immutable dataset revisions;
- tokenizer/DVAE lineage;
- training configuration and hardware when known;
- comparable evaluation set and metrics;
- stress/homograph regression results;
- status: historical experiment, candidate, or recommended release.

Large checkpoints remain on Hugging Face/Kaggle; GitHub holds the code, manifests, evals, tests, and release-quality workflows.
