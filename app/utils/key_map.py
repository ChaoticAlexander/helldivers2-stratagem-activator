from app.types.types import Direction


class KeyMap:
    key_map: dict[Direction, int]

    def __init__(self, up: int, down: int, left: int, right: int) -> None:
        self.key_map = {
            Direction.UP: up,
            Direction.DOWN: down,
            Direction.LEFT: left,
            Direction.RIGHT: right,
        }

    def get_key_by_direction(self, direction: Direction):
        return self.key_map.get(direction)

    def __repr__(self) -> str:
        string = "{\n"
        for k, v in self.key_map.items():
            string = f"{string}\t{k}: {v},\n"
        return string + "}"
