from enum import IntEnum
from ._util import _int32


class DCAMERR(IntEnum):
    # status error
    DCAMERR_BUSY = _int32(0x80000101)  # API cannot process in busy state.
    DCAMERR_NOTREADY = _int32(0x80000103)  # API requires ready state.
    DCAMERR_NOTSTABLE = _int32(0x80000104)  # API requires stable or unstable state.
    DCAMERR_UNSTABLE = _int32(0x80000105)  # API does not support in unstable state.
    DCAMERR_NOTBUSY = _int32(0x80000107)  # API requires busy state.

    DCAMERR_EXCLUDED = _int32(0x80000110)  # some resource is exclusive and already used

    DCAMERR_COOLINGTROUBLE = _int32(0x80000302)  # something happens near cooler
    DCAMERR_NOTRIGGER = _int32(0x80000303)  # no trigger when necessary. Some camera supports this error.
    DCAMERR_TEMPERATURE_TROUBLE = _int32(0x80000304)  # camera warns its temperature
    DCAMERR_TOOFREQUENTTRIGGER = _int32(0x80000305)  # input too frequent trigger. Some camera supports this error.

    # wait error
    DCAMERR_ABORT = _int32(0x80000102)  # abort process
    DCAMERR_TIMEOUT = _int32(0x80000106)  # timeout
    DCAMERR_LOSTFRAME = _int32(0x80000301)  # frame data is lost
    DCAMERR_MISSINGFRAME_TROUBLE = _int32(0x80000f06)  # frame is lost but reason is low lever driver's bug
    DCAMERR_INVALIDIMAGE = _int32(0x80000321)  # hpk format data is invalid data

    # initialization error
    DCAMERR_NORESOURCE = _int32(0x80000201)  # not enough resource except memory
    DCAMERR_NOMEMORY = _int32(0x80000203)  # not enough memory
    DCAMERR_NOMODULE = _int32(0x80000204)  # no sub module
    DCAMERR_NODRIVER = _int32(0x80000205)  # no driver
    DCAMERR_NOCAMERA = _int32(0x80000206)  # no camera
    DCAMERR_NOGRABBER = _int32(0x80000207)  # no grabber
    DCAMERR_NOCOMBINATION = _int32(0x80000208)  # no combination on registry

    DCAMERR_FAILOPEN = _int32(0x80001001)  # DEPRECATED
    DCAMERR_INVALIDMODULE = _int32(0x80000211)  # dcam_init() found invalid module
    DCAMERR_INVALIDCOMMPORT = _int32(0x80000212)  # invalid serial port
    DCAMERR_FAILOPENBUS = _int32(0x81001001)  # the bus or driver are not available
    DCAMERR_FAILOPENCAMERA = _int32(0x82001001)  # camera report error during opening
    DCAMERR_FRAMEGRABBER_NEEDS_FIRMWAREUPDATE = _int32(
        0x80001002)  # need to update frame grabber firmware to use the camera

    # calling error
    DCAMERR_INVALIDCAMERA = _int32(0x80000806)  # invalid camera
    DCAMERR_INVALIDHANDLE = _int32(0x80000807)  # invalid camera handle
    DCAMERR_INVALIDPARAM = _int32(0x80000808)  # invalid parameter
    DCAMERR_INVALIDVALUE = _int32(0x80000821)  # invalid property value
    DCAMERR_OUTOFRANGE = _int32(0x80000822)  # value is out of range
    DCAMERR_NOTWRITABLE = _int32(0x80000823)  # the property is not writable
    DCAMERR_NOTREADABLE = _int32(0x80000824)  # the property is not readable
    DCAMERR_INVALIDPROPERTYID = _int32(0x80000825)  # the property id is invalid
    DCAMERR_NEWAPIREQUIRED = _int32(0x80000826)  # old API cannot present the value because only new API need to be used
    DCAMERR_WRONGHANDSHAKE = _int32(0x80000827)  # this error happens DCAM get error code from camera unexpectedly
    DCAMERR_NOPROPERTY = _int32(0x80000828)  # there is no altenative or influence id or no more property id
    DCAMERR_INVALIDCHANNEL = _int32(0x80000829)  # the property id specifies channel but channel is invalid
    DCAMERR_INVALIDVIEW = _int32(0x8000082a)  # the property id specifies channel but channel is invalid
    DCAMERR_INVALIDSUBARRAY = _int32(
        0x8000082b)  # the combination of subarray values are invalid. e.g. DCAM_IDPROP_SUBARRAYHPOS + DCAM_IDPROP_SUBARRAYHSIZE is greater than the number of horizontal pixel of sensor.
    DCAMERR_ACCESSDENY = _int32(0x8000082c)  # the property cannot access during this DCAM STATUS
    DCAMERR_NOVALUETEXT = _int32(0x8000082d)  # the property does not have value text
    DCAMERR_WRONGPROPERTYVALUE = _int32(0x8000082e)  # at least one property value is wrong
    DCAMERR_DISHARMONY = _int32(0x80000830)  # the paired camera does not have same parameter
    DCAMERR_FRAMEBUNDLESHOULDBEOFF = _int32(
        0x80000832)  # framebundle mode should be OFF under current property settings
    DCAMERR_INVALIDFRAMEINDEX = _int32(0x80000833)  # the frame index is invalid
    DCAMERR_INVALIDSESSIONINDEX = _int32(0x80000834)  # the session index is invalid
    DCAMERR_NOCORRECTIONDATA = _int32(0x80000838)  # not take the dark and shading correction data yet.
    DCAMERR_CHANNELDEPENDENTVALUE = _int32(
        0x80000839)  # each channel has own property value so can't return overall property value.
    DCAMERR_VIEWDEPENDENTVALUE = _int32(
        0x8000083a)  # each view has own property value so can't return overall property value.
    DCAMERR_NODEVICEBUFFER = _int32(
        0x8000083b)  # the frame count is larger than device momory size on using device memory.
    DCAMERR_REQUIREDSNAP = _int32(0x8000083c)  # the capture mode is sequence on using device memory.
    DCAMERR_LESSSYSTEMMEMORY = _int32(
        0x8000083f)  # the sysmte memory size is too small. PC doesn't have enough memory or is limited memory by 32bit OS.

    DCAMERR_NOTSUPPORT = _int32(0x80000f03)  # camera does not support the function or property with current settings

    # camera or bus trouble
    DCAMERR_FAILREADCAMERA = _int32(0x83001002)  # failed to read data from camera
    DCAMERR_FAILWRITECAMERA = _int32(0x83001003)  # failed to write data to the camera
    DCAMERR_CONFLICTCOMMPORT = _int32(0x83001004)  # conflict the com port name user set
    DCAMERR_OPTICS_UNPLUGGED = _int32(0x83001005)  # Optics part is unplugged so please check it.
    DCAMERR_FAILCALIBRATION = _int32(0x83001006)  # fail calibration

    DCAMERR_MISMATCH_CONFIGURATION = _int32(
        0x83001011)  # mismatch between camera output(connection) and frame grabber specs

    # _int32(0x84000100 - _int32(0x840001FF DCAMERR_INVALIDMEMBER_x
    DCAMERR_INVALIDMEMBER_3 = _int32(0x84000103)  # 3th member variable is invalid value
    DCAMERR_INVALIDMEMBER_5 = _int32(0x84000105)  # 5th member variable is invalid value
    DCAMERR_INVALIDMEMBER_7 = _int32(0x84000107)  # 7th member variable is invalid value
    DCAMERR_INVALIDMEMBER_8 = _int32(0x84000108)  # 7th member variable is invalid value
    DCAMERR_INVALIDMEMBER_9 = _int32(0x84000109)  # 9th member variable is invalid value
    DCAMERR_FAILEDOPENRECFILE = _int32(0x84001001)  # DCAMREC failed to open the file
    DCAMERR_INVALIDRECHANDLE = _int32(0x84001002)  # DCAMREC is invalid handle
    DCAMERR_FAILEDWRITEDATA = _int32(0x84001003)  # DCAMREC failed to write the data
    DCAMERR_FAILEDREADDATA = _int32(0x84001004)  # DCAMREC failed to read the data
    DCAMERR_NOWRECORDING = _int32(0x84001005)  # DCAMREC is recording data now
    DCAMERR_WRITEFULL = _int32(0x84001006)  # DCAMREC writes full frame of the session
    DCAMERR_ALREADYOCCUPIED = _int32(0x84001007)  # DCAMREC handle is already occupied by other HDCAM
    DCAMERR_TOOLARGEUSERDATASIZE = _int32(0x84001008)  # DCAMREC is set the large value to user data size
    DCAMERR_INVALIDWAITHANDLE = _int32(0x84002001)  # DCAMWAIT is invalid handle
    DCAMERR_NEWRUNTIMEREQUIRED = _int32(
        0x84002002)  # DCAM Module Version is older than the version that the camera requests
    DCAMERR_VERSIONMISMATCH = _int32(0x84002003)  # Camre returns the error on setting parameter to limit version
    DCAMERR_RUNAS_FACTORYMODE = _int32(0x84002004)  # Camera is running as a factory mode
    DCAMERR_IMAGE_UNKNOWNSIGNATURE = _int32(0x84003001)  # sigunature of image header is unknown or corrupted
    DCAMERR_IMAGE_NEWRUNTIMEREQUIRED = _int32(
        0x84003002)  # version of image header is newer than version that used DCAM supports
    DCAMERR_IMAGE_ERRORSTATUSEXIST = _int32(0x84003003)  # image header stands error status
    DCAMERR_IMAGE_HEADERCORRUPTED = _int32(0x84004004)  # image header value is strange
    DCAMERR_IMAGE_BROKENCONTENT = _int32(0x84004005)  # image content is corrupted

    # calling error for DCAM-API 2.1.3
    DCAMERR_UNKNOWNMSGID = _int32(0x80000801)  # unknown message id
    DCAMERR_UNKNOWNSTRID = _int32(0x80000802)  # unknown string id
    DCAMERR_UNKNOWNPARAMID = _int32(0x80000803)  # unkown parameter id
    DCAMERR_UNKNOWNBITSTYPE = _int32(0x80000804)  # unknown bitmap bits type
    DCAMERR_UNKNOWNDATATYPE = _int32(0x80000805)  # unknown frame data type

    # internal error
    DCAMERR_NONE = 0  # no error nothing to have done
    DCAMERR_INSTALLATIONINPROGRESS = _int32(0x80000f00)  # installation progress
    DCAMERR_UNREACH = _int32(0x80000f01)  # internal error
    DCAMERR_UNLOADED = _int32(0x80000f04)  # calling after process terminated
    DCAMERR_THRUADAPTER = _int32(0x80000f05)  #
    DCAMERR_NOCONNECTION = _int32(0x80000f07)  # HDCAM lost connection to camera

    DCAMERR_NOTIMPLEMENT = _int32(0x80000f02)  # not yet implementation

    DCAMERR_DELAYEDFRAME = _int32(
        0x80000f09)  # the frame waiting re-load from hardware buffer with SNAPSHOT of DEVICEBUFFER MODE

    DCAMERR_APIINIT_INITOPTIONBYTES = _int32(0xa4010003)  # DCAMAPI_INIT::initoptionbytes is invalid
    DCAMERR_APIINIT_INITOPTION = _int32(0xa4010004)  # DCAMAPI_INIT::initoption is invalid

    DCAMERR_INITOPTION_COLLISION_BASE = _int32(0xa401C000)
    DCAMERR_INITOPTION_COLLISION_MAX = _int32(0xa401FFFF)

    # Between DCAMERR_INITOPTION_COLLISION_BASE and DCAMERR_INITOPTION_COLLISION_MAX means there is collision with initoption in DCAMAPI_INIT.
    # The value "(error code) - DCAMERR_INITOPTION_COLLISION_BASE" indicates the index which second INITOPTION group happens.

    DCAMERR_MISSPROP_TRIGGERSOURCE = _int32(
        0xE0100110)  # the trigger mode is internal or syncreadout on using device memory.

    # success
    DCAMERR_SUCCESS = 1  # no error general success code app should check the value is positive


