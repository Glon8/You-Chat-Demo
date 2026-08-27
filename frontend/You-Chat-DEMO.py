import websocket
import json
import random

from data.values import op
from data.visuals import render

ws = None
ld = False


def control_pannel():
    global ws
    global ld

    gnr = op['gnr']
    data = None

    while True:
        if not ld:
            data = ws.recv()
        else:
            print('[Current WebSocket not accessible]')

        render()

        if data:
            print(f'\r\n[{data.snd_id}]> {data.trn_dt}\r\n')

        npt = input('> ')

        if npt == 'upd_lnk':
            gnr['ws_lnk'] = 'ws://' + input('new link > ')
            try:
                ws = websocket.create_connection(gnr['lnk'])
                ld = False
            except:
                ld = True
        if npt == 'upd_rcv':
            gnr['rcv_id'] = input('new receiver > ')
        if npt == 'snd':
            msg = input('message > ')

            ws.send(json.dumps({
                'snd_id': gnr['snd_id'],
                'rcv_id': gnr['rcv_id'],
                'req_type': 'msg',
                'trn_dt': msg
            }))
        if npt == 'dsc':
            ws.send(json.dumps({
                'snd_id': gnr['snd_id'],
                'req_type': 'dsc',
            }))


def main():
    global ws
    global ld

    gnr = op['gnr']

    gnr['snd_id'] = random.randint(1000, 9999)

    try:
        ws = websocket.create_connection('ws://localhost:5173')
        ld = False
        ws.send(json.dumps({
            'snd_id': gnr['snd_id'],
            'req_type': 'cnn',
        }))
    except:
        ld = True

    control_pannel()


if __name__ == '__main__':
    main()
