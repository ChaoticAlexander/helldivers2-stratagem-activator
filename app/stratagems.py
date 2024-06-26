import json
import random
import sys
import time
from typing import Dict, List

from app.modules import Config, Key
from app.types.stratagems import ActionMap, AvailableActions
from app.utils import log, showerror


class Stratagems:
    bindings: Dict[AvailableActions, int]
    codes: Dict[str, str]
    active_code_sequence: List[str]
    menu_open: bool = False
    no_menu_toggle: bool = False
    config: Config

    def __init__(self, stratagem_key: str, codes_file_path: str):
        self.config = Config()
        self.map_bindings()
        self.load_key_sequences(codes_file_path)
        self.load_active_key_sequence(stratagem_key)

    def map_bindings(self):
        self.bindings = {
            key: self.config["keybindings"][config_key]
            for (key, config_key) in ActionMap.items()
        }

    def load_key_sequences(self, file_path: str):
        try:
            log("Loading stratagem key sequences..")
            with open(file_path, encoding="utf-8") as f:
                self.codes = json.load(f)
        except FileNotFoundError:
            showerror("Error", f"File not found: {file_path}")
            sys.exit(1)
        except json.JSONDecodeError:
            showerror("Error", f"Error decoding JSON file: {file_path}")
            sys.exit(1)

    def load_active_key_sequence(self, key: str):
        if key in self.codes:
            self.active_code_sequence = self.codes[key].replace("NM ", "").split(" ")
            self.no_menu_toggle = (
                self.config["settings"]["open_mode"] == "none"
                or "NM" in self.codes[key]
                or len(self.active_code_sequence) == 1
            )
        else:
            showerror(
                "Stratagem execution error", f'Key "{key}" not found in codes.json'
            )
            sys.exit(1)

    def sleep(self):
        delay = (
            random.uniform(
                int(self.config["settings"]["delay_min"]),
                int(self.config["settings"]["delay_max"]),
            )
            * 0.001
        )
        log(f"sleeping for {delay}s")
        return time.sleep(delay)

    def simulate_key_presses(self):
        for element in self.active_code_sequence:
            Key.press(
                self.bindings[element],
                float(self.config["settings"]["press_time"]) * 0.001,
            )
            self.sleep()

    def toggle_menu(self):
        if self.no_menu_toggle:
            return
        if self.config["settings"]["open_mode"] == "hold":
            (Key.up if self.menu_open else Key.down)(self.bindings["O"])
        elif not self.menu_open:
            Key.press(
                self.bindings["O"], float(self.config["settings"]["press_time"]) * 0.001
            )
        self.menu_open = not self.menu_open
        self.sleep()

    def activate(self):
        log(f"Executing stratagem sequence: {self.active_code_sequence}")
        # Open stratagem menu
        self.toggle_menu()

        # Send Key Sequence
        self.simulate_key_presses()

        # Close stratagem menu
        self.toggle_menu()
