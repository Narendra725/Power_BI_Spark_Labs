import json
import os


def read_json(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except Exception as e:
        raise RuntimeError(f"Error reading json: {file_path}. Reason: {e}")


def create_folder(folder_path: str):
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        raise RuntimeError(f"Couldn't create folder: {folder_path}. Reason: {e}")


def create_or_replace_file(file_path: str, data: dict):
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        create_folder(folder)

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        raise RuntimeError(f"Error updating file: {file_path}. Reason: {e}")
