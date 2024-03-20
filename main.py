import sys
from app.modules import Config
from app.utils import log, showerror
from app.stratagems import Stratagems


def main():
  if len(sys.argv) < 2:
    showerror("Stratagem key missing","Please provide the stratagem key you want to activate.")
    sys.exit(1)

  key = sys.argv[1]

  config = Config()
  stratagems = Stratagems(config, key, 'codes.json')

  log(f"Activating stratagem with key: {key}")
  
  stratagems.activate()


if __name__ == '__main__':
  main()
