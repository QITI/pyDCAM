import ctypes
from .dcamapi_enum import *
from .dcamapi_struct import *

dcamapi = ctypes.windll.dcamapi

DCAM_DEFAULT_ARG = 0

def check_status(dcamerr):
    if not dcamerr == DCAMERR.DCAMERR_SUCCESS:
        print(dcamerr)
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

    def dcamdev_close(self):
        check_status(dcamapi.dcamdev_close(self.hdcam))

    def dcamdev_getcapbility(self):
        raise NotImplementedError

    def dcamdev_getstring(self):
        raise NotImplementedError


    def dcamprop_getattr(self, iProp):
        param = DCAMPROP_ATTR()
        param.cbSize = ctypes.sizeof(param)
        param.Iprop = iProp
        param.option = 0  # reserved
        param.iReserved1 = 0  # reserved
        param.iGroup = 0  # reserved

        check_status(dcamapi.dcamprop_getattr(param))

        return dict(
            attribute = int(param.attribute), # TODO use enum
            iUnit = int(param.iUnit), # TODO use enum
            attribute2 =int(param.attribute2), # TODO use enum
            valuemin = param.valuemin.value,
            valuemax=param.valuemax.value,
            valuestep=param.valuestep.value,
            valuedefault=param.valuedefault.value,
            nMaxChannel=param.nMaxChannel.value,
            nMaxView=param.nMaxView.value,
            #TODO add iProp array
        )



    def dcampropo_getvalue(self, iProp):
        fValue = ctypes.c_double()
        check_status(
            dcamapi.dcamprop_getvalue(self.hdcam, iProp, ctypes.byref(fValue))
        )
        return fValue.value

    def dcamprop_setvalue(self, iProp, fValue):
        fValue = float(fValue)
        check_status(
            dcamapi.dcamprop_setvalue(self.hdcam, iProp, fValue)
        )

    def dcamprop_setgetvalue(self, iProp, fValue):
        fValue = ctypes.c_double(fValue)
        check_status(
            dcamapi.dcamprop_setgetvalue(self.hdcam, iProp, ctypes.byref(fValue), 0)
        )
        return fValue.value

    def dcamprop_queryvalue(self):
        raise NotImplementedError

    def dcamprop_ids(self, option=DCAM_DEFAULT_ARG):
        iProp = ctypes.c_int32(0)

        while True:
            err = dcamapi.dcamprop_getnextid(self.hdcam, ctypes.byref(iProp), option)
            if err == DCAMERR.DCAMERR_NOPROPERTY:
                break
            else:
                yield iProp.value

    def dcamprop_getname(self, iProp):
        textbytes = 64
        text = ctypes.create_string_buffer(textbytes)

        check_status(
            dcamapi.dcamprop_getname(self.hdcam, iProp,ctypes.byref(text), textbytes)
        )

        return text.value.decode("ascii")

    def dcamprop_getvaluetext(self):
        raise NotImplementedError









