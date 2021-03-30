import ctypes
from .dcamapi_enum import *
from .dcamapi_struct import *

dcamapi = ctypes.windll.dcamapi

DCAM_DEFAULT_ARG = 0

def failed(dcamerr):
    return True if dcamerr < 0 else False

def check_status(dcamerr):
    if not dcamerr == DCAMERR.DCAMERR_SUCCESS:
        print(dcamerr)
        message = "[{0}]".format(DCAMERR(dcamerr).name)
        raise Exception(message) # TODO custom exception


def dcamapi_init():
    #option = (ctypes.c_int32 * 2)()
    #option[0] = DCAMAPI_INITOPTION.DCAMAPI_INITOPTION_APIVER__LATEST
    #option[1] = DCAMAPI_INITOPTION.DCAMAPI_INITOPTION_ENDMARK
    param = DCAMAPI_INIT()
    param.size = ctypes.sizeof(param)
    #param.initoption = ctypes.cast(ctypes.pointer(option), ctypes.c_char_p)
    #param.initoptionbytes = ctypes.sizeof(option)
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
        param.iProp = iProp
        #param.option = 0  # reserved
        #param.iReserved1 = 0  # reserved
        #param.iGroup = 0  # reserved
        #param.iReserved3 = 0  # reserved

        # TODO the return value is weird...
        err = dcamapi.dcamprop_getattr(self.hdcam, ctypes.byref(param))
        if failed(err):
            raise Exception # TODO custom exception


        return dict(
            attribute = int(param.attribute), # TODO use enum
            iUnit = int(param.iUnit), # TODO use enum
            attribute2 =int(param.attribute2), # TODO use enum
            valuemin = param.valuemin,
            valuemax=param.valuemax,
            valuestep=param.valuestep,
            valuedefault=param.valuedefault,
            nMaxChannel=param.nMaxChannel,
            nMaxView=param.nMaxView,
            #TODO add iProp array
        )


    def dcampropo_getvalue(self, iProp):
        fValue = ctypes.c_double()
        check_status(
            dcamapi.dcamprop_getvalue(self.hdcam, iProp, ctypes.byref(fValue))
        )
        return fValue.value

    def dcamprop_setvalue(self, iProp, fValue):
        fValue = ctypes.c_double(fValue)
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
            dcamapi.dcamprop_getname(self.hdcam, iProp, ctypes.byref(text), textbytes)
        )

        return text.value.decode("ascii")

    def dcamprop_getvaluetext(self):
        raise NotImplementedError

    def dcambuf_alloc(self, framecount=64):
        check_status(
            dcamapi.dcambuf_alloc(self.hdcam, framecount)
        )

    def dcambuf_attach(self):
        param = DCAMBUF_ATTACH()
        param.size = ctypes.sizeof(param)
        raise NotImplementedError

    def dcambuf_release(self, iKind):
        check_status(
            dcamapi.dcambuf_release(iKind)
        )

    def dcambuf_lockframe(self, iFrame=-1):
        frame = DCAMBUF_FRAME()
        frame.size = ctypes.sizeof(frame)
        frame.iFrame = iFrame # This can be set to -1 to retrieve the latest captured image.
        check_status(
            dcamapi.dcambuf_lockframe(self.hdcam, ctypes.byref(frame))
        )
        return frame

    def dcambuf_copyframe(self, iFrame=-1):
        frame = DCAMBUF_FRAME()
        frame.size = ctypes.sizeof(frame)
        frame.iFrame = iFrame  # This can be set to -1 to retrieve the latest captured image.


    def dcambuf_copymetadata(self):
        raise NotImplementedError

    def dcamcap_start(self, mode=DCAMCAP_START.DCAMCAP_START_SEQUENCE):
        check_status(
            dcamapi.dcamcap_start(self.hdcam, mode)
        )

    def dcamcap_stop(self):
        check_status(
            dcamapi.dcamcap_stop(self.hdcam)
        )

    def dcamcap_status(self):
        iStatus = ctypes.c_int32(0)
        check_status(
            dcamapi.dcamcap_status(self.hdcam, ctypes.byref(iStatus))
        )
        return DCAMCAP_STATUS(iStatus)

    def dcamcap_transferinfo(self):
        param = DCAMCAP_TRANSFERINFO()
        param.size = ctypes.sizeof(param)
        check_status(
            dcamapi.dcamcap_transferinfo(self.hdcam, ctypes.byref(param))
        )
        return param.nNewestFrameIndex, param.nFrameCount

    def dcamwait_open(self):
        param = DCAMWAIT_OPEN()
        param.size = ctypes.sizeof(param)
        param.hdcam = self.hdcam
        check_status(
            dcamapi.dcamwait_open(ctypes.byref(param))
        )
        return HDCAMWAIT(param.hwait, param.supportevent)


class HDCAMWAIT(object):
    def __init__(self, hwait, supportevent):
        self.h = hwait
        self.supportevent = supportevent

    def dcamwait_close(self):
        check_status(
            dcamapi.dcamwait_close(self.h)
        )

    def dcamwait_start(self, eventmask=DCAMWAIT_EVENT.DCAMWAIT_CAPEVENT_FRAMEREADY,
                       timeout=DCAMWAIT_TIMEOUT.DCAMWAIT_TIMEOUT_INFINITE):
        param = DCAMWAIT_START()
        param.size = ctypes.sizeof(param)
        param.eventmask = eventmask
        param.timeout = timeout
        check_status(
            dcamapi.dcamwait_start(self.h, ctypes.byref(param))
        )
        return param.eventhappened










