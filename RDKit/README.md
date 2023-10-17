# RDKit Repository

## Description

This repository contains Jupyter notebooks and datasets focused on molecular informatics using RDKit.

## Directory Structure

```
├── RDKit
│   ├── Fingerprints-applications.ipynb
│   ├── Fingerprints.ipynb
│   ├── RDKit-general
│   └── README.md
```

## Table of Contents

1. [Fingerprints Notebook](#fingerprints-notebook)
2. [RDKit General Notebook](#rdkit-general-notebook)
3. [Fingerprints Applications Notebook](#fingerprints-applications-notebook)
4. [Dataset](#dataset)

## RDKit General Notebook

**File:** [RDKit-general.ipynb](./RDKit-general.ipynb)

This notebook provides a general overview of RDKit functionalities:

- Basics of RDKit.
- Molecular visualization.
- Descriptors - basics.
- FingerPrints - basicss.

## Fingerprints Notebook

**File:** [Fingerprints.ipynb](./Fingerprints.ipynb)

This notebook develops the concept of molecular fingerprints. It covers:

- Introduction to fingerprints.
- Different types of fingerprints:
    1. Morgan
    2. Avalon
    3. Molecular ACCess System keys (MACCS)
    4. Atom-Pairs
    5. Topological-Torsion
    6. RDKit
- Tanimoto Similarity
- Dice and CosineSimilarity

## Fingerprints Applications Notebook

**File:** [Fingerprints-applications.ipynb](./Fingerprints-applications.ipynb)

In this notebook, we explore various applications of molecular fingerprints:

- Molecular Similarities.
- Clustering with Taylor-Butina.
- Tanimoto similarity calculations.
- Filtering Compounds.
- Scaffold analysis.

## Dataset

**File:** [solubility_clean.csv](./solubility_clean.csv)

This dataset contains molecular information and their respective solubility values. It is used across the notebooks for various demonstrations and exercises. This data was taken from here https://doi.org/10.1021/ci034243x

---

## Installation and Setup

1. Clone this repository.
2. Make sure you have Jupyter Notebook or Jupyter Lab installed.
3. Install RDKit using Conda.
4. Open the notebooks and explore.
