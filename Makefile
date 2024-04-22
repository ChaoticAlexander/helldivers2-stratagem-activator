setup:
	mkdir .venv
	pipenv install --dev

lint:
	pipenv run pre-commit run

lint-all:
	pipenv run pre-commit run -a

build:
	.venv\Scripts\activate && \
	pyinstaller app.py --onefile --noconsole --icon=icons/helldivers.ico --name stratagems
	pyinstaller app.py --onedir --noconsole --icon=icons/helldivers.ico --name stratagems
	pyinstaller settings.py --onefile --icon=icons/settings.ico --name settings
	pyinstaller debug.py --onefile --icon=icons/settings.ico --name debug
	pwsh -Command "Copy-Item -Path './config/codes.json' -Destination './dist/'"

release:
	make rebuild
	pwsh -Command "cd ./dist; if (-Not (Test-Path './release')) { New-Item -ItemType Directory -Path './release' }; Compress-Archive -LiteralPath 'stratagems.exe', 'settings.exe', 'codes.json' -Destination './release/stratagems-activator_packed.zip'"
	pwsh -Command "cd ./dist; if (-Not (Test-Path './release')) { New-Item -ItemType Directory -Path './release' }; Compress-Archive -LiteralPath './stratagems/stratagems.exe', './stratagems/_internal', 'settings.exe', 'codes.json' -Destination './release/stratagems-activator_unpacked.zip'"

clear_build:
	pwsh -Command "Remove-Item -Path '*.spec' -Force"
	pwsh -Command "Remove-Item -Path 'dist\*' -Recurse -Force"
	pwsh -Command "Remove-Item -Path 'build' -Recurse -Force"

rebuild:
	make clear_build
	make build
