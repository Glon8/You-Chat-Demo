import time

from ..values import pnd


def add_pending(snd_id, rcv_id, dt):
    pnd.append({'snd_id': snd_id, 'rcv_id': rcv_id, 'rcv_tm_stm': time.time(), 'trn_dt': dt})


old = """
    def add_pending(snd_id, rcv_id, timestamp, dt):
         rcv_tm = time.time()
         pnd.append({'snd_id': snd_id, 'rcv_id': rcv_id, 'tm_stm': timestamp, 'rcv_tm_stm': rcv_tm, 'data': dt})
    """
