from ..values import rel

from ..helpers.write_file import write_file
from ..helpers.get_dir import get_dir
from ..helpers.err_pop import err_pop


def rrel():
    if not rel:
        err_pop("Relay list is empty")
        return

    relay = input('relay name or link > ')

    key = next(
        (
            name for name, data in rel.items()
            if name == relay or data.get('link') == relay
        ),
        None
    )

    if not key:
        err_pop("Relay isn't recognised")
        return

    rel.pop(key)

    write_file(get_dir(), 'relays.json', rel)

    err_pop("Relay has been successfully removed")
