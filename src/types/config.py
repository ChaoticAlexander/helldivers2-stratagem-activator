from typing import Dict, Union, Literal

AvailableSettings = Literal['left', 'right', 'up', 'down', 'open', 'open_mode']
AvailableOpenModes = Literal['hold', 'toggle']

SettingsDict = Dict[AvailableSettings, Union[str, int]]