class DCAMBUF_FRAME_OPTION(IntEnum):
    DCAMBUF_FRAME_OPTION__VIEW_ALL = _int32(0x00000000)
    DCAMBUF_FRAME_OPTION__VIEW_1 = _int32(0x00100000)
    DCAMBUF_FRAME_OPTION__VIEW_2 = _int32(0x00200000)
    DCAMBUF_FRAME_OPTION__VIEW_3 = _int32(0x00300000)
    DCAMBUF_FRAME_OPTION__VIEW_4 = _int32(0x00400000)
    DCAMBUF_FRAME_OPTION__PROC_HIGHCONTRAST = _int32(0x00000010)
    DCAMBUF_FRAME_OPTION__VIEW__STEP = _int32(0x00100000)
    DCAMBUF_FRAME_OPTION__VIEW__MASK = _int32(0x00F00000)
    DCAMBUF_FRAME_OPTION__PROC__MASK = _int32(0x00000FF0)


class DCAMREC_FRAME_OPTION(IntEnum):
    DCAMREC_FRAME_OPTION__VIEW_CURRENT = _int32(0x00000000)
    DCAMREC_FRAME_OPTION__VIEW_1 = _int32(0x00100000)
    DCAMREC_FRAME_OPTION__VIEW_2 = _int32(0x00200000)
    DCAMREC_FRAME_OPTION__VIEW_3 = _int32(0x00300000)
    DCAMREC_FRAME_OPTION__VIEW_4 = _int32(0x00400000)
    DCAMREC_FRAME_OPTION__PROC_HIGHCONTRAST = _int32(0x00000010)
    DCAMREC_FRAME_OPTION__VIEW__STEP = _int32(0x00100000)
    DCAMREC_FRAME_OPTION__VIEW__MASK = _int32(0x00F00000)
    DCAMREC_FRAME_OPTION__PROC__MASK = _int32(0x00000FF0)


