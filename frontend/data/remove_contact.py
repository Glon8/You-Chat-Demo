from .values import cnt, msg, set_ERR
from .helpers import write_file, getDir


def rcnt():
    contact = input('contact name or id > ')

    if contact not in cnt and contact not in cnt.values():
        set_ERR("[Provided user not in contacts]")
        input('Press ENTER to continue...')
        return
    else:
        if contact in cnt:
            cnt_id = contact
        else:
            cnt_id = next(key for key, value in cnt.items() if value == contact)

    cnt.pop(cnt_id)
    write_file(getDir(), 'chats.json', cnt)

    if msg.get(cnt_id):
        msg.pop(cnt_id)
        write_file(getDir(), 'contacts.json', msg)

    set_ERR("[Contact has been successfully removed]")
    input('Press ENTER to continue...')
