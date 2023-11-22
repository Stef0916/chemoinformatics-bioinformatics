# Quantitative Structure-Activity Relationship (QSAR) Modelling of human acetylcholinesterase inhibitors

This project focuses on the analysis of potential inhibitors for Acetylcholinesterase, a key enzyme involved in Alzheimer's disease. The analysis puts together data preprocessing, exploratory data analysis, and machine learning model evaluation, with a particular emphasis on the Random Forest algorithm.

During the development of this project, I aimed to explore how the splitting of the data impacts the outcome of the ML algorithm prediction for the QSAR modeling. To do so, I splited the data into test and train dataset based on the Murcko Scaffold and Butina cluster and second using the train-test-split from scikit-learn.

I utilized the RDKit library, which is applied in cheminformatics, along with mordred for molecular fingerprints. For visualization and data processing, I used libraries such as matplotlib, seaborn, pandas, and numpy. The machine learning modeling was conducted with the scikit-learn library.

## Directory Structure

```
├── acetylcholinesterase-QSAR
│   ├── data
│   │   ├── 1-Bioactivity-data
│   │   ├── 2-Curation
│   │   ├── 3-Exploratory_analysis_Similarity
│   │   ├── 4.1-Data-bias-handeling
│   │   ├── 4.2-Data-bias-Fingerprints
│   │   ├── 4.3-Data-bias-ML-algorithm
│   │   ├── 5-Fingerprints
│   │   ├── 6-ML-algorithm
│   ├── images
│   │   ├── molecules1_morgan_bits_radius_2.pdf
│   │   ├── molecules1_morgan_bits_radius_3.pdf
│   ├── notebooks
│   │   ├── 1-Getting-bioactivity-data.ipynb
│   │   ├── 2-Molecular-Representation-Sanitization.ipynb
│   │   ├── 3-Exploratory-Data-Analysis.ipynb
│   │   ├── 4.1-Data-bias-handling.ipynb
│   │   ├── 4.2-Data-Bias-Fingerprints-descriptors.ipynb
│   │   ├── 4.3-Data-bias-ML-algorithm.ipynb
│   │   ├── 5-Fingerprints-descriptors.ipynb
│   │   ├── 6-ML-algorithm.ipynb
│   └── README.md
```

Inside this folder, you'll discover:

- A notebook detailing every step required for the data pre-processing, creating the model and making a prediction.
- The required csv, sdf and smi files.
- The images/plots in pdf resulting from the project.

## Workflow

1. Retrieve Bioactivity Data with IC50 as a filter using the chembl_webresource_client.
2. Cleaning the bioactivity data, dividing the data into active/inactive.
3. Data curation:
    - Smiles Standarization
    - Fragment Parents
    - Neutralization
    - Normalization
    - Canonical Tautomer
    - Stereo Parents
4. Calcultion the chemical similarity to analyze the bias on the structural data of the molecules. Based on this 2 different approaches were developed:
    - 4.1 Split the data into train and test based on the Murcko Scaffold and Butina clustering
    - 4.2 Spliiting of the data using train-test-split from scikit-learn
5. Computing the molecular descriptors using mordred:
    - 5.1 Elimination of missing values
    - 5.2 Correlation-based variable reduction
6. Screening of the most popular ML algorithms using R^2 and RMSE as metrics, and five-fold cross validation procedure.
5. Predictions on the test set.

## **Machine Learning Model:**

1. **I compared five models:** Linear Regression, k-Nearest Neighbor, Support Vector Machine, AdaBoost Regressor, and Random Forest Regressor using five-fold cross-validation. 

- 1.1 **Bias-data approach**: The best modelwas the Random Forest with R^2 = 0.72 and RMSE = 0.86. Subsequent predictions were made using the test set. My results were R2 = 0.29 and RMSE = 1.29, which indicates the poor prediction of the test data. The maximum difference between observed and predicted was 7.65, and the minimum was 0.0003.

- 1.2 **Random splitting approach**: The best modelwas the Random Forest with R^2 = 0.6 and RMSE = 0.94. Subsequent predictions were made using the test set. My results were R2 = 0.67 and RMSE = 0.94, which indicates a better prediction of the test data in comparision with the bias-data approach. The maximum difference between observed and predicted was 7.65, and the minimum was 0.0003.

## Conclusions

The prediction of the ML model is very poor in the majority of the molecules when usign the splitting based on the bias-splitting. One hypotesis is due to the splitting of the test and train dataset based on Murcko scaffold and Butina clustering, which increases the difficulty for the algorithm to predict the outcome. This is because similar molecules where placed either in the test or the train set.

However, the predictive model using the train-test-split from scikit-learn, without applying any pre-conditoned to split the data, gives much better predictions of the pIC50. But this doesn't mean this way is better, it only illustrates the importance of the method used to split the data. This decision has to be system dependen and according with the analysis of the data and personal objectives.

Overall, the objective of this project was to illustrate and understand how the spliting of the data has a profound effect on the ML algorithm and subsequent prediction.

## Perspective
The model will have to be optimized in order to be used as a predictive model.
