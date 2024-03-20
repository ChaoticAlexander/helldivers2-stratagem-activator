from app.types.config import AppConfig

config_file_path = 'config.ini'

default_settings: AppConfig = {
  'bindings': {
    'left': 75,
    'right': 77,
    'up': 72,
    'down': 80,
    'open': 29,
  },
  'settings': {
    'open_mode': 'hold',
    'delay_min': 20,
    'delay_max': 50
  }
}

settings_description = {
  'up': 'Up',
  'down': 'Down',
  'left': 'Left',
  'right': 'Right',
  'open': 'Open stratagem menu',
  'open_mode': 'Open mode (Hold/Toggle)',
  'delay_min': 'Minimum delay',
  'delay_max': 'Maximum delay'
}

settings_prompts = {
  'open_mode': 'Do you want to use HOLD or TOGGLE mode for the stratagem open key? (h/t)',
  'delay_min': 'Enter the minimum delay (ms)',
  'delay_max': 'Enter the maximum delay (ms)'
}
