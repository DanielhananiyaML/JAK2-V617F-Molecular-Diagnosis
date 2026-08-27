import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from variant_annotation import JAK2_V617F, summarize_variant, validate_variant
from sequence_level_analysis import SequenceAnalysis
from parse_clinvar_evidence import summarize


class TestJAK2Variant(unittest.TestCase):
    def test_canonical_variant(self):
        self.assertEqual(JAK2_V617F.gene, "JAK2")
        self.assertEqual(JAK2_V617F.hgvs_c, "c.1849G>T")
        self.assertEqual(JAK2_V617F.hgvs_p, "p.Val617Phe")
        self.assertEqual(JAK2_V617F.dbsnp, "rs77375493")
        self.assertEqual(JAK2_V617F.grch38_position, 5073770)
        self.assertEqual(validate_variant(JAK2_V617F), [])

    def test_summary_contains_core_identifiers(self):
        summary = summarize_variant(JAK2_V617F)
        for value in ("JAK2", "NM_004972.4", "p.Val617Phe", "rs77375493"):
            self.assertIn(value, summary)

    def test_sequence_consequence(self):
        result = SequenceAnalysis()
        self.assertEqual(result.reference_codon, "GTT")
        self.assertEqual(result.alternate_codon, "TTT")
        self.assertEqual(result.reference_aa, "Val")
        self.assertEqual(result.alternate_aa, "Phe")
        self.assertEqual(result.nucleotide_change, "G>T")

    def test_clinvar_summary_preserves_context(self):
        summary = summarize({"mock": "record"})
        self.assertIn("NM_004972.4:c.1849G>T", summary["variant"])
        self.assertIn("somatic", summary["somatic_context"].lower())
        self.assertIn("disease context", summary["evidence_note"])

    def test_command_line_validation(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "variant_annotation.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("PASS", result.stdout)

    def test_notebook_is_valid_json(self):
        notebook = ROOT / "analysis" / "JAK2_V617F_Analysis.ipynb"
        data = json.loads(notebook.read_text(encoding="utf-8"))
        self.assertEqual(data["nbformat"], 4)
        self.assertIn("cells", data)
        self.assertGreater(len(data["cells"]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
