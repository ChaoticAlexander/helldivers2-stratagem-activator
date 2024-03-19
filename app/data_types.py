from enum import Enum


class ActivationMode(Enum):
    HOLD = "HOLD"
    TOGGLE = "TOGGLE"


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"
