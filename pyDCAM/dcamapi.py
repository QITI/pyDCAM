import ctypes
import numpy as np
from .dcamapi_enum import *
from .dcamapi_struct import *
from .dcamprop import *
from typing import Tuple
import os

if os.environ["BUILDING_DOCS"] != "1":
    dcamapi = ctypes.windll.dcamapi


DCAM_DEFAULT_ARG = 0

_pixel_type_to_ctypes = {
    DCAM_PIXELTYPE.DCAM_PIXELTYPE_MONO16: ctypes.c_uint16,
    DCAM_PIXELTYPE.DCAM_PIXELTYPE_MONO8: ctypes.c_uint8
}

_pixel_type_to_numpy = {
    DCAM_PIXELTYPE.DCAM_PIXELTYPE_MONO16: np.uint16,
    DCAM_PIXELTYPE.DCAM_PIXELTYPE_MONO8: np.uint8
}


def failed(dcamerr):
    return True if dcamerr < 0 else False


class DCAMError(Exception):
    def __init__(self, error_code):
        self.error_code = error_code

    def __str__(self):
        return "{0}".format(
            DCAMERR(self.error_code).name
        )


def check_status(dcamerr):
    if not dcamerr == DCAMERR.DCAMERR_SUCCESS:
        raise DCAMError(dcamerr)


def dcamapi_init():
    # TODO Add init options
    # option = (ctypes.c_int32 * 2)()
    # option[0] = DCAMAPI_INITOPTION.DCAMAPI_INITOPTION_APIVER__LATEST
    # option[1] = DCAMAPI_INITOPTION.DCAMAPI_INITOPTION_ENDMARK
    param = DCAMAPI_INIT()
    param.size = ctypes.sizeof(param)
    # param.initoption = ctypes.cast(ctypes.pointer(option), ctypes.c_char_p)
    # param.initoptionbytes = ctypes.sizeof(option)
    param.initoption = None
    param.guid = None
    check_status(dcamapi.dcamapi_init(ctypes.byref(param)))
    return param.iDeviceCount


def dcamapi_uninit():
    check_status(dcamapi.dcamapi_uninit())


class _USE_DCAMAPI(object):
    def __enter__(self):
        return dcamapi_init()

    def __exit__(self, exc_type, exc_val, exc_tb):
        dcamapi_uninit()


use_dcamapi = _USE_DCAMAPI()


