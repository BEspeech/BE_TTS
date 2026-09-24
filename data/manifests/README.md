# Resource manifests

This directory contains lightweight, machine-readable metadata for public Belarusian speech/NLP artifacts used or referenced by BE_TTS.

## Rules

- Do not store large audio, dataset archives, or model weights here.
- Use canonical public URLs.
- Record the artifact-level license; do not inherit the repository MIT license.
- Use `per-artifact` when a collection contains resources with different terms.
- Use `other` only when that is the public artifact's declared license and add a note explaining review status.
- Date-snapshot volatile metrics such as downloads, likes, and views.
- Distinguish experimental/silver resources from reviewed release assets.

The initial manifest is [public-resources.yaml](public-resources.yaml).

## Validation contract (schema version 1)

Run `python tools/validate_resource_manifest.py` from the repository root. An optional positional path validates another manifest. Errors exit with status 1; success reports the resource count.

- `schema_version`: integer `1` (not a boolean).
- `snapshot_date`: quoted, valid calendar date in `YYYY-MM-DD` format.
- `language.code`: `be`.
- `resources`: non-empty list, with unique, nonblank string IDs.
- Required nonblank strings: `type`, `platform`, `owner`, `name`, `url`, `license`.
- Supported types: `model`, `dataset`, `collection`, `demo`.
- Supported platform hosts: `huggingface` → `huggingface.co`; `kaggle` → `www.kaggle.com`. URLs must use HTTPS with no credentials or custom port.
- Optional `metrics`: mapping of finite, non-negative numbers; booleans are rejected. Null is treated as absent for compatibility.

This is an offline metadata check, not verification of provenance or external artifact availability. Additional metadata fields are allowed for forward-compatible annotations.
