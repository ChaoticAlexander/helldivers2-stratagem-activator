from configparser import ConfigParser

config = ConfigParser()

config['settings'] = {
  'left': 75,
  'right': 77,
  'up': 72,
  'down': 80,
  'open': 29,
  'open_mode': 'hold'
}

def write_default_config():
  with open('config.ini', 'w') as configfile:
    config.write(configfile)

def read_config():
  config.read('config.ini')
  return config['settings']