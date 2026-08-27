#!/usr/bin/env python3
"""Reproducible retrieval and summary of public GSE168368 count data.

GSE168368 is an expression-profiling study with 29 GEO samples. The
processed count matrix is checked against the complete Series record.
The dataset is expression data, not a variant-calling dataset.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import urllib.request
from pathlib import Path

URL = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE168368&file=GSE168368_gene_count_matrix.csv.gz&format=file"
ACCESSION = "GSE168368"
BIOPROJECT = "PRJNA707039"
SERIES_SAMPLE_COUNT = 29
SERIES_GROUP_COUNTS = {"PV": 9, "ET": 12, "NC": 8}

# Common identifiers for the human JAK2 gene. The processed GEO matrix may
# use Ensembl IDs, Entrez IDs, or gene symbols, so matching must not assume
# that the first column contains HGNC symbols.
JAK2_ENSEMBL = "ENSG00000096968"
JAK2_ENTREZ = "3717"
JAK2_SYMBOL = "JAK2"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def download_matrix(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(URL, output)


def classify_sample(name: str) -> str | None:
    name = str(name).upper()
    for group in ("PV", "ET", "NC"):
        if name.startswith(group):
            return group
    return None


def normalize_gene_id(value: object) -> str:
    """Normalize common versioned Ensembl identifiers for matching."""
    value = str(value).strip().upper()
    return re.sub(r"\.\d+$", "", value)


def is_jak2_identifier(value: object) -> bool:
    normalized = normalize_gene_id(value)
    return normalized in {JAK2_ENSEMBL, JAK2_ENTREZ, JAK2_SYMBOL}


def summarize(matrix: Path, output: Path) -> None:
    import pandas as pd

    df = pd.read_csv(matrix, compression="gzip")
    sample_columns = [c for c in df.columns if classify_sample(c)]
    groups = {"PV": 0, "ET": 0, "NC": 0}
    for col in sample_columns:
        group = classify_sample(col)
        if group is not None:
            groups[group] += 1

    gene_col = df.columns[0]
    gene_values = df[gene_col].astype(str)
    jak2_rows = df.index[gene_values.map(is_jak2_identifier)].tolist()

    result = {
        "accession": ACCESSION,
        "bioproject": BIOPROJECT,
        "series_sample_count": SERIES_SAMPLE_COUNT,
        "series_group_counts": SERIES_GROUP_COUNTS,
        "matrix": str(matrix),
        "sha256": sha256(matrix),
        "rows": int(len(df)),
        "sample_columns": [str(c) for c in sample_columns],
        "matrix_sample_count": len(sample_columns),
        "matrix_group_counts": groups,
        "gene_identifier_column": str(gene_col),
        "jak2_identifiers_checked": [JAK2_SYMBOL, JAK2_ENTREZ, JAK2_ENSEMBL],
        "jak2_row_count": len(jak2_rows),
        "jak2_expression": {},
        "interpretation": (
            "Expression dataset; not a direct JAK2 V617F variant-calling dataset. "
            "Series-level sample count and processed-matrix sample count are "
            "reported separately. JAK2 expression is extracted by matching "
            "common human Ensembl, Entrez, or HGNC identifiers."
        ),
    }

    if len(jak2_rows) == 1:
        row = df.loc[jak2_rows[0]]
        result["jak2_expression"] = {
            str(col): float(row[col]) for col in sample_columns
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
