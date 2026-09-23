import time

from ..values import rel
from ..helpers import file_update, getDir


def arel():
    rel_link = "ws://" + input('relay link > ')
    name = input('relay name > ')

    rel[name] = {
        'link': rel_link,
        'last_seen': time.time(),
        'reported': False
    }

    file_update(getDir(), 'relays.json', rel)
