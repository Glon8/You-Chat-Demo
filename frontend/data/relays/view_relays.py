from ..values import rel, spr, _SUB_SEPERATOR


def vrel():
    print(f'{spr} RELAYS')

    if rel:
        for item in rel:
            print(f'[Name] {item.get('name')}')
            print(f'[Link] {item.get('link')}')
            print(f'[Last seen] {item.get('last_seen')}')
            print(_SUB_SEPERATOR)
    else:
        print(f'[No relays]')

    input('Press ENTER to continue...')