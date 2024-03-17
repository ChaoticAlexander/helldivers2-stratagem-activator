import os

files = {
  "stratagems.py": "--onefile --noconsole --icon=icons/helldivers.ico",
  "configure.py": "--onefile --icon=icons/settings.ico",
}

for file, options in files.items():
  os.system(f"pyinstaller {file} {options}")