from ..values import op


def get_prefix(protocol):
    sprt = op.get('gnr').get('sprt')

    if protocol == 'ws':
        return 'wss://' if sprt else 'ws://'
    elif protocol == 'http':
        return 'https://' if sprt else 'http://'
