import json
import os


def write_file(file_path, file_name, data):
    if not isinstance(file_path, str) or not os.path.exists(file_path):
        return None
    with open(f'{file_path}/{file_name}', 'w') as file:
        json.dump(data, file, indent=4)
