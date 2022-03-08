VERSION 0.6
FROM --platform=linux/amd64 python:3.9
WORKDIR /code

all:
    BUILD +test
    BUILD +lint
    BUILD +build

deps:
    COPY setup.py setup.py
    COPY README.md README.md
    COPY scripts scripts
	RUN pip install -e ".[docs,test,publish]"
    SAVE IMAGE

build:
    FROM +deps
	RUN python -m build --sdist --wheel --outdir dist/
	RUN twine check dist/*

test:
    FROM +deps
    COPY . .
    RUN pytest --ignore-glob='*site-packages*' --ignore='conda' --ignore='venv'

lint:
    FROM +deps
    COPY . .
    RUN flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics