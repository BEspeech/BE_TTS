# OSS readiness review — 2026-09-24

Reviewed main at `b258d7d25c596332fd775b2a52c3e95639a51aa1` and open [PR #6](https://github.com/BEspeech/BE_TTS/pull/6). This review adds engineering fixes independently of that documentation PR.

## Assessment

BE_TTS has a credible Belarusian speech research ecosystem, but this GitHub repository is a newly established engineering hub. Its current executable contribution is a resource-manifest validator. Linked training histories, models and datasets strengthen the ecosystem case; they do not establish adoption of the BE_TTS code itself.

The [Codex for OSS application](https://openai.com/form/codex-for-oss/) asks for ecosystem importance or meaningful usage and evidence of active maintenance. Its qualification, API-credit-use and additional-information answers each have a 500-character limit (checked 2026-09-24). Selection is not guaranteed by completing repository hygiene.

## Findings and disposition

| Priority | Finding | Disposition |
| --- | --- | --- |
| High | The only executable validator accepted impossible dates, boolean schema versions, NaN/infinite metrics and mismatched platform hosts. List-valued platforms and malformed YAML could produce tracebacks. | Fixed with explicit validation and CLI regression coverage. |
| High | No local TTS or homograph inference adapter, reviewed evaluation fixture or reproducible synthesis command is present. | Next substantive milestone: implement one public adapter with exact dependency/model revisions and a small permitted fixture. Do not describe planned directories as shipped features. |
| High | Artifact counts measure published repositories, not users, unique datasets or independent architectures. | Keep dated counts distinct from adoption. Obtain current, dated download evidence and concrete downstream usage before claiming reach. Do not sum overlapping corpora. |
| High | Linked artifact licenses and recording rights differ from the repository MIT license. | Existing caveat is appropriate. Metadata validation cannot establish rights; review exact model/data terms before selecting a recommended checkpoint. |
| Medium | Tests and a contributor quickstart were absent. | Added offline regression tests, CI execution and documented commands. |
| Medium | README still lists manifest publication and CI establishment as future tasks. | Correction already proposed in PR #6; coordinate that PR with this change. |
| Medium | Maintainer role and attribution across the linked profiles are not explicitly established. | Applicant must confirm their role and collaborators' contributions; do not infer authorship from links or admin access. |
| Medium | No checkpoint is accompanied here by immutable model/data revisions and a comparable evaluation. | Prioritize one reproducible checkpoint record over a longer inventory. |

The existing homograph documentation correctly limits the reported macro-F1 to its small gold validation set. Keep gold/silver distinctions and the reserved test split intact.

## Suggested application text

Drafts below avoid unverified adoption numbers. Confirm applicant authority and linked artifact availability before submission. Neither this change nor PR #6 submits an application.

### Why does this repository qualify?

BE_TTS is the public engineering hub for Belarusian speech technology, an under-resourced language ecosystem. It connects published TTS experiments, speech datasets and an open homograph/stress subsystem. The repository provides resource metadata and validation; reusable inference and evaluation integrations are the next milestone. Its value is shared language infrastructure, with public evidence linked in the repository docs.

### How will you use API credits for your project?

We will use credits for Codex-assisted code migration, regression tests, dataset metadata QA, inference adapters, and reproducible evaluation tooling. Maintainers will review changes and run deterministic checks before merging. Initial deliverables are a dictionary-backed stress adapter, a small reviewed evaluation fixture, checkpoint manifests with exact revisions, and CI regression coverage.

### Anything else we should know?

BE_TTS is a new hub consolidating work published across Hugging Face, Kaggle and related GitHub repositories. Checkpoint counts describe experiments, not independent models or adoption. Linked artifacts retain their own licenses. We distinguish human-reviewed gold labels from generated silver labels and report the scope of preliminary evaluation results explicitly.

## Before submission

1. Review PR #6 together with this engineering change. After both land, update its status paragraph to acknowledge the new `tests/` directory.
2. Confirm the applicant's public GitHub identity, primary/core maintainer role, account email and OpenAI organization ID in the form; keep personal details out of this document.
3. Link the strongest public implementation as supporting evidence and describe BE_TTS's consolidation role accurately.
4. Capture dated usage evidence and at least one real downstream use if available. Do not replace unknown values with estimates.
5. Publish a small reproducible integration when ready; avoid inventing a release just to improve the application.
