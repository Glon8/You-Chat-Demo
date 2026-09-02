import websocket
import json

from .values import op, set_WS, set_LD, set_ERR, get_ERR
from .link_listener import listen


def cnn():
    gnr = op['gnr']

    if not gnr["ws_lnk"]:
        set_LD(True)

        if not get_ERR():
            set_ERR("[Current WebSocket not accessible]")

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

        listen()

        set_LD(False)
        set_ERR('')
    except Exception:
        set_LD(True)
        if not get_ERR():
            set_ERR("[Current WebSocket not accessible]")
