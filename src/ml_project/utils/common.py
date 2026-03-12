import os
import box.exceptions import BoxvalueError
import yaml
from ml_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    """
    Reads a yaml file and returns a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the yaml file.
    Raises:
        ValueError: If the yaml file is empty.
    Returns:
        ConfigBox: ConfigBox object containing the yaml file data.

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxvalueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list[Path], verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: Any):
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as json_file:
        content = json.load(json_file)
    logger.info(f"json file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"