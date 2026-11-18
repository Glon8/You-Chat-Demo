import time
import json

from ..values import cnt, msg, get_WS, op
from ..helpers import err_pop


def update(cnt_id, tm_stm):
    # check if cnt_id in cnt
    if cnt_id and cnt_id not in cnt or not get_WS():
        return
    # get the chat with the contact
    chat = msg.get(cnt_id)
    # init empty package
    package = []
    # if update includes timestamp
    if tm_stm:
        # set 'last seen' timestamp
        ls_tm_stm = None
        # if chat is a list and not empty
        if isinstance(chat, list) and chat:
            for message in chat:
                msg_tm_stm = (message.get('trn_dt') or {}).get('tm_stm')

                if isinstance(msg_tm_stm, (int, float)) and msg_tm_stm > tm_stm:
                    package.append(message)
    # if there is no timestamp
    else:
        old = """if not chat:
            chat = []"""
        # set 'last seen' timestamp
        ls_tm_stm = (
                max((m.get('tm_stm') for m in chat if m.get('snd_id') == cnt_id), default=None) or
                cnt.get(cnt_id).get('last_seen')
        )
        # if chat is a list and not empty
        old = """if chat:"""
        if isinstance(chat, list) and chat:
            for message in chat:
                msg_tm_stm = (message.get('trn_dt') or {}).get('tm_stm')
                if (
                        isinstance(msg_tm_stm, (int, float)) and
                        msg_tm_stm > ls_tm_stm and
                        message.get('snd_id') == op.get('gnr').get('snd_id')
                ):
                    package.append(message)
    # pack the data
    old = """MSG = {'tm_stm': tm_stm, 'msg_snc': package}"""
    dt = {'ls_tm_stm': ls_tm_stm, 'dt_snc': package}
    # try to send through websocket
    try:
        old = """
        get_WS().send(
            json.dumps(
                {
                    "snd_id": op.get('gnr').get("snd_id"),
                    "rcv_id": cnt_id,
                    "req_type": "upd",
                    "trn_dt": MSG,
                    "tm_stm": time.time()
                }
            )
        )
        """
        get_WS().send(
            json.dumps(
                {
                    "snd_id": op.get('gnr').get("snd_id"),
                    "rcv_id": cnt_id,
                    "req_type": "upd",
                    "trn_dt": {
                        "tm_stm": time.time(),
                        "data": dt
                    },
                }
            )
        )
    except Exception as e:
        err_pop('Error: Failed to send the update!')
