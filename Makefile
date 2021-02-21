lint:
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

buildpkg:
	python -m build --sdist --wheel --outdir dist/

check:
	twine check dist/*

test:
	pytest

builddocs:
	sphinx-build docs/source docs/build

builddocsnetlify:
	pip install -e .[docs]
	sphinx-build docs/source docs/build

publish:
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	python -m build --sdist --wheel --outdir dist/
	twine check dist/*
	sphinx-build docs/source docs/build

