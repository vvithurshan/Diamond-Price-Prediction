import os
import sys # for logging and exception
from src.logger import logging
from srs.exception import CustomException

import  pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
# Initialize the Data Ingestion Configuration

# Defining Paths where I need to save my train, test, and raw data
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')

## Create Data Ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')
        try: 
            df = pd.read_csv(os.path.join('notebooks/data', 'gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.mkdirs(os.path.join(self.ingestion_config.raw_data_path), exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path, index = False)
            logging.info('Raw Data is created')

            train_set, test_set = train_test_split(df, test_size = 0.30, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            logging.info('Ingestion of Data is Completed')

            return (
                self.ingestion_config.train_path,
                self.ingestion_config.test_path
            )

        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e, sys)