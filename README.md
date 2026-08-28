# JAK2 V617F Molecular Diagnosis

## Molecular Characterization, Diagnostic Interpretation, and Bioinformatics Analysis of the JAK2 V617F Variant in Myeloproliferative Neoplasms

**Author:** Daniel Hananiya  
**Field:** Medical Laboratory Science | Molecular Biology | Molecular Diagnostics | Bioinformatics & Genomics  
**Project Type:** Molecular Hematology / Bioinformatics Portfolio Project  
**Status:** **Final validation completed; reproducible research workflow**  
**Focus:** JAK2 V617F • Myeloproliferative Neoplasms • Molecular Diagnostics • Variant Interpretation • Sequence Analysis

---

## Abstract

The **JAK2 V617F mutation** is a major acquired molecular driver of the classical Philadelphia chromosome-negative myeloproliferative neoplasms (MPNs), particularly **polycythemia vera (PV), essential thrombocythemia (ET), and primary myelofibrosis (PMF)**.

This repository presents a reproducible molecular hematology and bioinformatics case study integrating molecular biology, sequence analysis, public genomic resources, variant interpretation, diagnostic reasoning, automated testing, and scientific documentation.

The focal variant is **JAK2 NM_004972.4:c.1849G>T (p.Val617Phe; V617F)**, linked to **rs77375493** and represented on GRCh38 as **NC_000009.12:g.5073770G>T**. The production analysis engine retrieves the versioned reference transcript from NCBI at runtime, verifies the reference nucleotide at c.1849, extracts the affected codon, introduces the G>T substitution in silico, translates the reference and alternate codons, and confirms the Valine-to-Phenylalanine consequence.

The project is explicitly designed as an **educational/research and professional portfolio workflow, not a validated clinical diagnostic assay**.

> **DNA variant → transcript annotation → codon change → amino-acid consequence → JAK2 signaling dysregulation → MPN molecular context**

---

## Final Validation Status

The final validation layer covers:

- canonical HGVS identity: `NM_004972.4:c.1849G>T`
- protein consequence: `p.Val617Phe`
- canonical codon change: `GTC → TTC`
- dbSNP identifier: `rs77375493`
- GRCh38 genomic representation: `NC_000009.12:g.5073770G>T`
- deterministic sequence-analysis unit tests
- automated GitHub Actions testing
- public-data runtime validation already incorporated into the repository CI workflow
- provenance and limitation documentation
- independent cross-check against current ClinVar and peer-reviewed literature

See [`docs/validation_report.md`](docs/validation_report.md) for the final scientific-safety checklist and evidence trail.

---

## Project Objectives

1. Characterize JAK2 V617F at genomic, transcript, and protein levels.
2. Explain the biological role of JAK2 and the JAK-STAT pathway.
3. Demonstrate sequence-level verification of the c.1849G>T substitution.
4. Integrate public database identifiers and evidence.
5. Establish a reproducible molecular diagnostic workflow.
6. Provide a structured variant-interpretation framework.
7. Demonstrate automated computational quality control.
8. Provide a foundation for future MPN variant-analysis workflows.

---

## Canonical Variant

| Feature | Annotation |
|---|---|
| Gene | **JAK2** |
| Transcript | **NM_004972.4** |
| HGVS cDNA | **NM_004972.4:c.1849G>T** |
| Protein | **p.Val617Phe** |
| Short form | **V617F** |
| dbSNP | **rs77375493** |
| GRCh38 | **NC_000009.12:g.5073770G>T** |
| Variant class | Missense SNV |
| Functional region | JH2 pseudokinase domain |

---

## Repository Workflow

```text
Versioned public reference
          ↓
NCBI RefSeq NM_004972.4
          ↓
Locate c.1849
          ↓
Verify reference G
          ↓
Extract codon c.1849–c.1851
          ↓
Introduce G → T in silico
          ↓
Translate reference / alternate codons
          ↓
Verify p.Val617Phe
          ↓
Variant evidence / interpretation
          ↓
Automated tests + CI
          ↓
Reproducible scientific report
```

---

## Repository Structure

