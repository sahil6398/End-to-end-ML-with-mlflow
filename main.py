from ml_project import logger
from ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ml_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from ml_project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from ml_project.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from ml_project.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
import os

os.environ["MLFLOW_TRACKING_USERNAME"] = "sahil6398"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "ef0215b239a6d62811942fcaa35ed6655409ca2e"
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/sahil6398/End-to-end-ML-with-mlflow.mlflow"

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")    

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

