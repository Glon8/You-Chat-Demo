import threading

from ..values import get_ERR
from .connect import cnn, stop_waiting, wait_ping

from ..helpers.def_reports import def_reports


def rec():
    def_reports()

    stop_waiting()

    cnn()

    if len(get_ERR()) > 0:
        threading.Thread(
            target=wait_ping,
            daemon=True
        ).start()