class DCAMBUF_METADATAOPTION(IntEnum):
    DCAMBUF_METADATAOPTION__VIEW_ALL = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW_ALL
    DCAMBUF_METADATAOPTION__VIEW_1 = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW_1
    DCAMBUF_METADATAOPTION__VIEW_2 = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW_2
    DCAMBUF_METADATAOPTION__VIEW_3 = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW_3
    DCAMBUF_METADATAOPTION__VIEW_4 = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW_4
    DCAMBUF_METADATAOPTION__VIEW__STEP = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW__STEP
    DCAMBUF_METADATAOPTION__VIEW__MASK = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW__MASK


class DCAMREC_METADATAOPTION(IntEnum):
    DCAMBUF_METADATAOPTION__LOCATION_FRAME = _int32(0x00000000)
    DCAMBUF_METADATAOPTION__LOCATION_FILE = _int32(0x01000000)
    DCAMBUF_METADATAOPTION__LOCATION_SESSION = _int32(0x02000000)
    DCAMBUF_METADATAOPTION__LOCATION_MASK = _int32(0xFF000000)


class DCAM_PIXELTYPE(IntEnum):
    DCAM_PIXELTYPE_MONO8 = _int32(0x00000001)
    DCAM_PIXELTYPE_MONO16 = _int32(0x00000002)
    DCAM_PIXELTYPE_MONO12 = _int32(0x00000003)
    DCAM_PIXELTYPE_MONO12P = _int32(0x00000005)
    DCAM_PIXELTYPE_RGB24 = _int32(0x00000021)
    DCAM_PIXELTYPE_RGB48 = _int32(0x00000022)
    DCAM_PIXELTYPE_BGR24 = _int32(0x00000029)
    DCAM_PIXELTYPE_BGR48 = _int32(0x0000002a)
    DCAM_PIXELTYPE_NONE = _int32(0x00000000)


