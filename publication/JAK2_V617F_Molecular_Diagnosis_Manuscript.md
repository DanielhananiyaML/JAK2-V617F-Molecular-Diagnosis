# JAK2 V617F Molecular Diagnosis: A Reproducible Sequence-Level and Variant-Interpretation Workflow

**Daniel Hananiya**  
Medical Laboratory Science | Molecular Biology | Hematology | Bioinformatics

## Abstract

### Background
JAK2 V617F is a recurrent acquired molecular driver in classical BCR::ABL1-negative myeloproliferative neoplasms (MPNs). Its detection is clinically important, but the molecular result is most useful when represented consistently, computationally verified, and interpreted in its appropriate disease context.

### Objective
To develop a transparent, reproducible computational case study that follows JAK2 V617F from a versioned reference transcript through nucleotide substitution, codon analysis, protein consequence, public variant identifiers, and molecular diagnostic interpretation.

### Methods
The workflow centers on JAK2 RefSeq transcript NM_004972.4 and the canonical variant NM_004972.4:c.1849G>T (p.Val617Phe; rs77375493). A Python engine retrieves the transcript from NCBI at runtime, extracts the affected codon, verifies the reference G allele, introduces the alternate T allele, and translates the reference and mutant codons. A Jupyter notebook integrates the sequence engine with structured annotation, diagnostic context, visualization, and provenance documentation. Deterministic unit tests and GitHub Actions provide automated quality control.

### Results
The workflow verifies the expected sequence consequence from the reference transcript: the affected codon is transformed from a valine-encoding codon to a phenylalanine-encoding codon, yielding p.Val617Phe. The project separates live external data retrieval from deterministic tests and records transcript, assembly, variant and database identifiers for reproducibility.

### Conclusion
JAK2 V617F provides a useful model for demonstrating how medical laboratory science and computational biology can be integrated into a reproducible molecular diagnostic workflow. The framework can be extended to CALR, MPL, additional MPN drivers and broader NGS-based variant analysis.

**Keywords:** JAK2 V617F; myeloproliferative neoplasms; molecular diagnostics; bioinformatics; sequence analysis; variant interpretation; hematology; genomics.

---

## 1. Introduction

Classical BCR::ABL1-negative MPNs comprise clonal myeloid neoplasms in which dysregulated signaling contributes to abnormal hematopoiesis. JAK2 V617F is one of the best-characterized acquired driver alterations in this disease group. The variant affects the JH2 pseudokinase regulatory region of JAK2 and promotes inappropriate signaling through pathways including JAK-STAT.

The molecular laboratory increasingly operates at the intersection of wet-laboratory measurement and computational interpretation. A variant detected by PCR, sequencing or an NGS assay must be represented using stable identifiers, mapped to a reference sequence, annotated, quality controlled and interpreted with appropriate clinical context. This project uses JAK2 V617F as a focused case study to demonstrate that complete chain.

## 2. Aim

To develop a reproducible sequence-level and variant-interpretation workflow for JAK2 V617F that can serve as an educational molecular diagnostics and bioinformatics portfolio artifact.

## 3. Objectives

1. Verify the canonical JAK2 V617F representation.
2. Retrieve and analyze the relevant reference transcript.
3. Demonstrate the c.1849G>T substitution computationally.
4. Verify the p.Val617Phe consequence by codon translation.
5. Integrate stable public variant identifiers.
6. Document molecular diagnostic context and limitations.
7. Implement automated testing and continuous integration.
8. Provide a reproducible foundation for extension to other MPN driver genes.

## 4. Materials and Methods

### 4.1 Variant representation

The focal representation is NM_004972.4:c.1849G>T, p.Val617Phe, rs77375493. The GRCh38 genomic representation is NC_000009.12:g.5073770G>T.

### 4.2 Reference sequence analysis

The Python script `scripts/reference_sequence_analysis.py` retrieves NM_004972.4 from NCBI using E-utilities. FASTA headers are removed and sequence characters are normalized. Coding position 1849 is converted to zero-based indexing and the affected three-nucleotide codon is extracted. The program verifies the expected G reference allele before constructing the alternate codon.

### 4.3 Computational mutation and translation

The alternate allele T replaces the reference G at c.1849. Reference and alternate codons are translated using the standard genetic code. The expected biological consequence is Valine (V) to Phenylalanine (F) at residue 617.

### 4.4 Jupyter integration

