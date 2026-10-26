import time

from ..values import rel
from ..helpers import file_update, getDir, get_prefix


def arel():
    rel_link = get_prefix('ws') + input('relay link > ')
    name = input('relay name > ')

    rel[name] = {
        'link': rel_link,
        'last_seen': time.time(),
        'reported': False
    }

    file_update(getDir(), 'relays.json', rel)
