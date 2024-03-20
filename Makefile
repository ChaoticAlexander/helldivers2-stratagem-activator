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
	pwsh -Command "Copy-Item -Path 'config' -Destination 'dist/' -Recurse -Force"

clear_build:
	pwsh -Command "Remove-Item -Path '*.spec' -Force"
	pwsh -Command "Remove-Item -Path 'dist\*' -Force"
	pwsh -Command "Remove-Item -Path 'build' -Recurse -Force"

rebuild:
	make clear_build
	make build