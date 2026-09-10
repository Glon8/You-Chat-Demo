import requests

from .values import op


def relay_ping():
    ws_lnk = op.get('gnr').get("ws_lnk")

    http_address = ws_lnk.replace("ws://", "http://", 1)

    print(f'[Ping sent] {http_address}')
    try:
        response = requests.get(http_address + '/api/ping', timeout=3)

        res = response.status_code

        print(f'[Response code] {res}')

        return res == 200
    except requests.RequestException:
        print(f'[Response code] {404}')

        return False
