import yaml
import os
import json
from pathlib import Path
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from box import ConfigBox
from typing import Any
from logger import logging

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """This method takes in a path to yaml file and returns"""
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    # except BoxValueError:
    #     raise ValueError("Yaml file is empty.")
    except Exception as e:
        raise e

@ensure_annotations   
def create_directories(path_to_directories:list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at {path}")

@ensure_annotations
def save_json(path:Path, data:dict):

    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    logging.info(f"Json file saved at {path}")

@ensure_annotations
def get_size(path:Path)->str:

    """get size in KB

    args:
      path(Path): path of the file.

    Returns:
       str:size in KB
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"{size_in_kb} in KB"