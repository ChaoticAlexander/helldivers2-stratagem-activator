import logging


class Logger:
    def __init__(self, debug: bool = False):
        logging.basicConfig()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO if debug else logging.ERROR)

    def log_direction(self, dir: str):
        self.logger.info(f"Direction enter: {dir}")

    def log_key_press(self, key: int):
        self.logger.info(f"Key pressed: {key}")

    def log_error(self, message: str, e: Exception):
        self.logger.error(message)
        self.logger.error(f"error: {type(e)} {e.message}")

    def log_activation(self, down: bool = True):
        self.logger.info(f"Activation pressed {'down' if down else 'up'}")

    def log_stratagem(self, strategem):
        self.logger.info(f"Stratagem activated: {strategem}")
