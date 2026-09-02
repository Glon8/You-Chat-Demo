import os

from .values import op, cnt, spr, get_ERR


def render():
    os.system('cls' if os.name == 'nt' else 'clear')

    for key, item in op.items():
        if key == 'gnr':
            print(f'{spr} GENERAL')

            for name, value in item.items():
                if name == 'rcv_id':
                    rcv_name = cnt.get(value)
                    if rcv_name:
                        print(f'[rcv_id] {rcv_name} > {value}')
                    else:
                        print(f'[{name}] {value}')
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
