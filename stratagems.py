import sys
from helpers import activate_stratagem

def main():
    if len(sys.argv) < 2:
        print("Please provide the stratagem key name you want to activate.")
        sys.exit(1)

    key = sys.argv[1]

    activate_stratagem(key)

if __name__ == '__main__':
    main()
