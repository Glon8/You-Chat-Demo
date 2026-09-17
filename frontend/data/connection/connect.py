import threading
import websocket
import json
import time

from ..values import op, set_WS, set_ERR, get_ERR, cnt
from ..core_threads.link_listener import listen
from .update import update
from ..relay_api.ping import relay_ping

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
    try:
        ws = websocket.create_connection(gnr["ws_lnk"])

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
        time.sleep(0.3)
        # send update call to every contact in a list
        for key, cnt_info in cnt.items():
            update(key, None)
    except Exception as e:
        if not get_ERR():
            set_ERR("[Current WebSocket not accessible]")


def wait_ping():
    global _KILL
    global ping

    if not get_ERR():
        set_ERR("[No ping for current WebSocket]")
    # pinging until positive reply
    while not ping:
        time.sleep(60)
        if _KILL:
            _KILL = False
            return
        ping = relay_ping()

    set_ERR("")

    cnn()


def stop_waiting():
    global _KILL

    _KILL = True
