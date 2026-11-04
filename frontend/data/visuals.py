import os

from .values import op, cnt, spr, get_ERR


def render():
    os.system('cls' if os.name == 'nt' else 'clear')

    for key, item in op.items():
        if key == 'gnr':
            print(f'{spr} GENERAL')

            for name, value in item.items():
                if name == 'ws_lnk':
                    print(f'[Relay] {value}')
                elif name == 'snd_id':
                    print(f'[My id] {value}')
                elif name == 'rcv_id':
                    cnt_info = cnt.get(value)
                    rcv_name = None

                    if cnt_info:
                        rcv_name = cnt_info.get('name')

                    if rcv_name:
                        print(f'[Contact] {rcv_name} > {value}')
                    else:
                        print(f'[{name}] {value}')
                elif name == 'sprt':
                    print(f'[Secure Protocol] {value}')
                else:
                    print(f'[{name}] {value}')
        if key == 'slc_op':
            print(f'{spr} OPERATIONS')

            for val in item:
                print(val)

    rnd_err()


def rnd_err():
    err_msg = get_ERR()

    if err_msg:
        print(err_msg)
    else:
        print("[ EVERYTHING IS GOOD! ]")
