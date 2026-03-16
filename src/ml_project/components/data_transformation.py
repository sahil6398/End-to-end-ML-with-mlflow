from ml_project import logger
import os
from ml_project.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        logger.info("Reading data for data transformation")
        data = pd.read_csv(self.config.data_path)
        logger.info("Splitting data into train and test")
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        logger.info("Saving transformed data")
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into test and train splits")
        logger.info(train.shape)
        logger.info(test.shape)
