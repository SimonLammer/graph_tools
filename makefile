install:
	pip3 uninstall -y graphtool
	pip3 install --user .

pep8:
	autopep8 --in-place graphtool/*.py
	autopep8 --in-place graphtool/graph/*.py
	autopep8 --in-place graphtool/algorithms/*.py
	autopep8 --in-place graphtool/geometry/*.py
	autopep8 --in-place tests/*.py

test:
	#pipenv install -e .
	#pipenv run pytest tests/*.py
	pytest tests/*.py
	pycodestyle graphtool/*.py
	pycodestyle graphtool/graph/*.py
	pycodestyle graphtool/algorithms/*.py
	pycodestyle graphtool/geometry/*.py
	pycodestyle tests/*.py

clean:
	rm -f Pipfile Pipfile.lock
