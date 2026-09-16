from data.visuals import render
from data.link_update import lnk_upd
from data.send import snd
from data.connect import cnn
from data.disconnect import dsc
from data.helpers import config_load, def_component_loader, relays_load
from data.receiver_update import upd_rcv
from data.add_contact import acnt
from data.view_contacts import vcnt
from data.view_messages import vmsg
from data.remove_contact import rcnt
from data.messages_manager import manage
from data.values import cnt, msg
from data.view_relays import vrel
from data.add_relay import arel
from data.remove_relay import rrel


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
        if npt == "vrel":
            vrel()
        if npt == "arel":
            arel()
        if npt == "rrel":
            rrel()
        if npt == "vmsg":
            vmsg()


def main():
    config_load()

    def_component_loader('contacts', cnt)

    def_component_loader('chats', msg)

    relays_load()

    cnn()

    manage()

    control_panel()


if __name__ == "__main__":
    main()
