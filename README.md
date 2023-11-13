# Chemoinformatics - Bioinformatics Projects Repository

This repository serves as a central hub for all my chemoinformatics - bioinformatics projects. Each project has its own dedicated folder, where you can find more detailed information, code, datasets, and documentation specific to that project.

## Projects

Below is a list of the projects available in this repository:

1. [Cheminformatics Workflow](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow): The purpose of the projects listed in this folder is to explore the most part of cheminformatics with special focus in drug discovery:
    1. [RDKit generals](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/1-RDKit-general.ipynb):
        - SMILES representions
        - SMARTS representations
        - Files types
        - Files conversions
    2. [Library Filtering](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/2-Library_filtering.ipynb):
        - Load DataSet from PubChem
        - Remove Nan
        - Remove Duplicates
        - Molecues Visualization
        - Remove Inconclusive Results
        - Remove Active Agonist = Toxic
        - Remove Weak Compounds
    3. [ChEMBl webresource](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/3-chembl_webresource.ipynb):
        - Search for Target Protein
        - Select Homo Sapiens Cyclooxygenase-2
        - Retrieve Bioactivity Data by IC50
        - Remove empty entries
        - Remove duplicates
        - Manage Std Values Units
        - Label: Active, Inactive, Intermediate
        - Convert IC50 to pIC50
    4. [Data curation](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/4-Data_curation.ipynb):
        - Smiles Standarization
        - Fragment Parents
        - Neutralization
        - Normalization
        - Canonical Tautomer
        - Stereo Parents
        - Hydrogen Cleanup
        - Conformer Generation
    5. [Molecular descriptors](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/5-Molecular-descriptors.ipynb):
        - MW, LogP, RB Descriptors
        - Aromatic Rings, Valence Electrons and BalabanJ descriptors
        - General RDKit Molecular Descriptors
    6. [Chemical substructre](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/6-Chemical_substracture.ipynb):
        - Substructure Search with SMARTS pattern
        - Has Substructure
        - Get Substructure
        - More than 1 Chemical Substructure Search
        - Substructure 1 & Substructure 2
        - Substructure 1 OR Substructure 2
    7. [Most common substructre](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/7-Most_common_substracture.ipynb):
        - MCS between 2 molecules
        - MCS between 1 molecule and a Dataset
        - Bermis-Murcko Scaffolds
    8. [Chemical similarity](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/8-Chemical_smilarity.ipynb):
        - Similarity Matrix Pairwise
        - Euclidean and Tanimoto to find th most similar compounds
    9. [Fingerprints](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/9-Fingerprints.ipynb):
        - Morgan Fingerprints
        - Avalon Fingerprints
        - Molecular ACCess System keys (MACCS)
        - Atom-Pair Fingerprints
        - Topological-Torsion Fingerprints
        - RDKit Fingerprints
    10. [Fingerprints applications project](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/10-Fingerprints-applications.ipynb): This project is intented to apply fingerprints in order to compute molecular similarities and clustering within a dataset taken from the literature.
    11. [Hydrogen bond donor descriptor project](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/11-Hydrogen_bond_donor-descriptor.ipynb): The project focused in the creation of a Python code to calculate a molecular descriptor that represents the capacity of the molecule to be a halogen bond donor. Use the code to calculate the halogen bond description for the given dataset. And finally, filter out compounds that do not have the halogen bond.
    12. [Activity Cliff](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/12-Activity_cliff.ipynb): This project aims to study the the Structure-Activity Landscape Index (SALI) which is used to understand the relationship between the structural similarity of compounds and their biological activities, helping to identify activity cliffs.
    13. [Clustering](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/13-Clustering.ipynb): Here, I review two clustering algorithm:
    - K-means
    - Taylor - Butina
    14. [Chemical Reaction](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/cheminformatics-workflow/notebooks/14-Chemical_reaction.ipynb): I reviewed the basic of chemical reaction using SMARTS.
2. [Quantitative Structure-Activity Relationship (QSAR) Modelling of human acetylcholinesterase inhibitors](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/acetylcholinesterase_2016): This project focuses on the analysis of potential inhibitors for Acetylcholinesterase, a key enzyme involved in Alzheimer's disease. The analysis puts together data preprocessing, exploratory data analysis, and machine learning model evaluation, with a particular emphasis on the Random Forest algorithm.
3. [Water Solubility Prediction using Molecular Descriptors](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/solubility_prediction_2005): This project aims to compute a robust ML algorithm in order to predict the solubility of molecular architectures. Using Molecular Descriptor from RDKit and ML algorithm a equation for the water solubility was extracted, and prediction performed with a validation dataset.
4. [RDKit](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/RDKit): This respository contains several notebooks in which I explore from basics to more advance topics about cheminformatics using RDKit. Here you can find:
    - RDKit basics
    - Fingerprints.
    - Fingerprints applications.
5. [HOMO-LUMO Energy Gap Prediction](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/HOMO-LUMO-prediction): This project takes inspiration from the 2020 publication ["A Structure-Based Platform for Predicting Chemical Reactivity"](https://www-sciencedirect-com.lama.univ-amu.fr/science/article/pii/S2451929420300851). I employed a range of cheminformatics tools to develop a regression model aimed at predicting the HOMO-LUMO energy gap. I calculated the Avalon fingerprints for the dataset using four distinct nBits values: 512, 1024, 2048, and 4096. These fingerprints served as features to train two regression models: the Random Forest and the LGBMRegressor.
6. [Predicting the Fluorination Strength of Electrophilic Fluorinating Reagents](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/prediction-fluorination-strength): This projects aims to reproduce a publication of 2022 ["Machine Learning Approach for Predicting the Fluorination Strenght of Electrophilic Fluorinating Reagents"](https://doi.org/10.1039/d2cp03281c), where the original data can also be found. During the development of this project, I aimed to reproduce the results observed by the author of the publication on predicting the fluorination strength of electrophilic fluorinating reagents. To achieve this, I began by examining the original dataset presented in the publication, where 130 different molecules were selected in two solvents: MeOH and DCM. I utilized the RDKit library, which is applied in cheminformatics, along with mordred for molecular fingerprints. For visualization and data processing, I used libraries such as matplotlib, seaborn, pandas, and numpy. The machine learning modeling was conducted with the scikit-learn library.

## Getting Started

To explore a specific project, simply click on its link above or navigate to the corresponding folder. Inside each project folder, you will typically find the following:

- **README.md**: Detailed information about the project, including its objectives, methodology, and results.
- **Datasets**: Any datasets used for training and testing the machine learning models.
- **Images**: Any image generated during the development of the project.
- **Documentation**: Additional documents, reports, or notebooks related to the project.
- **Code (if applicable)**: The source code for the project, organized into relevant files and directories.
- **License (if applicable)**: Information about the licensing of the project.