# JAK2 V617F Molecular Diagnosis

## Molecular Characterization, Sequence-Level Verification, Variant Interpretation, and Bioinformatics Workflow for a Major Myeloproliferative Neoplasm Driver Variant

**Author:** Daniel Hananiya  
**Project Area:** Medical Laboratory Science • Molecular Biology • Hematology • Bioinformatics • Molecular Diagnostics  
**Project Type:** Academic-Style Computational Molecular Hematology Project  
**Date:** August 2026

---

## Abstract

The JAK2 V617F variant is a recurrent acquired molecular alteration in the classical Philadelphia chromosome-negative myeloproliferative neoplasms (MPNs), particularly polycythemia vera (PV), essential thrombocythemia (ET), and primary myelofibrosis (PMF). This project develops a reproducible molecular and bioinformatics framework for characterizing the variant from nucleotide sequence through protein consequence and clinical context.

The focal variant is represented as **NM_004972.4:c.1849G>T**, producing **p.Val617Phe (V617F)** and corresponding to **rs77375493**. The GRCh38 genomic representation is **NC_000009.12:g.5073770G>T**. The workflow combines molecular hematology background, HGVS nomenclature, reference-sequence retrieval, codon-level analysis, in-silico mutation modeling, translation, public database annotation, diagnostic workflow design, variant interpretation, automated testing, and reproducibility documentation.

The central computational experiment retrieves the JAK2 RefSeq transcript at runtime, identifies coding position c.1849, verifies the reference nucleotide, extracts the affected codon, introduces the G>T substitution, translates the reference and alternate codons, and verifies the expected Valine-to-Phenylalanine change. The project demonstrates how a single nucleotide substitution can be followed through a transparent computational chain into biologically and clinically meaningful interpretation.

The repository is intended as an educational, research, and professional portfolio artifact. It is not a validated clinical diagnostic assay and does not replace laboratory validation or clinical judgment.

**Keywords:** JAK2 V617F, myeloproliferative neoplasms, molecular diagnostics, bioinformatics, hematology, sequence analysis, variant annotation, JAK-STAT, genomics.

---

# 1. Introduction

Myeloproliferative neoplasms are clonal myeloid disorders characterized by persistent proliferation of hematopoietic cells. The classical BCR::ABL1-negative MPNs include PV, ET, and PMF. Their molecular pathogenesis is strongly linked to dysregulation of cytokine signaling, particularly the JAK-STAT pathway.

JAK2 encodes a non-receptor tyrosine kinase involved in signaling downstream of multiple hematopoietic cytokine receptors. A recurrent somatic mutation affecting JAK2, commonly called V617F, alters a critical regulatory region and promotes inappropriate kinase signaling. Its discovery provided an important molecular bridge between abnormal hematopoiesis and the underlying genetic lesion.

This project uses JAK2 V617F as a focused case study in molecular diagnostics and computational biology. Rather than treating the mutation as a static database entry, the project traces it through several analytical levels:

**genomic representation → transcript representation → nucleotide substitution → codon → amino-acid consequence → functional interpretation → diagnostic context.**

---

# 2. Background

## 2.1 JAK-STAT Signaling

The JAK-STAT pathway transduces signals from extracellular cytokines and growth factors into regulated gene expression. Ligand binding promotes receptor-associated JAK activation, phosphorylation of receptor and STAT proteins, STAT dimerization, nuclear translocation, and transcriptional regulation.

JAK2 contains multiple structural domains. The JH2 pseudokinase domain contributes to autoinhibitory regulation of the adjacent JH1 kinase domain. The V617F substitution lies in the JH2 region and interferes with normal regulatory control.

## 2.2 JAK2 V617F

The canonical transcript representation investigated in this project is:

`NM_004972.4:c.1849G>T`

The corresponding protein consequence is:

`p.Val617Phe`

or simply:

`V617F`

The variant is a missense single-nucleotide substitution. The reference amino acid is valine and the alternate amino acid is phenylalanine.

## 2.3 Disease Context

JAK2 V617F is particularly important in PV and is also found in substantial subsets of ET and PMF. However, molecular diagnosis of an MPN is not based on the mutation alone. Blood counts, morphology, clinical features, bone marrow findings, and alternative molecular drivers such as CALR and MPL may be relevant.

---

# 3. Aim and Objectives

## 3.1 Aim

To develop and document a reproducible molecular and bioinformatics workflow for characterizing and interpreting the JAK2 V617F variant in the context of classical myeloproliferative neoplasms.

## 3.2 Objectives

1. Describe the biological function of JAK2 and the JAK-STAT pathway.
2. Characterize JAK2 V617F at genomic, transcript, nucleotide, codon, and protein levels.
3. Verify the c.1849G>T sequence consequence computationally.
4. Integrate public variant identifiers and database evidence.
5. Develop a molecular diagnostic workflow for JAK2 V617F.
6. Establish a structured variant interpretation framework.
7. Implement reproducible Python scripts and Jupyter analysis.
8. Implement deterministic automated tests and continuous integration.
9. Document limitations and appropriate clinical-context requirements.
10. Establish a foundation for future multi-gene MPN and NGS workflows.

