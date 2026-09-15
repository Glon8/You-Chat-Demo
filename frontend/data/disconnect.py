import json

from .values import op, set_ERR, get_WS
from .helpers import file_update, getDir
from .link_listener import dont_listen
from .connect import stop_waiting


def dsc():
    gnr = op['gnr']

    gnr["ws_lnk"] = "ws://"

    file_update(getDir(), 'config.json', gnr)

    ws = get_WS()

    if not ws:
        stop_waiting()
    else:
        ws.send(
            json.dumps(
                {
                     "snd_id": gnr["snd_id"],
                     "req_type": "dsc",
                }
            )
        )

        dont_listen()

    set_ERR('')