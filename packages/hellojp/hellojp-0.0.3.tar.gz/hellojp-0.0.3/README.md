## JFrog example project

This is an example python project demonstrating how to publish a module to Artifactory.

## Configuration

To resolve packages from Artifactory using pip, add the following to ~/.pip/pip.conf:
```
[global]
index-url = https://<Artifactory-url>/artifactory/api/pypi/<PyPI-Repository>/simple
local/simple
```

## Installation

Run the following commands to build & publish your module:
```
source venv/bin/activate
pip install twine
python setup.py sdist bdist_wheel
pip install dist/hellojp-0.0.1-py3-none-any.whl --force-reinstall
hellojp

twine upload dist/*
https://pypi.org/project/hellojp/0.0.2/
pip install hellojp==0.0.2

```
