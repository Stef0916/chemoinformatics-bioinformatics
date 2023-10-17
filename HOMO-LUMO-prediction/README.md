# Prediction of HOMO-LUMO Energy Gaps

This repository contains data and analysis related to the prediction of HOMO-LUMO energy gaps for various chemical compounds.

This project takes inspiration from the 2020 publication ["A Structure-Based Platform for Predicting Chemical Reactivity"](https://www-sciencedirect-com.lama.univ-amu.fr/science/article/pii/S2451929420300851). In this paper, the authors computed various chemical features with the goal of predicting chemical reactivity. Among the models they developed, one focused on predicting the HOMO-LUMO energy gap.

In this publication the authors highlight the importance of making sure that a set of molecules, which will be use as machine learning feature inputs to predict chemical reactions, have something in common. With that in mind, they got a fingerprint-based model where the tested the prediction of the HOMO-LUMO enegery gap from DFT calculations. This model got an average R^2 of 0.89 and a MAE in kcal/mol of 6.26 for a ten random 70/30 splits.

They selected all the chemical structures from the [QM9 dataset](http://dx.doi.org/10.1038/sdata.2014.22), which is quantum chemistry dataset of 134 kilo molecules calculated using Density Functional Theory (DFT) using 3LYP/6-31G(2df,p) level of quantum chemistry.

The objective is to reproduce the results observed in the original publication.

## Directory Structure

```
├── HOMO-LUMO-predictions
│   ├── data
│   │   ├── orbital_energies.csv
│   ├── images
│   │   ├── residuals.pdf
│   │   ├── LGBM_difference.pdf
│   │   ├── predcited_vs_observed.pdf
│   ├── notebooks
│   │   ├── HOMO-LUMO-gap.ipynb
│   └── README.md
```

Inside this folder, you'll discover:

- A notebook detailing every step required for the data pre-processing, creating the model and making a prediction.
- The required CSV files needed to perform the predictions.
- The images/plots in pdf resulting from the project.

## Contents

1. **residuals.pdf**: A plot visualizing the residuals from the prediction model.
2. **LGBM_difference.pdf**: A plot showcasing the performance differences associated with a LightGBM model.
3. **predicted_vs_observed.pdf**: A scatter plot comparing the predicted vs. observed HOMO-LUMO energy gaps.
4. **orbital_energies.csv**: A dataset containing:
   - **SMILES**: SMILES notation representing chemical compounds.
   - **Energygap**: The actual energy gap values for the corresponding compounds.
5. **homo-lumo-gap.ipynb**: A Jupyter notebook containing detailed analysis and modeling related to the HOMO-LUMO energy gap prediction.

## Data Pre-processing

- **Database**: taken from the original publication. [Access the Dataset Here](https://zivgitlab.uni-muenster.de/m_kueh11/fp-dm-tool/-/blob/master/DataAndSoftware_S1-S4.zip?ref_type=heads)
- **Handling Missing Data**
- **Handlin Duplicates**
- **Remove Fragments**
- **Avalon Fingerprint**

## Regression Models Evaluation

- 10-fold cross-validation: LGBMRegressor and RandomForestRegressor

## LGBMRegressor
- **Predictions**
- **Residual Analysis**

## Conclusions

In this study, I employed a range of cheminformatics tools to develop a regression model aimed at predicting the HOMO-LUMO energy gap. This model was based on a dataset sourced from the already mentioned publication. I calculated the Avalon fingerprints for the dataset using four distinct nBits values: 512, 1024, 2048, and 4096. These fingerprints served as features to train two regression models: the Random Forest and the LGBMRegressor.

Of the two, the LGBMRegressor outperformed, particularly when using the 4096-bit fingerprint, achieving a Mean Squared Error (MSE) of 5.46 and an R2R2 value of 0.92. Subsequent predictions were made using a test set, from which the observed vs. predicted values and residuals were scrutinized.

In summary, the algorithm appears proficient in predicting HOMO-LUMO energy gaps. However, as with many models, there's always room for enhancement, like reducing the number of features. It's also worth noting that data quality is one of the most important part in designing a predictive model. Unfortunately, this is a factor we often don't have much influence over.
