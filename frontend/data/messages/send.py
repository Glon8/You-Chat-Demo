import json
import time

from ..values import op, get_WS, cnt
from ..helpers import add_pending, err_pop


def snd():
    gnr = op["gnr"]

    if not gnr["rcv_id"]:
        err_pop("No receiver has been selected")
        return

    if gnr['rcv_id'] not in cnt:
        err_pop("Unknown number check your contacts")
        return

    dt = input("message > ")

    try:
        old = """
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
        """
        transfer_data = {
            "tm_stm": time.time(),
            "data": dt
        }

        get_WS().send(
            json.dumps(
                {
                    "snd_id": gnr["snd_id"],
                    "rcv_id": gnr["rcv_id"],
                    "req_type": "msg",
                    "trn_dt": transfer_data
                }
            )
        )
    except Exception as e:
        # inform
        err_pop("Message has been STORED and NOT SENT")

    old = """add_pending(gnr["snd_id"], gnr["rcv_id"], now_time, dt)"""
    add_pending(gnr["snd_id"], gnr["rcv_id"], transfer_data)