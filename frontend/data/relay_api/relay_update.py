import requests

from ..values import op, rel
from ..helpers import err_pop, get_prefix, file_update, getDir


def rel_upd():
    ws_lnk = op.get('gnr').get("ws_lnk")

    http_address = ws_lnk.replace(get_prefix('ws'), get_prefix('http'), 1)

    cnt_id = op.get('gnr').get('snd_id')

    dt = {
        'snd_id': cnt_id,
        'data': [item.get('link') for key, item in rel.items() if not item.get('reported')]
    }

    for key, item in rel.items():
        if not item['reported']:
            item['reported'] = True

    file_update(getDir(), 'relays.json', rel)

    try:
        requests.post(http_address + '/api/rel-upd', json=dt)
    except Exception as e:
        err_pop('Failed to send the relay update')
