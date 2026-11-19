import json

from .read_file import read_file
from .write_file import write_file


def file_update(file_path, file_name, data):
    saved_data = read_file(file_name)

    if saved_data:
        saved_data = json.loads(saved_data)
    else:
        saved_data = {}

    saved_data.update(data)

    write_file(file_path, file_name, saved_data)
