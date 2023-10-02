# Quantitative Structure-Activity Relationship (QSAR) Modelling of human acetylcholinesterase inhibitors

This project focuses on the analysis of potential inhibitors for Acetylcholinesterase, a key enzyme involved in Alzheimer's disease. The analysis puts together data preprocessing, exploratory data analysis, and machine learning model evaluation, with a particular emphasis on the Random Forest algorithm.

## Table of Contents

- [Introduction](#introduction)
- [Data Pre-processing](#data-pre-processing)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Regression Models Evaluation](#regression-models-evaluation)
- [Random Forest Analysis](#random-forest-analysis)
- [Hyperparameters](#hyperparameters)
- [10-fold Cross-Validation](#10-fold-cross-validation)
- [Conclusions](#conclusions)
- [References](#references)

In a separate folder named "predictions", you'll find the necessary resources to predict the pIC50 based on the descriptors. Specifically, predictions were made for the first five molecules of the dataset. Inside this folder, you'll discover:

- A notebook detailing every step required for making a prediction.
- The predict_function.py file, which contains essential function for prediction.
- The rf_model.pkl file, which is the trained Random Forest model.
- The required CSV files needed to perform the predictions.

## Introduction

- **Examining the Project Topic**: An overview of the significance of Acetylcholinesterase in drug discovery.

## Data Pre-processing

- **ChEMBL Database**: Source of the bioactivity data.
  - Importing necessary libraries.
  - Searching for the target protein.
  - Retrieving bioactivity data for Human Acetylcholinesterase.
- **Handling Missing Data**: Techniques used to handle and impute missing values.
- **Compound Classification**: Labeling compounds as active, intermediate, or inactive based on their bioactivity levels.

## Exploratory Data Analysis

- **Lipinski Descriptors**: Introduction to Lipinski's Rule of Five and its significance.
  - Cleaning SMILES notation.
  - Calculating molecular descriptors.
- **pIC50 Conversion**: Transforming IC50 values to a more interpretable scale.
- **Visualizations**: Various plots like countplots, scatter plots, pair plots, and box plots to understand the data distribution and relationships.

## Regression Models Evaluation

- **Machine Learning Model Comparison**: Evaluating different regression models to predict pIC50 values.
- **Analysis of Model Performance**: Interpreting the results from the machine learning models.

## Random Forest Analysis

- **Random Forest Model**: Building and evaluating a Random Forest model.
- **Residual Analysis**: Understanding the difference between observed and predicted values.

## Hyperparameters

- **Hyperparameter Tuning**: Using techniques like RandomizedSearchCV to find the best hyperparameters for the Random Forest model.

## 10-fold Cross-Validation

- A 10-fold cross-validation analysis to validate the performance of our model was performed. This method provides a more robust evaluation by training and testing the model on different subsets of the data multiple times.

## Conclusions

The project objective was to reproduce the previous published data of a 2016 publication called: **"Probing the origins of human acetylcholinesterase inhibition via QSAR modeling and molecular docking"**<sup><a href="#ref5">[5]</a></sup>: https://doi.org/10.7717/peerj.2322

This project is an exploration of the bioactivity data related to Human Acetylcholinesterase, a critical target in drug discovery. Beginning with an introduction to the ChEMBL Database, the data was processed and curated, ensuring its interpretability for subsequent analysis. This involved handling missing data, classifying compounds based on their bioactivity, and converting IC50 values to a more interpretable pIC50 scale.

During exploratory data analysis, the relationships between various Lipinski Descriptors and pIC50 values was reviewd and rationalized. Furthermore, the Mann-Whitney U Test offered a statistical perspective on the differences between active and inactive molecules across various descriptors.

Before proceeding with the ML modeling, the PaDEL's software was used to compute several fingerprint descriptors.

The Random Forest regression model was chosen based on a good trade-off between performance and computational cost.

In summary, this project exemplifies a meticulous approach for the QSAR modeling of a biological target utilizing several state-of-the-art computational tools applied to ML in drug discovery.

## References

- Original project by [dataprofessor](https://github.com/dataprofessor).
- [ChEMBL Database](https://www.ebi.ac.uk/chembl/)
- Yap, C. W. (2011). PaDEL-descriptor: An open-source software to calculate molecular descriptors and fingerprints. Journal of Computational Chemistry, 32(7), 1466-1474.
- References from publications can be found in the project notebook.

---

**Note**: This project was inspired by the work of [dataprofessor](https://github.com/dataprofessor). While the original framework was provided by dataprofessor, modifications, updates, and additional information were incorporated to enhance the analysis.

