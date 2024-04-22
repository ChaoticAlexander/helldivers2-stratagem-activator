import os
import sys

import fasteners

from app.stratagems import Stratagems
from app.utils import log, showerror


def main():
    lockfile_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "stratagems.lock"
    )

    # Attempt to acquire the lock
    lock = fasteners.InterProcessLock(lockfile_path)
    if not lock.acquire(blocking=False):
        sys.exit(0)

    try:
        if len(sys.argv) < 2:
            showerror(
                "Stratagem key missing",
                "Please provide the stratagem key you want to activate.",
            )
            sys.exit(1)

        key = sys.argv[1]

        stratagems = Stratagems(key, "codes.json")

        log(f"Activating stratagem with key: {key}")

        stratagems.activate()
    finally:
        lock.release()


if __name__ == "__main__":
    main()
