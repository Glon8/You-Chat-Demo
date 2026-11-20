import requests

from ..values import op
from .relay_update import rel_upd

from ..helpers.get_prefix import get_prefix


def relay_ping():
    gnr = op.get('gnr')
    ws_lnk = gnr.get("ws_lnk")
    cln_id = gnr.get('snd_id')
    http_address = get_prefix('http') + ws_lnk

    dt = {"snd_id": cln_id}

    print(f'\r\n[Ping sent] {http_address}')
    try:
        response = requests.post(http_address + '/api/ping', json=dt, timeout=3)

        stat = response.status_code

        try:
            dt = response.json()
        except Exception as e:
            dt = None

        if dt and dt.get('sync_stat') is True:
            rel_upd()

        print(f'[Response code] {stat}')

        return stat == 200
    except Exception as e:
        print(e)
        print(f'[Response code] 500')

        return False
