import time

from ..values import cnt, msg, get_WS, op

from ..helpers.err_pop import err_pop
from ..helpers.request_sender import request_sender


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
        # set 'last seen' timestamp
        ls_tm_stm = (
                max(((m.get('trn_dt') or {}).get('tm_stm') for m in chat if m.get('snd_id') == cnt_id), default=None) or
                cnt.get(cnt_id).get('last_seen')
        )
        # if chat is a list and not empty
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
    dt = {'ls_tm_stm': ls_tm_stm, 'dt_snc': package}
    transfer_data = {"tm_stm": time.time(), "data": dt}
    # try to send through websocket
    _SENT = request_sender("upd", transfer_data)

    if not _SENT:
        # inform
        err_pop('Error: Failed to send the update!')
