$(shell test -s ".env" || cp ".env.example" ".env")
ENVARS := $(shell cat ".env" | xargs)

ifndef DEST
override DEST = "."
endif

.PHONY: precommit
precommit:
	@ln -sf $(PWD)/.github/hooks/pre-commit .git/hooks/pre-commit
	echo "precommit: hook successfully configured"

.PHONY: upstream
upstream:
	@git remote add upstream https://github.com/iamogbz/py-boilerplate
	@git push origin master
	@git push --all
	echo "upstream: remote successfully configured"

.PHONY: help
help:
	@echo "make help                         - show commands that can be run"
	@echo "make install                      - install project requirements"
	@echo "make test keyword='Parse'         - run only test match keyword"
	@echo "make tests                        - run all tests"
	@echo "make coverage                     - run all tests and collect coverage"
	@echo "make build                        - build pyex executable from src"
	@echo "DEST='/usr/local/bin' make build  - build pyex executable into folder"

.PHONY: venv
venv:
	test -d venv || python3 -m venv venv
	touch venv/bin/activate

.PHONY: install
install: venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -Ur requirements.txt

.PHONY: test-prep
test-prep:
	@echo "[install]\nprefix=" > ~/.pydistutils.cfg

.PHONY: test-clean
test-clean:
	@rm ~/.pydistutils.cfg

.PHONY: tests
tests: test-prep
	env ${ENVARS} pytest
	$(MAKE) test-clean

.PHONY: test
test: test-prep
	env ${ENVARS} pytest -s -k $(keyword)
	$(MAKE) test-clean

.PHONY: coverage
coverage:
	@env ${ENVARS} coverage run --source=. -m pytest
	@coverage html

.PHONY: build
build:
	@python src src -O $(DEST)/pyex -G "__tests__" "__pycache__" "*.pyc"

ifndef VERBOSE
.SILENT:
endif
