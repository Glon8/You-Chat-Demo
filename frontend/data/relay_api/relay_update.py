import requests

from ..values import op, rel

from ..helpers.err_pop import err_pop
from ..helpers.get_prefix import get_prefix
from ..helpers.file_update import file_update
from ..helpers.get_dir import get_dir


def rel_upd():
    ws_lnk = op.get('gnr').get("ws_lnk")

    http_address = get_prefix('http') + ws_lnk

    cnt_id = op.get('gnr').get('snd_id')

    dt = {
        'snd_id': cnt_id,
        'data': [item.get('link') for key, item in rel.items() if not item.get('reported')]
    }

    for key, item in rel.items():
        if not item['reported']:
            item['reported'] = True

    file_update(get_dir(), 'relays.json', rel)

    try:
        requests.post(http_address + '/api/rel-upd', json=dt)
    except Exception as e:
        err_pop('Failed to send the relay update')
