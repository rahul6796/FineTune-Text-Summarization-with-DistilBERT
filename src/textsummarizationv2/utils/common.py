

import os 
from src.textsummarizationv2.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import yaml



@ensure_annotations
def read_yaml(path_to_yaml: Path, verbose = True) -> ConfigBox:
    """
    Args:
        path_to_yaml: input like path.
    Return:
        ConfigBox: ConfigBox object containing the configuration from the yaml files.
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml_path : {yaml_file} load successfully !')
            return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error reading yaml file: {e}")


@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):

    """
    this method are used to create directores.

    Args:
        path_to_directories: input like path.
    Return:
        None
    """

    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory {path} created successfully !")
    except Exception as e:
        logger.error(f'error raised from create directories : : {e}')


@ensure_annotations
def get_size(path: Path) -> int:
    """
    this method return the size of file.

    Args:
        path: input like path.
    Returns:
        size: size of file.
    """
    try:
        size_in_kb = os.path.getsize(path/1024)
        return f"~ size in{size_in_kb} kb"
    except Exception as e:
        logger.error(f'error is raised from get size function :; {e}')
