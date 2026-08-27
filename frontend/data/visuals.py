import os

from .values import op, spr


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
