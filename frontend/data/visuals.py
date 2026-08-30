import os

from .values import op, spr, get_RPL, set_RPL, get_ERR


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

    rnd_err()

    render_msg()


def render_msg():
    rpl = get_RPL()
    if rpl:
        print(f"\r\n[{rpl['snd_id']}]> {rpl['trn_dt']}\r\n")
        set_RPL(None)


def rnd_err():
    err_msg = get_ERR()

    if err_msg:
        print(err_msg)
