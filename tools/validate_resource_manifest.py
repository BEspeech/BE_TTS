#!/usr/bin/env python3
"""Validate the public BE_TTS resource manifest.

This check is intentionally offline and deterministic. It validates metadata
shape and basic invariants without depending on external platform availability.
"""

from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "manifests" / "public-resources.yaml"

REQUIRED_RESOURCE_FIELDS = {"id", "type", "platform", "owner", "name", "url", "license"}
ALLOWED_PLATFORMS = {"huggingface", "kaggle"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_url(value: object, resource_id: str) -> None:
    if not isinstance(value, str):
        fail(f"{resource_id}: url must be a string")
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        fail(f"{resource_id}: url must be an absolute https URL: {value!r}")


def validate_metrics(metrics: object, resource_id: str) -> None:
    if metrics is None:
        return
    if not isinstance(metrics, dict):
        fail(f"{resource_id}: metrics must be a mapping")
    for key, value in metrics.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            fail(f"{resource_id}: metric {key!r} must be numeric")
        if value < 0:
            fail(f"{resource_id}: metric {key!r} must be non-negative")


def main() -> None:
    if not MANIFEST.exists():
        fail(f"manifest not found: {MANIFEST}")

    with MANIFEST.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)

    if not isinstance(data, dict):
        fail("manifest root must be a mapping")
    if data.get("schema_version") != 1:
        fail("schema_version must be 1")
    if not isinstance(data.get("snapshot_date"), str):
        fail("snapshot_date must be a quoted YYYY-MM-DD string")

    language = data.get("language")
    if not isinstance(language, dict) or language.get("code") != "be":
        fail("language.code must be 'be'")

    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        fail("resources must be a non-empty list")

    seen_ids: set[str] = set()
    for index, resource in enumerate(resources):
        if not isinstance(resource, dict):
            fail(f"resource #{index + 1} must be a mapping")

        missing = REQUIRED_RESOURCE_FIELDS - resource.keys()
        if missing:
            fail(f"resource #{index + 1} missing fields: {sorted(missing)}")

        resource_id = resource["id"]
        if not isinstance(resource_id, str) or not resource_id:
            fail(f"resource #{index + 1}: id must be a non-empty string")
        if resource_id in seen_ids:
            fail(f"duplicate resource id: {resource_id}")
        seen_ids.add(resource_id)

        platform = resource["platform"]
        if platform not in ALLOWED_PLATFORMS:
            fail(f"{resource_id}: unsupported platform {platform!r}")

        license_value = resource["license"]
        if not isinstance(license_value, str) or not license_value.strip():
            fail(f"{resource_id}: license must be a non-empty string")

        for field in ("type", "owner", "name"):
            if not isinstance(resource[field], str) or not resource[field].strip():
                fail(f"{resource_id}: {field} must be a non-empty string")

        validate_url(resource["url"], resource_id)
        validate_metrics(resource.get("metrics"), resource_id)

    print(f"OK: {len(resources)} resources validated from {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
