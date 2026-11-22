import threading
import websocket
import time

from ..values import op, set_WS, set_ERR, get_ERR, cnt, get_WS
from ..core_threads.link_listener import listen, dont_listen
from .update import update
from ..relay_api.ping import relay_ping

from ..helpers.get_prefix import get_prefix
from ..helpers.err_pop import err_pop
from ..helpers.request_sender import request_sender

_KILL = threading.Event()
_OPEN_THREAD = None
ping = True


def cnn():
    global ping
    global _OPEN_THREAD

    gnr = op['gnr']

    if not gnr["ws_lnk"]:
        if not get_ERR():
            set_ERR("[Current WebSocket not accessible]")
    # pinging to relay
    ping = relay_ping()
    # check if relay is offline
    if not ping and (_OPEN_THREAD is None or not _OPEN_THREAD.is_alive()):
        _OPEN_THREAD = threading.Thread(target=wait_ping, daemon=True)
        _OPEN_THREAD.start()
        return

    ws = get_WS()

    if ws is not None and ws.connected:
        ws.close()
        dont_listen()
        time.sleep(10)  # < temporary solution, for async await issue (useEffect on js)

    try:
        ws = websocket.create_connection(get_prefix('ws') + gnr["ws_lnk"])
    except Exception as e:
        if not get_ERR():
            set_ERR(f"[Current WebSocket not accessible]")

        err_pop(e)

    set_WS(ws)

    _SEND = request_sender("cnn", {})

    if not _SEND:
        if not get_ERR():
            set_ERR(f"[Current WebSocket not accessible]")
    # starting to listen to the relay
    listen()
    # cleaning error message
    set_ERR('')
    # wait for registration to take place
    # <================================== ISSUE TO GET SOLVED
    # Should wait longer because lack of knowledge when the relay may ask for list sharing, that adds to pending -
    # time, original waiting time - 0.3 sec.
    # Solutions:
    # * Add a timer as on the relay.
    # * Check when the relay makes registration.
    # * Make a relay drop a response back by http.
    time.sleep(2)
    # send update call to every contact in a list
    for key, cnt_info in cnt.items():
        update(key, None)


def wait_ping():
    # import global values
    global _KILL
    global ping

    if not get_ERR():
        set_ERR("[No ping for current WebSocket]")
    # RELAY SLEEP check
    # await shortly
    _KILL.wait(timeout=15)
    # ping to check if relay already awaken
    if not _KILL.is_set():
        ping = relay_ping()
    # HEART BEAT check
    # pinging until positive reply
    while not ping and not _KILL.wait(timeout=30):
        ping = relay_ping()

    if _KILL.is_set():
        _KILL.clear()
        return

    set_ERR("")

    cnn()


def ws_ping():
    # import global value
    global _OPEN_THREAD
    # if there ISNT open thread or that ISNT 'alive'
    if _OPEN_THREAD is None or not _OPEN_THREAD.is_alive():
        _OPEN_THREAD = threading.Thread(target=wait_ping, daemon=True)
        _OPEN_THREAD.start()


def stop_waiting():
    # import global values
    global _KILL
    global _OPEN_THREAD

    # if _KILL is false and there IS open thread that IS 'alive'
    if not _KILL.is_set() and _OPEN_THREAD is not None and _OPEN_THREAD.is_alive():
        # switch _KILL to true
        _KILL.set()
