import json
import threading
import time

from .values import get_WS, cnt
from .helpers import add_pending, err_pop
from .update import update
from .connect import cnn

_KILL = False


def lnk_lst():
    global _KILL

    while True:
        try:
            if _KILL:
                _KILL = False
                break

            if not get_WS():
                return

            package = get_WS().recv()  # < receive package

            unload = json.loads(package)  # < parse JSON

            ul = unload  # < shorthand
            snd = ul.get("snd_id")

            if ul['req_type'] == 'msg':
                # if a request type is a message > pass to pending
                add_pending(ul.get("snd_id"), ul.get("rcv_id"), ul.get('tm_stm'), ul.get('trn_dt'))
            elif ul['req_type'] == 'upd':
                dt = ul['trn_dt']
                tm_stm = dt.get('tm_stm')

                if tm_stm:
                    update(ul.get("snd_id"), tm_stm)

                for msg in dt.get('msg_snc'):
                    add_pending(msg.get("snd_id"), msg.get("rcv_id"), msg.get('tm_stm'), msg.get('trn_dt'))

            # check if a sender is in contacts > update its "last_seen" tag to now
            if snd in cnt:
                cnt[snd]['last_seen'] = time.time()

        except Exception:
            err_pop("Link listener has been crashed")
            cnn()
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
