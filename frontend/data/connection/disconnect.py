import json

from ..values import op, set_ERR, get_WS
from ..core_threads.link_listener import dont_listen
from .connect import stop_waiting


def dsc():
    try:
        get_WS().send(
            json.dumps(
                {
                    "snd_id": op['gnr']["snd_id"],
                    "req_type": "dsc",
                }
            )
        )

        dont_listen()
    except Exception as e:
        stop_waiting()

    set_ERR('')
