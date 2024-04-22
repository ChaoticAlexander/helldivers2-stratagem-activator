from typing import Union, get_args

import keyboard

from app.constants.config import (default_settings, settings_description,
                                  settings_prompts)
from app.types.config import AvailableKeys, AvailableSettings, OpenModeMap
from app.utils.config import filter_event

from .config import Config


class Configurator:
    config: Config

    def __init__(self):
        """Starts the configuration process."""
        self.config = Config()
        self.init_bindings()
        self.init_settings()
        self.config.write_config()

    def init_bindings(self):
        """Initializes keybindings assignment process."""
        for key in get_args(AvailableKeys):
            self.read_key_and_assign(key)

    def init_settings(self):
        """Initializes settings assignment process."""
        for key in get_args(AvailableSettings):
            retry_message = (
                settings_prompts[f"{key}_retry"]
                if f"{key}_retry" in settings_prompts
                else None
            )
            args = [OpenModeMap.keys(), retry_message] if key == "open_mode" else []
            self.read_value_and_assign(key, *args)

    def read_key(self):
        """Reads a key press from the user."""
        while True:
            # Keep waiting until a key is pressed
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_UP:
                break

        return event

    def assign_key(self, key: str, event):
        """Assigns given key to a keybinding."""
        event_info = filter_event(event)
        key_code = (
            f"{event.scan_code}.1" if event_info["is_extended"] else event.scan_code
        )
        print(
            "Assigning",
            "Numpad" if event.is_keypad else "",
            event.name,
            f"{' Arrow' if event_info['is_arrow_key'] else ''} to {key}: {key_code}",
        )
        self.config["keybindings"][key] = key_code

    def read_key_and_assign(self, key):
        """Reads and assigns a key press from the user."""
        print(f'Press the key you want to use for "{settings_description[key]}"')
        event = self.read_key()
        self.assign_key(key, event)
        print()

    def read_value(
        self,
        key: AvailableSettings,
        acceptable_values: Union[list[str], None] = None,
        retry_msg: Union[str, None] = None,
    ):
        """Reads a value from the user using input."""
        default_value = self.get_default_value(key)
        default_message = f"leave empty for default ({default_value}): "
        while True:
            print(f"{settings_prompts[key]}")
            value = input(default_message)
            if not value or value and not acceptable_values:
                break
            if acceptable_values and value in acceptable_values:
                break
            print(retry_msg)
            print()
        return value if value else default_value

    def read_value_and_assign(self, key: AvailableSettings, *args):
        """Reads and assigns a value from the user using input."""
        value = self.read_value(key, *args)
        value = OpenModeMap[value[0]] if key == "open_mode" else value
        print(f"Assigning {value} to {key}")
        self.config["settings"][key] = value
        print()

    def get_default_value(self, key: AvailableSettings):
        """Returns the default value for a given key."""
        val = self.config["settings"][key]
        return val if val else default_settings["settings"][key]
