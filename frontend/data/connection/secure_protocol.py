from ..values import op
from ..helpers import file_update, getDir

def sprt():
    gnr = op.get('gnr')

    gnr['sprt'] = not gnr.get('sprt', False)

    file_update(getDir(), 'config.json', gnr)