import sys
from os.path import isfile
from .messagebox import showerror
from src.utils.logger import log
from configparser import ConfigParser
from src.types.config import SettingsDict


class Config:
  config_file_path: str
  parser = ConfigParser()
  settings: SettingsDict
  default_settings: SettingsDict = {
    'left': 75,
    'right': 77,
    'up': 72,
    'down': 80,
    'open': 29,
    'open_mode': 'hold'
  }

  def __init__(self, config_file_path: str = 'config.ini'):
    self.config_file_path = config_file_path
    if isfile(config_file_path):
      log('File found, loading configuration..')
      self.read_config()
    else:
      log('File not found, creating file and loading default configuration..')
      self.write_default_config()
      self.default_settings
    self.settings = {
      key: int(value)
      if value.isdigit() else value
      for key, value in self.parser['settings'].items()
    }
      
  def __getitem__(self, key):
    """Property to access settings, with digit strings converted to integers."""
    return self.settings[key]

  def write_default_config(self):
    """Write default settings to config file."""
    try:
      with open(self.config_file_path, 'w') as config_file:
        self.parser['settings'] = self.default_settings
        self.parser.write(config_file)
    except IOError:
      showerror('Error', f'Error while creating config file: {self.config_file_path}')
      sys.exit(1)

  def read_config(self):
    """Reads settings from config file."""
    self.parser.read(self.config_file_path)
