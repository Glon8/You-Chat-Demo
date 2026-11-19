import threading

from ..values import op, pnd, msg, msg_instance

from ..helpers.file_update import file_update
from ..helpers.get_dir import get_dir

_KILL = False

"""
OLD
{
    "snd_id",      - sender number
    "rcv_id",      - receiver number
    "tm_stm",      - message creation timestamp
    "rcv_tm_stm",  - receive timestamp     <- created locally upon receive
    "msg"          - message content       <- ENCRYPTED
}
NEW
{
    "snd_id",      - sender number
    "rcv_id",      - receiver number
    "rcv_tm_stm",  - receive timestamp     <- created locally upon receive
    "trn_dt": {    - transferred data      <- ENCRYPTED
        "tm_stm",  - message creation timestamp
        "data"     - message content
    }
}
"""


def msg_mng():
    # get a global value
    global _KILL

    while True:
        # if _KILL is true > set _KILL to false
        if _KILL:
            _KILL = False
            break
        # values init
        cluster = 100
        rcv_lst = []
        # pending to active messages
        while cluster > 0 and pnd:
            package = pnd.pop(0)
            # unpack
            user_id = (op.get('gnr') or {}).get('snd_id')
            snd_id = str(package.get('snd_id'))
            rcv_id = str(package.get('rcv_id'))
            # find chat id
            chat_id = snd_id if snd_id != user_id else rcv_id
            # pass unknown number to .trash
            if not chat_id:
                chat_id = '.trash'
            # convert chat_id to string
            chat_id = str(chat_id)
            # if no chat with such id, create one
            if chat_id not in msg:
                msg_instance(chat_id)
            # check for a duplicate message by timestamp and value
            if not any(
                    MSG.get('snd_id') == snd_id
                    and (MSG.get('trn_dt') or {}).get('tm_stm') == (package.get('trn_dt') or {}).get('tm_stm')
                    and (MSG.get('trn_dt') or {}).get('data') == (package.get('trn_dt') or {}).get('data')
                    for MSG in msg[chat_id]
            ):
                # pass the package to the chat
                msg[chat_id].append(package)
                # if chat_id is a contact, add it to received list
                if chat_id != ".trash":
                    rcv_lst.append(chat_id)
            cluster -= 1

        for rcv in rcv_lst:
            msg[rcv].sort(key=lambda x: x["rcv_tm_stm"])

        rcv_lst.clear()
        # update local file
        if cluster < 100:
            file_update(get_dir(), 'chats.json', msg)


def manage():
    threading.Thread(
        target=msg_mng,
        daemon=True
    ).start()


def dont_manage():
    global _KILL

    _KILL = True
