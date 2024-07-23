from src.logger import logging
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME="Data Ingestion Stage"
try:
    logging.info(f">>> stage {STAGE_NAME} started<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>> stage {STAGE_NAME} completed<<<")
except Exception as e:
    logging.exception(e)
    raise e