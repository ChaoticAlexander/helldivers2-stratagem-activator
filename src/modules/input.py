import ctypes
import time
from .logger import log

SendInput = ctypes.windll.user32.SendInput

# Constants
KEYEVENTF_KEYDOWN = 0x0008
KEYEVENTF_KEYUP = 0x0002

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
  def simulate(hex_key_code, key_down=True):
    """Simulate pressing or releasing a key."""
    log(f'Simulating key press with code: {hex_key_code}')
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    flags = KEYEVENTF_KEYDOWN if key_down else KEYEVENTF_KEYDOWN | KEYEVENTF_KEYUP
    ii_.ki = KeyBdInput(0, hex_key_code, flags, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

  @staticmethod
  def press(hex_key_code, delay=0.02):
    """Simulate pressing a key with an optional delay before releasing."""
    Key.simulate(hex_key_code, key_down=True)
    time.sleep(delay)
    Key.simulate(hex_key_code, key_down=False)

  @staticmethod
  def down(hex_key_code):
    """Simulate pressing a key."""
    Key.simulate(hex_key_code, key_down=True)

  @staticmethod
  def up(hex_key_code):
    """Simulate releasing a key."""
    Key.simulate(hex_key_code, key_down=False)
