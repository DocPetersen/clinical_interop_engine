import logging
import datetime
import csv
from typing import List, Dict

def log_rejected_record(record: Dict, reason: str):
    """Handles logging of rejected records to a persistent file."""
    log_entry = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), record.get("MRN"), reason]
    with open('logs/rejected_records.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(['Timestamp', 'MRN', 'Error_Reason'])
        writer.writerow(log_entry)

def process_batch(record_list: List[Dict]) -> Dict[str, int]:
    """Processes a batch of records, delegating validation and loading."""
    stats = {"processed": 0, "success": 0, "failed": 0}
    
    # We import these locally or pass them in to avoid circular imports
    from src.validator import validate_patient_record
    from src.db_loader import load_to_snowflake
    
    for record in record_list:
        stats["processed"] += 1
        is_valid, reason = validate_patient_record(record)
        
        if is_valid:
            if load_to_snowflake(record):
                stats["success"] += 1
            else:
                stats["failed"] += 1
        else:
            log_rejected_record(record, reason)
            stats["failed"] += 1
            
    logging.info(f"Batch processing complete: {stats}")
    return stats
