# pyDCAM
`pyDCAM` is the python bindings for Hamamatsu DCAM-API, allowing one to control Hamamatsu cameras in python.
The documentation and the examples can be found at: https://pydcam.pages.dev/
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
Run the tests in the tests folder:
```
pytest -v tests/
```
