import json
import threading
import time

from ..values import get_WS, cnt, get_ERR, set_ERR
from ..helpers import add_pending, err_pop, file_update, getDir
from ..connection.update import update

_KILL = threading.Event()

_OPEN_THREAD = None


def lnk_lst():
    global _KILL

    while not _KILL.is_set():  # initially was just True
        if not get_WS():
            return

        try:
            # listen for incoming package
            package = get_WS().recv()
            # parse the package from JSON
            unload = json.loads(package)
            # create shorthand
            ul = unload
            # get package sender
            snd = ul.get("snd_id")
            # check is it a message call
            if ul['req_type'] == 'msg':
                # if a request type is a message, pass to pending
                add_pending(ul.get("snd_id"), ul.get("rcv_id"), ul.get('tm_stm'), ul.get('trn_dt'))
            # check is it an update call
            elif ul['req_type'] == 'upd':
                # extract data
                dt = ul['trn_dt']
                # extract timestamp
                tm_stm = dt.get('tm_stm')
                # if there is a timestamp, send update in return
                if tm_stm:
                    update(ul.get("snd_id"), tm_stm)
                # pass all the received messages to pending
                for msg in dt.get('msg_snc'):
                    add_pending(msg.get("snd_id"), msg.get("rcv_id"), msg.get('tm_stm'), msg.get('msg'))
            # check if a sender is in contacts, update its "last_seen" tag to now
            if snd in cnt:
                cnt[snd]['last_seen'] = time.time()
                # overwrite contacts - save
                file_update(getDir(), 'contacts.json', cnt)
        except Exception as e:
            if not get_ERR():
                set_ERR("[Current WebSocket not accessible]")
            err_pop("Link listener has been crashed")
            break


def listen():
    global _KILL
    global _OPEN_THREAD

    if get_WS() and (not _OPEN_THREAD or not _OPEN_THREAD.is_alive()):
        _KILL.clear()

        _OPEN_THREAD = threading.Thread(target=lnk_lst, daemon=True)

        _OPEN_THREAD.start()


def dont_listen():
    global _KILL

    if not get_WS() and _OPEN_THREAD and _OPEN_THREAD.is_alive():
        _KILL.set()
