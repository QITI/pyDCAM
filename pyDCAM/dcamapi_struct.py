import ctypes

c_HDCAM = ctypes.POINTER(ctypes.c_void_p)
c_HDCAMWAIT = ctypes.POINTER(ctypes.c_void_p)
c_HDCAMREC = ctypes.POINTER(ctypes.c_void_p)

class DCAMPROP_ATTR(ctypes.Structure):
    """The dcam property attribute structure."""

    _fields_ = [("cbSize", ctypes.c_int32),
                ("iProp", ctypes.c_int32),
                ("option", ctypes.c_int32),
                ("iReserved1", ctypes.c_int32),
                ("attribute", ctypes.c_int32),
                ("iGroup", ctypes.c_int32),
                ("iUnit", ctypes.c_int32),
                ("attribute2", ctypes.c_int32),
                ("valuemin", ctypes.c_double),
                ("valuemax", ctypes.c_double),
                ("valuestep", ctypes.c_double),
                ("valuedefault", ctypes.c_double),
                ("nMaxChannel", ctypes.c_int32),
                ("iReserved3", ctypes.c_int32),
                ("nMaxView", ctypes.c_int32),
                ("iProp_NumberOfElement", ctypes.c_int32),
                ("iProp_ArrayBase", ctypes.c_int32),
                ("iPropStep_Element", ctypes.c_int32)]


class DCAMPROP_VALUETEXT(ctypes.Structure):
    """The dcam text property structure."""
    _fields_ = [("cbSize", ctypes.c_int32),
                ("iProp", ctypes.c_int32),
                ("value", ctypes.c_double),
                ("text", ctypes.c_char_p),
                ("textbytes", ctypes.c_int32)]


class DCAMAPI_INIT(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("iDeviceCount", ctypes.c_int32),
                ("reserved", ctypes.c_int32),
                ("initoptionbytes", ctypes.c_int32),
                ("initoption", ctypes.c_char_p),
                ("guid", ctypes.c_char_p)]


class DCAMDEV_OPEN(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("index", ctypes.c_int32),
                ("hdcam", c_HDCAM)]


class DCAMDEV_CAPABILITY(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("domain", ctypes.c_int32),
                ("capflag", ctypes.c_int32),
                ("kind", ctypes.c_int32)]


class DCAMDEV_CAPABILITY_LUT(ctypes.Structure):
    _fields_ = [("hdr", DCAMDEV_CAPABILITY),
                ("linearpointmax", ctypes.c_int32)]


class DCAMDEV_CAPABILITY_REGION(ctypes.Structure):
    _fields_ = [("hdr", DCAMDEV_CAPABILITY),
                ("horzunit", ctypes.c_int32),
                ("vertunit", ctypes.c_int32)]


class DCAMDEV_CAPABILITY_FRAMEOPTION(ctypes.Structure):
    _fields_ = [("hdr", DCAMDEV_CAPABILITY),
                ("supportproc", ctypes.c_int32)]


class DCAMDEV_STRING(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("iString", ctypes.c_int32),
                ("text", ctypes.c_char_p),
                ("textbytes", ctypes.c_int32)]


class DCAMDATA_HDR(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("iKind", ctypes.c_int32),
                ("option", ctypes.c_int32),
                ("reserved2", ctypes.c_int32)]


class DCAMDATA_REGION(ctypes.Structure):
    _fields_ = [("hdr", DCAMDATA_HDR),
                ("option", ctypes.c_int32),
                ("type", ctypes.c_int32),
                ("data", ctypes.c_void_p),
                ("datasize", ctypes.c_int32),
                ("reserved", ctypes.c_int32)]


class DCAMDATA_REGIONRECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_short),
                ("top", ctypes.c_short),
                ("right", ctypes.c_short),
                ("bottom", ctypes.c_short)]


class DCAMDATA_LUT(ctypes.Structure):
    _fields_ = [("hdr", DCAMDATA_HDR),
                ("type", ctypes.c_int32),
                ("page", ctypes.c_int32),
                ("data", ctypes.c_void_p),
                ("datasize", ctypes.c_int32),
                ("reserved", ctypes.c_int32)]


class DCAMDATA_LINEARLUT(ctypes.Structure):
    _fields_ = [("lutin", ctypes.c_int32),
                ("lutout", ctypes.c_int32)]


class DCAMBUF_ATTACH(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("iKind", ctypes.c_int32),
                ("buffer", ctypes.POINTER(ctypes.c_void_p)),
                ("buffercount", ctypes.c_int32)]


class DCAM_TIMESTAMP(ctypes.Structure):
    _fields_ = [("sec", ctypes.c_uint32),
                ("microsec", ctypes.c_int32)]


class DCAMCAP_TRANSFERINFO(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("iKind", ctypes.c_int32),
                ("nNewestFrameIndex", ctypes.c_int32),
                ("nFrameCount", ctypes.c_int32)]


class DCAMBUF_FRAME(ctypes.Structure):
    # copyframe() and lockframe() use this structure. Some members have different direction.
    _fields_ = [("size", ctypes.c_int32),
                ("iKind", ctypes.c_int32),
                ("option", ctypes.c_int32),
                ("iFrame", ctypes.c_int32),
                ("buf", ctypes.c_void_p),
                ("rowbytes", ctypes.c_int32),
                ("type", ctypes.c_int32),
                ("width", ctypes.c_int32),
                ("height", ctypes.c_int32),
                ("left", ctypes.c_int32),
                ("top", ctypes.c_int32),
                ("timestamp", DCAM_TIMESTAMP),
                ("framestamp", ctypes.c_int32),
                ("camerastamp", ctypes.c_int32)]


