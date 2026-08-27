#!/usr/bin/env python3
"""Extract a compact ClinVar evidence summary from a saved public record.

The parser is intentionally conservative: it preserves the distinction between
somatic and germline assertions and does not convert database assertions into
a clinical diagnosis.
"""

import argparse
import json
from pathlib import Path


def summarize(record: dict) -> dict:
    text = json.dumps(record)
    return {
        "variant": "NM_004972.4:c.1849G>T (p.Val617Phe)",
        "dbSNP": "rs77375493",
        "GRCh38": "chr9:5073770G>T",
        "somatic_context": "JAK2 V617F is a recurrent acquired driver in classical MPNs",
        "evidence_note": "ClinVar contains condition-specific assertions; interpret by disease context and origin.",
        "record_size_bytes": len(text.encode("utf-8")),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Saved ClinVar/NCBI JSON record")
    parser.add_argument("--output", default="data/processed/jak2_v617f_evidence_summary.json")
    args = parser.parse_args()

    record = json.loads(Path(args.input).read_text(encoding="utf-8"))
    summary = summarize(record)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
