from datetime import datetime

from ..values import rel, spr, _SUB_SEPERATOR


def vrel():
    print(f'{spr} RELAYS')

    if rel:
        for key, item in rel.items():
            print(f'[Name] {key}')
            print(f'[Link] {item.get('link')}')
            dt = datetime.fromtimestamp(item.get('last_seen'))
            print(f'[Last seen] {dt.day:02d}.{dt.month:02d}.{dt.year:02d} - {dt.hour:02d}:{dt.minute:02d}')
            print(f'[Reported] {item.get('reported')}')
            print(_SUB_SEPERATOR)
    else:
        print(f'[No relays]')

    input('Press ENTER to continue...')
