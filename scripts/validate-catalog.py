#!/usr/bin/env python3
"""Validate index.json against the DESIGN.md catalog."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "index.json"
CATALOG_DIR = ROOT / "design-mds"

REQUIRED_HEADING_PREFIXES = (
    "## 1. Visual Theme",
    "## 2. Color Palette",
    "## 3. Typography",
    "## 4. Component Styl",
    "## 5. Layout Principles",
    "## 6. Depth",
    "## 7. Do",
    "## 8. Responsive",
    "## 9. Agent Prompt",
)


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)


def main() -> int:
    errors = 0

    if not INDEX_PATH.is_file():
        fail(f"missing {INDEX_PATH.relative_to(ROOT)}")
        return 1

    try:
        index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"index.json is not valid JSON: {exc}")
        return 1

    if not isinstance(index, list) or not all(isinstance(item, str) for item in index):
        fail("index.json must be a JSON array of strings")
        return 1

    if len(index) != len(set(index)):
        fail("index.json contains duplicate domains")
        errors += 1

    if index != sorted(index):
        fail("index.json is not sorted")
        errors += 1

    if not CATALOG_DIR.is_dir():
        fail(f"missing {CATALOG_DIR.relative_to(ROOT)}/")
        return 1

    folders = sorted(path.name for path in CATALOG_DIR.iterdir() if path.is_dir())
    indexed = set(index)
    on_disk = set(folders)

    for domain in sorted(indexed - on_disk):
        fail(f"index entry has no catalog folder: {domain}")
        errors += 1

    for domain in sorted(on_disk - indexed):
        fail(f"catalog folder is not listed in index.json: {domain}")
        errors += 1

    for domain in index:
        design_md = CATALOG_DIR / domain / "DESIGN.md"
        if not design_md.is_file():
            fail(f"missing DESIGN.md for {domain}")
            errors += 1
            continue

        text = design_md.read_text(encoding="utf-8")
        if not text.strip():
            fail(f"empty DESIGN.md for {domain}")
            errors += 1
            continue

        headings = [
            line.strip() for line in text.splitlines() if line.startswith("## ")
        ]
        for prefix in REQUIRED_HEADING_PREFIXES:
            if not any(heading.startswith(prefix) for heading in headings):
                fail(f"{domain}: missing section starting with {prefix!r}")
                errors += 1

    if errors:
        fail(f"{errors} catalog check(s) failed")
        return 1

    print(f"ok: {len(index)} design systems, index and DESIGN.md files match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
