from .values import cnt, spr


def vcnt():
    print(f'{spr} CONTACTS')

    if cnt:
        for key, val in cnt.items():
            print(f'[{val}] {key}')
    else:
        print(f'[No contacts]')

    input('Press ENTER to continue...')
