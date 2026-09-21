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