class HDCAM(object):
    def __init__(self, index=0):
        param = DCAMDEV_OPEN()
        param.index = index
        param.size = ctypes.sizeof(param)
        param.size = ctypes.sizeof(param)

        check_status(dcamapi.dcamdev_open(ctypes.byref(param)))

        self.hdcam = param.hdcam

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dcamdev_close()

    def dcamdev_close(self):
        check_status(dcamapi.dcamdev_close(self.hdcam))

    def dcamdev_getcapbility(self):
        raise NotImplementedError

    def dcamdev_getstring(self, iString: DCAM_IDSTR) -> str:
        param = DCAMDEV_STRING()
        param.size = ctypes.sizeof(param)
        param.iString = iString

        TEXT_BYTES = 100
        text = ctypes.create_string_buffer(TEXT_BYTES)
        param.text = ctypes.cast(text, ctypes.c_char_p)
        param.textbytes = TEXT_BYTES

        check_status(
            dcamapi.dcamdev_getstring(self.hdcam, ctypes.byref(param))
        )

        return text.value.decode("ascii")

    def dcamprop_getattr(self, iProp: DCAMPROPMODEVALUE):
        param = DCAMPROP_ATTR()
        param.cbSize = ctypes.sizeof(param)
        param.iProp = iProp
        # param.option = 0  # reserved
        # param.iReserved1 = 0  # reserved
        # param.iGroup = 0  # reserved
        # param.iReserved3 = 0  # reserved

        # TODO the return value is weird...
        err = dcamapi.dcamprop_getattr(self.hdcam, ctypes.byref(param))

        if failed(err):
            raise Exception  # TODO custom exception

        return dict(
            attribute=param.attribute,  # TODO use enum
            iUnit=DCAMPROPUNIT(param.iUnit),
            attribute2=param.attribute2,  # TODO use enum
            valuemin=param.valuemin,
            valuemax=param.valuemax,
            valuestep=param.valuestep,
            valuedefault=param.valuedefault,
            nMaxChannel=param.nMaxChannel,
            nMaxView=param.nMaxView,
            # TODO add iProp array
        )

    def dcamprop_getvalue(self, iProp: DCAMIDPROP) -> float:
        fValue = ctypes.c_double()
        check_status(
            dcamapi.dcamprop_getvalue(self.hdcam, iProp, ctypes.byref(fValue))
        )
        return fValue.value

    def dcamprop_setvalue(self, iProp: DCAMIDPROP, fValue):
        fValue = ctypes.c_double(float(fValue))
        check_status(
            dcamapi.dcamprop_setvalue(self.hdcam, iProp, fValue)
        )

    def dcamprop_setgetvalue(self, iProp: DCAMIDPROP, fValue: float) -> float:
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

    def dcamprop_getname(self, iProp: DCAMPROPMODEVALUE):
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

    def dcambuf_release(self, iKind = 0):
        check_status(
            dcamapi.dcambuf_release(self.hdcam, iKind)
        )

    # TODO Add options to return timestamp and framestamp.

    def dcambuf_lockframe(self, iFrame=-1):
        frame = DCAMBUF_FRAME()
        frame.size = ctypes.sizeof(frame)
        frame.iFrame = iFrame  # This can be set to -1 to retrieve the latest captured image.
        check_status(
            dcamapi.dcambuf_lockframe(self.hdcam, ctypes.byref(frame))
        )

        img = np.ctypeslib.as_array(ctypes.cast(frame.buf, ctypes.POINTER(_pixel_type_to_ctypes[frame.type])),
                                    shape=(frame.height, frame.width))

        return img

    def dcambuf_copyframe(self, iFrame=-1):
        frame = DCAMBUF_FRAME()
        frame.size = ctypes.sizeof(frame)
        frame.iFrame = iFrame  # This can be set to -1 to retrieve the latest captured image.

        # TODO Support offset
        # TODO Not sure if this should be image rowbytes of buffer rowbytes
        frame.rowbytes = int(self.dcamprop_getvalue(DCAMIDPROP.DCAM_IDPROP_IMAGE_ROWBYTES))
        frame.width = int(self.dcamprop_getvalue(DCAMIDPROP.DCAM_IDPROP_IMAGE_WIDTH))
        frame.height = int(self.dcamprop_getvalue(DCAMIDPROP.DCAM_IDPROP_IMAGE_HEIGHT))
        frame.left = 0
        frame.top = 0

        pixel_type = DCAM_PIXELTYPE(self.dcamprop_getvalue(DCAMIDPROP.DCAM_IDPROP_IMAGE_PIXELTYPE))

        img = np.empty(shape=(frame.height, frame.width), dtype=_pixel_type_to_numpy[pixel_type])
        frame.buf = img.ctypes.data

        check_status(
            dcamapi.dcambuf_copyframe(self.hdcam, ctypes.byref(frame))
        )

        return img

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

    def dcamcap_firetrigger(self):
        check_status(
            dcamapi.dcamcap_firetrigger(self.hdcam, ctypes.c_int32(0))
        )

    def dcamwait_open(self):
        param = DCAMWAIT_OPEN()
        param.size = ctypes.sizeof(param)
        param.hdcam = self.hdcam
        check_status(
            dcamapi.dcamwait_open(ctypes.byref(param))
        )
        return HDCAMWAIT(param.hwait, param.supportevent)

    # ===== quick API =====

    @property
    def readout_speed(self) -> DCAMPROPMODEVALUE:
        return DCAMPROPMODEVALUE(self.dcamprop_getvalue(DCAMIDPROP.DCAM_IDPROP_READOUTSPEED))
    
    @readout_speed.setter
    def readout_speed(self, value: DCAMPROPMODEVALUE):
        self.dcamprop_setvalue(DCAMIDPROP.DCAM_IDPROP_READOUTSPEED, float(value))

    @property
    def camera_id(self) -> str:
        return self.dcamdev_getstring(DCAM_IDSTR.DCAM_IDSTR_CAMERAID)

    @property
    def model(self) -> str:
        return self.dcamdev_getstring(DCAM_IDSTR.DCAM_IDSTR_MODEL)

    @property
    def bus(self) -> str:
        return self.dcamdev_getstring(DCAM_IDSTR.DCAM_IDSTR_BUS)

    @property
    def exposure_time(self) -> float:
        return self.dcamprop_getvalue(DCAMIDPROP.DCAM_IDPROP_EXPOSURETIME)

    @exposure_time.setter
    def exposure_time(self, value: float):
        self.dcamprop_setvalue(DCAMIDPROP.DCAM_IDPROP_EXPOSURETIME, value)

    @property
    def subarray_pos(self) -> Tuple[int, int]:
        """The subarray position in (x, y)"""
        return (int(self.dcamprop_getvalue(DCAMIDPROP.DCAM_IDPROP_SUBARRAYHPOS)),
            int(self.dcamprop_getvalue(DCAMIDPROP.DCAM_IDPROP_SUBARRAYVPOS)))


    @subarray_pos.setter
    def subarray_pos(self, value: Tuple[int, int]):
        self.dcamprop_setvalue(DCAMIDPROP.DCAM_IDPROP_SUBARRAYHPOS, value[0])
        self.dcamprop_setvalue(DCAMIDPROP.DCAM_IDPROP_SUBARRAYVPOS, value[1])

    @property
    def subarray_mode(self) -> bool:
        """The subarray mode. True for on, False for off."""
        mode = self.dcamprop_getvalue(DCAMIDPROP.DCAM_IDPROP_SUBARRAYMODE)
        if mode == DCAMPROPMODEVALUE.DCAMPROP_MODE__ON:
            return True
        elif mode == DCAMPROPMODEVALUE.DCAMPROP_MODE__ON:
            return False
        else:
            raise AssertionError

    @subarray_mode.setter
    def subarray_mode(self, value: bool):
        mode = DCAMPROPMODEVALUE.DCAMPROP_MODE__ON if value else DCAMPROPMODEVALUE.DCAMPROP_MODE__OFF
        self.dcamprop_setvalue(DCAMIDPROP.DCAM_IDPROP_SUBARRAYMODE, mode)

    @property
    def subarray_size(self) -> Tuple[int, int]:
        """The subarray size in (width, height)"""
        return (int(self.dcamprop_getvalue(DCAMIDPROP.DCAM_IDPROP_SUBARRAYHSIZE)),
                int(self.dcamprop_getvalue(DCAMIDPROP.DCAM_IDPROP_SUBARRAYVSIZE)))

    @subarray_size.setter
    def subarray_size(self, value: Tuple[int, int]):
        self.dcamprop_setvalue(DCAMIDPROP.DCAM_IDPROP_SUBARRAYHSIZE, value[0])
        self.dcamprop_setvalue(DCAMIDPROP.DCAM_IDPROP_SUBARRAYVSIZE, value[1])



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

    def dcamwait_abort(self):
        check_status(
            dcamapi.dcamwait_abort(self.h)
        )
