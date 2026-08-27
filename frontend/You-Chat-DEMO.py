import websocket
import json
import random

from data.values import op
from data.visuals import render

ws = None
ld = False


def control_pannel():
    global ws
    global ld

    gnr = op["gnr"]
    data = None
    err_msg = ""

    while True:
        render()

        if err_msg:
            print(err_msg)

        if data:
            data = json.loads(data)
            print(f"\r\n[{data['snd_id']}]> {data['trn_dt']}\r\n")
            data = None

        npt = input("> ")

        if npt == "upd_lnk":
            gnr["ws_lnk"] = "ws://" + input("new link > ")
            try:
                ws = websocket.create_connection(gnr["ws_lnk"])
                ld = False
                ws.send(
                    json.dumps(
                        {
                            "snd_id": gnr["snd_id"],
                            "req_type": "cnn",
                        }
                    )
                )
            except:
                ld = True
        if npt == "upd_rcv":
            gnr["rcv_id"] = input("new receiver > ")
        if npt == "snd":
            if not ld:
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

                data = ws.recv()
            else:
                print("[Current WebSocket not accessible]")
        if npt == "dsc":
            gnr["ws_lnk"] = "ws://"

            if not ld:
                ws.send(
                    json.dumps(
                        {
                            "snd_id": gnr["snd_id"],
                            "req_type": "dsc",
                        }
                    )
                )


def main():
    global ws
    global ld

    gnr = op["gnr"]

    gnr["snd_id"] = random.randint(1000, 9999)

    try:
        ws = websocket.create_connection("ws://localhost:5173")
        ld = False
        ws.send(
            json.dumps(
                {
                    "snd_id": gnr["snd_id"],
                    "req_type": "cnn",
                }
            )
        )
    except:
        ld = True

    control_pannel()


if __name__ == "__main__":
    main()
