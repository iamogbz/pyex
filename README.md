# pyex

Convert folder containing python source code to a single executable file

[![Build Status](https://travis-ci.org/iamogbz/pyex.svg?branch=master)](https://travis-ci.org/iamogbz/pyex?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/iamogbz/pyex/badge.svg?branch=master)](https://coveralls.io/github/iamogbz/pyex?branch=master)

## Requirements

A version of [Python](https://www.python.org/downloads/) in your path, preferably Python 3

## Install

Clone repository

```sh
git clone git@github.com:iamogbz/pyex.git
```

Build `pyex` from src using pyex src into your `/usr/local/bin` directory

```sh
make build
```

## Usage

```sh
$ pyex -h
usage: pyex [-h] --output OUTPUT [--install] [--ignore [IGNORE [IGNORE ...]]]
            path

positional arguments:
  path                  path to the python script (folder with __main__.py
                        entry point)

optional arguments:
  -h, --help            show this help message and exit
  -O OUTPUT, --output OUTPUT
                        filename of built executable
  -I, --install         install requirements.txt and include in executable
  -G [IGNORE [IGNORE ...]], --ignore [IGNORE [IGNORE ...]]
                        glob pattern of src files to ignore
```

First check your code can be executed

```sh
python /path/to/directory
```

If satisfied, build single executable file

```sh
pyex /path/to/directory -O /path/to/executable -G "__tests__" "__pycache__" "*.pyc"
```

## Caveats

1. Requires a `__main__.py` file in the directory being coverted
2. Code in resulting executable is always compiled on first run
