import json
import threading
import time

from ..values import get_WS, cnt, get_ERR, set_ERR
from ..helpers import add_pending, err_pop, file_update, getDir
from ..connection.update import update

_KILL = threading.Event()

_OPEN_THREAD = None


def lnk_lst():
    # get a global value
    global _KILL
    # while _KILL is not false
    while not _KILL.is_set():
        # if no websocket > return
        if not get_WS():
            return

        try:
            # listen for incoming package
            package = get_WS().recv()
            # parse the package from JSON
            unload = json.loads(package)
            # create shorthand
            ul = unload
            print(ul)
            # get package sender
            snd = ul.get("snd_id")
            # check is it a message call
            if ul.get('req_type') == 'msg':
                # if a request type is a message, pass to pending
                old = """add_pending(ul.get("snd_id"), ul.get("rcv_id"), ul.get('tm_stm'), ul.get('trn_dt'))"""
                add_pending(ul.get("snd_id"), ul.get("rcv_id"), ul.get('trn_dt'))
            # check is it an update call
            elif ul['req_type'] == 'upd':
                # extract data
                dt = ul['trn_dt']
                # extract 'last seen' timestamp
                old = """tm_stm = dt.get('tm_stm')"""
                ls_tm_stm = (dt.get('data') or {}).get('ls_tm_stm')
                # if there is a 'last seen' timestamp, send update in return
                if ls_tm_stm:
                    update(ul.get("snd_id"), ls_tm_stm)
                # extract sync_data
                sync_data = dt.get('dt_snc')
                # if sync_data IS a list and ISNT empty > pass all the received messages to pending
                if isinstance(sync_data, list) and sync_data:
                    for msg in sync_data:
                        old = """add_pending(msg.get("snd_id"), msg.get("rcv_id"), msg.get('tm_stm'), msg.get('msg'))"""
                        add_pending(msg.get("snd_id"), msg.get("rcv_id"), msg.get('trn_dt'))
            # check if a sender is in contacts, update its "last_seen" tag to now
            if snd in cnt:
                cnt[snd]['last_seen'] = time.time()
                # overwrite contacts - save
                file_update(getDir(), 'contacts.json', cnt)
        except Exception as e:
            # inform
            if not get_ERR():
                set_ERR("[Current WebSocket not accessible]")
            err_pop("Link listener has been crashed")
            break


def listen():
    # get a global values
    global _KILL
    global _OPEN_THREAD
    # if there IS a websocket and there is NO open thread OR NO 'alive' threat
    if get_WS() and (not _OPEN_THREAD or not _OPEN_THREAD.is_alive()):
        # set _KILL to true
        _KILL.clear()
        # append new thread
        _OPEN_THREAD = threading.Thread(target=lnk_lst, daemon=True)
        # init the thread
        _OPEN_THREAD.start()


def dont_listen():
    # get a global value
    global _KILL
    # if NO websocket and there IS open thread that IS 'alive'
    if not get_WS() and _OPEN_THREAD and _OPEN_THREAD.is_alive():
        # switch _KILL to false
        _KILL.set()
