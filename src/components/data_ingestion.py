# Components are all the modules which are we going to create.

# DATA INGESTION : Reading the dataset from database or other file locations or diffrent
#                  kinds of databases also.

# Initially we need to read the database. Reading the data from specefic database process is 
# called as data ingestion.

# It will have all the code to reading the data.

# We can divide data into train and test.



import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from exception import CustomException
from logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig



@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts',"train.csv")
    test_data_path = os.path.join('artifacts',"test.csv")
    row_data_path = os.path.join('artifacts',"data.csv")

class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component.")
        try:
            df = pd.read_csv('Notebook/data/stud.csv')
            logging.info("Read the dataset as dataframe.")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)

            df.to_csv(self.ingestion_config.row_data_path, index = False, header = True)

            logging.info("Train test split initiated.")
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)

            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info("Ingestion of the data is completed.")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data =obj.initiate_data_ingestion()

    data_transformation = DataTransformation()  
    data_transformation.initiate_data_transformation(train_data, test_data)