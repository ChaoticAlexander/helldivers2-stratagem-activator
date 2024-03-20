from typing import TypedDict, Literal

AvailableOpenModes = Literal['hold', 'toggle']


class Keybindings(TypedDict):
  up: str
  down: str
  left: str
  right: str
  open: str


class Settings(TypedDict):
  open_mode: AvailableOpenModes
  delay_min: str
  delay_max: str


class AppConfig(TypedDict):
  keybindings: Keybindings
  settings: Settings
