import os
import logging
import pandas as pd
from snowflake.connector import connect

def get_db_connection():
    """Establishes a secure connection to Snowflake using environment variables."""
    return connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

def load_to_snowflake(record: dict) -> bool:
    """Loads a single patient record into the Snowflake staging table."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Example insert statement - adjust based on your schema
        query = """
            INSERT INTO clinical_data (mrn, visit_date, diagnosis)
            VALUES (%(MRN)s, %(date)s, %(diagnosis)s)
        """
        cursor.execute(query, record)
        conn.commit()
        cursor.close()
        conn.close()
        return True
        
    except Exception as e:
        logging.error(f"Failed to load record {record.get('MRN')}: {e}")
        return False
