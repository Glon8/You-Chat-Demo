import json

from ..values import op, set_ERR, get_WS
from ..core_threads.link_listener import dont_listen
from .connect import stop_waiting

from ..helpers.def_reports import def_reports
from ..helpers.request_sender import request_sender


def dsc():
    if get_WS():
        request_sender("dsc",{})

        dont_listen()

        get_WS().close()
    else:
        stop_waiting()

    def_reports()

    set_ERR('')

"""
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
"""
