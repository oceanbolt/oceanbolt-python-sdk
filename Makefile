lint:
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

buildpkg:
	python -m build --sdist --wheel --outdir dist/

check:
	twine check dist/*

test:
	pytest

builddocs:
	cd docs
	make html

