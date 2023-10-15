import ctypes
import numpy as np
from .dcamapi_enum import *
from .dcamapi_struct import *
from .dcamprop import *
from typing import Tuple
import os

if "BUILDING_DOCS" not in os.environ:
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
    """Initialize the DCAM-API. It should be called before using any other DCAM-API functions."""
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
    """Uninitialize the DCAM-API."""
    check_status(dcamapi.dcamapi_uninit())


class _USE_DCAMAPI(object):
    def __enter__(self):
        return dcamapi_init()

    def __exit__(self, exc_type, exc_val, exc_tb):
        dcamapi_uninit()


use_dcamapi = _USE_DCAMAPI()


class HDCAM(object):
    """Camera handle. 

    It's recommended to use with statement to ensure the camera is closed properly.
    
    Parameters
    ----------
    index : int, optional
        The index of the camera to open. Defaults to 0.

    Examples
    --------
    >>> with HDCAM() as hdcam:
    >>>     print(hdcam.model)
    >>>     print(hdcam.camera_id)
    
    """
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
        """Close the camera handle."""
        check_status(dcamapi.dcamdev_close(self.hdcam))

    def dcamdev_getstring(self, iString: DCAM_IDSTR) -> str:
        """Get the string of the camera.
        
        Parameters
        ----------
        iString : DCAM_IDSTR
            The string to get. 

        """
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
        """Get the value of the property.
        
        Parameters
        ----------
        iProp : DCAMIDPROP
            The property ID.

        Returns
        -------
        float
            The value of the property.
        """
        fValue = ctypes.c_double()
        check_status(
            dcamapi.dcamprop_getvalue(self.hdcam, iProp, ctypes.byref(fValue))
        )
        return fValue.value

    def dcamprop_setvalue(self, iProp: DCAMIDPROP, fValue):
        """Set the value of the property.
        
        Parameters
        ----------
        iProp : DCAMIDPROP
            The property ID.

        Raises
        ------
        DCAMError
            If the device does not support a property. An error with code DCAMERR_NOTSUPPORT is raised.
            If a property does not have auto-rounding and the fValue is not a valid value,
            an error with code DCAMERR_INVALIDPARAM is raised.
        """
        fValue = ctypes.c_double(float(fValue))
        check_status(
            dcamapi.dcamprop_setvalue(self.hdcam, iProp, fValue)
        )

    def dcamprop_setgetvalue(self, iProp: DCAMIDPROP, fValue: float) -> float:
        """Set the value of the property and get the accurate value if successful. 

        Parameters
        ----------
        iProp : DCAMIDPROP
            The property ID.

        Returns
        -------
        float
            The value of the property.

        Raises
        ------
        DCAMError
            If the device does not support a property. An error with code DCAMERR_NOTSUPPORT is raised.
            If a property does not have auto-rounding and the fValue is not a valid value,
            an error with code DCAMERR_INVALIDPARAM is raised.
        """
        fValue = ctypes.c_double(fValue)
        check_status(
            dcamapi.dcamprop_setgetvalue(self.hdcam, iProp, ctypes.byref(fValue), 0)
        )
        return fValue.value

    def dcamprop_ids(self, option: DCAMPROPOPTION = DCAMPROPOPTION.DCAMPROP_OPTION_SUPPORT) -> DCAMIDPROP:
        """Generator for enumerating the property IDs.
        
        Parameters
        ----------
        option: DCAMPROPOPTION, optional
            Defaults to the properties supported by the device.

        Yields
        ------
        iProp: DCAMIDPROP
            The property ID.

        Examples
        --------
        >>> with HDCAM() as hdcam:
        >>>     for iProp in hdcam.dcamprop_ids():
        >>>         print(hdcam.dcamprop_getname(iProp))

        """
        iProp = ctypes.c_int32(0)

        while True:
            err = dcamapi.dcamprop_getnextid(self.hdcam, ctypes.byref(iProp), option)
            if err == DCAMERR.DCAMERR_NOPROPERTY:
                break
            else:
                yield iProp.value

    def dcamprop_getname(self, iProp: DCAMIDPROP) -> str:
        """Get the name of the property.

        Parameters
        ----------
        iProp : DCAMIDPROP
            The property ID.

        Returns
        -------
        str
            The name of the property.
        """
        textbytes = 64
        text = ctypes.create_string_buffer(textbytes)

        check_status(
            dcamapi.dcamprop_getname(self.hdcam, iProp, ctypes.byref(text), textbytes)
        )

        return text.value.decode("ascii")


    def dcambuf_alloc(self, framecount=64):
        """Allocates internal image buffers for image acquisition. 
        
        This function does not start the capture. To start capture, dcamcap_start() should be called.

        When the internal buffers are no longer necessary, call dcambuf_release() to release them.
        
        Parameters
        ----------
        framecount : int, optional
            The number of frames to allocate. Defaults to 64.
        """
        check_status(
            dcamapi.dcambuf_alloc(self.hdcam, framecount)
        )


    def dcambuf_release(self, iKind = 0):
        """Release the internal image buffers allocated by dcambuf_alloc()."""
        check_status(
            dcamapi.dcambuf_release(self.hdcam, iKind)
        )

    def dcambuf_lockframe(self, iFrame=-1) -> np.ndarray:
        """ Returns a NumPy array pointing to the captured image buffer.

        If the host software dcambuf_copyframe needs to copy the image data into its own memory, 
        use dcambuf_copyframe() instead of this function.

        Parameters
        ----------
        iFrame : int, optional
            The frame index. Defaults to -1, which retrieves the latest captured image.

        Returns
        -------
        img: np.ndarray
            The captured image buffer.

        See Also
        --------
        HDCAM.dcambuf_copyframe : The function that copied the captured image buffer instead of pointing to it.
        """
        frame = DCAMBUF_FRAME()
        frame.size = ctypes.sizeof(frame)
        frame.iFrame = iFrame  # This can be set to -1 to retrieve the latest captured image.
        check_status(
            dcamapi.dcambuf_lockframe(self.hdcam, ctypes.byref(frame))
        )

        img = np.ctypeslib.as_array(ctypes.cast(frame.buf, ctypes.POINTER(_pixel_type_to_ctypes[frame.type])),
                                    shape=(frame.height, frame.width))

        return img

    def dcambuf_copyframe(self, iFrame=-1) -> np.ndarray:
        """Returns a NumPy array containing the captured image copied from the buffer.
        
        Parameters
        ----------
        iFrame : int, optional
            The frame index. Defaults to -1, which retrieves the latest captured image.

        Returns
        -------
        img: np.ndarray
            The captured image buffer.
        
        """
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

    def dcamcap_start(self, mode=DCAMCAP_START.DCAMCAP_START_SEQUENCE):
        """start capturing images. 
        
        Before calling this function, a capturing buffer should be prepared.
        
        Parameters
        ----------
        mode : DCAMCAP_START, optional
            The capture mode. Defaults to DCAMCAP_START_SEQUENCE.
            With the DCAMCAP_START_SEQUENCE mode, capturing will be continuing until the dcamcap_stop() function is called. 
            With the DCAMCAP_START_SNAP mode, 
            capturing is terminated when the capturing buffer is filled or until the dcamcap_stop() function is called.
        
        See Also
        --------
        HDCAM.dcamcap_stop : Stop capturing images.
        HDCAM.dcambuf_alloc : Allocate internal image buffers for image acquisition.
        
        """
        check_status(
            dcamapi.dcamcap_start(self.hdcam, mode)
        )

    def dcamcap_stop(self):
        """Stop capturing images.

        See Also
        --------
        HDCAM.dcamcap_start : Start capturing images.
        """
        check_status(
            dcamapi.dcamcap_stop(self.hdcam)
        )

    def dcamcap_status(self):
        iStatus = ctypes.c_int32(0)
        check_status(
            dcamapi.dcamcap_status(self.hdcam, ctypes.byref(iStatus))
        )
        return DCAMCAP_STATUS(iStatus)

    def dcamcap_transferinfo(self) -> Tuple[int, int]:
        """Get the transfer information.
        
        Returns
        -------
        nNewestFrameIndex: int
            The index of the newest frame of the transferred image.

        nFrameCount: int
            The number of iamges has been transferred.
        """
        param = DCAMCAP_TRANSFERINFO()
        param.size = ctypes.sizeof(param)
        check_status(
            dcamapi.dcamcap_transferinfo(self.hdcam, ctypes.byref(param))
        )
        return param.nNewestFrameIndex, param.nFrameCount

    def dcamcap_firetrigger(self):
        """Fire a software trigger.
        
        This is only effective if the software trigger mode.
        """
        check_status(
            dcamapi.dcamcap_firetrigger(self.hdcam, ctypes.c_int32(0))
        )

    def dcamwait_open(self) -> "HDCAMWAIT":
        """Open a wait handle for the camera.
        
        See Also
        --------
        HDCAMWAIT.dcamwait_close : Close the wait handle.
        """
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
        """The camera ID."""
        return self.dcamdev_getstring(DCAM_IDSTR.DCAM_IDSTR_CAMERAID)

    @property
    def model(self) -> str:
        """The camera model."""
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
    """Wait handle for the camera. It is used to block the program and wait for a specific event.

    Instead of instantiating this class directly, use HDCAM.dcamwait_open() to open a wait handle.

    See Also
    --------
    HDCAM.dcamwait_open : Open a wait handle for the camera.

    """
    def __init__(self, hwait, supportevent):
        self.h = hwait
        self.supportevent = supportevent

    def dcamwait_close(self):
        check_status(
            dcamapi.dcamwait_close(self.h)
        )

    def dcamwait_start(self, eventmask=DCAMWAIT_EVENT.DCAMWAIT_CAPEVENT_FRAMEREADY,
                       timeout=DCAMWAIT_TIMEOUT.DCAMWAIT_TIMEOUT_INFINITE):
        """Start waiting for a specific event.
        
        Parameters
        ----------
        eventmask : DCAMWAIT_EVENT, optional
            The event to wait for. Defaults to waiting for the next frame ready event.

        timeout : int, optional
            The timeout in milliseconds. Defaults to no timeout.

        """
        param = DCAMWAIT_START()
        param.size = ctypes.sizeof(param)
        param.eventmask = eventmask
        param.timeout = timeout
        check_status(
            dcamapi.dcamwait_start(self.h, ctypes.byref(param))
        )
        return param.eventhappened

    def dcamwait_abort(self):
        """Abort waiting for the event."""
        check_status(
            dcamapi.dcamwait_abort(self.h)
        )
