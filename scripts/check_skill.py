#!/usr/bin/env python3
"""Validate Facet Core's package structure and fixed output contract."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "facet-core"
SKILL = SKILL_DIR / "SKILL.md"
OUTPUT_CONTRACT = SKILL_DIR / "references" / "output-contract.md"
REGRESSION = ROOT / "tests" / "facet-core-regression.md"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_file(path: Path) -> str:
    if not path.is_file():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


skill_text = require_file(SKILL)
contract_text = require_file(OUTPUT_CONTRACT)
regression_text = require_file(REGRESSION)

if not skill_text.startswith("---\n"):
    fail("SKILL.md must begin with YAML frontmatter")

parts = skill_text.split("---\n", 2)
if len(parts) != 3:
    fail("SKILL.md frontmatter is not closed")

frontmatter = parts[1]
keys = re.findall(r"^([a-zA-Z0-9_-]+):", frontmatter, flags=re.MULTILINE)
if set(keys) != {"name", "description"}:
    fail("SKILL.md frontmatter must contain only name and description")
if not re.search(r"^name:\s*facet-core\s*$", frontmatter, flags=re.MULTILINE):
    fail("skill name must be facet-core")
description = re.search(r"^description:\s*(.+)$", frontmatter, flags=re.MULTILINE)
if description is None or not description.group(1).strip():
    fail("skill description is required")
if len(description.group(1)) > 1024:
    fail("skill description exceeds 1024 characters")

for reference in sorted(set(re.findall(r"`(references/[^`]+\.md)`", skill_text))):
    if not (SKILL_DIR / reference).is_file():
        fail(f"SKILL.md links to missing reference: {reference}")

label_sets = {
    "Korean": [
        "메시지 이동 경로",
        "회사가 하는 말",
        "제품에서 보이는 것",
        "어디서 틀어지나",
        "왜 그런 것으로 보이나",
    ],
    "English": [
        "Where the message travels",
        "What the company says",
        "What the product shows",
        "Where it changes",
        "Why it may be this way",
    ],
}


def assert_order(text: str, labels: list[str], source: str) -> None:
    positions = []
    for label in labels:
        position = text.find(label)
        if position < 0:
            fail(f"{source} is missing required label: {label}")
        positions.append(position)
    if positions != sorted(positions):
        fail(f"{source} does not preserve the fixed output order")


for language, labels in label_sets.items():
    assert_order(
        contract_text,
        [f"**{label}**" for label in labels],
        f"output contract ({language})",
    )
    assert_order(
        regression_text,
        [f"`{label}`" for label in labels],
        f"regression suite ({language})",
    )

unfinished_markers = ("TO" + "DO", "FIX" + "ME")
unfinished_pattern = re.compile(r"\b(?:" + "|".join(unfinished_markers) + r")\b")
scanned_suffixes = {".md", ".py", ".yaml", ".yml", ".txt"}
skipped_dirs = {".git", "dist"}

for path in ROOT.rglob("*"):
    if path.is_file() and not skipped_dirs & set(path.parts) and path.suffix in scanned_suffixes:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if unfinished_pattern.search(text):
            fail(f"unfinished marker found in {path.relative_to(ROOT)}")

print("OK: Facet Core structure and output contract are valid")
