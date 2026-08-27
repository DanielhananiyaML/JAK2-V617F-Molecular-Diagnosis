#!/usr/bin/env python3
"""Retrieve NM_004972.4 and verify the JAK2 V617F sequence consequence.

The script uses the NCBI E-utilities endpoint at runtime rather than storing a
third-party copy of the reference sequence in the repository. It extracts the
coding sequence around codon 617, introduces the c.1849G>T substitution, and
translates the affected codon.

Educational/research workflow; not a clinical diagnostic assay.
"""

from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request

ACCESSION = "NM_004972.4"
CODING_POSITION = 1849  # HGVS c.1849; 1-based coding DNA coordinate
EXPECTED_REF = "G"
EXPECTED_ALT = "T"
EXPECTED_CODON_POSITION = 617

# Standard genetic code for the codons used in this analysis.
CODON_TABLE = {
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TTT": "F", "TTC": "F",
}


def fetch_fasta(accession: str = ACCESSION) -> str:
    """Fetch an NCBI RefSeq record as FASTA."""
    params = urllib.parse.urlencode({
        "db": "nuccore",
        "id": accession,
        "rettype": "fasta",
        "retmode": "text",
    })
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?{params}"
    request = urllib.request.Request(url, headers={"User-Agent": "JAK2-V617F-Molecular-Diagnosis/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_fasta(text: str) -> str:
    """Return sequence characters from a FASTA document."""
    lines = [line.strip() for line in text.splitlines() if not line.startswith(">")]
    sequence = "".join(lines).upper()
    if not sequence:
        raise ValueError("No sequence was returned by NCBI.")
    return sequence


def analyze_codon(sequence: str) -> dict[str, object]:
    """Analyze the nucleotide at c.1849 and its affected codon.

    NM_004972.4 c.1849 is coding position 1849. The codon is positions
    c.1849-c.1851, so the 0-based Python slice starts at 1848.
    """
    if len(sequence) < CODING_POSITION + 2:
        raise ValueError("Reference sequence is unexpectedly short for c.1849.")

    idx = CODING_POSITION - 1
    reference_base = sequence[idx]
    codon = sequence[idx:idx + 3]
    if reference_base != EXPECTED_REF:
        raise ValueError(
            f"Reference mismatch at c.{CODING_POSITION}: expected {EXPECTED_REF}, "
            f"observed {reference_base}."
        )
    if len(codon) != 3:
        raise ValueError("Could not extract a complete codon.")
    if codon not in CODON_TABLE:
        raise ValueError(f"Unexpected reference codon at c.1849: {codon}")

    mutant_codon = EXPECTED_ALT + codon[1:]
    if mutant_codon not in CODON_TABLE:
        raise ValueError(f"Unexpected mutant codon: {mutant_codon}")

    return {
        "accession": ACCESSION,
        "hgvs_c": f"{ACCESSION}:c.{CODING_POSITION}{EXPECTED_REF}>{EXPECTED_ALT}",
        "protein_position": EXPECTED_CODON_POSITION,
        "reference_codon": codon,
        "alternate_codon": mutant_codon,
        "reference_amino_acid": CODON_TABLE[codon],
        "alternate_amino_acid": CODON_TABLE[mutant_codon],
        "hgvs_p": "p.Val617Phe",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify JAK2 V617F from NM_004972.4")
    parser.add_argument("--output", help="Optional JSON output path")
    args = parser.parse_args()

    fasta = fetch_fasta()
    sequence = parse_fasta(fasta)
    result = analyze_codon(sequence)

    print(json.dumps(result, indent=2))
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2)
            handle.write("\n")


if __name__ == "__main__":
    main()
