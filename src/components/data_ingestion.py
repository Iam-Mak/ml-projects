import os
import sys
import pandas as pd

from src.exception import CustomException
from src.logger import logger

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    
    data_source: str = os.path.join('notebook', 'data', 'stud.csv')
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logger.info("Starting data ingestion process")
        try:
            df = pd.read_csv(self.ingestion_config.data_source)
            logger.info("Dataset loaded successfully")
            logger.info(f"Dataset shape: {df.shape}")

            if df.empty:
                raise ValueError("Dataset is empty")
            
        
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logger.info("Raw data saved")

            logger.info("Performing train-test split")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logger.info(f"Training data shape: {train_set.shape}")
            logger.info(f"Testing data shape: {test_set.shape}")
            logger.info("Data ingestion completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
        

''' 
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation
from src.utils import load_object  # if you saved the model

if __name__=="__main__":
    obj=DataIngestion()
    train_data, test_data=obj.initiate_data_ingestion()


    data_transformation = DataTransformation()
    train_arr, test_arr,_= data_transformation.initiate_data_transformation(train_data,test_data)
 
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))

    trained_model = load_object("artifacts/model.pkl")  # adjust path if needed

    # Step 5: Split test data into X_test and y_test
    X_test = test_arr[:, :-1]
    y_test = test_arr[:, -1]

    # Step 6: Evaluate model
    evaluator = ModelEvaluation(trained_model, X_test, y_test)
    metrics = evaluator.evaluate()
    print(metrics)
'''