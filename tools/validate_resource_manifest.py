#!/usr/bin/env python3
"""Validate the public BE_TTS resource manifest.

This check is intentionally offline and deterministic. It validates metadata
shape and basic invariants without depending on external platform availability.
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "manifests" / "public-resources.yaml"

REQUIRED_RESOURCE_FIELDS = {"id", "type", "platform", "owner", "name", "url", "license"}
ALLOWED_PLATFORMS = {"huggingface", "kaggle"}
ALLOWED_TYPES = {"model", "dataset", "collection", "demo"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_url(value: object, resource_id: str) -> None:
    if not isinstance(value, str):
        fail(f"{resource_id}: url must be a string")
    try:
        parsed = urlparse(value)
    except ValueError:
        fail(f"{resource_id}: malformed URL: {value!r}")
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
        if (isinstance(value, float) and not math.isfinite(value)) or value < 0:
            fail(f"{resource_id}: metric {key!r} must be finite and non-negative")


def validate_manifest(path: Path) -> int:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        fail(f"cannot read manifest {path}: {exc}")

    if not isinstance(data, dict):
        fail("manifest root must be a mapping")
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        fail("schema_version must be 1")
    if not isinstance(data.get("snapshot_date"), str):
        fail("snapshot_date must be a quoted YYYY-MM-DD string")

    snapshot_date = data["snapshot_date"]
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", snapshot_date):
        fail("snapshot_date must use YYYY-MM-DD format")
    try:
        date.fromisoformat(snapshot_date)
    except ValueError:
        fail("snapshot_date must be a valid calendar date")

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
        if not isinstance(resource_id, str) or not resource_id.strip():
            fail(f"resource #{index + 1}: id must be a non-empty string")
        if resource_id in seen_ids:
            fail(f"duplicate resource id: {resource_id}")
        seen_ids.add(resource_id)

        platform = resource["platform"]
        if not isinstance(platform, str) or platform not in ALLOWED_PLATFORMS:
            fail(f"{resource_id}: unsupported platform {platform!r}")

        license_value = resource["license"]
        if not isinstance(license_value, str) or not license_value.strip():
            fail(f"{resource_id}: license must be a non-empty string")

        for field in ("type", "owner", "name"):
            if not isinstance(resource[field], str) or not resource[field].strip():
                fail(f"{resource_id}: {field} must be a non-empty string")

        if resource["type"] not in ALLOWED_TYPES:
            fail(f"{resource_id}: unsupported type {resource['type']!r}")

        validate_url(resource["url"], resource_id)
        parsed = urlparse(resource["url"])
        expected_host = {"huggingface": "huggingface.co", "kaggle": "www.kaggle.com"}[platform]
        if parsed.netloc != expected_host:
            fail(f"{resource_id}: url host must be {expected_host}")
        validate_metrics(resource.get("metrics"), resource_id)

    return len(resources)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", nargs="?", type=Path, default=MANIFEST)
    args = parser.parse_args()
    count = validate_manifest(args.manifest)
    print(f"OK: {count} resources validated from {args.manifest}")


if __name__ == "__main__":
    main()
