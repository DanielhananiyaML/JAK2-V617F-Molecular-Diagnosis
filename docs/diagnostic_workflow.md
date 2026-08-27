# JAK2 V617F Molecular Diagnostic Workflow

## Purpose

This document describes an educational, laboratory-oriented framework for investigating JAK2 V617F in suspected BCR::ABL1-negative myeloproliferative neoplasms (MPNs).

The workflow emphasizes that molecular testing is one component of an integrated diagnostic process. Current classification systems combine clinical findings, peripheral blood parameters, bone-marrow morphology and molecular/genetic evidence. citeturn0search6turn0search13

---

## 1. Clinical and Laboratory Suspicion

The diagnostic process begins with the patient's clinical presentation and laboratory phenotype.

Potential triggers for investigation may include unexplained:

- erythrocytosis;
- thrombocytosis;
- leukocytosis;
- splenomegaly;
- thrombosis or unusual-site thrombosis; or
- other findings suggestive of an MPN.

A CBC and peripheral blood film provide important initial information but are not sufficient by themselves to establish the molecular diagnosis.

---

## 2. Specimen Considerations

Depending on the laboratory protocol and diagnostic question, molecular analysis may use DNA extracted from peripheral blood or bone-marrow material.

Pre-analytical factors should be documented, including:

- specimen type;
- collection conditions;
- nucleic-acid extraction method;
- DNA concentration and quality;
- storage conditions; and
- time from collection to processing where relevant.

This repository does not prescribe a clinical specimen acceptance policy.

---

## 3. Molecular Testing Strategy

A simplified molecular strategy for suspected classical MPN is:

```text
Suspected BCR::ABL1-negative MPN
                ↓
          JAK2 V617F test
                ↓
        ┌───────┴────────┐
        │                │
     Positive          Negative
        │                │
        ▼                ▼
Integrate with       Consider other
clinical and         driver mutations
morphologic          and diagnostic
findings             possibilities
                         │
                  ┌──────┼──────┐
                  │      │      │
                 CALR   MPL   JAK2 exon 12
```

The exact order and extent of testing should follow the laboratory's validated algorithm and the clinical context.

---

## 4. JAK2 V617F Assay Options

### 4.1 Allele-Specific PCR

Allele-specific PCR uses primers designed to distinguish the mutant allele from the wild-type sequence.

**Strengths**

- targeted;
- relatively rapid;
- suitable for focused JAK2 V617F testing;
- can be designed for sensitive detection.

**Limitations**

- targets a specific known variant;
- does not comprehensively interrogate other JAK2 alterations;
- assay performance depends on primer design and laboratory validation.

---

### 4.2 Real-Time PCR

Real-time PCR can quantify amplification during the reaction and may be used for sensitive detection of JAK2 V617F and estimation of mutant burden when an appropriately validated assay is available.

Important analytical parameters include:

- limit of detection;
- amplification efficiency;
- specificity;
- controls;
- reproducibility; and
- interpretation thresholds.

---

### 4.3 Digital PCR

Digital PCR partitions a sample into many individual reactions and estimates target concentration from positive and negative partitions.

Potential advantages include high analytical sensitivity and quantitative assessment of low-level variants. Its suitability depends on assay design, instrumentation and validation.

---

### 4.4 Sanger Sequencing

Sanger sequencing can identify sequence changes within an amplified target and can provide direct sequence confirmation.

However, its sensitivity for low-level somatic variants is generally lower than that of highly sensitive targeted assays, so it may not be optimal for every JAK2 V617F diagnostic question.

---

### 4.5 Next-Generation Sequencing

Targeted NGS panels can interrogate JAK2 together with additional MPN-associated and myeloid genes.

A simplified targeted-NGS workflow is:

```text
DNA
 ↓
Library preparation
 ↓
Target enrichment
 ↓
Sequencing
 ↓
FASTQ
 ↓
Quality control
 ↓
Alignment
 ↓
Variant calling
 ↓
Filtering
 ↓
Annotation
 ↓
Interpretation
```

NGS can be especially useful when the clinical question extends beyond a single known variant.

---

## 5. Integrated Interpretation

A positive JAK2 V617F result should not be interpreted as an isolated diagnosis.

A useful conceptual model is:

```text
Molecular result
      +
CBC / blood phenotype
      +
Peripheral blood morphology
      +
Bone-marrow morphology
      +
Clinical findings
      +
Additional molecular findings
      ↓
Integrated diagnostic interpretation
```

The WHO 5th edition explicitly emphasizes integration of peripheral blood findings, molecular data and bone-marrow morphology when distinguishing PV, ET and PMF. citeturn0search6

---

## 6. Variant Verification

For the canonical JAK2 V617F variant, the repository uses:

```text
Gene:        JAK2
Transcript:  NM_004972.4
cDNA:        c.1849G>T
Protein:     p.Val617Phe
dbSNP:       rs77375493
GRCh38:      NC_000009.12:g.5073770G>T
```

ClinGen's Allele Registry and NCBI ClinVar independently support these representations. citeturn0search4turn0search1

Explicit transcript and genome-assembly versions should be retained in all computational outputs.

---

## 7. Molecular Result Categories

A validated assay may produce outcomes such as:

### Positive

JAK2 V617F is detected above the validated assay threshold.

### Negative

JAK2 V617F is not detected within the assay's validated analytical capability.

### Indeterminate / Invalid

The assay cannot be interpreted because of quality-control failure, insufficient material, inhibition, inadequate amplification or another validated rejection criterion.

The exact reporting terminology should follow the performing laboratory's validated SOP.

---

## 8. Quality Control

A robust molecular assay should incorporate appropriate controls and documented acceptance criteria.

Conceptually:

```text
Positive control ──┐
Negative control ──┼──► Assay validity
Internal control ──┘

Patient sample ─────────► Result interpretation
```

Quality-control documentation should include relevant assay controls, run acceptance criteria, analytical sensitivity, specificity and reproducibility.

---

## 9. From Diagnostic Result to Bioinformatics

For sequencing-based approaches, the diagnostic workflow connects directly to computational analysis:

```text
Patient DNA
    ↓
Sequencing
    ↓
FASTQ
    ↓
QC
    ↓
Alignment
    ↓
Variant calling
    ↓
JAK2 V617F detection
    ↓
HGVS annotation
    ↓
ClinVar / dbSNP / ClinGen evidence
    ↓
Integrated interpretation
```

This transition is the focus of the next computational components of the repository.

---

## 10. Important Diagnostic Caveat

A negative JAK2 V617F test does **not** automatically exclude an MPN. ET and PMF may carry other driver mutations, particularly CALR or MPL alterations, and PV can involve other activating JAK2 mutations such as exon 12 variants. citeturn0search6turn0search14

Consequently, a molecular diagnostic algorithm should be interpreted in relation to the patient's phenotype and the laboratory's validated testing strategy.

---

## 11. Project Extension

The repository will subsequently implement a computational case-study workflow that demonstrates:

1. retrieval of the canonical JAK2 V617F variant;
2. verification of transcript and genomic coordinates;
3. annotation using public resources;
4. comparison of variant representations;
5. evidence retrieval;
6. generation of a reproducible summary table.

---

## Disclaimer

This document is an educational portfolio resource and does not constitute a clinical laboratory SOP, diagnostic recommendation or substitute for professional medical judgment.
