.PHONY: help
help:
	@echo "make help		- show commands that can be run"
	@echo "make install		- install project requirements"
	@echo "make test 		- run tests"
	@echo "make build 		- build pyex executable from src"

.PHONY: install
install:
	@pip install -r requirements.txt

.PHONY: test
test:
	@export PYTHONPATH=./src:$$PYTHONPATH && pytest

.PHONY: build
build:
	@python src src -O /usr/local/bin/pyex -G "__tests__" "__pycache__" "*.pyc"