class DCAMBUF_ATTACHKIND(IntEnum):
    DCAMBUF_ATTACHKIND_TIMESTAMP = 1
    DCAMBUF_ATTACHKIND_FRAMESTAMP = 2
    DCAMBUF_ATTACHKIND_PRIMARY_TIMESTAMP = 3
    DCAMBUF_ATTACHKIND_PRIMARY_FRAMESTAMP = 4
    DCAMBUF_ATTACHKIND_FRAME = 0


class DCAMCAP_TRANSFERKIND(IntEnum):
    DCAMCAP_TRANSFERKIND_FRAME = 0


class DCAMCAP_STATUS(IntEnum):
    DCAMCAP_STATUS_ERROR = _int32(0x0000)
    DCAMCAP_STATUS_BUSY = _int32(0x0001)
    DCAMCAP_STATUS_READY = _int32(0x0002)
    DCAMCAP_STATUS_STABLE = _int32(0x0003)
    DCAMCAP_STATUS_UNSTABLE = _int32(0x0004)


class DCAMWAIT_EVENT(IntEnum):
    DCAMWAIT_CAPEVENT_TRANSFERRED = _int32(0x0001)
    DCAMWAIT_CAPEVENT_FRAMEREADY = _int32(0x0002) # all modules support
    DCAMWAIT_CAPEVENT_CYCLEEND = _int32(0x0004) # all modules support
    DCAMWAIT_CAPEVENT_EXPOSUREEND = _int32(0x0008)
    DCAMWAIT_CAPEVENT_STOPPED = _int32(0x0010)
    DCAMWAIT_CAPEVENT_RELOADFRAME = _int32(0x0020)

    DCAMWAIT_RECEVENT_STOPPED = _int32(0x0100)
    DCAMWAIT_RECEVENT_WARNING = _int32(0x0200)
    DCAMWAIT_RECEVENT_MISSED = _int32(0x0400)
    DCAMWAIT_RECEVENT_DISKFULL = _int32(0x1000)
    DCAMWAIT_RECEVENT_WRITEFAULT = _int32(0x2000)
    DCAMWAIT_RECEVENT_SKIPPED = _int32(0x4000)
    DCAMWAIT_RECEVENT_WRITEFRAME = _int32(0x8000)


