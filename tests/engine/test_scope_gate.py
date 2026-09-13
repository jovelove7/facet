"""Regression tests for the Facet Engine v0 scope gate.

Each test names the rule it guards. The OpenAI case reproduces a real failure:
two audit runs judged a visual-identity design brief against product history
and reported a break that does not exist.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.scope_gate import (  # noqa: E402
    Basis,
    Claim,
    Evidence,
    GovernedDimension,
    Label,
    ScopeStatus,
    ValidationStatus,
    Verdict,
    check,
)

VISUAL = GovernedDimension(
    dimension="visual_identity",
    basis=Basis.EXPLICIT,
    rationale="The brief addressed an inconsistent visual identity.",
    source_quote="Sam asked us to create one system, one identity.",
)

OPENAI = Claim(id="c1", text="one system, one identity", governs=(VISUAL,))

TYPEFACE = Evidence(
    id="e1",
    claim_id="c1",
    source="https://openai.com/brand/",
    quote="OpenAI Sans replaced the scattered typefaces.",
    surface="visual_identity",
)

CODEX_HISTORY = Evidence(
    id="e2",
    claim_id="c1",
    source="https://help.openai.com/en/articles/20001275/",
    quote="ChatGPT and Codex histories are separate.",
    surface="product_history",
)

UNPLACED = Evidence(
    id="e3",
    claim_id="c1",
    source="https://example.com/review",
    quote="The app feels consistent.",
    surface=None,
)


class ScopeGateTest(unittest.TestCase):
    def test_scope_gate_openai_visual_identity(self):
        # Rule: R2_BREAK_REQUIRES_IN_SCOPE. Real failure, runs 1 and 2 of the OpenAI audit.
        broken = check(OPENAI, [TYPEFACE, CODEX_HISTORY], Verdict("c1", Label.BREAK, ("e2",)))
        self.assertEqual(broken.status, ValidationStatus.INVALID_VERDICT)
        self.assertIn("R2_BREAK_REQUIRES_IN_SCOPE", broken.violations)
        self.assertIn("e2", broken.separate_considerations)

        # The verdict the audit should have reached passes.
        held = check(OPENAI, [TYPEFACE, CODEX_HISTORY], Verdict("c1", Label.HELD, ("e1",)))
        self.assertEqual(held.status, ValidationStatus.VALID)

    def test_scope_gate_surface_overrides_model_label(self):
        # Rule: R1_SURFACE_OUTSIDE_GOVERNS. A model label of IN_SCOPE cannot rescue
        # evidence whose surface the claim does not govern.
        mislabeled = Evidence(
            id="e2",
            claim_id="c1",
            source=CODEX_HISTORY.source,
            quote=CODEX_HISTORY.quote,
            surface="product_history",
            scope_status=ScopeStatus.IN_SCOPE,
        )
        result = check(OPENAI, [mislabeled], Verdict("c1", Label.BREAK, ("e2",)))
        self.assertEqual(result.dispositions["e2"], ScopeStatus.OUT_OF_SCOPE)
        self.assertEqual(result.status, ValidationStatus.INVALID_VERDICT)

    def test_scope_gate_break_requires_in_scope(self):
        # Rule: R2_BREAK_REQUIRES_IN_SCOPE. Unresolved evidence is quarantined.
        result = check(OPENAI, [UNPLACED], Verdict("c1", Label.BREAK, ("e3",)))
        self.assertEqual(result.dispositions["e3"], ScopeStatus.UNRESOLVED_SCOPE)
        self.assertIn("R2_BREAK_REQUIRES_IN_SCOPE", result.violations)

    def test_scope_gate_held_requires_in_scope(self):
        # Rule: R2_HELD_REQUIRES_IN_SCOPE. Out-of-scope good news cannot hold a promise.
        result = check(OPENAI, [CODEX_HISTORY], Verdict("c1", Label.HELD, ("e2",)))
        self.assertIn("R2_HELD_REQUIRES_IN_SCOPE", result.violations)

    def test_scope_gate_out_of_scope_preserved(self):
        # Rule: R3_OUT_OF_SCOPE_PRESERVED. Excluded from the verdict, kept for the reader.
        result = check(OPENAI, [TYPEFACE, CODEX_HISTORY], Verdict("c1", Label.HELD, ("e1",)))
        self.assertEqual(result.separate_considerations, ["e2"])

    def test_scope_gate_explicit_requires_quote(self):
        # Rule: G1_EXPLICIT_REQUIRES_QUOTE.
        unquoted = GovernedDimension("visual_identity", Basis.EXPLICIT, "stated", source_quote="  ")
        claim = Claim(id="c1", text="one system, one identity", governs=(unquoted,))
        result = check(claim, [TYPEFACE], Verdict("c1", Label.HELD, ("e1",)))
        self.assertIn("G1_EXPLICIT_REQUIRES_QUOTE", result.violations)

    def test_scope_gate_inferred_flags_review(self):
        # Rule: G2_INFERRED_FLAGS_REVIEW. Inferred scope is allowed and marked, not blocked.
        inferred = GovernedDimension("visual_identity", Basis.INFERRED, "framed by the brief")
        claim = Claim(id="c1", text="one system, one identity", governs=(inferred,))
        result = check(claim, [TYPEFACE], Verdict("c1", Label.HELD, ("e1",)))
        self.assertEqual(result.status, ValidationStatus.VALID)
        self.assertEqual(result.scope_basis, Basis.INFERRED)
        self.assertTrue(result.scope_review_required)

    def test_scope_gate_mixed_evidence_allows_verdict(self):
        # Rule: R2. One in-scope reference is enough; the others do not invalidate it.
        result = check(
            OPENAI,
            [TYPEFACE, CODEX_HISTORY, UNPLACED],
            Verdict("c1", Label.BREAK, ("e1", "e2", "e3")),
        )
        self.assertEqual(result.status, ValidationStatus.VALID)
        self.assertEqual(result.separate_considerations, ["e2"])

    def test_scope_gate_evidence_belongs_to_claim(self):
        # Rule: R0_EVIDENCE_BELONGS_TO_CLAIM. In-scope evidence from another claim does not count.
        foreign = Evidence("e9", "c2", TYPEFACE.source, TYPEFACE.quote, "visual_identity")
        result = check(OPENAI, [foreign], Verdict("c1", Label.HELD, ("e9",)))
        self.assertIn("R0_EVIDENCE_BELONGS_TO_CLAIM", result.violations)
        self.assertIn("R2_HELD_REQUIRES_IN_SCOPE", result.violations)

    def test_scope_gate_unknown_needs_no_evidence(self):
        # The scope gate never rejects an UNKNOWN verdict.
        result = check(OPENAI, [], Verdict("c1", Label.UNKNOWN, ()))
        self.assertEqual(result.status, ValidationStatus.VALID)


if __name__ == "__main__":
    unittest.main()
