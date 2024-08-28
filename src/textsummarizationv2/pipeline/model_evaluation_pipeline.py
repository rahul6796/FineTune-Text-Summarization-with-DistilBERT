



from typing import Any
from src.textsummarizationv2.config.configuration import ConfigurationManager
from src.textsummarizationv2.components.model_evaluation import ModelEvaluation




class ModelEvaluationPipeline:

    def __init__(self) -> None:
        pass



    def main(self):
        config = ConfigurationManager()
        model_evaluation_config =  config.get_model_evaluation_config()
        model_evalution = ModelEvaluation(config=model_evaluation_config)
        model_evalution.evaluation()

        