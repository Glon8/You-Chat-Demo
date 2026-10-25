import threading

from ..helpers import def_reports
from ..values import get_ERR
from .connect import cnn, stop_waiting, wait_ping
from ..core_threads.link_listener import dont_listen

def rec():
    def_reports()

    dont_listen()

    stop_waiting()

    cnn()

    if len(get_ERR()) > 0:
        threading.Thread(
            target=wait_ping,
            daemon=True
        ).start()