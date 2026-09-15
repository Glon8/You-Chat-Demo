import time
import json

from .values import cnt, msg, get_WS, op


def update(cnt_id, timestamp):
    # check if cnt_id in cnt
    if cnt_id and cnt_id not in cnt or not get_WS():
        return

    chat = msg.get(cnt_id)
    package = []

    if timestamp:
        tm_stm = None

        if chat:
            for message in chat:
                if message.get('tm_stm') > timestamp:
                    package.append(message)
    else:
        if not chat:
            chat = []

        tm_stm = max((m.get('tm_stm') for m in chat if m.get('snd_id') == cnt_id), default=None) or cnt.get(cnt_id).get('last_seen')

        if chat:
            for message in chat:
                if message.get('tm_stm') > tm_stm:
                    package.append(message)

    MSG = {'tm_stm': tm_stm, 'msg_snc': package}

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
