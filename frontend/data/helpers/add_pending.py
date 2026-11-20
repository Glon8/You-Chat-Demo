import time

from ..values import pnd


def add_pending(snd_id, rcv_id, dt):
    pnd.append({'snd_id': snd_id, 'rcv_id': rcv_id, 'rcv_tm_stm': time.time(), 'trn_dt': dt})
