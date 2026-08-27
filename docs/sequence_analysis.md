# Sequence-Level JAK2 V617F Analysis

## Purpose

This workflow moves the project from static variant metadata to direct sequence-level verification of the canonical JAK2 V617F consequence.

The reference transcript is **NM_004972.4**, which NCBI identifies as the RefSeq mRNA for human JAK2 transcript variant 1. citeturn0search1

The target variant is **NM_004972.4:c.1849G>T**, producing **p.Val617Phe (V617F)**. ClinVar reports the corresponding GRCh38 genomic representation as **NC_000009.12:g.5073770G>T** and links the variant to **rs77375493**. citeturn0search0turn0search2

## Computational logic

```text
NM_004972.4
     │
     ▼
Fetch reference FASTA
     │
     ▼
Locate coding position c.1849
     │
     ▼
Verify reference base = G
     │
     ▼
Extract c.1849–c.1851 codon
     │
     ▼
Introduce G → T
     │
     ▼
Translate reference and alternate codons
     │
     ▼
Verify Valine → Phenylalanine
     │
     ▼
p.Val617Phe
```

## Reproducibility

Run:

```bash
python scripts/reference_sequence_analysis.py
```

or write a structured JSON result:

```bash
python scripts/reference_sequence_analysis.py --output results/jak2_v617f_sequence.json
```

The runtime sequence is retrieved from NCBI rather than storing a copied reference sequence in the repository. This keeps the project traceable to the RefSeq accession and avoids silently maintaining a stale local copy.

## Biological interpretation

ClinVar describes JAK2 V617F as a somatic G-to-T transversion producing a Val617Phe substitution in the negative-regulatory JH2 domain and associates it with classical myeloproliferative neoplasms. citeturn0search7

The computational sequence analysis therefore establishes the chain:

**reference nucleotide → variant nucleotide → codon → amino acid → protein consequence**.

It does **not** by itself establish a clinical diagnosis. Molecular findings must be interpreted with hematologic, morphologic, clinical, and additional molecular evidence.

## Testing strategy

The repository includes offline unit tests using a synthetic sequence fragment so that the core codon logic can be tested without depending on network availability. The live NCBI retrieval step is intentionally separated from deterministic unit testing.
