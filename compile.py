import os

files = {
    "main.py": "--onefile --noconsole --icon=icons/helldivers.ico --name=stratagems",
    "./src/configure.py": "--onefile --icon=icons/settings.ico --name=settings",
}

for file, options in files.items():
  os.system(f"pyinstaller {file} {options}")
