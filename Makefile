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
	pyinstaller settings.py --onefile --icon=icons/settings.ico --name settings
	pwsh -Command "Copy-Item -Path './config/codes.json' -Destination './dist/'"

clear_build:
	pwsh -Command "Remove-Item -Path '*.spec' -Force"
	pwsh -Command "Remove-Item -Path 'dist\*' -Force"
	pwsh -Command "Remove-Item -Path 'build' -Recurse -Force"

rebuild:
	make clear_build
	make build
