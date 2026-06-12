import pandas as pd
import logging

def validate_data(file_path):
    """
    Validates clinical input data for schema compliance and data integrity.
    """
    logging.info(f"Reading data from {file_path}")
    df = pd.read_csv(file_path)
    
    # 1. Check for critical missing values
    if df.isnull().values.any():
        logging.warning("Missing values detected in the dataset.")
        # Optional: You could add logic here to drop or fill values
        df = df.dropna()
        
    # 2. Add custom clinical validation rules (example)
    # Ensure ages are within a realistic range
    if 'age' in df.columns:
        invalid_ages = df[(df['age'] < 0) | (df['age'] > 120)]
        if not invalid_ages.empty:
            logging.error(f"Found {len(invalid_ages)} records with invalid age ranges.")
            # Optionally save these to an error log file
            invalid_ages.to_csv("logs/invalid_records.csv", mode='a')
            df = df.drop(invalid_ages.index)

    logging.info("Validation sequence finished.")
    return df
