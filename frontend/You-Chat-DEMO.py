from data.values import op
from data.visuals import render
from data.link_update import lnk_upd
from data.send import snd
from data.connect import cnn
from data.disconnect import dsc
from data.helpers import config_load, message_load, file_update, getDir


def control_panel():
    gnr = op["gnr"]

    while True:
        render()

        npt = input("> ")

        if npt == "upd_lnk":
            lnk_upd()
        if npt == "upd_rcv":
            gnr["rcv_id"] = input("new receiver > ")
            file_update(getDir(), 'config.json', gnr)
        if npt == "snd":
            snd()
        if npt == "dsc":
            dsc()


def main():
    config_load()

    message_load()

    cnn()

    control_panel()


if __name__ == "__main__":
    main()