`analysis/JAK2_V617F_Analysis.ipynb` imports the sequence engine and executes the analysis as an end-to-end workflow. It produces structured tables, consequence checks, diagnostic context and a molecular interpretation visualization.

### 4.5 Quality control

The repository contains deterministic tests for the core sequence logic. GitHub Actions compiles the Python code and runs the test suite across multiple supported Python versions. The live NCBI retrieval is deliberately not required for deterministic unit tests.

## 5. Results

The computational workflow establishes the following chain:

```text
JAK2 NM_004972.4
        ↓
c.1849G>T
        ↓
affected codon
        ↓
Valine → Phenylalanine
        ↓
p.Val617Phe
        ↓
JAK2 V617F
        ↓
MPN molecular context
```

The sequence engine verifies the expected reference allele and codon-level consequence rather than relying solely on a hard-coded final annotation. This makes the result inspectable and testable.

## 6. Molecular and Diagnostic Interpretation

JAK2 V617F is a major molecular driver in classical MPNs and is particularly associated with polycythemia vera, while also occurring in subsets of essential thrombocythemia and primary myelofibrosis. A positive molecular result should be interpreted together with clinical findings, CBC parameters, peripheral-blood and bone-marrow morphology, and other molecular findings where appropriate.

A negative JAK2 V617F result does not by itself exclude an MPN. Alternative molecular drivers, assay sensitivity, specimen characteristics and the broader diagnostic framework must be considered.

Public database evidence should also be interpreted with care. Disease-specific and somatic/germline contexts are not interchangeable. The repository therefore treats public evidence as contextual evidence rather than as an automatic substitute for clinical interpretation.

## 7. Reproducibility

The project records the transcript accession/version, genome assembly, HGVS representation and dbSNP identifier. The analysis is version controlled through GitHub, while GitHub Actions provides automated quality checks. Future iterations should additionally pin database release versions and software dependencies.

## 8. Limitations

This project is not a clinically validated diagnostic assay. It does not estimate analytical sensitivity, limit of detection, variant allele fraction, specimen quality or inter-assay performance. Public databases are dynamic resources and their content may change. The computational sequence model is intentionally focused on a single canonical variant and does not represent the full molecular heterogeneity of MPNs.

## 9. Future Work

The framework can be extended to CALR and MPL, followed by a broader MPN gene panel. A future NGS implementation could incorporate FASTQ quality control, alignment, variant calling, filtering, annotation, evidence aggregation and structured reporting. The same architecture could also support a multi-variant educational database.

## 10. Conclusion

This project demonstrates a transparent path from a clinically relevant molecular variant to a reproducible computational analysis. JAK2 V617F is represented using standardized identifiers, verified against a versioned reference sequence, transformed computationally, translated to its protein consequence, contextualized within MPN biology, and supported by automated testing.

The broader objective is to demonstrate the value of combining medical laboratory expertise with computational molecular biology: the laboratory generates molecular evidence, while bioinformatics provides a reproducible framework for representing, validating, interpreting and communicating that evidence.

## References

1. Baxter EJ, Scott LM, Campbell PJ, et al. Acquired mutation of the tyrosine kinase JAK2 in human myeloproliferative disorders. *Lancet*. 2005;365:1054–1061.
2. James C, Ugo V, Le Couédic JP, et al. A unique clonal JAK2 mutation leading to constitutive signalling causes polycythaemia vera. *Nature*. 2005;434:1144–1148.
3. Kralovics R, Passamonti F, Buser AS, et al. A gain-of-function mutation of JAK2 in myeloproliferative disorders. *N Engl J Med*. 2005;352:1779–1790.
4. Arber DA, Orazi A, Hasserjian RP, et al. International Consensus Classification of myeloid neoplasms and acute leukemias. *Blood*. 2022;140:1200–1228.
5. Khoury JD, Solary E, Abla O, et al. The 5th edition of the World Health Organization classification of haematolymphoid tumours: myeloid and histiocytic/dendritic neoplasms. *Leukemia*. 2022;36:1703–1719.
6. Richards S, Aziz N, Bale S, et al. Standards and guidelines for the interpretation of sequence variants. *Genet Med*. 2015;17:405–424.
7. National Center for Biotechnology Information. RefSeq: NM_004972.4, human JAK2.
8. National Center for Biotechnology Information. ClinVar and dbSNP records for JAK2 V617F / rs77375493.

---

**Repository:** https://github.com/DanielhananiyaML/JAK2-V617F-Molecular-Diagnosis

**Author:** Daniel Hananiya
