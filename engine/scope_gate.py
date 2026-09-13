"""Facet Engine v0: scope gate.

Scope Gate decides only whether a piece of evidence is eligible to take part in
a claim's verdict. It does not decide whether the evidence was interpreted
correctly.

The model interprets. This module checks that the interpretation stays inside
the rules. It never produces a verdict of its own; it accepts or rejects one.

Rules implemented here are defined in:
- skills/facet-core/SKILL.md, Workflow step 1 (promise boundary) and step 5 (scope gate)
- skills/facet-core/references/diagnosis.md, "When the promise held" and "Adjacent promises"
- skills/facet-core/references/evidence-protocol.md, "Locating supplied wording"
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Basis(str, Enum):
    EXPLICIT = "explicit"
    INFERRED = "inferred"


class ScopeStatus(str, Enum):
    IN_SCOPE = "IN_SCOPE"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"
    UNRESOLVED_SCOPE = "UNRESOLVED_SCOPE"


class Label(str, Enum):
    HELD = "HELD"
    BREAK = "BREAK"
    UNKNOWN = "UNKNOWN"


class ValidationStatus(str, Enum):
    VALID = "VALID"
    INVALID_VERDICT = "INVALID_VERDICT"


@dataclass(frozen=True)
class GovernedDimension:
    dimension: str
    basis: Basis
    rationale: str
    source_quote: Optional[str] = None


@dataclass(frozen=True)
class Claim:
    id: str
    text: str
    governs: tuple[GovernedDimension, ...]


@dataclass(frozen=True)
class Evidence:
    id: str
    claim_id: str
    source: str
    quote: str
    surface: Optional[str]
    # Proposed by the model. Only UNRESOLVED_SCOPE is honored as given;
    # IN_SCOPE and OUT_OF_SCOPE are recomputed from surface and governs (R1).
    scope_status: Optional[ScopeStatus] = None


@dataclass(frozen=True)
class Verdict:
    claim_id: str
    label: Label
    evidence_ids: tuple[str, ...]


@dataclass
class ValidationResult:
    status: ValidationStatus
    violations: list[str]
    dispositions: dict[str, ScopeStatus]
    separate_considerations: list[str]
    scope_basis: Basis
    scope_review_required: bool

    def to_dict(self) -> dict:
        return {
            "status": self.status.value,
            "violations": self.violations,
            "dispositions": {k: v.value for k, v in self.dispositions.items()},
            "separate_considerations": self.separate_considerations,
            "scope_basis": self.scope_basis.value,
            "scope_review_required": self.scope_review_required,
        }


def disposition(claim: Claim, evidence: Evidence) -> ScopeStatus:
    # Rule: R1_SURFACE_OUTSIDE_GOVERNS
    # Source: SKILL.md step 5, "does the wording actually govern the surface being judged?"
    if evidence.scope_status == ScopeStatus.UNRESOLVED_SCOPE or evidence.surface is None:
        return ScopeStatus.UNRESOLVED_SCOPE
    governed = {g.dimension for g in claim.governs}
    return ScopeStatus.IN_SCOPE if evidence.surface in governed else ScopeStatus.OUT_OF_SCOPE


def check(claim: Claim, evidence: list[Evidence], verdict: Verdict) -> ValidationResult:
    violations: list[str] = []

    # Rule: G1_EXPLICIT_REQUIRES_QUOTE
    # Source: references/evidence-protocol.md, "Locating supplied wording"
    for g in claim.governs:
        if g.basis == Basis.EXPLICIT and not (g.source_quote or "").strip():
            violations.append("G1_EXPLICIT_REQUIRES_QUOTE")

    # Rule: R0_EVIDENCE_BELONGS_TO_CLAIM
    # A verdict may cite only evidence recorded against the same claim.
    by_id = {e.id: e for e in evidence}
    if verdict.claim_id != claim.id:
        violations.append("R0_VERDICT_CLAIM_MISMATCH")
    for eid in verdict.evidence_ids:
        e = by_id.get(eid)
        if e is None or e.claim_id != claim.id:
            violations.append("R0_EVIDENCE_BELONGS_TO_CLAIM")

    dispositions = {e.id: disposition(claim, e) for e in evidence if e.claim_id == claim.id}

    # Rule: R2_HELD_REQUIRES_IN_SCOPE, R2_BREAK_REQUIRES_IN_SCOPE
    # Source: SKILL.md step 5; references/diagnosis.md, "Adjacent promises"
    # OUT_OF_SCOPE and UNRESOLVED_SCOPE never count toward a verdict.
    if verdict.label in (Label.HELD, Label.BREAK):
        if not any(dispositions.get(eid) == ScopeStatus.IN_SCOPE for eid in verdict.evidence_ids):
            violations.append(f"R2_{verdict.label.value}_REQUIRES_IN_SCOPE")

    # Rule: R3_OUT_OF_SCOPE_PRESERVED
    # Source: references/diagnosis.md, "Adjacent promises"
    separate = [eid for eid, d in dispositions.items() if d == ScopeStatus.OUT_OF_SCOPE]

    # Rule: G2_INFERRED_FLAGS_REVIEW
    # Inferred scope is allowed; it is marked for review, not blocked.
    inferred = any(g.basis == Basis.INFERRED for g in claim.governs)

    violations = list(dict.fromkeys(violations))
    return ValidationResult(
        status=ValidationStatus.INVALID_VERDICT if violations else ValidationStatus.VALID,
        violations=violations,
        dispositions=dispositions,
        separate_considerations=separate,
        scope_basis=Basis.INFERRED if inferred else Basis.EXPLICIT,
        scope_review_required=inferred,
    )
