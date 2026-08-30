import json

from .values import op, ld, set_ERR, get_WS, get_ERR
from .helpers import file_update, getDir


def dsc():
    gnr = op['gnr']

    gnr["ws_lnk"] = "ws://"

    file_update(getDir(), 'config.json', gnr)

    if not ld:
        get_WS().send(
            json.dumps(
                {
                    "snd_id": gnr["snd_id"],
                    "req_type": "dsc",
                }
            )
        )

        set_ERR('')
    elif not get_ERR():
        set_ERR("[Current WebSocket not accessible]")
