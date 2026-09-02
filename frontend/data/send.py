import json
import time

from .values import op, ld, get_WS, cnt
from .helpers import add_pending, err_pop


def snd():
    gnr = op["gnr"]
    if not ld and gnr['rcv_id'] in cnt:
        now_time = time.time()
        MSG = input("message > ")

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

        add_pending(gnr["snd_id"], gnr["rcv_id"], now_time, MSG)
    else:
        if gnr['rcv_id'] not in cnt:
            err_pop("Unknown number check your contacts")
        else:
            err_pop("Current WebSocket not accessible")
