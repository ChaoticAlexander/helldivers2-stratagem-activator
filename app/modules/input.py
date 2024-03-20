import ctypes
import time
from app.utils.logger import log

SendInput = ctypes.windll.user32.SendInput

# Constants
KEYEVENTF_KEYDOWN = 0x0008
KEYEVENTF_KEYUP = KEYEVENTF_KEYDOWN | 0x0002
KEYEVENTF_EXTENDEDKEY = 0x0001

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
  _fields_ = [
    ("wVk", ctypes.c_ushort),
    ("wScan", ctypes.c_ushort),
    ("dwFlags", ctypes.c_ulong),
    ("time", ctypes.c_ulong),
    ("dwExtraInfo", PUL)
  ]


class HardwareInput(ctypes.Structure):
  _fields_ = [
    ("uMsg", ctypes.c_ulong),
    ("wParamL", ctypes.c_short),
    ("wParamH", ctypes.c_ushort)
  ]


class MouseInput(ctypes.Structure):
  _fields_ = [
    ("dx", ctypes.c_long),
    ("dy", ctypes.c_long),
    ("mouseData", ctypes.c_ulong),
    ("dwFlags", ctypes.c_ulong),
    ("time", ctypes.c_ulong),
    ("dwExtraInfo", PUL)
  ]


class Input_I(ctypes.Union):
  _fields_ = [
    ("ki", KeyBdInput),
    ("mi", MouseInput),
    ("hi", HardwareInput)
  ]


class Input(ctypes.Structure):
  _fields_ = [
    ("type", ctypes.c_ulong),
    ("ii", Input_I)
  ]


class Key:
  @staticmethod
  def simulate(key_code, key_down=True):
    """Simulate pressing or releasing a key."""
    key_code, _, ext = key_code.partition('.')
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    flags = KEYEVENTF_KEYDOWN if key_down else KEYEVENTF_KEYUP
    if ext:
      flags |= KEYEVENTF_EXTENDEDKEY
    ii_.ki = KeyBdInput(0, int(key_code), flags, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    if key_down:
      log(f'Simulating key with code: {key_code}, extended: {bool(ext)}')
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
