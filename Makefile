.PHONY: help
help:
	@echo "make help		- show commands that can be run"
	@echo "make install		- install project requirements"
	@echo "make tests 		- run all tests"
	@echo "make test-name 	- run only tests marked with 'name'"
	@echo "make build 		- build pyex executable from src"

.PHONY: install
install:
	@pip install -r requirements.txt

.PHONY: tests
tests:
	@export PYTHONPATH=./src:$$PYTHONPATH && pytest

.PHONY: test
test-%:
	@export PYTHONPATH=./src:$$PYTHONPATH && pytest -m $*

.PHONY: build
build:
	@python src src -O /usr/local/bin/pyex -G "__tests__" "__pycache__" "*.pyc"
