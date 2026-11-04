import time

from ..values import cnt, spr
from datetime import datetime

def vcnt():
    print(f'{spr} CONTACTS')

    if cnt:
        for key, val in cnt.items():
            if val.get('name'):
                print(f'[{val.get('name')}] {key}')
            else:
                print(f'[No name] {key}')

            dt = datetime.fromtimestamp(val.get('last_seen'))
            print(f'[Last seen] {dt.day:02d}.{dt.month:02d}.{dt.year:02d} - {dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}')
    else:
        print(f'[No contacts]')

    input('Press ENTER to continue...')
