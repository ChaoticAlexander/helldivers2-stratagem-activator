from typing import Literal, TypedDict

AvailableKeys = Literal["up", "down", "left", "right", "open"]
AvailableSettings = Literal["open_mode", "delay_min", "delay_max"]
AvailableOpenModes = Literal["hold", "toggle", "none"]
OpenModeMap = {
    "h": "hold",
    "t": "toggle",
    "n": "none"
}


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
