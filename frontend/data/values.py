_SUB_SEPERATOR = "-------------------<"

_OPERATIONS = {
    "gnr": {
        "ws_lnk": "ws://",
        "snd_id": 0,
        "rcv_id": 0,
    },
    "slc_op": [
        _SUB_SEPERATOR + ' Connection',
        "* cnn     - connect to saved relay",
        "* dsc     - disconnect entirely from a relay",
        "* rec     - attempt reconnect to previously connected relay",
        _SUB_SEPERATOR + ' Contacts',
        "* vcnt    - view saved contacts",
        "* acnt    - add contact",
        "* rcnt    - remove contact",
        "* rcv     - receiver change",
        _SUB_SEPERATOR + ' Relays',
        "* vrel    - view saved relays",
        "* arel    - add relay",
        "* rrel    - remove relay",
        _SUB_SEPERATOR + ' Messages',
        "* vmsg    - view saved/received messages",
        "* snd     - send a message",
        _SUB_SEPERATOR + ' Status',
    ],
}

_MESSAGES = {}

_CONTACTS = {}

_PENDING = []

_RELAYS = {}

_SEPERATOR = "========================<"
_SUB_SEPERATOR = "-------------------<"

_WEBSOCKET = None

_ERROR_MESSAGE = ''

op = _OPERATIONS
spr = _SEPERATOR
pnd = _PENDING
msg = _MESSAGES
cnt = _CONTACTS
rel = _RELAYS


def get_WS():
    return _WEBSOCKET


def set_WS(new):
    global _WEBSOCKET
    _WEBSOCKET = new


def set_ERR(new):
    global _ERROR_MESSAGE
    if not isinstance(new, str):
        return
    _ERROR_MESSAGE = new


def get_ERR():
    return _ERROR_MESSAGE


def msg_instance(snd_id):
    snd = str(snd_id)

    if not msg.get(snd):
        msg[snd] = []
