import time
import hashlib

from ..values import pnd


def add_pending(snd_id, rcv_id, dt):
    rcv_tm_stm = time.time()

    tm_stm = (dt or {}).get('tm_stm')

    itm_id = hashlib.sha3_256(f'{snd_id}{rcv_id}{tm_stm or rcv_tm_stm}'.encode()).hexdigest()

    pnd.append({'snd_id': snd_id, 'rcv_id': rcv_id, 'rcv_tm_stm': rcv_tm_stm, 'itm_id': itm_id, 'trn_dt': dt})
