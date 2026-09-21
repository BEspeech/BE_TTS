# BE_TTS Roadmap

This roadmap describes the transition from a distributed set of public Belarusian speech/NLP artifacts to a reproducible open-source engineering hub.

## Phase 0 — OSS foundation

- [x] Establish a public GitHub hub.
- [x] Add project mission, ecosystem context, and contribution rules.
- [x] Add a machine-readable inventory of public datasets, models, demos, and their licenses.
- [x] Define initial repository conventions for code, evaluations, examples, and manifests.

## Phase 1 — Reproducibility

- [ ] Add lightweight dataset/model loaders.
- [ ] Build the canonical dataset/provenance registry ([#4](https://github.com/BEspeech/BE_TTS/issues/4)).
- [ ] Add small, redistributable fixtures for tests.
- [x] Add initial provenance/license metadata validation for resource manifests.
- [ ] Add CI for formatting, tests, and documentation links.
- [ ] Publish reproducible baseline commands.

## Phase 2 — Homographs, stress, and pronunciation

- [ ] Define a stable input/output schema for contextual homograph resolution.
- [ ] Publish a compact reviewed evaluation set.
- [ ] Add inference adapters for public homograph models ([#3](https://github.com/BEspeech/BE_TTS/issues/3)).
- [ ] Add metrics split by homograph, variant, confidence, and source.
- [ ] Add regression tests for known Belarusian pronunciation failures.

## Phase 3 — Text normalization and phonemization

- [ ] Define normalization stages and contracts.
- [ ] Integrate Belarusian stress resolution before phonemization where required.
- [ ] Add IPA/phoneme comparison fixtures.
- [ ] Document orthography assumptions and edge cases.

## Phase 4 — TTS evaluation

- [ ] Normalize the XTTS experiment lineage into reproducible manifests ([#2](https://github.com/BEspeech/BE_TTS/issues/2)).
- [ ] Add adapters for representative public Belarusian TTS checkpoints.
- [ ] Define reproducible pronunciation and intelligibility evaluation.
- [ ] Add human-evaluation templates and versioned benchmark manifests.
- [ ] Track model regressions across releases.

## Phase 5 — Maintainer automation

- [ ] Automate resource-card and metadata validation.
- [ ] Automate link, license, and provenance checks.
- [ ] Use AI-assisted review for tests, documentation, and contribution triage.
- [ ] Generate release QA summaries from deterministic test/eval results.
- [ ] Keep large datasets and model artifacts outside Git while making them discoverable and reproducible here.

## Release principle

BE_TTS should make Belarusian speech research easier to reproduce without pretending all public artifacts have identical maturity or licensing status. Each release should clearly distinguish:

- reviewed vs. experimental assets;
- gold vs. generated/silver annotations;
- repository MIT-licensed code vs. externally licensed data/models;
- confirmed measurements vs. interpretation.
