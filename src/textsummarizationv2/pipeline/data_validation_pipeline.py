

from src.textsummarizationv2.config.configuration import ConfigurationManager
from src.textsummarizationv2.components.data_validation import DataValidation



class DataValidationPipeline:

    def __init__(self) -> None:
        pass
        

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
        

