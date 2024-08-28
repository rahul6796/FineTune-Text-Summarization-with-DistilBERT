

from src.textsummarizationv2.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textsummarizationv2.pipeline.data_validation_pipeline import DataValidationPipeline
from src.textsummarizationv2.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.textsummarizationv2.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.textsummarizationv2.logging import logger

stage_name = "Data Ingestion"

try:
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"Data ingestion completed successfully for stage: {stage_name}")
except Exception as e:
    logger.error(f'main data ingestion : : {e}')

stage_name = "Data Validation"

try:
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f"Data validation completed successfully for stage: {stage_name}")
except Exception as e:
    logger.error(f'main data vaidation : : {e}')


stage_name = "Data Transformation"

try:
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f"Data transformation completed successfully for stage: {stage_name}")
except Exception as e:
    logger.error(f'main data transformation : : {e}')



stage_name = "model trainer"

try:
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f"Model Trainer completed successfully for stage: {stage_name}")
except Exception as e:
    logger.error(f'Model Trainer : : {e}')