# Belarusian homographs and stress

Correct stress is a core TTS problem in Belarusian. Some written forms are homographs whose pronunciation depends on grammatical analysis or sentence context.

BE_TTS therefore treats detection, dictionary candidates, contextual disambiguation and QA as a separate subsystem before phonemization and synthesis.

## Open-source dictionary/runtime

Repository:
https://github.com/idegterov/homograph-bel

The public `homograph-bel` package provides offline homograph detection, dictionary lookup, morphology evidence and constrained contextual stress selection.

Its bundled Dictionary v2 is derived from GrammarDB `RELEASE-202601`.

| Metric | Count |
| --- | ---: |
| Homograph surfaces | **19,992** |
| Stressed candidate options | **40,167** |
| GrammarDB analyses | **73,047** |
| Contextual homographs | **7,218** |
| Free-variant homographs | **12,068** |
| Conflict homographs | **706** |
| Production-supported candidates | **33,921** |
| Candidate-only options | **6,246** |

Runtime detection is deterministic and offline. The API returns exact text offsets, stable IDs, dictionary version and a closed set of stress candidates.

That closed-candidate contract is intentional: a contextual model selects among dictionary-backed pronunciations instead of inventing stress forms.

## Candidate QA

Repository:
https://github.com/idegterov/HomographBel-Dictionary-QA

A separate review workflow isolates cases that are not yet safe for production labeling.

| Record | Count |
| --- | ---: |
| Contextual homographs under review | **2,454** |
| Two-candidate homographs | **2,400** |
| Three-candidate homographs | **54** |
| All candidates | **4,962** |
| Candidate-only candidates to review | **2,677** |
| Production-supported comparison candidates | **2,285** |
| Linked GrammarDB analyses | **14,291** |

Accepted decisions are imported through a release-bound rebuild/re-adjudication process rather than editing a production dictionary directly.

## Contextual neural model

https://huggingface.co/fosters/homograph-bel-xlm-roberta-base

The XLM-R model resolves one exact homograph occurrence from sentence context.

```text
input:
sentence + exact target span + dictionary candidates

output:
dictionary-approved stressed form
+ candidate probabilities
+ support status
```

Published details:

- backbone: `FacebookAI/xlm-roberta-base`;
- dictionary: `GrammarDB-RELEASE-202601`;
- Belarusian official 2008 orthography;
- 3 epochs / 4,785 optimizer steps;
- effective batch size 64;
- BF16 on NVIDIA L40S;
- preliminary gold-validation macro-F1: **0.901211**.

## Training data

The model card reports:

| Split | Contexts | Homographs | Observed variants | Label quality |
| --- | ---: | ---: | ---: | --- |
| Train | **102,029** | **1,941** | **2,896** | 2,128 gold; 18,390 silver-high; 81,511 silver-medium |
| Silver validation | **5,134** | **1,027** | **1,397** | model-labelled diagnostic |
| Gold validation | **275** | **28** | **43** | human-reviewed |
| Gold test | **538** | **28** | **43** | human-reviewed, reserved |

The scale and the quality labels must be reported together. Most training examples are silver/model-generated, while the gold validation set is much smaller. The 0.901211 result therefore must not be represented as broad performance across all 1,941 trained homographs.

## Intended TTS pipeline

```text
Belarusian text
      ↓
deterministic homograph detection
      ↓
dictionary candidates + morphology evidence
      ↓
contextual resolver
      ↓
validated stressed form
      ↓
phonemization
      ↓
TTS
```

Production boundaries:

- abstain when context is insufficient;
- never accept out-of-dictionary variants;
- do not treat softmax confidence as calibrated until validated;
- distinguish `candidate_only` from production-supported pronunciations;
- keep the reserved gold test separate from training iteration.

## Why this matters for BE_TTS

This makes the project more than a generic language fine-tune. The homograph track combines:

- a reproducible linguistic dictionary;
- morphology-backed candidates;
- human QA;
- constrained LLM-selection support;
- a task-specific contextual model;
- gold/silver split discipline;
- explicit integration before phonemization/TTS.

The `Naciski` XTTS checkpoints and BeTTSNaciski demo show the same problem being addressed at the synthesis layer.

## Next steps

1. Add a stable BE_TTS adapter to `homograph-bel`.
2. Add reviewed pronunciation regression cases.
3. Publish a versioned benchmark manifest.
4. Compare dictionary-only, constrained-LLM, XLM-R and combined strategies on the same gold set.
5. Calibrate confidence/abstention thresholds before production auto-accept.
6. Measure end-to-end TTS pronunciation impact, not only classifier accuracy.
