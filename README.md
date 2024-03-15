## Important Note

Due to this executing keyboard input events, windows might falsly detect this as a wacatac trojan.
Add the executable to the exceptions to remedy this.
If you don't feel comfortable with the warning, you can go through the code and/or compile it yourself.

## Description

A simple script for loading a key sequence by key from a JSON file, based on given parameter.

You can either use the binaries provided in the release section, or compile it yourself using pyinstaller.

(If you choose to compile it yourself, you might get a warning from windows defender saying that this is malicious.
This is because of the "--noconsole" flag.
Disable your anti-virus while compiling and reactivate after you're done to work around this issue.)

Compilation command:
```
pyinstaller --onefile --noconsole --icon=favicon.ico stratagems.py
```
The compiled binary will appear in the dist folder.

**NOTE: The codes.json file needs to be in the same directory as your stratagems.exe file**

## Usage:

To use this just call the binary while providing the stratagem key as a parameter.

example:

```
stratagems.exe jump_pack
```

For loupedeck users:
Create a new "Run" action and browse to the strategems.exe file.
in the path input add || followed by the action key  (actions can be viewed inside the codes.json file)

**loupedeck usage example:**

```
C:\helldivers\stratagems.exe || jump_pack
```
