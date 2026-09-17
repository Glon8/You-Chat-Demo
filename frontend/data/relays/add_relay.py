from ..values import rel
from ..helpers import alt_file_update, getDir


def arel():
    rel_link = "ws://" + input('relay link > ')
    name = input('relay name > ')

    rel.append(
        {
            'link': rel_link,
            'name': name,
            'last_seen': -1
        }
    )

    alt_file_update(getDir(), 'relays.json', rel)
