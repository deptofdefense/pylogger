.PHONY: help
help:  ## Print the help documentation
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

#
# Python
#

.PHONY: requirements
requirements:  ## install Python requirements
	pip3 install -r requirements.txt

.PHONY: editable
editable:  ## install this repo as editable
	pip3 install -e .

.PHONY: python_build
python_build:
	python3  -m build

.PHONY: flake8
flake8:
	python3 -m flake8 pylogger setup.py

.PHONY: test
test_python:
	python3 -m unittest pylogger.tests -v

.PHONY: venv
venv:
	python3 -m venv .venv

#
# Clean Targets
#

clean:
	rm -fr bin
	rm -fr data
	rm -fr temp
	rm -fr *.egg-info
