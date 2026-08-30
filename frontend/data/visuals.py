import os
import json

from .values import op, spr, rpl, set_RPL


def render():
    os.system('cls' if os.name == 'nt' else 'clear')

    for key, item in op.items():
        if key == 'gnr':
            print(f'{spr} GENERAL')

            for name, value in item.items():
                print(f'[{name}] {value}')
        if key == 'slc_op':
            print(f'{spr} OPERATIONS')

            for val in item:
                print(val)

def render_msg():
    if rpl:
        set_RPL(json.loads(rpl))
        print(f"\r\n[{rpl['snd_id']}]> {rpl['trn_dt']}\r\n")
        set_RPL(None)