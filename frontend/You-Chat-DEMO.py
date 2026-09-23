# GENERAL
from data.visuals import render
from data.helpers import config_load, def_component_loader, def_reports
from data.values import cnt, msg, rel
# CONNECTION
from data.connection.link_update import lnk_upd
from data.connection.connect import cnn, stop_waiting
from data.connection.disconnect import dsc
# CORE_THREADS
from data.core_threads.messages_manager import manage
from data.core_threads.link_listener import dont_listen
# CONTACTS
from data.contacts.add_contact import acnt
from data.contacts.remove_contact import rcnt
from data.contacts.view_contacts import vcnt
from data.contacts.receiver_update import upd_rcv
# RELAYS
from data.relays.view_relays import vrel
from data.relays.add_relay import arel
from data.relays.remove_relay import rrel
# MESSAGES
from data.messages.send import snd
from data.messages.view_messages import vmsg


def control_panel():
    while True:
        render()

        npt = input("> ")
        # ========================< GENERAL
        if npt == "cnn":
            lnk_upd()
        if npt == "rcv":
            upd_rcv()
        if npt == "snd":
            snd()
        if npt == "dsc":
            dsc()
        if npt == "rec":
            def_reports()

            dont_listen()

            cnn()
        # ========================< CONTACTS
        if npt == "vcnt":
            vcnt()
        if npt == "acnt":
            acnt()
        if npt == "rcnt":
            rcnt()
        # ========================< RELAYS
        if npt == "vrel":
            vrel()
        if npt == "arel":
            arel()
        if npt == "rrel":
            rrel()
        # ========================< MESSAGES
        if npt == "vmsg":
            vmsg()


def main():
    config_load()

    def_component_loader('contacts', cnt)

    def_component_loader('chats', msg)

    def_component_loader('relays', rel)

    cnn()

    manage()

    control_panel()


if __name__ == "__main__":
    main()
