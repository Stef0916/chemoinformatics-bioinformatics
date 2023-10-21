# Chemoinformatics - Bioinformatics Projects Repository

This repository serves as a central hub for all my chemoinformatics - bioinformatics projects. Each project has its own dedicated folder, where you can find more detailed information, code, datasets, and documentation specific to that project.

## Projects

Below is a list of the projects available in this repository:

1. [Quantitative Structure-Activity Relationship (QSAR) Modelling of human acetylcholinesterase inhibitors](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/acetylcholinesterase_2016): This project focuses on the analysis of potential inhibitors for Acetylcholinesterase, a key enzyme involved in Alzheimer's disease. The analysis puts together data preprocessing, exploratory data analysis, and machine learning model evaluation, with a particular emphasis on the Random Forest algorithm.
2. [Water Solubility Prediction using Molecular Descriptors](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/solubility_prediction_2005): This project aims to compute a robust ML algorithm in order to predict the solubility of molecular architectures. Using Molecular Descriptor from RDKit and ML algorithm a equation for the water solubility was extracted, and prediction performed with a validation dataset.
3. [RDKit](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/RDKit): This respository contains several notebooks in which I explore from basics to more advance topics about cheminformatics using RDKit. Here you can find:
    - RDKit basics
    - Fingerprints.
    - Fingerprints applications.
4. [HOMO-LUMO Energy Gap Prediction](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/HOMO-LUMO-prediction): This project takes inspiration from the 2020 publication ["A Structure-Based Platform for Predicting Chemical Reactivity"](https://www-sciencedirect-com.lama.univ-amu.fr/science/article/pii/S2451929420300851). I employed a range of cheminformatics tools to develop a regression model aimed at predicting the HOMO-LUMO energy gap. I calculated the Avalon fingerprints for the dataset using four distinct nBits values: 512, 1024, 2048, and 4096. These fingerprints served as features to train two regression models: the Random Forest and the LGBMRegressor.
5. [Predicting the Fluorination Strength of Electrophilic Fluorinating Reagents](https://github.com/Stef0916/chemoinformatics-bioinformatics/tree/main/prediction-fluorination-strength): This projects aims to reproduce a publication of 2022 ["Machine Learning Approach for Predicting the Fluorination Strenght of Electrophilic Fluorinating Reagents"](https://doi.org/10.1039/d2cp03281c), where the original data can also be found. During the development of this project, I aimed to reproduce the results observed by the author of the publication on predicting the fluorination strength of electrophilic fluorinating reagents. To achieve this, I began by examining the original dataset presented in the publication, where 130 different molecules were selected in two solvents: MeOH and DCM. I utilized the RDKit library, which is applied in cheminformatics, along with mordred for molecular fingerprints. For visualization and data processing, I used libraries such as matplotlib, seaborn, pandas, and numpy. The machine learning modeling was conducted with the scikit-learn library.

## Getting Started

To explore a specific project, simply click on its link above or navigate to the corresponding folder. Inside each project folder, you will typically find the following:

- **README.md**: Detailed information about the project, including its objectives, methodology, and results.
- **Datasets**: Any datasets used for training and testing the machine learning models.
- **Images**: Any image generated during the development of the project.
- **Documentation**: Additional documents, reports, or notebooks related to the project.
- **Code (if applicable)**: The source code for the project, organized into relevant files and directories.
- **License (if applicable)**: Information about the licensing of the project.