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
OPENAI_EXAMPLES = {
    "Korean": ROOT / "examples" / "openai-one-system-one-identity.md",
    "English": ROOT / "examples" / "openai-one-system-one-identity.en.md",
}


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
openai_examples = {
    language: require_file(path) for language, path in OPENAI_EXAMPLES.items()
}

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


marker = "## Output regression"
if marker not in regression_text:
    fail("regression suite is missing the Output regression section")
regression_contract = regression_text.split(marker, 1)[1]

diagnosis_markers = {
    "Korean": ["진단:", "주된 문제 위치:", "연결이 끊긴 영역:"],
    "English": ["Diagnosis:", "Main problem location:", "Where the connection breaks:"],
}

for language, labels in label_sets.items():
    assert_order(
        contract_text,
        [f"**{label}**" for label in labels],
        f"output contract ({language})",
    )
    assert_order(
        regression_contract,
        [f"`{label}`" for label in labels],
        f"regression suite ({language})",
    )
    assert_order(
        contract_text,
        diagnosis_markers[language],
        f"diagnosis block ({language})",
    )

held_markers = {
    "Korean": ["판정:", "달성한 것:", "약속 범위 내 판정:", "별도 고려사항:", "주의:"],
    "English": [
        "Verdict:",
        "Achieved:",
        "Verdict within the promise's scope:",
        "Separate consideration:",
        "Caution:",
    ],
}

for marker in ("> **판정:", "> **Verdict:"):
    if marker not in contract_text:
        fail(f"held-within-scope branch is missing its lead verdict: {marker}")

for language, markers in held_markers.items():
    assert_order(
        contract_text,
        markers,
        f"held-within-scope branch ({language})",
    )

held_example_markers = {
    "Korean": ["> **판정:", "달성한 것:", "약속 범위 내 판정:", "별도 고려사항:", "주의:"],
    "English": ["> **Verdict:", "Achieved:", "Verdict within the promise's scope:", "Separate consideration:", "Caution:"],
}

for language, example_text in openai_examples.items():
    assert_order(
        example_text,
        [f"**{label}**" for label in label_sets[language]],
        f"OpenAI held example ({language})",
    )
    assert_order(
        example_text,
        held_example_markers[language],
        f"OpenAI held branch ({language})",
    )
    change_label = f"**{label_sets[language][3]}**"
    in_scope_evidence = example_text.split(change_label, 1)[0]
    adjacent_tokens = ("Codex", "model release", "Model release", "GPT-5.3")
    if any(token in in_scope_evidence for token in adjacent_tokens):
        fail(
            f"OpenAI held example ({language}) imports an adjacent product question "
            "into the in-scope evidence path"
        )

for marker in ("references/diagnosis.md", "references/capability-to-protection.md"):
    if marker not in skill_text:
        fail(f"SKILL.md no longer routes to {marker}")

for phrase in ("진단", "Diagnosis"):
    if phrase not in regression_text:
        fail(f"regression suite does not cover the diagnosis rule ({phrase})")

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
