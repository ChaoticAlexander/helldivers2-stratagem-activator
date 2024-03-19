import time

from app.config import Config
from app.types.types import Direction
from app.utils.input import Key


class Stratagems:
    def __init__(self, config: Config):
        self.config = config

    def get_input_sequence(self, key: str) -> list[str]:
        if key in self.config.key_codes:
            return self.config.key_codes[key].split(" ")
        else:
            print(f'Key "{key}" not found in codes.json')

    def simulate_key_presses(self, input_list: list[str]):
        for direction in input_list:
            try:
                self.press_key(Direction(direction))
                self.delay()
            except Exception as e:
                print(
                    "[Strategems.simulate_key_presses] Error when pressing key "
                    f"{direction}'. {type(e)}: {e}"
                )

    def press_key(self, direction: Direction):
        Key.press(self.config.key_map.get_key_by_direction(direction))

    def delay(self):
        time.sleep(self.config.delay)

    def activate_stratagem(self, key: str):
        # Press Ctrl key
        Key.down(self.config.activation_key)
        self.delay()

        # Send Key Sequence
        self.simulate_key_presses(self.get_input_sequence(key))

        # Release Ctrl key
        Key.up(self.config.activation_key)
