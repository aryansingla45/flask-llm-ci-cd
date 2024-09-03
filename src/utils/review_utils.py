# src/utils/review_utils.py

import yaml
import os

def load_file(file_path, pipeline_type):
    """
    Load the content of the file based on the pipeline type.
    Currently handles YAML and plain text files.
    """
    _, file_extension = os.path.splitext(file_path)
    
    if pipeline_type.lower() == "yaml":
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        with open(file_path, 'r') as file:
            return file.read()
