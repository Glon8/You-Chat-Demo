from data.visuals import render
from data.link_update import lnk_upd
from data.send import snd
from data.connect import cnn
from data.disconnect import dsc
from data.helpers import config_load, message_load, contacts_load
from data.receiver_update import upd_rcv
from data.add_contact import acnt
from data.view_contacts import vcnt
from data.view_messages import vmsg
from data.remove_contact import rcnt


def control_panel():
    while True:
        render()

        npt = input("> ")

        if npt == "upd_lnk":
            lnk_upd()
        if npt == "upd_rcv":
            upd_rcv()
        if npt == "snd":
            snd()
        if npt == "dsc":
            dsc()
        if npt == "vcnt":
            vcnt()
        if npt == "acnt":
            acnt()
        if npt == "rcnt":
            rcnt()
        if npt == "vmsg":
            vmsg()


def main():
    config_load()

    contacts_load()

    message_load()

    cnn()

    control_panel()


if __name__ == "__main__":
    main()
