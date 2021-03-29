import pytest
import pyDCAM


def test_dcamapi_init_uninit():
    pyDCAM.dcamapi_init()
    pyDCAM.dcamapi_uninit()


def test_dcamprop(camindex):
    pyDCAM.dcamapi_init()
    hdcam = pyDCAM.HDCAM(camindex)
    for iProp in hdcam.dcamprop_ids():
        attr = hdcam.dcamprop_getattr(iProp)
        name = hdcam.dcamprop_getname(iProp)
        value = hdcam.dcampropo_getvalue(iProp)

        print(name, ":", value)

