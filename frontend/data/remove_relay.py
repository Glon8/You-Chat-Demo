from .values import rel
from .helpers import write_file, getDir, err_pop


def rrel():
    if not rel:
        err_pop("Relay list is empty")
        return

    relay = input('relay name or link > ')

    item = next(
        (
            data for data in rel
            if data.get("name") == relay or data.get("link") == 'ws://' + relay
        ), None
    )

    if not item:
        err_pop("Relay isn't recognised")
        return

    rel.remove(item)

    write_file(getDir(), 'relays.json', rel)

    err_pop("Relay has been successfully removed")