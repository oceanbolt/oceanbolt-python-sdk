lint:
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

test:
	pytest

docs:
	cd doc
	make html

