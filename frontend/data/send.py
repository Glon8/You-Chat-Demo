import json
import time

from .values import op, get_WS, cnt
from .helpers import add_pending, err_pop


def snd():
    gnr = op["gnr"]

    if not gnr["rcv_id"]:
        err_pop("No receiver has been selected")
        return

    if gnr['rcv_id'] not in cnt:
        err_pop("Unknown number check your contacts")
        return

    now_time = time.time()
    MSG = input("message > ")

    try:
        get_WS().send(
            json.dumps(
                {
                    "snd_id": gnr["snd_id"],
                    "rcv_id": gnr["rcv_id"],
                    "req_type": "msg",
                    "trn_dt": MSG,
                    "tm_stm": now_time
                }
            )
        )
    except Exception as e:
        err_pop("Error: Failed to send the message")

    add_pending(gnr["snd_id"], gnr["rcv_id"], now_time, MSG)
