from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests


ROOT_SCHEMA_URL = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/3.0.0/schema.json"


# ----------------------------
# Schema helpers
# ----------------------------
def fetch_json(url: str) -> dict:
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return r.json()


def resolve_ref(base_url: str, ref: str) -> tuple[str, str | None]:
    if ref.startswith("#"):
        return base_url, ref

    if "#/" in ref:
        u, p = ref.split("#", 1)
        return urljoin(base_url, u), "#" + p

    return urljoin(base_url, ref), None


def get_by_pointer(doc: dict, pointer: str | None) -> dict:
    if not pointer or pointer == "#":
        return doc
    parts = pointer.lstrip("#/").split("/")
    cur = doc
    for p in parts:
        cur = cur[p]
    return cur


# ----------------------------
# Sample generator
# ----------------------------
def sample_value(schema_url: str, schema_obj: dict, property_name: str = "") -> Any:
    """
    Generate a dummy value for a schema node.
    Supports: $ref, type, required, properties, array, enum
    """
    if not isinstance(schema_obj, dict):
        return None

    # $ref
    if "$ref" in schema_obj:
        ref_url, ptr = resolve_ref(schema_url, schema_obj["$ref"])
        ref_doc = fetch_json(ref_url)
        resolved = get_by_pointer(ref_doc, ptr)
        return sample_value(ref_url, resolved, property_name)

    # enum
    if "enum" in schema_obj:
        return schema_obj["enum"][0]

    # oneOf/anyOf/allOf (pick first)
    for comb in ("oneOf", "anyOf", "allOf"):
        if comb in schema_obj and isinstance(schema_obj[comb], list) and schema_obj[comb]:
            return sample_value(schema_url, schema_obj[comb][0], property_name)

    t = schema_obj.get("type")

    # nullable union like ["string","null"]
    if isinstance(t, list):
        if "null" in t:
            non_null = [x for x in t if x != "null"]
            if non_null:
                return sample_value(schema_url, {**schema_obj, "type": non_null[0]}, property_name)
        return None

    # primitives with smarter defaults based on property name
    if t == "string":
        return _smart_string_value(schema_obj, property_name)

    if t == "integer":
        return _smart_int_value(property_name)

    if t == "number":
        return _smart_number_value(property_name)

    if t == "boolean":
        return _smart_bool_value(property_name)

    if t == "array":
        items = schema_obj.get("items", {})
        return [sample_value(schema_url, items, property_name)] if items else []

    if t == "object" or "properties" in schema_obj:
        props = schema_obj.get("properties", {})
        required = schema_obj.get("required", [])
        out = {}

        # fill required props first
        for k in required:
            if k in props:
                out[k] = sample_value(schema_url, props[k], k)
            else:
                # required exists but property missing → put generic placeholder
                out[k] = None

        # optionally include 1-2 non-required props (helps shape)
        extra_count = 0
        for k, v in props.items():
            if k in out:
                continue
            out[k] = sample_value(schema_url, v, k)
            extra_count += 1
            if extra_count >= 2:
                break

        return out

    # fallback
    return None


def _smart_string_value(schema_obj: dict, prop_name: str) -> str:
    """Generate meaningful string values based on property name."""
    name_lower = prop_name.lower()

    # special-case common formats
    fmt = schema_obj.get("format")
    if fmt == "uri":
        return "https://example.com"
    if fmt == "date-time":
        return "2026-01-01T00:00:00Z"

    # infer from property name
    if "name" in name_lower:
        return "Sample Name"
    if "title" in name_lower:
        return "Sample Title"
    if "description" in name_lower:
        return "This is a sample description for the report."
    if "url" in name_lower or "uri" in name_lower:
        return "https://example.com"
    if "color" in name_lower:
        return "#FF5733"
    if "font" in name_lower:
        return "Arial"
    if "id" in name_lower:
        return "sample-id-123"
    if "type" in name_lower:
        return "sampleType"
    if "version" in name_lower:
        return "1.0.0"
    if "path" in name_lower:
        return "/sample/path"
    if "email" in name_lower:
        return "user@example.com"
    if "phone" in name_lower:
        return "+1-555-123-4567"

    # default
    return "sample_value"


def _smart_int_value(prop_name: str) -> int:
    """Generate meaningful integer values."""
    name_lower = prop_name.lower()

    if "width" in name_lower:
        return 1280
    if "height" in name_lower:
        return 720
    if "x" == name_lower or "left" in name_lower:
        return 100
    if "y" == name_lower or "top" in name_lower:
        return 50
    if "z" == name_lower or "order" in name_lower:
        return 1
    if "count" in name_lower or "size" in name_lower:
        return 5
    if "index" in name_lower:
        return 0

    return 42  # default meaningful number


def _smart_number_value(prop_name: str) -> float:
    """Generate meaningful float values."""
    name_lower = prop_name.lower()

    if "opacity" in name_lower:
        return 1.0
    if "scale" in name_lower:
        return 1.0
    if "percentage" in name_lower or "percent" in name_lower:
        return 0.75

    return 3.14  # default


def _smart_bool_value(prop_name: str) -> bool:
    """Generate meaningful boolean values."""
    name_lower = prop_name.lower()

    if "enabled" in name_lower or "visible" in name_lower or "show" in name_lower:
        return True
    if "disabled" in name_lower or "hidden" in name_lower or "hide" in name_lower:
        return False

    return True  # default to true for most cases


def generate_sample_report_json():
    schema = fetch_json(ROOT_SCHEMA_URL)

    # Root of schema might itself be object or $ref
    report_sample = sample_value(ROOT_SCHEMA_URL, schema)

    Path("out").mkdir(exist_ok=True)
    Path("out/report.json").write_text(json.dumps(report_sample, indent=2), encoding="utf-8")
    print("✅ Generated sample report.json at: out/report.json")


if __name__ == "__main__":
    generate_sample_report_json()
