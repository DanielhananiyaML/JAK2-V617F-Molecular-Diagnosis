import unittest
from unittest.mock import patch

from scripts.reference_sequence_analysis import analyze_codon, parse_fasta


class TestReferenceSequenceAnalysis(unittest.TestCase):
    def test_parse_fasta(self):
        self.assertEqual(parse_fasta(">NM_004972.4\nACGT\nAC\n"), "ACGTAC")

    def test_v617f_consequence(self):
        # Synthetic sequence fragment positioned so c.1849 is the first base
        # of the affected codon. This avoids requiring network access in CI.
        sequence = "A" * 1848 + "GTT" + "A" * 10
        result = analyze_codon(sequence)
        self.assertEqual(result["reference_codon"], "GTT")
        self.assertEqual(result["alternate_codon"], "TTT")
        self.assertEqual(result["reference_amino_acid"], "V")
        self.assertEqual(result["alternate_amino_acid"], "F")
        self.assertEqual(result["hgvs_c"], "NM_004972.4:c.1849G>T")
        self.assertEqual(result["hgvs_p"], "p.Val617Phe")

    def test_reference_mismatch_is_rejected(self):
        sequence = "A" * 1848 + "CTT" + "A" * 10
        with self.assertRaises(ValueError):
            analyze_codon(sequence)


if __name__ == "__main__":
    unittest.main()
