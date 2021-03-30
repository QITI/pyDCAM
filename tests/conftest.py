import pytest
import pyDCAM

@pytest.fixture()
def camindex():
    return 0

@pytest.fixture()
def hdcam(camindex):
    pyDCAM.dcamapi_init()
    hdcam = pyDCAM.HDCAM(camindex)
    yield hdcam
    hdcam.dcamdev_close()
    pyDCAM.dcamapi_uninit()