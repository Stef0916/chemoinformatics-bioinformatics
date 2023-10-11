# Water Solubility Prediction using Molecular Descriptors

This project aims to compute a robust ML algorithm in order to predict the solubility of molecular architectures. Using Molecular Descriptor from RDKit and ML algorithm a equation for the water solubility was extracted, and prediction performed with a validation dataset.

## Directory Structure

```
├── solubility_prediction-2005
│   ├── data
│   │   ├── data_to_train_model.csv
│   │   ├── molecular_descriptors.csv
│   │   ├── solubility_train_clean.csv
│   │   ├── solubility_train_molecules.csv
│   │   ├── solubility_validation_molecular_descriptors.csv
│   │   ├── solubility_validation_molecules.csv
│   │   ├── validation_prediction_linear_model.csv
│   │   └── validation_prediction_random_forest_model.csv
│   ├── images
│   │   ├── logS_exp_vs_pedicted_xtrain_xtest.pdf
│   │   ├── LR_difference.pdf
│   │   ├── LR_predcited_vs_actual.pdf
│   │   ├── LR_residuals.pdf
│   │   ├── residuals_xtest_xtrain.pdf
│   │   ├── RF_difference.pdf
│   │   ├── RF_predicted_vs_actual.pdf
│   │   └── RF_residuals.pdf
│   ├── notebooks
│   │   ├── data_precprocessing-1.ipynb
│   │   └── regression-model-2.ipynb
│   └── README.md
```

Inside this folder, you'll discover:

- A notebook detailing every step required for the data pre-processing, creating the model and making a prediction.
- The required CSV files needed to perform the predictions.
- The images/plots in pdf resulting from the project.

## Introduction

## Data Pre-processing

- **Database**: taken from the original publication ['ESOL:  Estimating Aqueous Solubility Directly from Molecular Structure'](https://risweb.st-andrews.ac.uk/portal/en/datasets/dls100-solubility-dataset(3a3a5abc-8458-4924-8e6c-b804347605e8).html)
- **Handling Missing Data**: Techniques used to handle and impute missing values.
- **Molecular Descriptor**: MW, LogP, RB, AP were extracted from RDKit library.

## Regression Models Evaluation

- **Machine Learning Model Comparison**: Evaluating different regression models to predict LogS values.
- **Analysis of Model Performance**: Interpreting the results from the machine learning models.

## Linear Regression Analysis
- **Linear Regression Model**: Building and evaluating a Linear Regression model.
_ **Extracting the equation**: Evaluating the coefficients and interception wrt the original publication.
- **Residual Analysis**: Understanding the difference between observed and predicted values.

## Random Forest Analysis

- **Random Forest Model**: Building and evaluating a Random Forest model.
- **Residual Analysis**: Understanding the difference between observed and predicted values.

## Hyperparameters

- **Hyperparameter Tuning**: Using techniques like RandomizedSearchCV to find the best hyperparameters for the Random Forest model.

## Linear Regression vs Random Forest Comparision
Using MSE, R^2 and predictions, the Random Forest Model outperformed the Linear Regression Model.

## Conclusions

Drawing inspiration from previous studies on solubility prediction, this project aimed to replicate and validate the results. Molecular descriptors such as MW, LogP, RB, and AP were extracted using the RDKit library. These descriptors were then employed to develop various regression models. Upon comparing Linear Regression and Random Forest models, the latter emerged superior in its predictive accuracy for water solubility on the validation set. These findings not only align with prior observations but also demonstrate enhanced performance when utilizing the Random Forest model.

