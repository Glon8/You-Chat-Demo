from .values import msg, cnt, spr, op, set_ERR


def vmsg():
    print(f'{spr} MESSAGES')

    if not msg:
        print(f'[No messages]')
        return

    user = op['gnr']['snd_id']

    contact = input('contact id or name > ')

    if contact not in cnt and contact not in cnt.values():
        set_ERR("[Provided user not in contacts]")
        input('Press ENTER to continue...')
        return
    else:
        if contact in cnt:
            cnt_id = contact
            cnt_name = cnt[contact]
        else:
            cnt_id = next(key for key, value in cnt.items() if value == contact)
            cnt_name = contact

    chat = msg.get(cnt_id)

    if not chat:
        set_ERR("[There no chat with this contact]")
        input('Press ENTER to continue...')
        return

    for message in chat:
        if message['snd'] == cnt_id:
            name = cnt_name
        elif message['snd'] == user:
            name = 'Me'
        else:
            name = cnt_id

        print(
            f"[{name}][{message['timestamp']}]:"
            f"{message['msg']}"
        )

    input('Press ENTER to continue...')
