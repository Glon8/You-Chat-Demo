from .values import cnt, spr


def vcnt():
    print(f'{spr} CONTACTS')

    if cnt:
        for key, val in cnt.items():
            if val.get('name'):
                print(f'[{val.get('name')}] {key}')
            else:
                print(f'[No name] {key}')
            print(f'[Last seen] {val.get('last_seen')}')
    else:
        print(f'[No contacts]')

    input('Press ENTER to continue...')
