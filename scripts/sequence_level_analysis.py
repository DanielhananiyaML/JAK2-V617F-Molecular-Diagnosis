#!/usr/bin/env python3
"""Sequence-level demonstration of the JAK2 V617F nucleotide consequence.

This script uses the codon-level representation to demonstrate how a single
G>T substitution changes the encoded amino acid. It is intentionally small,
deterministic, and suitable for educational/research reproducibility.
"""

from dataclasses import dataclass
import argparse
import csv

CODON_TABLE = {
    "GTT": "Val", "GTC": "Val", "GTA": "Val", "GTG": "Val",
    "TTT": "Phe", "TTC": "Phe",
}


@dataclass(frozen=True)
class SequenceAnalysis:
    gene: str = "JAK2"
    transcript: str = "NM_004972.4"
    protein_position: int = 617
    reference_codon: str = "GTT"
    alternate_codon: str = "TTT"

    @property
    def reference_aa(self) -> str:
        return CODON_TABLE[self.reference_codon]

    @property
    def alternate_aa(self) -> str:
        return CODON_TABLE[self.alternate_codon]

    @property
    def nucleotide_change(self) -> str:
        return f"{self.reference_codon[0]}>{self.alternate_codon[0]}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze the JAK2 V617F codon change")
    parser.add_argument("-o", "--output", help="Optional CSV output path")
    args = parser.parse_args()

    result = SequenceAnalysis()
    assert result.reference_aa == "Val"
    assert result.alternate_aa == "Phe"
    assert result.nucleotide_change == "G>T"

    record = {
        "gene": result.gene,
        "transcript": result.transcript,
        "protein_position": result.protein_position,
        "reference_codon": result.reference_codon,
        "alternate_codon": result.alternate_codon,
        "reference_amino_acid": result.reference_aa,
        "alternate_amino_acid": result.alternate_aa,
        "nucleotide_change": result.nucleotide_change,
        "protein_change": f"p.{result.reference_aa}{result.protein_position}{result.alternate_aa}",
    }

    if args.output:
        with open(args.output, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=record.keys())
            writer.writeheader()
            writer.writerow(record)
    else:
        print("JAK2 V617F sequence-level analysis")
        for key, value in record.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
