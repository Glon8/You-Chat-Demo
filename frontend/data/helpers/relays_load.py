import json

from ..values import rel
from .read_file import read_file
from .get_dir import get_dir
from .write_file import write_file


def relays_load():
    data = read_file(f'{get_dir()}/relays.json')

    if data:
        data = json.loads(data)
        # strict verification needed
        if not data:
            return

        for item in data:
            rel.append(item)
    else:
        write_file(get_dir(), 'relays.json', {})
