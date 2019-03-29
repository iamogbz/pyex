ifndef DEST
override DEST = "."
endif

.PHONY: help
help:
	@echo "make help                         - show commands that can be run"
	@echo "make install                      - install project requirements"
	@echo "make test keyword='Parse'         - run only test match keyword"
	@echo "make tests                        - run all tests"
	@echo "make coverage                     - run all tests and collect coverage"
	@echo "make build                        - build pyex executable from src"
	@echo "DEST='/usr/local/bin' make build  - build pyex executable into folder"

.PHONY: install
install:
	@pip install -r requirements.txt

.PHONY: tests
tests:
	@export PYTHONPATH=./src:$$PYTHONPATH && pytest

.PHONY: test
test:
	@export PYTHONPATH=./src:$$PYTHONPATH && pytest -k $(keyword)

.PHONY: coverage
coverage:
	@export PYTHONPATH=./src:$$PYTHONPATH && coverage run --source=. -m pytest
	@coverage html

.PHONY: build
build:
	@python src src -O $(DEST)/pyex -G "__tests__" "__pycache__" "*.pyc"
