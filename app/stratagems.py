import time

from app.config import Config
from app.types.types import Direction
from app.utils.input import Key
from app.utils.log import Logger


class Stratagems:
    def __init__(self, config: Config):
        self.config = config
        self.logger = Logger(debug=self.config.debug)

    def get_input_sequence(self, key: str) -> list[str]:
        if key in self.config.key_codes:
            return self.config.key_codes[key].split(" ")
        else:
            self.logger.log_error(f'Key "{key}" not found in codes.json', None)

    def simulate_key_presses(self, input_list: list[str]):
        for direction in input_list:
            try:
                self.logger.log_direction(direction)
                self.press_key(Direction(direction))
                self.delay()
            except Exception as e:
                self.logger.log_error(
                    "[Strategems.simulate_key_presses] Error when pressing key "
                    f"{direction}'.",
                    e,
                )

    def press_key(self, direction: Direction):
        key = self.config.key_map.get_key_by_direction(direction)
        self.logger.log_key_press(key)
        Key.press(key)

    def delay(self):
        time.sleep(self.config.delay)

    def activate_stratagem(self, key: str):
        self.logger.log_stratagem(key)

        # Press Ctrl key
        Key.down(self.config.activation_key)
        self.logger.log_activation()
        self.delay()

        # Send Key Sequence
        self.simulate_key_presses(self.get_input_sequence(key))

        # Release Ctrl key
        Key.up(self.config.activation_key)
        self.logger.log_activation(False)
