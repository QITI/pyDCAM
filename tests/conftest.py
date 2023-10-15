import pytest
import pyDCAM
import importlib

@pytest.fixture()
def camindex():
    return 0

@pytest.fixture()
def hdcam(camindex):
    importlib.reload(pyDCAM)

    pyDCAM.dcamapi_init()
    hdcam = pyDCAM.HDCAM(camindex)
    yield hdcam
    hdcam.dcamdev_close()
    pyDCAM.dcamapi_uninit()