```text
JAK2-V617F-Molecular-Diagnosis/
├── .github/workflows/ci.yml
├── README.md
├── LICENSE
├── CITATION.cff
├── analysis/
│   └── JAK2_V617F_Analysis.ipynb
├── docs/
│   ├── molecular_background.md
│   ├── diagnostic_workflow.md
│   ├── sequence_analysis.md
│   ├── variant_interpretation.md
│   ├── validation_report.md
│   └── JAK2_V617F_Academic_Project_Report.md
├── figures/
│   └── jak2_v617f_sequence_consequence.svg
├── scripts/
│   ├── jak2_v617f_analysis.py
│   ├── public_variant_annotation.py
│   ├── reference_sequence_analysis.py
│   └── sequence_level_analysis.py
└── tests/
    ├── test_jak2_analysis.py
    └── test_reference_sequence_analysis.py
```

---

## Running the Production Sequence Analysis

```bash
python scripts/reference_sequence_analysis.py
```

To save a structured JSON result:

```bash
python scripts/reference_sequence_analysis.py --output results/jak2_v617f_sequence.json
```

The production script retrieves the reference sequence from NCBI rather than storing a copied third-party sequence in the repository. This keeps the workflow traceable to the accession and reduces the risk of maintaining an untracked local reference copy.

### Offline validation

The notebook also contains a clearly labelled deterministic offline fixture for validating the sequence-analysis logic when external network access is unavailable. The fixture is **synthetic test data and is not presented as the NCBI biological reference sequence**.

---

## Running Tests

The deterministic unit tests can be run with:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

GitHub Actions performs automated testing across supported Python versions and includes the repository's public-data runtime validation.

---

## Scientific Interpretation

JAK2 V617F occurs in the JH2 pseudokinase domain and disrupts normal negative regulation of JAK2 kinase activity, contributing to constitutive JAK-STAT signaling. The variant is strongly associated with classical MPNs, especially PV, and is also detected in ET and PMF.

A molecular result must be interpreted with the patient's hematologic phenotype, morphology, clinical findings, assay characteristics, and additional molecular markers where appropriate. Absence of JAK2 V617F does not by itself exclude an MPN.

Database classifications must be interpreted in the correct **variant-origin and disease context**. ClinVar aggregate germline classifications should not be presented as equivalent to a somatic MPN oncogenicity assertion.

---

## Reproducibility and Quality Assurance

The project records:

- Reference transcript/accession
- Genome assembly
- HGVS representation
- Database identifiers
- Analysis parameters
- Python scripts
- Jupyter analysis
- Automated tests
- GitHub Actions workflow
- Scientific documentation
- Validation and limitation statements

The live NCBI retrieval step is intentionally separated from deterministic unit tests so that the core sequence logic can be tested without network dependence.

---

## Limitations and Scientific Safety

This project is **not a validated clinical diagnostic assay**. It does not establish a patient's disease status and must not be used to make treatment or patient-management decisions.

Public database annotations may change. Variant interpretation depends on reference versions, assay methodology, disease context, specimen type, allele burden, and clinical evidence. Computational verification of a sequence consequence does not replace laboratory validation or clinical judgment.

For clinical use, testing should be performed using appropriately validated laboratory methods and interpreted within current professional diagnostic frameworks.

---

## Academic Project Report

A full academic-style report covering the background, objectives, methodology, sequence analysis, diagnostic workflow, interpretation, reproducibility, limitations, conclusions, and references is available at:

`docs/JAK2_V617F_Academic_Project_Report.md`

---

## Citation

**Hananiya, D. (2026). JAK2 V617F Molecular Diagnosis: Molecular Characterization, Diagnostic Interpretation, and Bioinformatics Analysis of the JAK2 V617F Variant in Myeloproliferative Neoplasms. GitHub.**

See `CITATION.cff` for machine-readable citation metadata.

---

## Author

**Daniel Hananiya**  
Medical Laboratory Scientist | Molecular Biology Researcher | Molecular Diagnostics | Bioinformatics & Genomics

### Project Philosophy

> **From the laboratory bench to the genome, and from genomic data to biological meaning.**

---

## Disclaimer

This repository is intended for **educational, research, and professional portfolio purposes**. It does not provide medical advice, establish a clinical diagnosis, or replace validated laboratory procedures, professional guidelines, or qualified clinical interpretation.