class DCAMCAP_START(IntEnum):
    DCAMCAP_START_SEQUENCE = -1
    DCAMCAP_START_SNAP = 0


class DCAM_IDSTR(IntEnum):
    DCAM_IDSTR_BUS = _int32(0x04000101)
    DCAM_IDSTR_CAMERAID = _int32(0x04000102)
    DCAM_IDSTR_VENDOR = _int32(0x04000103)
    DCAM_IDSTR_MODEL = _int32(0x04000104)
    DCAM_IDSTR_CAMERAVERSION = _int32(0x04000105)
    DCAM_IDSTR_DRIVERVERSION = _int32(0x04000106)
    DCAM_IDSTR_MODULEVERSION = _int32(0x04000107)
    DCAM_IDSTR_DCAMAPIVERSION = _int32(0x04000108)
    DCAM_IDSTR_CAMERA_SERIESNAME = _int32(0x0400012C)
    DCAM_IDSTR_OPTICALBLOCK_MODEL = _int32(0x04001101)
    DCAM_IDSTR_OPTICALBLOCK_ID = _int32(0x04001102)
    DCAM_IDSTR_OPTICALBLOCK_DESCRIPTION = _int32(0x04001103)
    DCAM_IDSTR_OPTICALBLOCK_CHANNEL_1 = _int32(0x04001104)
    DCAM_IDSTR_OPTICALBLOCK_CHANNEL_2 = _int32(0x04001105)


class DCAMWAIT_TIMEOUT(IntEnum):
    DCAMWAIT_TIMEOUT_INFINITE = _int32(0x80000000)


class DCAMAPI_INITOPTION(IntEnum):
    DCAMAPI_INITOPTION_APIVER__LATEST = _int32(0x00000001)
    DCAMAPI_INITOPTION_APIVER__4_0 = _int32(0x00000400)
    DCAMAPI_INITOPTION_MULTIVIEW__DISABLE = _int32(0x00010002)
    DCAMAPI_INITOPTION_ENDMARK = _int32(0x00000000)


class DCAMBUF_METADATAKIND(IntEnum):
    DCAMBUF_METADATAKIND_TIMESTAMPS = _int32(0x00010000)
    DCAMBUF_METADATAKIND_FRAMESTAMPS = _int32(0x00020000)


class DCAMREC_METADATAKIND(IntEnum):
    DCAMREC_METADATAKIND_USERDATATEXT = _int32(0x00000001)
    DCAMREC_METADATAKIND_USERDATABIN = _int32(0x00000002)
    DCAMREC_METADATAKIND_TIMESTAMPS = _int32(0x00010000)
    DCAMREC_METADATAKIND_FRAMESTAMPS = _int32(0x00020000)


class DCAMDATA_OPTION(IntEnum):
    DCAMDATA_OPTION__VIEW_ALL = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW_ALL
    DCAMDATA_OPTION__VIEW_1 = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW_1
    DCAMDATA_OPTION__VIEW_2 = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW_2
    DCAMDATA_OPTION__VIEW_3 = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW_3
    DCAMDATA_OPTION__VIEW_4 = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW_4
    DCAMDATA_OPTION__VIEW__STEP = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW__STEP
    DCAMDATA_OPTION__VIEW__MASK = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__VIEW__MASK


class DCAMDATA_KIND(IntEnum):
    DCAMDATA_KIND__REGION = _int32(0x00000001)
    DCAMDATA_KIND__LUT = _int32(0x00000002)
    DCAMDATA_KIND__NONE = _int32(0x00000000)


