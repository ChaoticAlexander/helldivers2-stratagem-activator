import sys
import time
import json
from lib import press_key, key_down, key_up

# Constants for Directx scan codes
DIK_LCONTROL = 0x1D
DIK_UP = 0xC8
DIK_LEFT = 0xCB
DIK_RIGHT = 0xCD
DIK_DOWN = 0xD0

# Dictionary mapping keys to Directx scan codes
dic = {
    'u': DIK_UP,
    'l': DIK_LEFT,
    'r': DIK_RIGHT,
    'd': DIK_DOWN
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

    # Press Ctrl key
    key_down(DIK_LCONTROL)
    time.sleep(0.02)

    # Send Key Sequence
    simulate_key_presses(input_list)

    # Release Ctrl key
    key_up(DIK_LCONTROL)