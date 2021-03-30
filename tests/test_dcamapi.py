import pytest
import pyDCAM
import numpy as np
import ctypes

def test_dcamapi_init_uninit():
    pyDCAM.dcamapi_init()
    pyDCAM.dcamapi_uninit()

def test_dcamdev_open_close(camindex):
    pyDCAM.dcamapi_init()
    hdcam = pyDCAM.HDCAM(camindex)
    hdcam.dcamdev_close()

def test_dcamprop(hdcam):
    for iProp in hdcam.dcamprop_ids():
        attr = hdcam.dcamprop_getattr(iProp)
        name = hdcam.dcamprop_getname(iProp)
        value = hdcam.dcampropo_getvalue(iProp)
        print(name, ":", value)


def test_capture_single_image(hdcam):
    width = int(hdcam.dcampropo_getvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_IMAGE_WIDTH))
    height = int(hdcam.dcampropo_getvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_IMAGE_HEIGHT))
    hdcam.dcamprop_setvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_READOUTSPEED, pyDCAM.DCAMPROPMODEVALUE.DCAMPROP_READOUTSPEED__SLOWEST)
    hdcam.dcamprop_setvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_EXPOSURETIME, 0.01)
    array = np.empty((height, width), dtype=np.uint16)
    hdcam.dcambuf_alloc(10)
    hwait = hdcam.dcamwait_open()
    hdcam.dcamcap_start()
    hwait.dcamwait_start()
    frame = hdcam.dcambuf_lockframe()
    ctypes.memmove(array.ctypes.data, frame.buf, width * height * 2)