class DCAMDATA_ATTRIBUTE(IntEnum):
    DCAMDATA_ATTRIBUTE__ACCESSREADY = _int32(0x01000000)
    DCAMDATA_ATTRIBUTE__ACCESSBUSY = _int32(0x02000000)
    DCAMDATA_ATTRIBUTE__HASVIEW = _int32(0x10000000)
    DCAMDATA_ATTRIBUTE__MASK = _int32(0xFF000000)


class DCAMDATA_REGIONTYPE(IntEnum):
    DCAMDATA_REGIONTYPE__BYTEMASK = _int32(0x00000001)
    DCAMDATA_REGIONTYPE__RECT16ARRAY = _int32(0x00000002)
    DCAMDATA_REGIONTYPE__ACCESSREADY = DCAMDATA_ATTRIBUTE.DCAMDATA_ATTRIBUTE__ACCESSREADY
    DCAMDATA_REGIONTYPE__ACCESSBUSY = DCAMDATA_ATTRIBUTE.DCAMDATA_ATTRIBUTE__ACCESSBUSY
    DCAMDATA_REGIONTYPE__HASVIEW = DCAMDATA_ATTRIBUTE.DCAMDATA_ATTRIBUTE__HASVIEW
    DCAMDATA_REGIONTYPE__BODYMASK = _int32(0x00FFFFFF)
    DCAMDATA_REGIONTYPE__ATTRIBUTEMASK = DCAMDATA_ATTRIBUTE.DCAMDATA_ATTRIBUTE__MASK
    DCAMDATA_REGIONTYPE__NONE = _int32(0x00000000)


class DCAMDATA_LUTTYPE(IntEnum):
    DCAMDATA_LUTTYPE__SEGMENTED_LINEAR = _int32(0x00000001)
    DCAMDATA_LUTTYPE__MONO16 = _int32(0x00000002)
    DCAMDATA_LUTTYPE__ACCESSREADY = DCAMDATA_ATTRIBUTE.DCAMDATA_ATTRIBUTE__ACCESSREADY
    DCAMDATA_LUTTYPE__ACCESSBUSY = DCAMDATA_ATTRIBUTE.DCAMDATA_ATTRIBUTE__ACCESSBUSY
    DCAMDATA_LUTTYPE__BODYMASK = _int32(0x00FFFFFF)
    DCAMDATA_LUTTYPE__ATTRIBUTEMASK = DCAMDATA_ATTRIBUTE.DCAMDATA_ATTRIBUTE__MASK
    DCAMDATA_LUTTYPE__NONE = _int32(0x00000000)


class DCAMBUF_PROCTYPE(IntEnum):
    DCAMBUF_PROCTYPE__HIGHCONTRASTMODE = DCAMBUF_FRAME_OPTION.DCAMBUF_FRAME_OPTION__PROC_HIGHCONTRAST
    DCAMBUF_PROCTYPE__NONE = _int32(0x00000000)


class DCAM_CODEPAGE(IntEnum):
    DCAM_CODEPAGE__SHIFT_JIS = 932  # Shift JIS
    DCAM_CODEPAGE__UTF16_LE = 1200  # UTF-16 (Little Endian)
    DCAM_CODEPAGE__UTF16_BE = 1201  # UTF-16 (Big Endian)
    DCAM_CODEPAGE__UTF7 = 65000  # UTF-7 translation
    DCAM_CODEPAGE__UTF8 = 65001  # UTF-8 translation
    DCAM_CODEPAGE__NONE = _int32(0x00000000)


class DCAMDEV_CAPDOMAIN(IntEnum):
    DCAMDEV_CAPDOMAIN__DCAMDATA = _int32(0x00000001)
    DCAMDEV_CAPDOMAIN__FRAMEOPTION = _int32(0x00000002)
    DCAMDEV_CAPDOMAIN__FUNCTION = _int32(0x00000000)


class DCAMDEV_CAPFLAG(IntEnum):
    DCAMDEV_CAPFLAG_FRAMESTAMP = _int32(0x00000001)
    DCAMDEV_CAPFLAG_TIMESTAMP = _int32(0x00000002)
    DCAMDEV_CAPFLAG_CAMERASTAMP = _int32(0x00000004)
    DCAMDEV_CAPFLAG_NONE = _int32(0x00000000)


class DCAMREC_STATUSFLAG(IntEnum):
    DCAMREC_STATUSFLAG_NONE = _int32(0x00000000)
    DCAMREC_STATUSFLAG_RECORDING = _int32(0x00000001)
