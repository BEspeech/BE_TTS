# Project status and public resources

This page summarizes published work across platforms and the tools currently available in this GitHub repository. Figures are snapshots from 2026-09-21; follow the linked artifact cards for current details.

## Project and public work

BE_TTS aims to make Belarusian speech technology reusable: speech datasets and quality control, TTS training and evaluation, and context-aware homograph stress resolution.

| Area | Public evidence | What it shows |
| --- | --- | --- |
| XTTS training | [XTTS lineage](XTTSV2.md), [published checkpoints](https://huggingface.co/archivartaunik/models) | More than 40 XTTS-labelled experiment/checkpoint repositories, including corpus variants, staged checkpoints and stress-aware runs. These are experiments, not independent architectures or comparable benchmark results. |
| Speech data | [Dataset inventory](DATASETS.md), [Ministerskija collection](https://huggingface.co/collections/fosters/ministerskija), [Belarusian audio corpus](https://huggingface.co/datasets/fosters/be-bel-audio-corpus) | Collection metadata reports 35 books, 60,022 aligned pairs and 260 hours; a separate corpus card reports 49,606 rows. These collections may overlap and should not be summed. |
| Homographs | [homograph-bel](https://github.com/idegterov/homograph-bel), [candidate QA](https://github.com/idegterov/HomographBel-Dictionary-QA), [contextual model](https://huggingface.co/fosters/homograph-bel-xlm-roberta-base) | Open dictionary/runtime and QA workflow plus contextual selection among dictionary candidates. The reported 0.901211 macro-F1 is preliminary on 275 gold validation contexts across 28 homographs. |
| Demos | [Bextts](https://huggingface.co/spaces/archivartaunik/Bextts), [BeTTSNaciski](https://huggingface.co/spaces/archivartaunik/BeTTSNaciski) | Public inference interfaces, including a stress-aware demo; availability may vary. |
| GitHub hub | [Manifest](../data/manifests/public-resources.yaml), [validator](../tools/validate_resource_manifest.py), [CI](../.github/workflows/validate-resources.yml) | Machine-readable external resource metadata with offline validation. |

## What exists in this repository today

The repository currently contains project documentation, an external resource manifest, an offline Python validator, and a GitHub Actions workflow for that validator. The planned `src/`, `evals/`, `tests/` and `examples/` directories are not yet published here. Linked models and datasets live on Hugging Face and Kaggle; their source, licensing and provenance must be assessed per artifact. A successful manifest check validates metadata shape, not dataset rights, model quality, URL availability or training reproducibility.

## Next engineering milestones

The next useful release is a small, reproducible vertical slice: a public Belarusian stress test set with provenance, a dictionary-backed baseline, an adapter from text and target spans to stress candidates, and regression tests in CI. Next, publish checkpoint-specific experiment manifests with immutable dataset and model revisions, training settings, permitted reuse terms and comparable evaluations. See the [roadmap](ROADMAP.md) and [contributing guide](../CONTRIBUTING.md).
