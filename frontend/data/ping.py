import requests

from .values import op


def relay_ping():
    ws_lnk = op.get('gnr').get("ws_lnk")

    http_address = ws_lnk.replace("ws://", "http://", 1)

    try:
        response = requests.get(http_address + '/ping', timeout=3)

        return response == 200
    except requests.RequestException:
        return False
