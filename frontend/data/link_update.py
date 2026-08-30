from .values import op
from .connect import cnn
from .helpers import file_update, getDir


def lnk_upd():
    gnr = op["gnr"]

    gnr["ws_lnk"] = "ws://" + input("new link > ")

    file_update(getDir(), 'config.json', gnr)

    cnn()
