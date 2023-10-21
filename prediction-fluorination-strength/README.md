# Predicting the Fluorination Strength of Electrophilic Fluorinating Reagents

This projects aims to reproduce a publication of 2022 ["Machine Learning Approach for Predicting the Fluorination Strenght of Electrophilic Fluorinating Reagents"](https://doi.org/10.1039/d2cp03281c), where the original data can also be found.

During the development of this project, I aimed to reproduce the results observed by the author of the publication on predicting the fluorination strength of electrophilic fluorinating reagents. To achieve this, I began by examining the original dataset presented in the publication, where 130 different molecules were selected in two solvents: MeOH and DCM.

I utilized the RDKit library, which is applied in cheminformatics, along with mordred for molecular fingerprints. For visualization and data processing, I used libraries such as matplotlib, seaborn, pandas, and numpy. The machine learning modeling was conducted with the scikit-learn library.

## Directory Structure

```
├── prediction-fluorination-strength
│   ├── data
│   │   ├── data_pca_2.xlsx
│   │   ├── data_tsne_2.xlsx
│   │   ├── encoded_data-tsne-pca.xlsx
│   │   ├── encoded_scaled_test.xlsx
│   │   ├── encoded_scaled_train.xlsx
│   │   ├── F260_raw.xlsx
│   │   ├── FDP_test_scaled.xlsx
│   │   ├──  FDP_train_scaled.xlsx
│   │   └── ...
│   ├── images
│   │   ├── Feature_importance.pdf
│   │   ├── molecules_for_N-Fluoroammoniums.pdf
│   │   ├── molecules_for_N-Fluorocarboxamides.pdf
│   │   ├── molecules_for_N-Fluoroheterocycles.pdf
│   │   ├── molecules_for_N-Fluoropyridiniums.pdf
│   │   ├── molecules_for_N-Fluorosulfonamides.pdf
│   │   ├── molecules_for_N-Fluorosulfonimides.pdf
│   │   └── ...
│   ├── notebooks
│   │   ├── data-preprocessing-1.ipynb
│   │   ├── pca-tsne-2.ipynb
│   │   ├── train-test_split-3.ipynb
│   │   ├── regression-models-4.ipynb
│   └── README.md
```

Inside this folder, you'll discover:

- A notebook detailing every step required for the data pre-processing, creating the model and making a prediction.
- The required xlsx files needed to perform the predictions.
- The images/plots in pdf resulting from the project.

## Workflow

The following workflow was performed according with the named publication:
1. Calculation of molecular descriptor using Mordred.
2. Feature engineering:
    - 2.1 Elimination of missing values
    - 2.2 Correlation-based variable reduction
    - 2.3 Elimination of feature with constant values
3. One-hot encoding for the two solvents and the molecular categories.
4. Screening of the most popular ML algorithms using R^2 and RMSE as metrics, and five-fold cross validation procedure.
5. Predictions on the test set.


## **Steps for Data preprocessing:**

1. **Calculation of Molecular Descriptors using Mordred:** At this step, I calculated 1826 molecular fingerprints which were later reduced to 88 after feature engineering.
2. **Feature Engineering:**
- 2.1. Elimination of missing values
- 2.2. Correlation-based variable reduction
- 2.3. Elimination of features with constant values
- 2.4. Visualization: Descriptors were visualized in relation to the Type of Reagent class after reducing dimensionality with t-SNE and PCA.

## **Machine Learning Model:**

1. **I compared five models:** Linear Regression, k-Nearest Neighbor, Support Vector Machine, AdaBoost Regressor, and Random Forest Regressor using five-fold cross-validation. **The best model** was the Random Forest with R^2 = 0.88 and RMSE = 7.48. For comparison, the author achieved an R2 and RMSE of 0.93 and 6.94, respectively, for the Random Forest Regressor. Subsequent predictions were made using the test set. My results were R2 = 0.83 and RMSE = 13.5, while the author achieved R2 = 0.78 and RMSE = 9.64. The maximum difference between observed and predicted was 56.98, and the minimum was 0.02.

2. Lastly, **feature importance** was also calculated. One feature, the **BCUTc-1h** fingerprint, stood out with a score of 0.591254. This was evidently the most significant feature for the regression model. It was followed by **GATS2c, MATS1c, SMR_VSA3, RPCG and GATS1p** with importances of 0.047039, 0.046649, 0.037366, 0.035910, and 0.020104, respectively.

## Conclusions

Overall, the model predicted the test set reasonably well, and I successfully replicated most of the implementation that the author used in the development of her project. In the domain of the feature importance, there are further opportunities for exploration, such as re-running the model while focusing solely on the most important features.