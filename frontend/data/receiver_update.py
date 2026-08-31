from .values import op, cnt, set_ERR
from .helpers import file_update, getDir


def upd_rcv():
    gnr = op['gnr']

    rcv = input("new receiver > ")

    if rcv not in cnt and rcv not in cnt.values():
        set_ERR("[Provided user not in contacts]")
        return

    gnr["rcv_id"] = rcv

    file_update(getDir(), 'config.json', gnr)
