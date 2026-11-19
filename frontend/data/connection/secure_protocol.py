from ..values import op

from ..helpers.file_update import file_update
from ..helpers.get_dir import get_dir


def sprt():
    gnr = op.get('gnr')

    gnr['sprt'] = not gnr.get('sprt', False)

    file_update(get_dir(), 'config.json', gnr)
