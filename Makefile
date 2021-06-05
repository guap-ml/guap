# Makefile

.DEFAULT_GOAL := help

repo_name = guap
version = 0.1.4


help:
	@echo "AVAILABLE COMMANDS"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf " \033[36m%-30s\033[0m %s\n", $$1, $$2}'

bake: ## Init a poetry env and installing some useful packages (run this first). Install poetry with `pip install poetry`.
	@poetry init
	@poetry add  loguru
	@poetry add --dev hypothesis pytest-cov tox radon cloc black isort mypy setuptools
	@echo "Python 🐍 env set using Poetry 🎉"
	@git init .
	@echo "Coding time! ✨ 🚀"

devmoji: ## Init devmoji (add emojis to commit messages). Install it with `npm install -g devmoji`.
	@cp .git/hooks/prepare-commit-msg.sample .git/hooks/prepare-commit-msg
	@echo "#!/bin/sh\n\nCOMMIT_MSG_FILE=\$$1\nCOMMIT_MSG=\$$(cat \$$COMMIT_MSG_FILE)\n\necho \"\$${COMMIT_MSG}\" | devmoji > \$$1" > .git/hooks/prepare-commit-msg

update_deps: ## Update dependencies.
	@poetry update

test: ## Run unit tests.
	@poetry run pytest --disable-pytest-warnings
	@echo "The tests pass! ✨ 🍰 ✨"

coverage: ## Run coverage tests.
	@poetry run pytest --cov=./$(repo_name) --disable-pytest-warnings
	@echo "The tests pass! ✨ 🍰 ✨"

tox: ## Run tox.
	@poetry run tox
	@echo "The tests pass! ✨ 🍰 ✨"

reqs: ## Generate a requirements.txt file.
	@poetry export --without-hashes -f requirements.txt -o requirements/prod.txt

reqs_dev: ## Generate a requirements_dev.txt file.
	@poetry export --dev --without-hashes -f requirements.txt -o requirements/dev.txt

cloc: ## Count blank lines, comment lines, and physical lines of source code.
	@poetry run cloc --exclude-dir .venv,.DS_Store --exclude-ext gif,pyc .

code_metrics: ## Compute various metrics from the source code (code quality).
	@poetry run radon cc mi hal . -a -na

format: ## Format the source code using black.
	@poetry run black .
	@poetry run isort .

check_format: ## Check what to change using black.
	@poetry run black --check .

isort: ## Sort the imports using isort.
	@poetry run isort .

mypy: ## Run mypy for data type check
	@poetry run mypy $(repo_name)/

build: ## Build the python package using Poetry.
	@poetry build

generate_setup: ## Generate a setup.py file.
	@tar -xvf dist/*.tar.gz '*/setup.py'
	@cp guap-${version}/setup.py setup.py
	@poetry run black setup.py

clean: ## Delete unwanted files.
	@rm -rf `find . -name __pycache__`
	@rm -rf `find . -name dist`
	@rm -rf `find . -name build`
	@rm -rf `find . -name .DS_Store`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -rf `find . -type d -name '*.egg-info' `
	@rm -rf `find . -type d -name 'pip-wheel-metadata' `
	@rm -rf `find . -type d -name 'tmp*' `
	@rm -rf `find . -type d -name $(repo_name)-$(version)`
	@rm -rf .DS_Store
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf htmlcov
	@rm -rf *.egg-info
	@rm -f .coverage
	@rm -f .coverage.*
	@rm -rf generated
	@find . -name '*.pyc' -exec rm --force {} +
	@find . -name '*.pyo' -exec rm --force {} +
	@find . -name '*~'    -exec rm --force {} +
	@find . -name '.tox'  -exec rm --force {} +
	@echo "Your repo is clean! 🧹 👌🏼 ✨"
