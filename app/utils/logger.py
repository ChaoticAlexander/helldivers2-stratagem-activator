from os import getenv
from os.path import isfile
from dotenv import load_dotenv

env_loaded = False


def log(msg):
  if isfile('.env') and not env_loaded:
    load_dotenv()
    globals()['env_loaded'] = True

  if getenv('DEBUG_MODE') == 'true':
    print(msg)
