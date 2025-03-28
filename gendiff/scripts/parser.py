import json
import os

import yaml


def parse_json(file):
    return json.load(file)


def parse_yaml(file):
    return yaml.safe_load(file)


def parse_file(file_path):
    with open(file_path, "r") as f:
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension in ('.yaml', '.yml'):
            return parse_yaml(f)
        
        elif file_extension == '.json':
            return parse_json(f)
            
