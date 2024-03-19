import keyboard
from configparser import ConfigParser

config = ConfigParser()

key_bindings = {
    "LEFT": None,
    "RIGHT": None,
    "UP": None,
    "DOWN": None,
    "OPEN": None
}

key_description = {
    "LEFT": "Left",
    "RIGHT": "Right",
    "UP": "Up",
    "DOWN": "Down",
    "OPEN": "Stratagem open"
}


def assign_key(key, event):
  print(f"Assigning {event.name}({event.scan_code}) to {key}")
  key_bindings[key] = event.scan_code


for key, description in key_description.items():
  print(f"Press the key you want to use for {description}")
  # Suppress other events while waiting for a key press
  event = keyboard.read_event(suppress=True)

  while event.event_type != keyboard.KEY_DOWN:
    # Keep waiting until a key is pressed
    event = keyboard.read_event(suppress=True)

  assign_key(key, event)
  print()

open_mode = None
while open_mode not in ["h", "t"]:
  if open_mode is not None:
    print("Invalid choice. Please enter h for HOLD or t for TOGGLE.")

  print("Do you want to use HOLD or TOGGLE mode for the stratagem open key? (h/t)")
  # Suppress other events while waiting for a key press
  event = keyboard.read_event(suppress=True)

  while event.event_type != keyboard.KEY_DOWN:
    event = keyboard.read_event(suppress=True)

  open_mode = event.name.lower()
  print()

open_mode = 'hold' if open_mode == 'h' else 'toggle'

print(f"Stratagem open will be used in {open_mode} mode.")

config['settings'] = {
    **key_bindings,
    "OPEN_MODE": open_mode.lower()
}

with open('config.ini', 'w') as configfile:
  config.write(configfile)
