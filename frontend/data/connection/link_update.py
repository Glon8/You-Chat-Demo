from ..values import op, rel
from .connect import cnn, stop_waiting
from .disconnect import dsc

from ..helpers.file_update import file_update
from ..helpers.get_dir import get_dir
from ..helpers.err_pop import err_pop
from ..helpers.def_reports import def_reports


def lnk_upd():
    dsc()

    gnr = op["gnr"]

    npt = input("Relay link or name > ")

    rel_item = next((data for key, data in rel.items() if key == npt or data.get("link") == npt), None)

    if rel_item:
        gnr["ws_lnk"] = rel_item.get('link')

        def_reports()
    else:
        err_pop("This relay not in a list")
        return

    file_update(get_dir(), 'config.json', gnr)

    stop_waiting()

    cnn()
