import  ctypes
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

