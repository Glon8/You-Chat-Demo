from ..values import op, rel

from .file_update import file_update
from .get_dir import get_dir


def def_reports():
    gnr = op.get('gnr')

    for key, item in rel.items():
        if item.get("link") == gnr["ws_lnk"]:
            item['reported'] = True
        else:
            item['reported'] = False

    file_update(get_dir(), 'relays.json', rel)
