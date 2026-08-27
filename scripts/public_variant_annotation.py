#!/usr/bin/env python3
"""Retrieve public ClinVar evidence for JAK2 V617F.

This script uses NCBI's public ClinVar API and writes a compact JSON summary.
Educational/research use only; not a clinical diagnostic decision tool.
"""

import argparse
import json
import urllib.parse
import urllib.request

VARIANT = "NM_004972.4:c.1849G>T"


def fetch_clinvar(hgvs: str) -> dict:
    term = urllib.parse.quote(hgvs, safe="")
    url = (
        "https://api.ncbi.nlm.nih.gov/variation/v0/beta/refsnp/search?"
        f"q={term}"
    )
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "JAK2-V617F-Molecular-Diagnosis/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/processed/jak2_v617f_public_annotation.json")
    args = parser.parse_args()

    result = fetch_clinvar(VARIANT)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
    print(f"Saved public annotation to {args.output}")


if __name__ == "__main__":
    main()
