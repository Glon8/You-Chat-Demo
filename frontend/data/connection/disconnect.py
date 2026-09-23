import json

from ..values import op, set_ERR, get_WS
from ..core_threads.link_listener import dont_listen
from .connect import stop_waiting
from ..helpers import def_reports


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

        get_WS().close()
    except Exception as e:
        stop_waiting()

    def_reports()

    set_ERR('')
