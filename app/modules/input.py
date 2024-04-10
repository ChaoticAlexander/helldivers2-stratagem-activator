import ctypes
import time
from app.types.input import Input, Input_I, KeyBdInput
from app.utils.logger import log

SendInput = ctypes.windll.user32.SendInput

# Constants
KEYEVENTF_KEYDOWN = 0x0008
KEYEVENTF_KEYUP = KEYEVENTF_KEYDOWN | 0x0002
KEYEVENTF_EXTENDEDKEY = 0x0001


class Key:
    @staticmethod
    def simulate(key_code, key_down=True):
        """Simulate pressing or releasing a key."""
        key_code, _, ext = key_code.partition(".")
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        flags = KEYEVENTF_KEYDOWN if key_down else KEYEVENTF_KEYUP
        if ext:
            flags |= KEYEVENTF_EXTENDEDKEY
        ii_.ki = KeyBdInput(0, int(key_code), flags, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        if key_down:
            log(f"Simulating key with code: {key_code}, extended: {bool(ext)}")
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    @staticmethod
    def press(key_code, delay=0.02):
        """Simulate pressing a key with an optional delay before releasing."""
        Key.simulate(key_code, key_down=True)
        time.sleep(delay)
        Key.simulate(key_code, key_down=False)

    @staticmethod
    def down(key_code):
        """Simulate pressing a key."""
        Key.simulate(key_code, key_down=True)

    @staticmethod
    def up(key_code):
        """Simulate releasing a key."""
        Key.simulate(key_code, key_down=False)
