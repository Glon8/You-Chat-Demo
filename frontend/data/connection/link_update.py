from ..values import op, rel
from .connect import cnn, stop_waiting
from ..helpers import file_update, getDir, err_pop


def lnk_upd():
    gnr = op["gnr"]

    npt = input("Relay link or name > ")

    if any(data.get('name') == npt for data in rel):
        item = next((data for data in rel if data.get("name") == npt), None)

        gnr["ws_lnk"] = item.get('link')
    elif any(data.get('link') == 'ws://' + npt for data in rel):
        gnr["ws_lnk"] = 'ws://' + npt
    else:
        err_pop("This relay not in a list")
        return

    file_update(getDir(), 'config.json', gnr)

    stop_waiting()

    cnn()
