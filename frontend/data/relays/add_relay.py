import time

from ..values import rel

from ..helpers.file_update import file_update
from ..helpers.get_dir import get_dir


def arel():
    rel_link = input('relay link > ')
    name = input('relay name > ')

    rel[name] = {
        'link': rel_link,
        'last_seen': time.time(),
        'reported': False
    }

    file_update(get_dir(), 'relays.json', rel)
