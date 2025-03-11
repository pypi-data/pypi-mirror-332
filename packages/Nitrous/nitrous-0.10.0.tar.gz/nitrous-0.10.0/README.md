Project Nitrous
===============

![nitrous logo](doc/nitrous.png)

Project Nitrous is a port of TurboGears 1 to a modern development stack

* Python 3
* CherryPy recent
* SQLAlchemy recent
* IPython recent

### Dev/Test Setup
```commandline
virtualenv -p python3.10 venv
. venv/bin/activate
pip install -e .[dev]
```

#### Running tests:
```commandline
pytest -q tests/
```