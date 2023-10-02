import pandas as pd
from sklearn.feature_selection import VarianceThreshold
import joblib

def predict_pIC50(input_data_path, model_path, original_data_path):
    """
    Predict pIC50 values for given input data using a trained model.
    
    Parameters:
    - input_data_path: Path to the .csv file containing descriptors for the molecules to predict.
    - model_path: Path to the saved Random Forest model.
    - original_data_path: Path to the .csv file containing descriptors for the original training data.
    
    Returns:
    - A list containing predicted pIC50 values.
    """
    
    # Load the input data
    sample_descriptors = pd.read_csv(input_data_path)
    
    # Load the original training data
    df_descriptors = pd.read_csv(original_data_path)
    X_original = df_descriptors.drop(columns=["Name"])
    
    # Initialize and fit the VarianceThreshold object
    selection = VarianceThreshold(threshold=(.8 * (1 - .8)))
    selection.fit(X_original)
    
    # Transform the sample data
    sample_X = selection.transform(sample_descriptors.drop(columns=["Name"]))
    
    # Load the trained model
    rf_model = joblib.load(model_path)
    
    # Make predictions
    predictions = rf_model.predict(sample_X)
    
    return predictions
