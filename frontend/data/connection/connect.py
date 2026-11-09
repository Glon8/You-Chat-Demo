import threading
import websocket
import json
import time

from ..values import op, set_WS, set_ERR, get_ERR, cnt, get_WS
from ..core_threads.link_listener import listen, dont_listen
from .update import update
from ..relay_api.ping import relay_ping
from ..helpers import get_prefix

_KILL = False
ping = True


def cnn():
    global ping

    gnr = op['gnr']

    if not gnr["ws_lnk"]:
        if not get_ERR():
            set_ERR("[Current WebSocket not accessible]")

    # pinging to relay
    ping = relay_ping()

    # check if relay is offline
    if not ping:
        threading.Thread(
            target=wait_ping,
            daemon=True
        ).start()
        return

    ws = get_WS()

    if ws:
        ws.close()
        dont_listen()
        time.sleep(10)  # < temporary solution, for async await issue (useEffect on js)

    try:
        ws = websocket.create_connection(get_prefix('ws') + gnr["ws_lnk"])

        set_WS(ws)

        ws.send(
            json.dumps(
                {
                    "snd_id": gnr["snd_id"],
                    "req_type": "cnn",
                }
            )
        )
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
    except Exception as e:
        if not get_ERR():
            set_ERR(f"[Current WebSocket not accessible]")


def wait_ping():
    global _KILL
    global ping

    if not get_ERR():
        set_ERR("[No ping for current WebSocket]")
    # RELAY SLEEP check
    # await shortly
    time.sleep(10)
    # ping to check if relay already awaken
    ping = relay_ping()
    # HEART BEAT check
    # pinging until positive reply
    while not ping and not _KILL:
        time.sleep(60)
        ping = relay_ping()

    if _KILL:
        _KILL = False
        return

    set_ERR("")

    cnn()


def stop_waiting():
    global _KILL

    _KILL = True
