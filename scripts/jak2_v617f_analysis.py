#!/usr/bin/env python3
"""Create a reproducible summary of the canonical JAK2 V617F variant.

Educational/research utility only; this is not a clinical diagnostic assay.
"""

from dataclasses import asdict, dataclass
import argparse
import csv


@dataclass(frozen=True)
class Variant:
    gene: str = "JAK2"
    transcript: str = "NM_004972.4"
    hgvs_c: str = "NM_004972.4:c.1849G>T"
    hgvs_p: str = "p.Val617Phe"
    dbsnp: str = "rs77375493"
    assembly: str = "GRCh38"
    genomic_hgvs: str = "NC_000009.12:g.5073770G>T"
    functional_region: str = "JH2 pseudokinase domain"


def validate(v: Variant) -> None:
    """Validate the expected canonical identifiers used by this project."""
    assert v.gene == "JAK2"
    assert v.hgvs_c.endswith("c.1849G>T")
    assert v.hgvs_p == "p.Val617Phe"
    assert v.dbsnp == "rs77375493"
    assert v.assembly == "GRCh38"
    assert v.genomic_hgvs.endswith("g.5073770G>T")


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize JAK2 V617F")
    parser.add_argument("-o", "--output", help="Optional CSV output path")
    args = parser.parse_args()

    variant = Variant()
    validate(variant)
    record = asdict(variant)

    if args.output:
        with open(args.output, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=record.keys())
            writer.writeheader()
            writer.writerow(record)
    else:
        for key, value in record.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
