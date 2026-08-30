import websocket
import json

from ..values import op, set_LB, set_WS


def lnk_upd():
    gnr = op["gnr"]

    gnr["ws_lnk"] = "ws://" + input("new link > ")

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
        
        set_LB(False)
    except Exception:
        set_LB(True)
