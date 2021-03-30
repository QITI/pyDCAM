import pytest
import pyDCAM
import numpy as np
import ctypes
import time

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
        value = hdcam.dcamprop_getvalue(iProp)
        print(name, ":", value)


def test_dcambuf_lockframe(hdcam):
    hdcam.dcamprop_setvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_READOUTSPEED, pyDCAM.DCAMPROPMODEVALUE.DCAMPROP_READOUTSPEED__SLOWEST)
    hdcam.dcamprop_setvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_EXPOSURETIME, 0.01)

    hdcam.dcambuf_alloc(10)
    hwait = hdcam.dcamwait_open()
    hdcam.dcamcap_start()
    hwait.dcamwait_start()
    array1 = hdcam.dcambuf_lockframe()
    array1_copy = array1.copy()
    assert np.all(array1 == array1_copy)

    # After calling dcambuf_lockframe again. The buffer that array1 is pointing at now filled the data from array2
    hwait.dcamwait_start()
    array2 = hdcam.dcambuf_lockframe()
    assert np.all(array1 == array2)
    assert not np.all(array1 == array1_copy)

def test_dcambuf_copyframe(hdcam):
    hdcam.dcamprop_setvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_READOUTSPEED, pyDCAM.DCAMPROPMODEVALUE.DCAMPROP_READOUTSPEED__SLOWEST)
    hdcam.dcamprop_setvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_EXPOSURETIME, 0.01)

    hdcam.dcambuf_alloc(10)
    hwait = hdcam.dcamwait_open()
    hdcam.dcamcap_start()
    hwait.dcamwait_start()
    array1 = hdcam.dcambuf_copyframe()
    array1_copy = array1.copy()
    assert np.all(array1 == array1_copy)

    # After calling dcambuf_lockframe again. The buffer that array1 is pointing at now filled the data from array2
    hwait.dcamwait_start()
    array2 = hdcam.dcambuf_copyframe()
    assert not np.all(array1 == array2)
    assert np.all(array1 == array1_copy)


def test_dcambuf_lockframe_and_copyframe(hdcam):
    hdcam.dcamprop_setvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_READOUTSPEED, pyDCAM.DCAMPROPMODEVALUE.DCAMPROP_READOUTSPEED__SLOWEST)
    hdcam.dcamprop_setvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_EXPOSURETIME, 0.01)

    hdcam.dcambuf_alloc(10)
    hwait = hdcam.dcamwait_open()
    hdcam.dcamcap_start()
    hwait.dcamwait_start()
    array1_copyframe = hdcam.dcambuf_copyframe()
    array1_lockframe = hdcam.dcambuf_lockframe()
    assert np.all(array1_copyframe == array1_lockframe)


def test_capture_with_software_trigger(hdcam):
    hdcam.dcamprop_setvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_TRIGGERSOURCE, pyDCAM.DCAMPROPMODEVALUE.DCAMPROP_TRIGGERSOURCE__SOFTWARE)
    hdcam.dcamprop_setvalue(pyDCAM.DCAMIDPROP.DCAM_IDPROP_EXPOSURETIME, 0.001) # set exposure time to 1ms
    hdcam.dcambuf_alloc(10)
    hdcam.dcamcap_start()

    TIMEOUT = 100  # 100ms. This should give enough time for the image to be transfered

    hwait = hdcam.dcamwait_open()

    # There isn't any trigger, so no image should be transferred.
    with pytest.raises(Exception) as excinfo: # TODO catch proper error once we implement it
        hwait.dcamwait_start(timeout=TIMEOUT)  # It should raise timeout error
    print(excinfo)
    index, n_image = hdcam.dcamcap_transferinfo()
    assert index == -1
    assert n_image == 0

    # 1st trigger
    hdcam.dcamcap_firetrigger()
    hwait.dcamwait_start(timeout=TIMEOUT)
    index, n_image = hdcam.dcamcap_transferinfo()
    assert index == 0
    assert n_image == 1

    # 2nd trigger
    hdcam.dcamcap_firetrigger()
    hwait.dcamwait_start(timeout=TIMEOUT)
    index, n_image = hdcam.dcamcap_transferinfo()
    assert index == 1
    assert n_image == 2

