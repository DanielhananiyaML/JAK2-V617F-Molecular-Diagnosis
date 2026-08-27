#!/usr/bin/env python3
"""Reproducible retrieval and summary of public GSE168368 count data.

The dataset is expression data, not a variant-calling dataset. The script
therefore summarizes sample groups and JAK2 expression when the public count
matrix is supplied, without claiming direct detection of JAK2 V617F.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from pathlib import Path

URL = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE168368&file=GSE168368_gene_count_matrix.csv.gz&format=file"
ACCESSION = "GSE168368"
BIOPROJECT = "PRJNA707039"
EXPECTED_SAMPLES = 29


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def download_matrix(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(URL, output)


def summarize(matrix: Path, output: Path) -> None:
    import pandas as pd

    df = pd.read_csv(matrix, compression="gzip")
    sample_columns = [c for c in df.columns if str(c).startswith(("PV", "ET", "NC"))]
    groups = {"PV": 0, "ET": 0, "NC": 0}
    for col in sample_columns:
        for group in groups:
            if str(col).startswith(group):
                groups[group] += 1
                break

    if len(sample_columns) != EXPECTED_SAMPLES:
        raise ValueError(f"Expected {EXPECTED_SAMPLES} sample columns, found {len(sample_columns)}")

    gene_col = df.columns[0]
    result = {
        "accession": ACCESSION,
        "bioproject": BIOPROJECT,
        "matrix": str(matrix),
        "sha256": sha256(matrix),
        "rows": int(len(df)),
        "sample_columns": sample_columns,
        "group_counts": groups,
        "interpretation": "Expression dataset; not a direct JAK2 V617F variant-calling dataset.",
        "gene_identifier_column": str(gene_col),
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--matrix", type=Path, default=Path("data/raw/GSE168368_gene_count_matrix.csv.gz"))
    parser.add_argument("--output", type=Path, default=Path("data/processed/GSE168368_summary.json"))
    args = parser.parse_args()

    if args.download or not args.matrix.exists():
        print(f"Downloading {ACCESSION} processed matrix from NCBI GEO...")
        download_matrix(args.matrix)
    summarize(args.matrix, args.output)


if __name__ == "__main__":
    main()
