import os
import sys
import time
import json
from lib.config import config, write_default_config, read_config
from lib.input import press_key, key_down, key_up

if os.path.exists("config.ini"):
    read_config()
else:
    write_default_config()

dic = {
    'u': int(config['settings']['up']),
    'l': int(config['settings']['left']),
    'r': int(config['settings']['right']),
    'd': int(config['settings']['down']),
    'o': int(config['settings']['open'])
}

def load_key_sequences(file_path):
    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'File not found: {file_path}')
        sys.exit(1)
    except json.JSONDecodeError:
        print(f'Error decoding JSON file: {file_path}')
        sys.exit(1)

def get_input_sequence(key, data):
    if key in data:
        return data[key].split(' ')
    else:
        print(f'Key "{key}" not found in codes.json')
        sys.exit(1)

def simulate_key_presses(input_list):
    for i in input_list:
        btn_key = i.lower()
        press_key(dic[btn_key])
        time.sleep(0.02)

def activate_stratagem(key):
    data = load_key_sequences('codes.json')
    input_list = get_input_sequence(key, data)

    # Open stratagem menu
    if (config['settings']['open_mode'] == 'hold'):
        key_down(dic['o'])
        time.sleep(0.02)
    else:
        press_key(dic['o'])
        time.sleep(0.02)

    # Send Key Sequence
    simulate_key_presses(input_list)

    # Close stratagem menu
    if (config['settings']['open_mode'] == 'hold'):
        key_up(dic['o'])
    else:
        press_key(dic['o'])
