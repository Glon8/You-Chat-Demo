from ..values import op, cnt

from ..helpers.file_update import file_update
from ..helpers.get_dir import get_dir
from ..helpers.err_pop import err_pop


def upd_rcv():
    gnr = op['gnr']

    rcv = input("contact number or name> ")

    rcv_in_cnt_name = any(data.get("name") == rcv for data in cnt.values())

    if rcv not in cnt and not rcv_in_cnt_name:
        err_pop("This number not a contact")
        return

    if rcv_in_cnt_name:
        rcv = next(key for key, value in cnt.items() if value.get('name') == rcv)

    gnr["rcv_id"] = rcv

    file_update(get_dir(), 'config.json', gnr)
