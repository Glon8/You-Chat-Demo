from ..values import cnt, msg

from ..helpers.write_file import write_file
from ..helpers.get_dir import get_dir
from ..helpers.err_pop import err_pop


def rcnt():
    if not cnt:
        err_pop("Contacts list is empty")
        return

    contact = input('contact name or id > ')

    if contact not in cnt and not any(data.get("name") == contact for data in cnt.values()):
        err_pop("Provided user not in contacts")
        return

    if contact in cnt:
        cnt_id = contact
    else:
        cnt_id = next(key for key, value in cnt.items() if value.get('name') == contact)

    cnt.pop(cnt_id)
    write_file(get_dir(), 'contacts.json', cnt)

    if msg.get(cnt_id):
        msg.pop(cnt_id)
        write_file(get_dir(), 'chats.json', msg)

    err_pop("Contact has been successfully removed")
