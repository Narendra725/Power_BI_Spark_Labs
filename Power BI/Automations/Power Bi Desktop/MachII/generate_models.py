from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import requests

# ROOT_SCHEMA_URL = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/3.0.0/schema.json"
# ROOT_SCHEMA_URL = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json"
# ROOT_SCHEMA_URL = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.3.0/schema.json"
# ROOT_SCHEMA_URL = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmark/1.4.0/schema.json"
# ROOT_SCHEMA_URL = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/versionMetadata/1.0.0/schema.json"
ROOT_SCHEMA_URL = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.0.0/schema.json"



root_class = "page"
output_file = "page_metadata"

OUT_DIR = Path("generated_models")
CACHE_DIR = Path("schemas_cache")

OUT_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)


# -----------------------------
# HELPERS
# -----------------------------
def safe_name(name: str) -> str:
    name = re.sub(r"[^0-9a-zA-Z_]", "_", name)
    return "_" + name if name and name[0].isdigit() else name


def pascal(name: str) -> str:
    parts = re.split(r"[^0-9a-zA-Z]+", name)
    return "".join(p.capitalize() for p in parts if p) or "Model"


def fetch(url: str) -> dict:
    key = safe_name(url)
    path = CACHE_DIR / f"{key}.json"

    if path.exists():
        return json.loads(path.read_text())

    data = requests.get(url).json()
    path.write_text(json.dumps(data, indent=2))
    return data


def resolve(base: str, ref: str):
    if ref.startswith("#"):
        return base, ref
    if "#/" in ref:
        u, p = ref.split("#", 1)
        return urljoin(base, u), "#" + p
    return urljoin(base, ref), None


def pointer(doc: dict, ptr: str | None):
    if not ptr:
        return doc
    cur = doc
    for p in ptr.lstrip("#/").split("/"):
        cur = cur[p]
    return cur


def node_id(url: str, ptr: str | None):
    return f"{url}{ptr or ''}"


# -----------------------------
# NODE
# -----------------------------
@dataclass
class Node:
    name: str
    schema: dict
    origin: str
    ptr: str | None


# -----------------------------
# COLLECTOR
# -----------------------------
class Collector:
    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.visited = set()

    def collect(self, url: str):
        self._walk(url, fetch(url), None, "Root")

    def _walk(self, url, obj, ptr, name):
        nid = node_id(url, ptr)
        if nid in self.visited:
            return
        self.visited.add(nid)

        # definitions
        for k, v in obj.get("definitions", {}).items():
            p = f"#/definitions/{k}"
            nid = node_id(url, p)
            self.nodes[nid] = Node(pascal(k), v, url, p)
            self._walk(url, v, p, k)

        # properties
        for k, v in obj.get("properties", {}).items():
            self._fragment(url, v, f"{name}_{k}")

        # combinators
        for comb in ("allOf", "anyOf", "oneOf"):
            for i, v in enumerate(obj.get(comb, []) or []):
                self._fragment(url, v, f"{name}_{comb}_{i}")

        if "items" in obj:
            self._fragment(url, obj["items"], f"{name}_Item")

    def _fragment(self, base, frag, name):
        if not isinstance(frag, dict):
            return

        if "$ref" in frag:
            u, p = resolve(base, frag["$ref"])
            doc = fetch(u)
            resolved = pointer(doc, p)
            nid = node_id(u, p)

            if nid not in self.nodes:
                cls = pascal((p or name).split("/")[-1])
                self.nodes[nid] = Node(cls, resolved, u, p)

            self._walk(u, resolved, p, name)
            return

        if frag.get("type") == "object" and "properties" in frag:
            p = f"#inline/{name}"
            nid = node_id(base, p)
            self.nodes[nid] = Node(pascal(name), frag, base, p)
            self._walk(base, frag, p, name)

        # recursive
        for k, v in frag.get("properties", {}).items():
            self._fragment(base, v, f"{name}_{k}")

        for comb in ("allOf", "anyOf", "oneOf"):
            for i, v in enumerate(frag.get(comb, []) or []):
                self._fragment(base, v, f"{name}_{comb}_{i}")

        if "items" in frag:
            self._fragment(base, frag["items"], f"{name}_Item")


# -----------------------------
# TYPE BUILDER
# -----------------------------
class TypeBuilder:
    def __init__(self, nodes):
        self.map = {k: v.name for k, v in nodes.items()}

    def build(self, base, schema):
        if "$ref" in schema:
            u, p = resolve(base, schema["$ref"])
            key = node_id(u, p)
            if key not in self.map:
                raise Exception(f"Missing ref {key}")
            return self.map[key]

        t = schema.get("type")

        if "allOf" in schema:
            return " & ".join(self.build(base, s) for s in schema["allOf"])

        if t == "array":
            return f"list[{self.build(base, schema.get('items', {}))}]"

        if t == "object":
            return "dict[str, Any]"

        return {
            "string": "str",
            "number": "float",
            "integer": "int",
            "boolean": "bool",
        }.get(t, "Any")


# -----------------------------
# EMITTER
# -----------------------------
def emit(node: Node, tb: TypeBuilder):
    lines = [f"class {node.name}(BaseModel):"]
    props = node.schema.get("properties", {})

    if not props:
        return "\n".join(lines + ["    pass"])

    for k, v in props.items():
        name = safe_name(k)
        typ = tb.build(node.origin, v)
        lines.append(f"    {name}: {typ} | None = None")

    return "\n".join(lines)


# -----------------------------
# MAIN
# -----------------------------
def main():
    c = Collector()
    c.collect(ROOT_SCHEMA_URL)

    tb = TypeBuilder(c.nodes)

    base = f"""from pydantic import BaseModel, ConfigDict

class {root_class}(BaseModel):
    model_config = ConfigDict(extra="allow")
"""
    (OUT_DIR / "base.py").write_text(base)

    models = []
    for n in c.nodes.values():
        models.append(emit(n, tb))

    content = f"""
from typing import Any
from .base import {root_class}

{chr(10).join(models)}
"""
    (OUT_DIR / f"{output_file}.py").write_text(content)

    print("✅ Done:", len(models), "models")


if __name__ == "__main__":
    main()