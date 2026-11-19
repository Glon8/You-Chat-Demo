import json
import random

from ..values import op
from .read_file import read_file
from .get_dir import get_dir
from .write_file import write_file


def config_load():
    gnr = op['gnr']
    data = read_file(f'{get_dir()}/config.json')

    if data:
        data = json.loads(data)
        # strict verification needed
        if not data:
            return

        for key, val in gnr.items():
            if gnr[key] != data[key]:
                gnr[key] = data[key]
    else:
        gnr["snd_id"] = str(random.randint(1000, 9999))

        data = {}

        for key, val in gnr.items():
            data[key] = gnr[key]

        write_file(get_dir(), 'config.json', data)
