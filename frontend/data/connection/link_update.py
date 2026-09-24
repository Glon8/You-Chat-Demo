from ..values import op, rel
from .connect import cnn, stop_waiting
from ..helpers import file_update, getDir, err_pop, def_reports


def lnk_upd():
    gnr = op["gnr"]

    npt = input("Relay link or name > ")

    rel_item = next((data for key, data in rel.items() if key == npt or data.get("link") == 'wss://' + npt), None)

    if rel_item:
        gnr["ws_lnk"] = rel_item.get('link')

        def_reports()
    else:
        err_pop("This relay not in a list")
        return

    file_update(getDir(), 'config.json', gnr)

    stop_waiting()

    cnn()
