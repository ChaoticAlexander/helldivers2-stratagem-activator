from typing import Dict, Literal, Union

AvailableActions = Literal["U", "D", "L", "R", "O"]

ActionMap: Dict[AvailableActions, str] = {
    "U": "up",
    "D": "down",
    "L": "left",
    "R": "right",
    "O": "open",
}

ActionsDict = Dict[AvailableActions, Union[str, int]]
