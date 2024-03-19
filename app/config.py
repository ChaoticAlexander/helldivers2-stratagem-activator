import json
import os
import sys
from tkinter import LEFT, RIGHT

from dotenv import load_dotenv

from app.constants import ACTIVATION_KEY, DELAY, DOWN, MODE, UP
from app.data_types import ActivationMode
from app.key_map import KeyMap


class Config:
    activation_key: int
    delay: float
    mode: ActivationMode
    key_map: KeyMap
    key_codes: dict[str, str]

    def __init__(self):
        self.current_directory = os.path.join(
            os.path.dirname(os.path.realpath(sys.argv[0])), "config\\"
        )
        load_dotenv(os.path.join(self.current_directory, ".env"))
        self.set_activation_key(os.environ[ACTIVATION_KEY])
        self.set_delay(os.environ[DELAY])
        self.set_mode(os.environ[MODE])
        self.initialize_key_map()
        self.load_key_sequences()

    def set_activation_key(self, key: str):
        try:
            self.activation_key = int(key, 16)
        except Exception as e:
            print(e)
            sys.exit("Invalid activation key value: " + key)

    def set_delay(self, delay: str):
        try:
            self.delay = float(delay)
        except Exception as e:
            print(e)
            sys.exit("Invalid Delay value: (decimal number)" + delay)

    def set_mode(self, mode: str):
        try:
            self.mode = ActivationMode(mode)
        except Exception as e:
            print(e)
            sys.exit("Invalid Mode value (TOGGLE or HOLD): " + mode)

    def initialize_key_map(self):
        self.key_map = KeyMap(
            up=os.environ[UP],
            down=os.environ[DOWN],
            left=os.environ[LEFT],
            right=os.environ[RIGHT],
        )

    def load_key_sequences(self):
        try:
            with open(os.path.join(self.current_directory, "codes.json")) as f:
                self.key_codes = json.load(f)
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error decoding JSON file")
            sys.exit(1)