class DCAMREC_FRAME(ctypes.Structure):
    # currently same as DCAM_FRAME
    _fields_ = [("size", ctypes.c_int32),
                ("iKind", ctypes.c_int32),
                ("option", ctypes.c_int32),
                ("iFrame", ctypes.c_int32),
                ("buf", ctypes.c_void_p),
                ("rowbytes", ctypes.c_int32),
                ("type", ctypes.c_int32),
                ("width", ctypes.c_int32),
                ("height", ctypes.c_int32),
                ("left", ctypes.c_int32),
                ("top", ctypes.c_int32),
                ("timestamp", DCAM_TIMESTAMP),
                ("framestamp", ctypes.c_int32),
                ("camerastamp", ctypes.c_int32)]


class DCAMWAIT_OPEN(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("supportevent", ctypes.c_int32),
                ("hwait", c_HDCAMWAIT),
                ("hdcam", c_HDCAM)
                ]


class DCAMWAIT_START(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("eventhappened", ctypes.c_int32),
                ("eventmask", ctypes.c_int32),
                ("timeout", ctypes.c_int32)]


class DCAMREC_OPENA(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("reserved", ctypes.c_int32),
                ("hrec", c_HDCAMREC),
                ("path", ctypes.c_char_p),
                ("ext", ctypes.c_char_p),
                ("maxframepersession", ctypes.c_int32),
                ("userdatasize", ctypes.c_int32),
                ("userdatasize_session", ctypes.c_int32),
                ("userdatasize_file", ctypes.c_int32),
                ("usertextsize", ctypes.c_int32),
                ("usertextsize_session", ctypes.c_int32),
                ("usertextsize_file", ctypes.c_int32)]


class DCAMREC_OPENW(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("reserved", ctypes.c_int32),
                ("hrec", c_HDCAMREC),
                ("path", ctypes.c_wchar_p),
                ("ext", ctypes.c_wchar_p),
                ("maxframepersession", ctypes.c_int32),
                ("userdatasize", ctypes.c_int32),
                ("userdatasize_session", ctypes.c_int32),
                ("userdatasize_file", ctypes.c_int32),
                ("usertextsize", ctypes.c_int32),
                ("usertextsize_session", ctypes.c_int32),
                ("usertextsize_file", ctypes.c_int32)]


class DCAMREC_OPEN(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("reserved", ctypes.c_int32),
                ("hrec", c_HDCAMREC),
                ("path", ctypes.c_char_p),
                ("ext", ctypes.c_char_p),
                ("maxframepersession", ctypes.c_int32),
                ("userdatasize", ctypes.c_int32),
                ("userdatasize_session", ctypes.c_int32),
                ("userdatasize_file", ctypes.c_int32),
                ("usertextsize", ctypes.c_int32),
                ("usertextsize_session", ctypes.c_int32),
                ("usertextsize_file", ctypes.c_int32)]


class DCAMREC_STATUS(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("currentsession_index", ctypes.c_int32),
                ("maxframecount_per_session", ctypes.c_int32),
                ("currentframe_index", ctypes.c_int32),
                ("missingframe_count", ctypes.c_int32),
                ("flags", ctypes.c_int32),
                ("totalframecount", ctypes.c_int32),
                ("reserved", ctypes.c_int32)]


class DCAM_METADATAHDR(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("iKind", ctypes.c_int32),
                ("option", ctypes.c_int32),
                ("iFrame", ctypes.c_int32)]


class DCAM_METADATABLOCKHDR(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int32),
                ("iKind", ctypes.c_int32),
                ("option", ctypes.c_int32),
                ("iFrame", ctypes.c_int32),
                ("in_count", ctypes.c_int32),
                ("outcount", ctypes.c_int32)]


class DCAM_USERDATATEXT(ctypes.Structure):
    _fields_ = [("hdr", DCAM_METADATAHDR),
                ("text", ctypes.c_char_p),
                ("text_len", ctypes.c_int32),
                ("codepage", ctypes.c_int32)]


class DCAM_USERDATABIN(ctypes.Structure):
    _fields_ = [("hdr", DCAM_METADATAHDR),
                ("bin", ctypes.c_void_p),
                ("bin_len", ctypes.c_int32),
                ("reserved", ctypes.c_int32)]


class DCAM_TIMESTAMPBLOCK(ctypes.Structure):
    _fields_ = [("hdr", DCAM_METADATABLOCKHDR),
                ("timestamps", DCAM_TIMESTAMP),
                ("timestampsize", ctypes.c_int32),
                ("timestampvalidsize", ctypes.c_int32),
                ("timestampkind", ctypes.c_int32),
                ("reserved", ctypes.c_int32)]


class DCAM_FRAMESTAMPBLOCK(ctypes.Structure):
    _fields_ = [("hdr", DCAM_METADATABLOCKHDR),
                ("framestamps", ctypes.c_int32),
                ("reserved", ctypes.c_int32)]


class DCAM_METADATATEXTBLOCK(ctypes.Structure):
    _fields_ = [("hdr", DCAM_METADATABLOCKHDR),
                ("text", ctypes.c_void_p),
                ("textsizes", ctypes.c_int32),
                ("bytesperunit", ctypes.c_int32),
                ("reserved", ctypes.c_int32),
                ("textcodepage", ctypes.c_int32)]


class DCAM_METADATABINBLOCK(ctypes.Structure):
    _fields_ = [("hdr", DCAM_METADATABLOCKHDR),
                ("bin", ctypes.c_void_p),
                ("binsizes", ctypes.c_int32),
                ("bytesperunit", ctypes.c_int32),
                ("reserved", ctypes.c_int32),
                ("textcodepage", ctypes.c_int32)]
