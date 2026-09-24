from ..values import rel
from ..helpers import write_file, getDir, err_pop


def rrel():
    if not rel:
        err_pop("Relay list is empty")
        return

    relay = input('relay name or link > ')

    key = next(
        (
            name for name, data in rel.items()
            if name == relay or data.get('link') == 'wss://' + relay
        ),
        None
    )

    if not key:
        err_pop("Relay isn't recognised")
        return

    rel.pop(key)

    write_file(getDir(), 'relays.json', rel)

    err_pop("Relay has been successfully removed")
