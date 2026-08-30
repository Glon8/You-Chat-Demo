import websocket
import json
import random

from data.values import op, set_LD, ld, ws, set_WS
from data.visuals import render, render_msg
from data.handlers.link_update import lnk_upd
from data.handlers.send import snd


def control_pannel():
    gnr = op["gnr"]
    err_msg = ""

    while True:
        render()

        if err_msg:
            print(err_msg)

        render_msg()

        npt = input("> ")

        if npt == "upd_lnk":
            lnk_upd()
        if npt == "upd_rcv":
            gnr["rcv_id"] = input("new receiver > ")
        if npt == "snd":
            snd()
        if npt == "dsc":
            gnr["ws_lnk"] = "ws://"

            if not ld():
                ws().send(
                    json.dumps(
                        {
                            "snd_id": gnr["snd_id"],
                            "req_type": "dsc",
                        }
                    )
                )


def main():
    gnr = op["gnr"]

    gnr["snd_id"] = random.randint(1000, 9999)

    try:
        ws = websocket.create_connection("ws://localhost:5173")

        set_WS(ws)

        set_LD(False)

        ws.send(
            json.dumps(
                {
                    "snd_id": gnr["snd_id"],
                    "req_type": "cnn",
                }
            )
        )
    except Exception:
        set_LD(True)

    control_pannel()


if __name__ == "__main__":
    main()
