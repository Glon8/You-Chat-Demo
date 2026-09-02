import threading

from .values import op, pnd, msg, msg_instance
from .helpers import file_update, getDir, err_pop

_KILL = False


def msg_mng():
    global _KILL

    while True:
        if _KILL:
            _KILL = False
            break

        cluster = 100
        # pending to active messages
        while cluster > 0 and pnd:
            package = pnd.pop(0)

            user_id = op['gnr']['snd_id']
            snd_id = package.get('snd_id')
            rcv_id = package.get('rcv_id')

            chat_id = snd_id if snd_id != user_id else rcv_id

            if not chat_id:
                chat_id = '.trash'

            chat_id = str(chat_id)

            if chat_id not in msg:
                msg_instance(chat_id)

            msg[chat_id].append(package)

            cluster -= 1
        # update local file
        if cluster < 100:
            file_update(getDir(), 'chats.json', msg)


def manage():
    threading.Thread(
        target=msg_mng,
        daemon=True
    ).start()


def dont_manage():
    global _KILL

    _KILL = True
