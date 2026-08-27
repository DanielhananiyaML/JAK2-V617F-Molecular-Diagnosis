#!/usr/bin/env python3
"""JAK2 V617F reference annotation and validation utility.

This script provides a small, reproducible starting point for the project.
It does not perform clinical variant calling or clinical diagnosis.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Variant:
    gene: str
    transcript: str
    hgvs_c: str
    hgvs_p: str
    dbsnp: str
    chromosome: str
    grch38_position: int
    reference: str
    alternate: str


JAK2_V617F = Variant(
    gene="JAK2",
    transcript="NM_004972.4",
    hgvs_c="c.1849G>T",
    hgvs_p="p.Val617Phe",
    dbsnp="rs77375493",
    chromosome="9",
    grch38_position=5073770,
    reference="G",
    alternate="T",
)


def summarize_variant(variant: Variant) -> str:
    """Return a human-readable summary of the variant."""
    return (
        f"Gene: {variant.gene}\n"
        f"Transcript: {variant.transcript}\n"
        f"HGVS: {variant.transcript}:{variant.hgvs_c}\n"
        f"Protein: {variant.hgvs_p}\n"
        f"dbSNP: {variant.dbsnp}\n"
        f"GRCh38: chr{variant.chromosome}:{variant.grch38_position} "
        f"{variant.reference}>{variant.alternate}"
    )


def validate_variant(variant: Variant) -> list[str]:
    """Run basic internal consistency checks."""
    errors = []
    if variant.gene != "JAK2":
        errors.append("Unexpected gene")
    if variant.hgvs_c != "c.1849G>T":
        errors.append("Unexpected HGVS cDNA notation")
    if variant.hgvs_p != "p.Val617Phe":
        errors.append("Unexpected protein consequence")
    if (variant.reference, variant.alternate) != ("G", "T"):
        errors.append("Unexpected reference/alternate allele")
    return errors


if __name__ == "__main__":
    problems = validate_variant(JAK2_V617F)
    if problems:
        raise SystemExit("Validation failed: " + "; ".join(problems))

    print("JAK2 V617F variant validation: PASS")
    print("-" * 42)
    print(summarize_variant(JAK2_V617F))
