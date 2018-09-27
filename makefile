install:
	pip3 uninstall -y graphtool
	pip3 install --user .

pep8:
	autopep8 --in-place graphtool/*.py
	autopep8 --in-place tests/*.py

test: install
	#pipenv install -e .
	#pipenv run pytest tests/*.py
	pytest tests/*.py
	pycodestyle graphtool/*.py
	pycodestyle tests/*.py

clean:
	rm -f Pipfile Pipfile.lock
