import time

from ..values import cnt

from ..helpers.file_update import file_update
from ..helpers.get_dir import get_dir


def acnt():
    cnt_id = input('contacts id > ')
    name = input('contacts name > ')

    cnt[cnt_id] = {
        'name': name,
        'last_seen': time.time()
    }

    file_update(get_dir(), 'contacts.json', cnt)
