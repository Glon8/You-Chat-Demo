import json

from .values import op, ld, set_RPL, set_ERR, get_ERR, msg, msg_instance, get_RPL, get_WS
from .helpers import file_update, getDir, append_message


def snd():
    if not ld:
        gnr = op["gnr"]
        MSG = input("message > ")

        get_WS().send(
            json.dumps(
                {
                    "snd_id": gnr["snd_id"],
                    "rcv_id": gnr["rcv_id"],
                    "req_type": "msg",
                    "trn_dt": MSG,
                }
            )
        )

        msg_instance(gnr["rcv_id"])

        append_message(gnr["rcv_id"], gnr["snd_id"], MSG)

        set_RPL(json.loads(get_WS().recv()))

        append_message(gnr["rcv_id"], gnr["rcv_id"], get_RPL()['trn_dt'])

        file_update(getDir(), 'chats.json', msg)

        set_ERR('')

    elif not get_ERR():
        set_ERR("[Current WebSocket not accessible]")
