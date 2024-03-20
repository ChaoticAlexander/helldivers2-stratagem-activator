import sys

from app.config import Config
from app.stratagems import Stratagems


def main():
    if len(sys.argv) < 2:
        print("Please provide the stratagem key name you want to activate.")
        return

    config: Config = Config()

    strategem_name: str = sys.argv[1]

    strategems = Stratagems(
        config=config,
    )
    strategems.activate_stratagem(strategem_name)


if __name__ == "__main__":
    main()
