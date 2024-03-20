import sys
from configparser import ConfigParser
from os.path import isfile

from app.constants.config import config_file_path, default_settings
from app.utils import log, showerror


class Config:
    config_path: str
    parser: ConfigParser

    def __init__(self, config_path: str = config_file_path):
        self.config_path = config_path
        self.parser = ConfigParser()
        if isfile(config_path):
            log("File found, loading configuration..")
            self.read_config()
        else:
            log("File not found, creating file and loading default configuration..")
            self.write_default_config()

    def __getitem__(self, key):
        """Property to access settings, with digit strings converted to integers."""
        keys = key.split(".")
        try:
            value = self.parser._sections
            for k in keys:
                value = value[k]
            return value
        except KeyError:
            showerror("Error", f"Setting not found: {key}")
            sys.exit(1)

    def write_default_config(self):
        """Write default settings to config file."""
        self.parser.read_dict(default_settings)
        try:
            with open(self.config_path, "w", encoding="utf-8") as config_file:
                self.parser.write(config_file)
        except IOError:
            showerror("Error", f"Error while creating config file: {self.config_path}")
            sys.exit(1)

    def read_config(self):
        """Reads settings from config file."""
        self.parser.read(self.config_path)
