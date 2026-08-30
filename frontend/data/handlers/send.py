import json

from ..values import op, ld, ws, set_RPL


def snd():
    if not ld and ws():
        gnr = op["gnr"]
        msg = input("message > ")

        ws.send(
            json.dumps(
                {
                    "snd_id": gnr["snd_id"],
                    "rcv_id": gnr["rcv_id"],
                    "req_type": "msg",
                    "trn_dt": msg,
                }
            )
        )

        set_RPL(ws.recv())
    else:
        print("[Current WebSocket not accessible]")
