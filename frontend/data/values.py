_OPERATIONS = {
    "gnr": {
        "ws_lnk": "ws://localhost:5173",
        "snd_id": 0,
        "rcv_id": 0,
    },
    "slc_op": [
        "* upd_lnk - update link/connect to relay",
        "* upd_rcv - update the receiver",
        "* snd     - send a message",
        "* dsc     - disconnect from relay",
        "* vcnt    - view contacts",
        "* acnt    - add contact",
        "* rcnt    - remove contact",
        "* vmsg    - view messages",
    ],
}

_MESSAGES = {}

_CONTACTS = {}

_SEPERATOR = "========================<"
_LINK_DOWN = False
_WEBSOCKET = None
_REPLY = None
_ERROR_MESSAGE = ''

op = _OPERATIONS
spr = _SEPERATOR
ld = _LINK_DOWN
msg = _MESSAGES
cnt = _CONTACTS


def get_WS():
    return _WEBSOCKET


def set_WS(new):
    global _WEBSOCKET
    _WEBSOCKET = new


def set_LD(new):
    global _LINK_DOWN
    if not isinstance(new, bool):
        return
    _LINK_DOWN = new


def get_RPL():
    return _REPLY


def set_RPL(new):
    global _REPLY

    _REPLY = new


def set_ERR(new):
    global _ERROR_MESSAGE
    if not isinstance(new, str):
        return
    _ERROR_MESSAGE = new


def get_ERR():
    return _ERROR_MESSAGE


def msg_instance(name):
    if not msg.get(str(name)):
        msg[str(name)] = []
