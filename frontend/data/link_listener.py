import json
import threading

from .values import get_WS
from .helpers import add_pending, err_pop

_KILL = False


def lnk_lst():
    global _KILL

    while True:
        try:
            if _KILL:
                _KILL = False
                break

            package = get_WS().recv()  # < receive package

            unload = json.loads(package)  # < parse JSON

            ul = unload  # < shorthand

            add_pending(ul["snd_id"], ul["rcv_id"], ul['tm_stm'], ul['trn_dt'])  # < pass to pending
        except Exception:
            err_pop("Link listener has been crashed")
            break


def listen():
    if get_WS():
        threading.Thread(
            target=lnk_lst,
            daemon=True
        ).start()


def dont_listen():
    global _KILL

    _KILL = True
