import json 

def Json(file_path):
    """Read a JSON file and return its contents as a dictionary."""
    with open(file_path, 'r') as f:
        return json.load(f)