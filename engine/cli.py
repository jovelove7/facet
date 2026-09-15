"""Command line entry for the Facet Reference Engine.

    facet check audit.json

Reads an audit record, runs the scope gate, and prints the result as JSON.
Exit status: 0 valid, 1 invalid verdict, 2 unreadable record.
Fields the engine does not use, such as audit metadata, are ignored.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Optional

from .scope_gate import (
    ENGINE_VERSION,
    Basis,
    Claim,
    Evidence,
    GovernedSurface,
    Label,
    ScopeStatus,
    ValidationStatus,
    Verdict,
    check,
)


def load(record: dict) -> tuple[Claim, list[Evidence], Verdict]:
    c = record["claim"]
    claim = Claim(
        id=c["id"],
        text=c["text"],
        governs=tuple(
            GovernedSurface(
                surface=g["surface"],
                basis=Basis(g["basis"]),
                rationale=g["rationale"],
                source_quote=g.get("source_quote"),
            )
            for g in c["governs"]
        ),
    )
    evidence = [
        Evidence(
            id=e["id"],
            claim_id=e["claim_id"],
            source=e["source"],
            quote=e["quote"],
            surface=e.get("surface"),
            scope_status=ScopeStatus(e["scope_status"]) if e.get("scope_status") else None,
        )
        for e in record.get("evidence", [])
    ]
    v = record["verdict"]
    verdict = Verdict(claim_id=v["claim_id"], label=Label(v["label"]), evidence_ids=tuple(v["evidence_ids"]))
    return claim, evidence, verdict


def run(record: dict) -> dict:
    return {"engine_version": ENGINE_VERSION, **check(*load(record)).to_dict()}


def dumps(output: dict) -> str:
    # Stable bytes, so two runs over the same record can be compared directly.
    return json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="facet", description="Facet Reference Engine")
    commands = parser.add_subparsers(dest="command", required=True)
    check_cmd = commands.add_parser("check", help="validate an audit record against the scope gate")
    check_cmd.add_argument("audit", help="path to an audit JSON record, or - for stdin")
    args = parser.parse_args(argv)

    try:
        if args.audit == "-":
            text = sys.stdin.read()
        else:
            with open(args.audit, encoding="utf-8") as f:
                text = f.read()
        output = run(json.loads(text))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"facet: cannot read audit record: {exc}", file=sys.stderr)
        return 2

    sys.stdout.write(dumps(output))
    return 0 if output["status"] == ValidationStatus.VALID.value else 1


if __name__ == "__main__":
    sys.exit(main())
