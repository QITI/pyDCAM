# pyDCAM
## Dependencies
### DCAM-API
`pyDCAM` relies on DCAM-API to interact with the camera. The installation file of DCAM-API can be downloaded from: https://dcam-api.com/downloads/
## Installation
One can install `pyDCAM` package via setuptools:
```
python setup.py install
```
To install the package in [develop mode](https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install) instead, use:
```
python setup.py develop
```

## Test
Run the tests in the test folder:
```
pytest -v test/
```
