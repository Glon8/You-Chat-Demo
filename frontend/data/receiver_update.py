from .values import op, cnt
from .helpers import file_update, getDir, err_pop


def upd_rcv():
    gnr = op['gnr']

    rcv = input("new receiver > ")

    if rcv not in cnt and rcv not in cnt.values():
        err_pop("This number not a contact")
        return

    if rcv in cnt.values():
        rcv = next(key for key, value in cnt.items() if value == rcv)

    gnr["rcv_id"] = rcv

    file_update(getDir(), 'config.json', gnr)
