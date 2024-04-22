import ctypes
from ctypes import wintypes
import time
from app.types.input import KeyBdInput, Input, Input_I
from app.constants.input import (
    KEYEVENTF_EXTENDEDKEY,
    KEYEVENTF_KEYDOWN,
    KEYEVENTF_KEYUP,
    KEYEVENTF_SCANCODE,
    INPUT_KEYBOARD,
)
from app.utils.logger import log

user32 = ctypes.windll.user32
SendInput = user32.SendInput


class Key:
    @staticmethod
    def simulate(key_code, key_down=True):
        """Simulate pressing or releasing a key."""
        key_code, _, ext = key_code.partition(".")
        state = KEYEVENTF_KEYDOWN if key_down else KEYEVENTF_KEYUP
        flags = KEYEVENTF_SCANCODE | state
        if ext:
            flags |= KEYEVENTF_EXTENDEDKEY
        input_struct = Input(
            INPUT_KEYBOARD,
            ii=Input_I(
                ki=KeyBdInput(
                    0, int(key_code), flags, 0, ctypes.pointer(wintypes.WPARAM(0))
                )
            ),
        )
        if key_down:
            log(f"Simulating key with code: {key_code}, extended: {bool(ext)}")
        SendInput(1, ctypes.pointer(input_struct), ctypes.sizeof(input_struct))

    @staticmethod
    def press(key_code, delay=0.02):
        """Simulate pressing a key with an optional delay before releasing."""
        Key.down(key_code)
        time.sleep(delay)
        Key.up(key_code)

    @staticmethod
    def down(key_code):
        """Simulate pressing a key."""
        Key.simulate(key_code, key_down=True)

    @staticmethod
    def up(key_code):
        """Simulate releasing a key."""
        Key.simulate(key_code, key_down=False)
