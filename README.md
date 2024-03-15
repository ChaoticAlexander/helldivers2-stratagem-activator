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

NOTE:
The codes.json file needs to be in the same directory as your stratagems.exe file

usage:

To use this just call the binary while providing the stratagem key as a parameter.

example:

```
stratagems.exe jump_pack
```

loupedeck usage example:

```
stratagems.exe || jump_pack
```
