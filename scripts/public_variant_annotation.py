#!/usr/bin/env python3
"""Retrieve public NCBI variation evidence for JAK2 V617F.

Educational/research use only; not a clinical diagnostic decision tool.
"""

import argparse
import json
import urllib.request

RSID = "rs77375493"
HGVS = "NM_004972.4:c.1849G>T"


def fetch_rsnp(rsid: str) -> dict:
    numeric_id = rsid.removeprefix("rs")
    url = f"https://api.ncbi.nlm.nih.gov/variation/v0/beta/refsnp/{numeric_id}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "JAK2-V617F-Molecular-Diagnosis/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def main() -> None:
    parser = argparse.ArgumentParser(description="Retrieve public JAK2 V617F variant evidence")
    parser.add_argument(
        "--output",
        default="data/processed/jak2_v617f_rs77375493.json",
        help="Output JSON path",
    )
    args = parser.parse_args()

    result = fetch_rsnp(RSID)
    output = {
        "gene": "JAK2",
        "hgvs": HGVS,
        "dbsnp": RSID,
        "source": "NCBI Variation Services",
        "record": result,
    }

    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2)

    print(f"Saved {RSID} public annotation to {args.output}")


if __name__ == "__main__":
    main()
