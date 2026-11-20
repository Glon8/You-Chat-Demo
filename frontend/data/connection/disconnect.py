from ..values import set_ERR, get_WS
from ..core_threads.link_listener import dont_listen
from .connect import stop_waiting

from ..helpers.def_reports import def_reports
from ..helpers.request_sender import request_sender


def dsc():
    _WS = get_WS()
    _SENT = False

    if _WS:
        _SENT = request_sender("dsc", {})

        if _SENT:
            dont_listen()

            _WS.close()

    if not _SENT:
        stop_waiting()

    def_reports()

    set_ERR('')
