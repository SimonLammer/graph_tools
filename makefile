install:
	pip3 install numpy
	pip3 install pygame
	pip3 install pycodestyle
	pip3 install -e .

pep8:
	autopep8 --in-place graphtool/*.py
	autopep8 --in-place tests/*.py

test:
	pytest tests/*.py
	pycodestyle graphtool/*.py
	pycodestyle tests/*.py
