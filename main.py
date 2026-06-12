import logging
from src.validator import validate_data
from src.processor import process_records
from src.db_loader import load_to_snowflake

# Configure basic logging to track the pipeline's progress
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    logging.info("Starting Clinical Data Interoperability Engine...")
    
    try:
        # 1. Validation Phase
        raw_data = "data/clinical_input.csv" # Replace with your actual path
        clean_data = validate_data(raw_data)
        logging.info("Data validation complete.")
        
        # 2. Processing Phase
        transformed_data = process_records(clean_data)
        logging.info("Data transformation complete.")
        
        # 3. Loading Phase
        load_to_snowflake(transformed_data)
        logging.info("Data successfully loaded to warehouse.")
        
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()
