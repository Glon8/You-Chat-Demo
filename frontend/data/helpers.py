import json
import os
import sys
import random

from pathlib import Path

from .values import op, msg, cnt, pnd


def getDir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(os.path.abspath(sys.executable))

    return str(Path(__file__).resolve().parent.parent)


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None


def write_file(file_path, file_name, data):
    if not isinstance(file_path, str) or not os.path.exists(file_path):
        return None
    with open(f'{file_path}/{file_name}', 'w') as file:
        json.dump(data, file, indent=4)


def config_load():
    gnr = op['gnr']
    data = read_file(f'{getDir()}/config.json')

    if data:
        data = json.loads(data)
        # strict verification needed
        if not data:
            return

        for key, val in gnr.items():
            if gnr[key] != data[key]:
                gnr[key] = data[key]
    else:
        gnr["snd_id"] = str(random.randint(1000, 9999))

        gnr["ws_lnk"] = "ws://localhost:5173"

        data = {}

        for key, val in gnr.items():
            data[key] = gnr[key]

        write_file(getDir(), 'config.json', data)


def message_load():
    data = read_file(f'{getDir()}/chats.json')

    if data:
        data = json.loads(data)

        # strict verification needed
        if not data:
            return

        for key, val in data.items():
            msg[key] = val
    else:
        data = {}

        write_file(getDir(), 'chats.json', data)


def contacts_load():
    data = read_file(f'{getDir()}/contacts.json')

    if data:
        data = json.loads(data)

        # strict verification needed
        if not data:
            return

        for key, val in data.items():
            cnt[key] = val
    else:
        data = {}

        write_file(getDir(), 'contacts.json', data)


def file_update(file_path, file_name, data):
    saved_data = read_file(file_name)

    if saved_data:
        saved_data = json.loads(saved_data)
    else:
        saved_data = {}

    saved_data.update(data)

    write_file(file_path, file_name, saved_data)


def add_pending(snd_id, rcv_id, timestamp, message):
    pnd.append({'snd_id': snd_id, 'rcv_id': rcv_id, 'tm_stm': timestamp, 'msg': message})


def err_pop(message):
    print(f'[{message}]')
    input('Press ENTER to continue...')
