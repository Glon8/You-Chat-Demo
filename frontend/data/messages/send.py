import time

from ..values import op, cnt

from ..helpers.err_pop import err_pop
from ..helpers.add_pending import add_pending
from ..helpers.request_sender import request_sender


def snd():
    gnr = op.get("gnr")
    rcv = gnr.get("rcv_id")

    if not rcv:
        err_pop("No receiver has been selected")
        return

    if rcv not in cnt:
        err_pop("Unknown number check your contacts")
        return

    dt = input("message > ")

    transfer_data = {
        "tm_stm": time.time(),
        "data": dt
    }

    _SENT = request_sender("msg", transfer_data)

    if not _SENT:
        # inform
        err_pop("Message has been STORED and NOT SENT")

    add_pending(gnr["snd_id"], rcv, transfer_data)
