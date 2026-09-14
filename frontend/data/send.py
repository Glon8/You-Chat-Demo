import json
import time

from .values import op, ld, get_WS, cnt
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
    ws = get_WS()

    if ws:
        ws.send(
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
    else:
        err_pop("Current WebSocket not accessible")


    add_pending(gnr["snd_id"], gnr["rcv_id"], now_time, MSG)
