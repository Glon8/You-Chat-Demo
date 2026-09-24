import requests

from ..values import op
from .relay_update import rel_upd


def relay_ping():
    ws_lnk = op.get('gnr').get("ws_lnk")

    http_address = ws_lnk.replace("wss://", "https://", 1)

    cln_id = op.get('gnr').get('snd_id')

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
        print(f'[Response code] {404}')

        return False
