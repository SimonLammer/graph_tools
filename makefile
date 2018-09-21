install:
	pip3 uninstall -y graphtool
	pip3 install .

pep8:
	autopep8 --in-place graphtool/*.py
	autopep8 --in-place tests/*.py

test:
	pytest tests/*.py
	pycodestyle graphtool/*.py
	pycodestyle tests/*.py
