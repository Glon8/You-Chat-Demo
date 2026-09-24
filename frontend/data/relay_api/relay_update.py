import requests

from ..values import op, rel
from ..helpers import err_pop


def rel_upd():
    ws_lnk = op.get('gnr').get("ws_lnk")

    http_address = ws_lnk.replace("wss://", "https://", 1)

    cnt_id = op.get('gnr').get('snd_id')
    dt = {
        'snd_id': cnt_id,
        'data': [item.get('link') for key, item in rel.items() if not item.get('reported')]
    }

    try:
        requests.post(http_address + '/api/rel-upd', json=dt)
    except Exception as e:
        err_pop('Failed to send the relay update')
