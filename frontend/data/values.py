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
    ],
}

_SEPERATOR = "========================<"
_LINK_DOWN = False
_WEBSOCKET = None
_REPLY = None

op = _OPERATIONS
spr = _SEPERATOR
ld = _LINK_DOWN
ws = _WEBSOCKET
rpl = _REPLY

def set_WS(new):
    global _WEBSOCKET
    _WEBSOCKET = new

def set_LB(new):
    global _LINK_DOWN
    if not isinstance(new, bool):
        return
    _LINK_DOWN = new

def set_RPL(new):
    global _REPLY
    if not isinstance(new, str):
        return
    _REPLY = new