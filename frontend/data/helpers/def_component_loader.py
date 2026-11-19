import json

from .read_file import read_file
from .get_dir import get_dir
from .write_file import write_file


def def_component_loader(file_name, local_var):
    data = read_file(f'{get_dir()}/{file_name}.json')

    if data:
        data = json.loads(data)
        # strict verification needed
        if not data:
            return

        for key, val in data.items():
            local_var[key] = val
    else:
        write_file(get_dir(), f'{file_name}.json', {})
