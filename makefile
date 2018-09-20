install:
	pip3 install numpy
	pip3 install pygame
	pip3 install pycodestyle
	pip3 install -e .

pep8:
	autopep8 --in-place graphtool/*.py tests/*.py

test:
	pytest --cov=graphtool
  pycodestyle graphtool tests
