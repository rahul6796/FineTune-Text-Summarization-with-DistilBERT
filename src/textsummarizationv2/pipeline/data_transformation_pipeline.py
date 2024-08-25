


from src.textsummarizationv2.config.configuration import ConfigurationManager
from src.textsummarizationv2.components.data_transformation import DataTransformation



class DataTransformationPipeline:

    def __init__(self) -> None:
        pass 


    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
