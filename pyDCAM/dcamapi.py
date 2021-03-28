import ctypes
from .dcamapi_enum import *
from .dcamapi_struct import *

dcamapi = ctypes.windll.dcamapi

def check_status(dcamerr):
    if not dcamerr == DCAMERR.DCAMERR_SUCCESS:
        message = "[{0}]".format(DCAMERR(dcamerr).name)
        raise Exception(message)


def dcamapi_init():
    param = DCAMAPI_INIT()
    param.size = ctypes.sizeof(param)
    param.initoption = None
    param.guid = None
    check_status(dcamapi.dcamapi_init(ctypes.byref(param)))
    return param.iDeviceCount


def dcamapi_uninit():
    check_status(dcamapi.dcamapi_uninit())


class HDCAM(object):
    def __init__(self, index=0):
        param = DCAMDEV_OPEN()
        param.index = index
        param.size = ctypes.sizeof(param)
        check_status(dcamapi.dcamdev_open(ctypes.byref(param)))
        self.hdcam = param.hdcam

    def close(self):
        check_status(dcamapi.dcamdev_close(self.hdcam))

    def getcapbility(self):
        check_status()


