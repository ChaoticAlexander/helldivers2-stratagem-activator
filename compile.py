import os

files = {
    "main.py": "--onefile --noconsole --icon=icons/helldivers.ico --name=stratagems --clean",
    "settings.py": "--onefile --icon=icons/settings.ico --name=settings --clean",
}

for file, options in files.items():
  os.system(f"pyinstaller {file} {options}")