---

# 4. Materials and Computational Resources

The project uses public reference and variant resources and open computational tooling.

### Reference and evidence resources

- NCBI RefSeq / NCBI E-utilities
- ClinVar
- dbSNP
- Ensembl
- UniProt
- PubMed
- COSMIC where appropriate

### Computational tools

- Python 3
- Jupyter Notebook
- Pandas
- Git
- GitHub
- GitHub Actions
- Standard Python library modules for HTTP retrieval, parsing, JSON output, and testing

### Reference variant

| Attribute | Value |
|---|---|
| Gene | JAK2 |
| Transcript | NM_004972.4 |
| HGVS c. | NM_004972.4:c.1849G>T |
| HGVS p. | p.Val617Phe |
| dbSNP | rs77375493 |
| Genome | GRCh38 |
| Genomic HGVS | NC_000009.12:g.5073770G>T |
| Domain | JH2 pseudokinase domain |

---

# 5. Methodology

## 5.1 Reference Sequence Retrieval

The sequence analysis uses NCBI E-utilities to retrieve the JAK2 RefSeq transcript **NM_004972.4** at runtime. The repository deliberately avoids silently maintaining a copied third-party reference sequence.

The workflow is:

```text
NM_004972.4
     ↓
NCBI EFetch
     ↓
FASTA
     ↓
Sequence parsing
     ↓
Coding position 1849
```

## 5.2 Sequence Parsing

FASTA headers are removed and sequence lines are concatenated. The resulting sequence is normalized to uppercase. The program verifies that a sequence has been returned and that it is long enough to contain the affected codon.

## 5.3 Codon Extraction

HGVS c.1849 represents the first nucleotide of codon 617. Therefore, the affected codon occupies c.1849–c.1851. In Python's zero-based indexing, the extraction begins at index 1848.

The program verifies that the reference base at c.1849 is G.

## 5.4 In-Silico Variant Introduction

The alternate allele T is introduced at the first position of the affected codon. This produces the alternate codon while leaving the remaining two nucleotides unchanged.

Conceptually:

```text
Reference: GTT → Valine (V)
Variant:   TTT → Phenylalanine (F)
```

The exact codon returned by the current reference sequence is treated as the authoritative computational input; the expected protein consequence is then checked against p.Val617Phe.

## 5.5 Translation

The affected reference and alternate codons are translated using the standard genetic code. The analysis confirms the expected amino-acid substitution from valine to phenylalanine.

## 5.6 Public Variant Annotation

The project records the variant's canonical identifiers and provides a public-database annotation workflow. Database evidence should always be interpreted according to the relevant disease and somatic/germline context.

## 5.7 Variant Interpretation

The interpretation framework integrates:

- molecular identity;
- predicted molecular consequence;
- known biological function;
- disease association;
- laboratory phenotype;
- morphology;
- clinical context; and
- additional molecular findings.

The workflow deliberately avoids presenting a single database classification as an unconditional clinical diagnosis.

---

# 6. Molecular Diagnostic Workflow

A laboratory workflow for suspected MPN may be conceptualized as:

```text
Clinical suspicion
       ↓
CBC / hematologic assessment
       ↓
Peripheral blood ± bone marrow evaluation
       ↓
DNA extraction
       ↓
Targeted JAK2 testing
       ↓
PCR / allele-specific PCR / sequencing / NGS
       ↓
Quality control
       ↓
Variant detection
       ↓
JAK2 V617F verification
       ↓
Molecular annotation
       ↓
Integrated clinical interpretation
```

The choice of assay depends on the laboratory's validated methodology, sensitivity requirements, specimen type, and clinical indication.

---

# 7. Bioinformatics Workflow

```text
Reference / variant data
        ↓
Quality control
        ↓
Reference alignment or targeted sequence analysis
        ↓
Variant detection
        ↓
HGVS representation
        ↓
Database annotation
        ↓
Functional interpretation
        ↓
Clinical contextualization
        ↓
Report / research output
```

For this project, the sequence-level component is intentionally focused on a single well-characterized variant to make every computational step transparent.

---

# 8. Software Architecture

The repository is organized into separate layers:

```text
Documentation
     │
     ├── molecular background
     ├── diagnostic workflow
     ├── sequence analysis
     └── variant interpretation

Analysis
     │
     └── Jupyter notebook

Scripts
     │
     ├── variant summary
     ├── public annotation
     ├── sequence analysis
     └── reference-sequence verification

Tests
     │
     └── deterministic unit tests

CI
     │
     └── GitHub Actions
```

This separation improves maintainability and makes it easier to extend the project to additional variants and genes.

---

# 9. Results and Expected Computational Findings

The project establishes the expected canonical relationship:

```text
JAK2
 ↓
NM_004972.4
 ↓
c.1849G>T
 ↓
Affected codon
 ↓
Valine → Phenylalanine
 ↓
p.Val617Phe
 ↓
V617F
```

