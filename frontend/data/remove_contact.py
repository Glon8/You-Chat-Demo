from .values import cnt, msg, op
from .helpers import write_file, getDir, err_pop


def rcnt():
    contact = input('contact name or id > ')

    if contact not in cnt and contact not in cnt.values():
        err_pop("Provided user not in contacts")
        return
    else:
        if contact in cnt:
            cnt_id = contact
        else:
            cnt_id = next(key for key, value in cnt.items() if value == contact)

    cnt.pop(cnt_id)
    write_file(getDir(), 'contacts.json', cnt)

    if msg.get(cnt_id):
        msg.pop(cnt_id)
        write_file(getDir(), 'chats.json', msg)

    err_pop("Contact has been successfully removed")
