import json

from ..values import op, get_WS
from .err_pop import err_pop


def request_sender(request_type, transfer_data):
    ws = get_WS()

    if ws is None or not ws.connected:
        err_pop(f'Request Sender Error: no websocket connection')
        return False

    if request_type not in ('cnn', 'dsc', 'msg', 'upd'):
        err_pop(f'Request Sender Error: request type mismatch ({request_type})')
        return False

    gnr = op.get('gnr', {})
    snd = gnr.get("snd_id")
    rcv = gnr.get("rcv_id")

    if not gnr or not snd or not rcv:
        err_pop(f'Request Sender Error: general data missing')
        return False

    if request_type in ("cnn", "dsc"):
        payload = {
            "snd_id": snd,
            "req_type": request_type,
        }
    else:
        payload = {
            "snd_id": snd,
            "rcv_id": rcv,
            "req_type": request_type,
            "trn_dt": transfer_data
        }

    try:
        ws.send(json.dumps(payload))
    except Exception as e:
        err_pop(f'Request Sender Error: failed to send ({e})')
        return False

    return True
