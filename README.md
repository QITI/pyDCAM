# pyDCAM
`pyDCAM` is the python bindings for Hamamatsu DCAM-API, allowing one to control Hamamatsu cameras in python.
The documentation and the examples can be found at: https://pydcam.pages.dev/
## Dependencies
### DCAM-API
`pyDCAM` relies on DCAM-API to interact with the camera. The installation file of DCAM-API can be downloaded from: https://dcam-api.com/downloads/
## Installation
One can install `pyDCAM` package via the following command
```
pip install .
```
One can also clone the repository to install it in the develop mode:
```
pip install -e .
```

## Test
Run the tests in the tests folder:
```
pytest -v tests/
```
