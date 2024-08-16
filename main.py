from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_data
import time
import datetime
import logging

# Logger initialization
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)

if __name__ == '__main__':
  logging.info(f"Starting data pipeline at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
  
  # STEP 1
  print("...................", "\n")
  logging.info(f"STEP 1: Extracting data...")
  t0 = time.time()
  data = extract_data()
  t1 = time.time()
  logging.info(f"---> STEP 1: Data Extracted Completed in {str(t1-t0)} seconds")

  # STEP 2
  print("...................", "\n")
  logging.info("STEP 2: Transforming data...")
  t0 = time.time()
  df = transform_data(data)
  t1 = time.time()
  logging.info(f"---> STEP 2: Data Transformed Completed in {str(t1-t0)} seconds")

  # STEP 3
  print("...................", "\n")
  logging.info("STEP 3: Loading data to database...")
  t0 = time.time()
  load_data(df)
  t1 = time.time()
  logging.info(f"---> STEP 3: Data Loaded Completed in {str(t1-t0)} seconds")

  print("...................", "\n")
  logging.info(f"Data pipeline compelted at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")