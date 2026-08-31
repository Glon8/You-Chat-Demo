from .values import cnt
from .helpers import file_update, getDir


def acnt():
    cnt_id = input('contacts id > ')
    name = input('contacts name > ')

    cnt[cnt_id] = name

    file_update(getDir(), 'contacts.json', cnt)
