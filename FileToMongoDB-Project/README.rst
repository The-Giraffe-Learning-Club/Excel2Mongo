py -m venv venv
venv\Scripts\activate.bat

python -m pip install --upgrade pip setuptools wheel

To update dependencies:
	python -m pip install pip-tools
	python -m piptools compile --upgrade requirements.in
	python -m piptools compile --upgrade dev-requirements.in



To cleanly install your dependencies into your virtual environment:
	python -m piptools sync requirements.txt dev-requirements.txt
	

python setup.py sdist bdist_wheel

python setup.py dist/fact-1.0.0.tar.gz dist/fact-1.0.0-py3-none-any.whl