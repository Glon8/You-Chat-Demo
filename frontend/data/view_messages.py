import threading
import time

from datetime import datetime

from .values import msg, cnt, spr, op
from .helpers import err_pop

_KILL = False

def vmsg():
    print(f'{spr} MESSAGES')

    if not msg:
        err_pop('No messages')
        return

    contact = input('contact id or name > ')

    if contact not in cnt and contact not in cnt.values():
        err_pop("Provided id/name not in contacts")
        cnt_id = contact
        cnt_name = 'Not in contacts'
    else:
        if contact in cnt:
            cnt_id = contact
            cnt_name = cnt[contact]
        else:
            cnt_id = next(key for key, value in cnt.items() if value == contact)
            cnt_name = contact

    chat = msg.get(cnt_id)

    if not chat:
        err_pop("There no chat with this contact")
        return

    visualize(cnt_id, cnt_name)

    input('===============================================<\r\n'
          ' Press ENTER to stop observe incoming messages |\r\n'
          '===============================================<\r\n')

    dont_visualize()

def msg_lst(cnt_id, cnt_name):
    global _KILL

    msg_cnt = 0

    time.sleep(0.1)

    while True:
        if _KILL:
            _KILL = False
            break

        chat = msg.get(cnt_id)

        if msg_cnt <= (len(chat) - 1):
            user = op['gnr']['snd_id']

            message = chat[msg_cnt]
            sender = message['snd_id']

            if sender == cnt_id:
                name = cnt_name
            elif sender == user:
                name = 'Me'
            else:
                name = cnt_id

            t = message['tm_stm']
            dt = datetime.fromtimestamp(t)

            print(
                f"[{name}]"
                f"[{dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}]:"
                f"{message['msg']}\r\n"
            )

            msg_cnt += 1

def visualize(cnt_id, cnt_name):
    threading.Thread(
        target=msg_lst,
        args=(cnt_id, cnt_name,),
        daemon=True
    ).start()

def dont_visualize():
    global _KILL

    _KILL = True
