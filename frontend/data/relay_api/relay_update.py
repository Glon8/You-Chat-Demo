import requests

from ..values import op, rel


def rel_upd():
    ws_lnk = op.get('gnr').get("ws_lnk")

    http_address = ws_lnk.replace("ws://", "http://", 1)

    cnt_id = op.get('gnr').get('snd_id')
    # client should send the links, that wasn't sent previously to THIS relay!
    # must be added check inside the relay links list!
    dt = {
        'snd_id': cnt_id,
        'data': [item for item in rel
                 if not item.get('reported') or item.get('reported') != ws_lnk]
    }

    try:
        response = requests.post(http_address + '/api/ping', json=dt)

        print(f'[Relay Update][Response received] {response.status_code}')  # < For testing only!
    except Exception as e:
        print(f'[Relay Update][Error][Failed to send the relay update]')