The computational implementation is designed to verify this relationship from the retrieved reference sequence rather than merely printing a predetermined answer.

The repository also contains a standalone summary script and an analysis notebook for tabular representation of the variant.

## Interpretation of the sequence consequence

The nucleotide substitution is a missense change. At the protein level, the reference valine is replaced by phenylalanine at residue 617. This occurs within the JH2 pseudokinase regulatory domain of JAK2.

## Biological interpretation

The V617F alteration reduces normal autoinhibitory regulation and promotes inappropriate JAK2 signaling. The resulting pathway activation contributes to abnormal myeloid proliferation and is a central molecular feature of classical MPN biology.

---

# 10. Quality Assurance and Reproducibility

A key feature of the project is the separation between network-dependent retrieval and deterministic testing.

The live sequence retrieval script uses NCBI at runtime. The unit tests use synthetic sequence fragments for the core codon logic, allowing tests to execute without network availability.

The repository also includes GitHub Actions for automated testing across multiple Python versions.

Reproducibility requires recording:

- reference accession and version;
- genome assembly;
- database versions;
- software versions;
- analysis parameters;
- input data;
- generated outputs; and
- code revision.

---

# 11. Limitations

1. The project is not a clinically validated diagnostic assay.
2. The reference retrieval step depends on availability of the NCBI service.
3. Public database content can change over time.
4. Variant classification may differ by disease and interpretation framework.
5. Molecular testing must be interpreted alongside clinical and laboratory findings.
6. A negative JAK2 V617F result does not exclude an MPN.
7. The current project focuses on a single driver variant and does not represent the full molecular landscape of MPNs.
8. The sequence-level demonstration does not model assay sensitivity, variant allele fraction, specimen quality, or analytical performance characteristics of a clinical test.

---

# 12. Future Development

The project can be expanded in four major directions.

### 12.1 Multi-driver MPN analysis

Add:

- CALR variants
- MPL variants
- broader myeloid gene panels

### 12.2 NGS workflow

Develop a reproducible FASTQ-to-VCF workflow incorporating:

- FastQC
- alignment
- BAM processing
- variant calling
- filtering
- annotation
- reporting

### 12.3 Variant evidence aggregation

Build automated structured retrieval from ClinVar, dbSNP, Ensembl, UniProt and literature resources.

### 12.4 Interactive reporting

Develop a lightweight dashboard that accepts a variant and returns genomic identity, transcript consequence, protein consequence, evidence links, and an educational interpretation summary.

---

# 13. Conclusion

This project demonstrates a complete conceptual and computational chain for investigating JAK2 V617F, from reference sequence retrieval to nucleotide substitution, codon-level analysis, protein consequence, molecular mechanism, clinical context, and reproducibility.

Its principal value is the integration of **medical laboratory science with computational molecular biology**. Rather than presenting JAK2 V617F only as a hematology fact, the project demonstrates how a clinically important molecular alteration can be represented, verified, analyzed, documented, tested, and communicated using reproducible computational methods.

The repository therefore provides a foundation for further development into a multi-variant MPN bioinformatics platform and a broader precision-medicine portfolio.

> **From the laboratory bench to the genome, and from genomic data to biological meaning.**

---

# 14. References and Authoritative Resources

1. Baxter EJ, Scott LM, Campbell PJ, et al. Acquired mutation of the tyrosine kinase JAK2 in human myeloproliferative disorders. *Lancet*. 2005;365:1054–1061.
2. James C, Ugo V, Le Couédic JP, et al. A unique clonal JAK2 mutation leading to constitutive signalling causes polycythaemia vera. *Nature*. 2005;434:1144–1148.
3. Kralovics R, Passamonti F, Buser AS, et al. A gain-of-function mutation of JAK2 in myeloproliferative disorders. *New England Journal of Medicine*. 2005;352:1779–1790.
4. Arber DA, Orazi A, Hasserjian RP, et al. International Consensus Classification of myeloid neoplasms and acute leukemias. *Blood*. 2022;140:1200–1228.
5. Khoury JD, Solary E, Abla O, et al. The 5th edition of the World Health Organization classification of haematolymphoid tumours: myeloid and histiocytic/dendritic neoplasms. *Leukemia*. 2022;36:1703–1719.
6. Richards S, Aziz N, Bale S, et al. Standards and guidelines for the interpretation of sequence variants. *Genetics in Medicine*. 2015;17:405–424.
7. National Center for Biotechnology Information. RefSeq transcript **NM_004972.4**, human JAK2.
8. National Center for Biotechnology Information. ClinVar records for JAK2 V617F / NM_004972.4:c.1849G>T.
9. National Center for Biotechnology Information. dbSNP record **rs77375493**.

---

# 15. Author

**Daniel Hananiya**  
Medical Laboratory Scientist | Molecular Biology Researcher | Bioinformatics Enthusiast

GitHub: `DanielhananiyaML/JAK2-V617F-Molecular-Diagnosis`
