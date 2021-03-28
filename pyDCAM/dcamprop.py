from enum import IntEnum
from ._util import _int32

class DCAMPROPMODEVALUE(IntEnum):
    # DCAM_IDPROP_SENSORMODE
    DCAMPROP_SENSORMODE__AREA = 1  # "AREA"
    DCAMPROP_SENSORMODE__SLIT = 2  # "SLIT"					 	# reserved
    DCAMPROP_SENSORMODE__LINE = 3  # "LINE"
    DCAMPROP_SENSORMODE__TDI = 4  # "TDI"
    DCAMPROP_SENSORMODE__FRAMING = 5  # "FRAMING"				 	# reserved
    DCAMPROP_SENSORMODE__PARTIALAREA = 6  # "PARTIAL AREA"			 	# reserved
    DCAMPROP_SENSORMODE__SLITLINE = 9  # "SLIT LINE"				 	# reserved
    DCAMPROP_SENSORMODE__TDI_EXTENDED = 10  # "TDI EXTENDED"
    DCAMPROP_SENSORMODE__PANORAMIC = 11  # "PANORAMIC"				 	# reserved
    DCAMPROP_SENSORMODE__PROGRESSIVE = 12  # "PROGRESSIVE"
    DCAMPROP_SENSORMODE__SPLITVIEW = 14  # "SPLIT VIEW"
    DCAMPROP_SENSORMODE__DUALLIGHTSHEET = 16  # "DUAL LIGHTSHEET"

    # DCAM_IDPROP_SHUTTER_MODE
    DCAMPROP_SHUTTER_MODE__GLOBAL = 1  # "GLOBAL"
    DCAMPROP_SHUTTER_MODE__ROLLING = 2  # "ROLLING"

    # DCAM_IDPROP_READOUTSPEED
    DCAMPROP_READOUTSPEED__SLOWEST = 1  # no text
    DCAMPROP_READOUTSPEED__FASTEST = _int32(0x7FFFFFFF)  # no text w/o

    # DCAM_IDPROP_READOUT_DIRECTION
    DCAMPROP_READOUT_DIRECTION__FORWARD = 1  # "FORWARD"
    DCAMPROP_READOUT_DIRECTION__BACKWARD = 2  # "BACKWARD"
    DCAMPROP_READOUT_DIRECTION__BYTRIGGER = 3  # "BY TRIGGER"
    DCAMPROP_READOUT_DIRECTION__DIVERGE = 5  # "DIVERGE"

    # DCAM_IDPROP_READOUT_UNIT
    #	DCAMPROP_READOUT_UNIT__LINE					= 1 	 		#	"LINE"					 	# reserved
    DCAMPROP_READOUT_UNIT__FRAME = 2  # "FRAME"
    DCAMPROP_READOUT_UNIT__BUNDLEDLINE = 3  # "BUNDLED LINE"
    DCAMPROP_READOUT_UNIT__BUNDLEDFRAME = 4  # "BUNDLED FRAME"

    # DCAM_IDPROP_CCDMODE
    DCAMPROP_CCDMODE__NORMALCCD = 1  # "NORMAL CCD"
    DCAMPROP_CCDMODE__EMCCD = 2  # "EM CCD"

    # DCAM_IDPROP_CMOSMODE
    DCAMPROP_CMOSMODE__NORMAL = 1  # "NORMAL"
    DCAMPROP_CMOSMODE__NONDESTRUCTIVE = 2  # "NON DESTRUCTIVE"

    # DCAM_IDPROP_OUTPUT_INTENSITY
    DCAMPROP_OUTPUT_INTENSITY__NORMAL = 1  # "NORMAL"
    DCAMPROP_OUTPUT_INTENSITY__TESTPATTERN = 2  # "TEST PATTERN"

    # DCAM_IDPROP_OUTPUTDATA_ORIENTATION	  													# reserved
    DCAMPROP_OUTPUTDATA_ORIENTATION__NORMAL = 1  # reserved
    DCAMPROP_OUTPUTDATA_ORIENTATION__MIRROR = 2  # reserved
    DCAMPROP_OUTPUTDATA_ORIENTATION__FLIP = 3  # reserved

    # DCAM_IDPROP_OUTPUTDATA_OPERATION
    DCAMPROP_OUTPUTDATA_OPERATION__RAW = 1
    DCAMPROP_OUTPUTDATA_OPERATION__ALIGNED = 2

    # DCAM_IDPROP_TESTPATTERN_KIND
    DCAMPROP_TESTPATTERN_KIND__FLAT = 2  # "FLAT"
    DCAMPROP_TESTPATTERN_KIND__IFLAT = 3  # "INVERT FLAT"
    DCAMPROP_TESTPATTERN_KIND__HORZGRADATION = 4  # "HORZGRADATION"
    DCAMPROP_TESTPATTERN_KIND__IHORZGRADATION = 5  # "INVERT HORZGRADATION"
    DCAMPROP_TESTPATTERN_KIND__VERTGRADATION = 6  # "VERTGRADATION"
    DCAMPROP_TESTPATTERN_KIND__IVERTGRADATION = 7  # "INVERT VERTGRADATION"
    DCAMPROP_TESTPATTERN_KIND__LINE = 8  # "LINE"
    DCAMPROP_TESTPATTERN_KIND__ILINE = 9  # "INVERT LINE"
    DCAMPROP_TESTPATTERN_KIND__DIAGONAL = 10  # "DIAGONAL"
    DCAMPROP_TESTPATTERN_KIND__IDIAGONAL = 11  # "INVERT DIAGONAL"
    DCAMPROP_TESTPATTERN_KIND__FRAMECOUNT = 12  # "FRAMECOUNT"

    # DCAM_IDPROP_DIGITALBINNING_METHOD
    DCAMPROP_DIGITALBINNING_METHOD__MINIMUM = 1  # "MINIMUM"
    DCAMPROP_DIGITALBINNING_METHOD__MAXIMUM = 2  # "MAXIMUM"
    DCAMPROP_DIGITALBINNING_METHOD__ODD = 3  # "ODD"
    DCAMPROP_DIGITALBINNING_METHOD__EVEN = 4  # "EVEN"
    DCAMPROP_DIGITALBINNING_METHOD__SUM = 5  # "SUM"
    DCAMPROP_DIGITALBINNING_METHOD__AVERAGE = 6  # "AVERAGE"

    # DCAM_IDPROP_TRIGGERSOURCE
    DCAMPROP_TRIGGERSOURCE__INTERNAL = 1  # "INTERNAL"
    DCAMPROP_TRIGGERSOURCE__EXTERNAL = 2  # "EXTERNAL"
    DCAMPROP_TRIGGERSOURCE__SOFTWARE = 3  # "SOFTWARE"
    DCAMPROP_TRIGGERSOURCE__MASTERPULSE = 4  # "MASTER PULSE"

    # DCAM_IDPROP_TRIGGERACTIVE
    DCAMPROP_TRIGGERACTIVE__EDGE = 1  # "EDGE"
    DCAMPROP_TRIGGERACTIVE__LEVEL = 2  # "LEVEL"
    DCAMPROP_TRIGGERACTIVE__SYNCREADOUT = 3  # "SYNCREADOUT"
    DCAMPROP_TRIGGERACTIVE__POINT = 4  # "POINT"

    # DCAM_IDPROP_BUS_SPEED
    DCAMPROP_BUS_SPEED__SLOWEST = 1  # no text
    DCAMPROP_BUS_SPEED__FASTEST = 0x7FFFFFFF  # no text w/o

    # DCAM_IDPROP_TRIGGER_MODE
    DCAMPROP_TRIGGER_MODE__NORMAL = 1  # "NORMAL"
    #	= 2
    DCAMPROP_TRIGGER_MODE__PIV = 3  # "PIV"
    DCAMPROP_TRIGGER_MODE__START = 6  # "START"
    DCAMPROP_TRIGGER_MODE__MULTIGATE = 7  # "MULTIGATE"				 	# reserved
    DCAMPROP_TRIGGER_MODE__MULTIFRAME = 8  # "MULTIFRAME"			 	# reserved

    # DCAM_IDPROP_TRIGGERPOLARITY
    DCAMPROP_TRIGGERPOLARITY__NEGATIVE = 1  # "NEGATIVE"
    DCAMPROP_TRIGGERPOLARITY__POSITIVE = 2  # "POSITIVE"

    # DCAM_IDPROP_TRIGGER_CONNECTOR
    DCAMPROP_TRIGGER_CONNECTOR__INTERFACE = 1  # "INTERFACE"
    DCAMPROP_TRIGGER_CONNECTOR__BNC = 2  # "BNC"
    DCAMPROP_TRIGGER_CONNECTOR__MULTI = 3  # "MULTI"

    # DCAM_IDPROP_INTERNALTRIGGER_HANDLING
    DCAMPROP_INTERNALTRIGGER_HANDLING__SHORTEREXPOSURETIME = 1  # "SHORTER EXPOSURE TIME"
    DCAMPROP_INTERNALTRIGGER_HANDLING__FASTERFRAMERATE = 2  # "FASTER FRAME RATE"
    DCAMPROP_INTERNALTRIGGER_HANDLING__ABANDONWRONGFRAME = 3  # "ABANDON WRONG FRAME"
    DCAMPROP_INTERNALTRIGGER_HANDLING__BURSTMODE = 4  # "BURST MODE"
    DCAMPROP_INTERNALTRIGGER_HANDLING__INDIVIDUALEXPOSURE = 7  # "INDIVIDUAL EXPOSURE TIME"

    # DCAM_IDPROP_SYNCREADOUT_SYSTEMBLANK
    DCAMPROP_SYNCREADOUT_SYSTEMBLANK__STANDARD = 1  # "STANDARD"
    DCAMPROP_SYNCREADOUT_SYSTEMBLANK__MINIMUM = 2  # "MINIMUM"

    # DCAM_IDPROP_TRIGGERENABLE_ACTIVE
    DCAMPROP_TRIGGERENABLE_ACTIVE__DENY = 1  # "DENY"
    DCAMPROP_TRIGGERENABLE_ACTIVE__ALWAYS = 2  # "ALWAYS"
    DCAMPROP_TRIGGERENABLE_ACTIVE__LEVEL = 3  # "LEVEL"
    DCAMPROP_TRIGGERENABLE_ACTIVE__START = 4  # "START"

    # DCAM_IDPROP_TRIGGERENABLE_POLARITY
    DCAMPROP_TRIGGERENABLE_POLARITY__NEGATIVE = 1  # "NEGATIVE"
    DCAMPROP_TRIGGERENABLE_POLARITY__POSITIVE = 2  # "POSITIVE"
    DCAMPROP_TRIGGERENABLE_POLARITY__INTERLOCK = 3  # "INTERLOCK"

    # DCAM_IDPROP_OUTPUTTRIGGER_CHANNELSYNC  					# numeric headletter options
    DCAMPROP_OUTPUTTRIGGER_CHANNELSYNC__1CHANNEL = 1  # "1 Channel"
    DCAMPROP_OUTPUTTRIGGER_CHANNELSYNC__2CHANNELS = 2  # "2 Channels"
    DCAMPROP_OUTPUTTRIGGER_CHANNELSYNC__3CHANNELS = 3  # "3 Channels"

    # DCAM_IDPROP_OUTPUTTRIGGER_PROGRAMABLESTART
    DCAMPROP_OUTPUTTRIGGER_PROGRAMABLESTART__FIRSTEXPOSURE = 1  # "FIRST EXPOSURE"
    DCAMPROP_OUTPUTTRIGGER_PROGRAMABLESTART__FIRSTREADOUT = 2  # "FIRST READOUT"

    # DCAM_IDPROP_OUTPUTTRIGGER_SOURCE
    DCAMPROP_OUTPUTTRIGGER_SOURCE__EXPOSURE = 1  # "EXPOSURE"
    DCAMPROP_OUTPUTTRIGGER_SOURCE__READOUTEND = 2  # "READOUT END"
    DCAMPROP_OUTPUTTRIGGER_SOURCE__VSYNC = 3  # "VSYNC"
    DCAMPROP_OUTPUTTRIGGER_SOURCE__HSYNC = 4  # "HSYNC"
    DCAMPROP_OUTPUTTRIGGER_SOURCE__TRIGGER = 6  # "TRIGGER"

    # DCAM_IDPROP_OUTPUTTRIGGER_POLARITY
    DCAMPROP_OUTPUTTRIGGER_POLARITY__NEGATIVE = 1  # "NEGATIVE"
    DCAMPROP_OUTPUTTRIGGER_POLARITY__POSITIVE = 2  # "POSITIVE"

    # DCAM_IDPROP_OUTPUTTRIGGER_ACTIVE
    DCAMPROP_OUTPUTTRIGGER_ACTIVE__EDGE = 1  # "EDGE"
    DCAMPROP_OUTPUTTRIGGER_ACTIVE__LEVEL = 2  # "LEVEL"
    #	DCAMPROP_OUTPUTTRIGGER_ACTIVE__PULSE		= 3 	 		#	"PULSE"					 	# reserved

    # DCAM_IDPROP_OUTPUTTRIGGER_KIND
    DCAMPROP_OUTPUTTRIGGER_KIND__LOW = 1  # "LOW"
    DCAMPROP_OUTPUTTRIGGER_KIND__EXPOSURE = 2  # "EXPOSURE"
    DCAMPROP_OUTPUTTRIGGER_KIND__PROGRAMABLE = 3  # "PROGRAMABLE"
    DCAMPROP_OUTPUTTRIGGER_KIND__TRIGGERREADY = 4  # "TRIGGER READY"
    DCAMPROP_OUTPUTTRIGGER_KIND__HIGH = 5  # "HIGH"

    # DCAM_IDPROP_OUTPUTTRIGGER_BASESENSOR
    DCAMPROP_OUTPUTTRIGGER_BASESENSOR__VIEW1 = 1  # "VIEW 1"
    DCAMPROP_OUTPUTTRIGGER_BASESENSOR__VIEW2 = 2  # "VIEW 2"
    DCAMPROP_OUTPUTTRIGGER_BASESENSOR__ANYVIEW = 15  # "ANY VIEW"
    DCAMPROP_OUTPUTTRIGGER_BASESENSOR__ALLVIEWS = 16  # "ALL VIEWS"

    # DCAM_IDPROP_EXPOSURETIME_CONTROL
    DCAMPROP_EXPOSURETIME_CONTROL__OFF = 1  # "OFF"
    DCAMPROP_EXPOSURETIME_CONTROL__NORMAL = 2  # "NORMAL"

    # DCAM_IDPROP_TRIGGER_FIRSTEXPOSURE
    DCAMPROP_TRIGGER_FIRSTEXPOSURE__NEW = 1  # "NEW"
    DCAMPROP_TRIGGER_FIRSTEXPOSURE__CURRENT = 2  # "CURRENT"

    # DCAM_IDPROP_TRIGGER_GLOBALEXPOSURE
    DCAMPROP_TRIGGER_GLOBALEXPOSURE__NONE = 1  # "NONE"
    DCAMPROP_TRIGGER_GLOBALEXPOSURE__ALWAYS = 2  # "ALWAYS"
    DCAMPROP_TRIGGER_GLOBALEXPOSURE__DELAYED = 3  # "DELAYED"
    DCAMPROP_TRIGGER_GLOBALEXPOSURE__EMULATE = 4  # "EMULATE"
    DCAMPROP_TRIGGER_GLOBALEXPOSURE__GLOBALRESET = 5  # "GLOBAL RESET"

    # DCAM_IDPROP_FIRSTTRIGGER_BEHAVIOR
    DCAMPROP_FIRSTTRIGGER_BEHAVIOR__STARTEXPOSURE = 1  # "START EXPOSURE"
    DCAMPROP_FIRSTTRIGGER_BEHAVIOR__STARTREADOUT = 2  # "START READOUT"

    # DCAM_IDPROP_MASTERPULSE_MODE
    DCAMPROP_MASTERPULSE_MODE__CONTINUOUS = 1  # "CONTINUOUS"
    DCAMPROP_MASTERPULSE_MODE__START = 2  # "START"
    DCAMPROP_MASTERPULSE_MODE__BURST = 3  # "BURST"

    # DCAM_IDPROP_MASTERPULSE_TRIGGERSOURCE
    DCAMPROP_MASTERPULSE_TRIGGERSOURCE__EXTERNAL = 1  # "EXTERNAL"
    DCAMPROP_MASTERPULSE_TRIGGERSOURCE__SOFTWARE = 2  # "SOFTWARE"

    # DCAM_IDPROP_MECHANICALSHUTTER
    DCAMPROP_MECHANICALSHUTTER__AUTO = 1  # "AUTO"
    DCAMPROP_MECHANICALSHUTTER__CLOSE = 2  # "CLOSE"
    DCAMPROP_MECHANICALSHUTTER__OPEN = 3  # "OPEN"

    # DCAM_IDPROP_MECHANICALSHUTTER_AUTOMODE  												# reserved
    #	DCAMPROP_MECHANICALSHUTTER_AUTOMODE__OPEN_WHEN_EXPOSURE	= 1  	# "OPEN WHEN EXPOSURE"	 	# reserved
    #	DCAMPROP_MECHANICALSHUTTER_AUTOMODE__CLOSE_WHEN_READOUT	= 2  	# "CLOSE WHEN READOUT"	 	# reserved

    # DCAM_IDPROP_LIGHTMODE
    DCAMPROP_LIGHTMODE__LOWLIGHT = 1  # "LOW LIGHT"
    DCAMPROP_LIGHTMODE__HIGHLIGHT = 2  # "HIGH LIGHT"

    # DCAM_IDPROP_SENSITIVITYMODE
    DCAMPROP_SENSITIVITYMODE__OFF = 1  # "OFF"
    DCAMPROP_SENSITIVITYMODE__ON = 2  # "ON"
    DCAMPROP_SENSITIVITY2_MODE__INTERLOCK = 3  # "INTERLOCK"

    # DCAM_IDPROP_EMGAINWARNING_STATUS
    DCAMPROP_EMGAINWARNING_STATUS__NORMAL = 1  # "NORMAL"
    DCAMPROP_EMGAINWARNING_STATUS__WARNING = 2  # "WARNING"
    DCAMPROP_EMGAINWARNING_STATUS__PROTECTED = 3  # "PROTECTED"

    # DCAM_IDPROP_PHOTONIMAGINGMODE  							# numeric headletter options
    DCAMPROP_PHOTONIMAGINGMODE__0 = 0  # "0"
    DCAMPROP_PHOTONIMAGINGMODE__1 = 1  # "1"
    DCAMPROP_PHOTONIMAGINGMODE__2 = 2  # "2"
    DCAMPROP_PHOTONIMAGINGMODE__3 = 3  # "2"

    # DCAM_IDPROP_SENSORCOOLER
    DCAMPROP_SENSORCOOLER__OFF = 1  # "OFF"
    DCAMPROP_SENSORCOOLER__ON = 2  # "ON"
    #	DCAMPROP_SENSORCOOLER__BEST					= 3 	 		#	"BEST"					 	# reserved
    DCAMPROP_SENSORCOOLER__MAX = 4  # "MAX"

    # DCAM_IDPROP_SENSORTEMPERATURE_STATUS
    DCAMPROP_SENSORTEMPERATURE_STATUS__NORMAL = 0  # "NORMAL"
    DCAMPROP_SENSORTEMPERATURE_STATUS__WARNING = 1  # "WARNING"
    DCAMPROP_SENSORTEMPERATURE_STATUS__PROTECTION = 2  # "PROTECTION"

    # DCAM_IDPROP_SENSORCOOLERSTATUS
    DCAMPROP_SENSORCOOLERSTATUS__ERROR4 = -4  # "ERROR4"
    DCAMPROP_SENSORCOOLERSTATUS__ERROR3 = -3  # "ERROR3"
    DCAMPROP_SENSORCOOLERSTATUS__ERROR2 = -2  # "ERROR2"
    DCAMPROP_SENSORCOOLERSTATUS__ERROR1 = -1  # "ERROR1"
    DCAMPROP_SENSORCOOLERSTATUS__NONE = 0  # "NONE"
    DCAMPROP_SENSORCOOLERSTATUS__OFF = 1  # "OFF"
    DCAMPROP_SENSORCOOLERSTATUS__READY = 2  # "READY"
    DCAMPROP_SENSORCOOLERSTATUS__BUSY = 3  # "BUSY"
    DCAMPROP_SENSORCOOLERSTATUS__ALWAYS = 4  # "ALWAYS"
    DCAMPROP_SENSORCOOLERSTATUS__WARNING = 5  # "WARNING"

    # DCAM_IDPROP_CONTRAST_CONTROL  															# reserved
    #	DCAMPROP_CONTRAST_CONTROL__OFF				= 1 	 		#	"OFF"					 	# reserved
    #	DCAMPROP_CONTRAST_CONTROL__ON				= 2 	 		#	"ON"					 	# reserved
    #	DCAMPROP_CONTRAST_CONTROL__FRONTPANEL		= 3 	 		#	"FRONT PANEL"			 	# reserved

    # DCAM_IDPROP_REALTIMEGAINCORRECT_LEVEL
    DCAMPROP_REALTIMEGAINCORRECT_LEVEL__1 = 1  # "1"
    DCAMPROP_REALTIMEGAINCORRECT_LEVEL__2 = 2  # "2"
    DCAMPROP_REALTIMEGAINCORRECT_LEVEL__3 = 3  # "3"
    DCAMPROP_REALTIMEGAINCORRECT_LEVEL__4 = 4  # "4"
    DCAMPROP_REALTIMEGAINCORRECT_LEVEL__5 = 5  # "5"

    # DCAM_IDPROP_WHITEBALANCEMODE
    DCAMPROP_WHITEBALANCEMODE__FLAT = 1  # "FLAT"
    DCAMPROP_WHITEBALANCEMODE__AUTO = 2  # "AUTO"
    DCAMPROP_WHITEBALANCEMODE__TEMPERATURE = 3  # "TEMPERATURE"
    DCAMPROP_WHITEBALANCEMODE__USERPRESET = 4  # "USER PRESET"

    # DCAM_IDPROP_DARKCALIB_TARGET
    DCAMPROP_DARKCALIB_TARGET__ALL = 1  # "ALL"
    DCAMPROP_DARKCALIB_TARGET__ANALOG = 2  # "ANALOG"

    # DCAM_IDPROP_SHADINGCALIB_METHOD
    DCAMPROP_SHADINGCALIB_METHOD__AVERAGE = 1  # "AVERAGE"
    DCAMPROP_SHADINGCALIB_METHOD__MAXIMUM = 2  # "MAXIMUM"
    DCAMPROP_SHADINGCALIB_METHOD__USETARGET = 3  # "USE TARGET"

    # DCAM_IDPROP_CAPTUREMODE
    DCAMPROP_CAPTUREMODE__NORMAL = 1  # "NORMAL"
    DCAMPROP_CAPTUREMODE__DARKCALIB = 2  # "DARK CALIBRATION"
    DCAMPROP_CAPTUREMODE__SHADINGCALIB = 3  # "SHADING CALIBRATION"
    DCAMPROP_CAPTUREMODE__TAPGAINCALIB = 4  # "TAP GAIN CALIBRATION"
    DCAMPROP_CAPTUREMODE__BACKFOCUSCALIB = 5  # "BACK FOCUS CALIBRATION"	 	#[ ORCA-D2 ]

    # DCAM_IDPROP_INTERFRAMEALU_ENABLE
    DCAMPROP_INTERFRAMEALU_ENABLE__OFF = 1  # "OFF"
    DCAMPROP_INTERFRAMEALU_ENABLE__TRIGGERSOURCE_ALL = 2  # "TRIGGER SOURCE ALL"
    DCAMPROP_INTERFRAMEALU_ENABLE__TRIGGERSOURCE_INTERNAL = 3  # "TRIGGER SOURCE INTERNAL ONLY"

    # DCAM_IDPROP_SUBTRACT_DATASTATUS/DCAM_IDPROP_SHADINGCALIB_DATASTATUS
    DCAMPROP_CALIBDATASTATUS__NONE = 1  # "NONE"
    DCAMPROP_CALIBDATASTATUS__FORWARD = 2  # "FORWARD"
    DCAMPROP_CALIBDATASTATUS__BACKWARD = 3  # "BACKWARD"
    DCAMPROP_CALIBDATASTATUS__BOTH = 4  # "BOTH"

    # DCAM_IDPROP_TAPGAINCALIB_METHOD
    DCAMPROP_TAPGAINCALIB_METHOD__AVE = 1  # "AVERAGE"
    DCAMPROP_TAPGAINCALIB_METHOD__MAX = 2  # "MAXIMUM"
    DCAMPROP_TAPGAINCALIB_METHOD__MIN = 3  # "MINIMUM"

    # DCAM_IDPROP_RECURSIVEFILTERFRAMES  						# numeric headletter options
    DCAMPROP_RECURSIVEFILTERFRAMES__2 = 2  # "2 FRAMES"
    DCAMPROP_RECURSIVEFILTERFRAMES__4 = 4  # "4 FRAMES"
    DCAMPROP_RECURSIVEFILTERFRAMES__8 = 8  # "8 FRAMES"
    DCAMPROP_RECURSIVEFILTERFRAMES__16 = 16  # "16 FRAMES"
    DCAMPROP_RECURSIVEFILTERFRAMES__32 = 32  # "32 FRAMES"
    DCAMPROP_RECURSIVEFILTERFRAMES__64 = 64  # "64 FRAMES"

    # DCAM_IDPROP_INTENSITYLUT_MODE
    DCAMPROP_INTENSITYLUT_MODE__THROUGH = 1  # "THROUGH"
    DCAMPROP_INTENSITYLUT_MODE__PAGE = 2  # "PAGE"
    DCAMPROP_INTENSITYLUT_MODE__CLIP = 3  # "CLIP"

    # DCAM_IDPROP_BINNING
    DCAMPROP_BINNING__1 = 1  # "1X1"
    DCAMPROP_BINNING__2 = 2  # "2X2"
    DCAMPROP_BINNING__4 = 4  # "4X4"
    DCAMPROP_BINNING__8 = 8  # "8X8"
    DCAMPROP_BINNING__16 = 16  # "16X16"
    DCAMPROP_BINNING__1_2 = 102  # "1X2"
    DCAMPROP_BINNING__2_4 = 204  # "2X4"

    # DCAM_IDPROP_COLORTYPE
    DCAMPROP_COLORTYPE__BW = 0x00000001  # "BW"
    DCAMPROP_COLORTYPE__RGB = 0x00000002  # "RGB"
    DCAMPROP_COLORTYPE__BGR = 0x00000003  # "BGR"
    # other values are resereved

    # DCAM_IDPROP_BITSPERCHANNEL  							# numeric headletter options
    DCAMPROP_BITSPERCHANNEL__8 = 8  # "8BIT"
    DCAMPROP_BITSPERCHANNEL__10 = 10  # "10BIT"
    DCAMPROP_BITSPERCHANNEL__12 = 12  # "12BIT"
    DCAMPROP_BITSPERCHANNEL__14 = 14  # "14BIT"
    DCAMPROP_BITSPERCHANNEL__16 = 16  # "16BIT"

    # DCAM_IDPROP_IMAGEFOOTER_FORMAT

    # DCAM_IDPROP_DEFECTCORRECT_MODE
    DCAMPROP_DEFECTCORRECT_MODE__OFF = 1  # "OFF"
    DCAMPROP_DEFECTCORRECT_MODE__ON = 2  # "ON"

    # DCAM_IDPROP_DEFECTCORRECT_METHOD
    DCAMPROP_DEFECTCORRECT_METHOD__CEILING = 3  # "CEILING"
    DCAMPROP_DEFECTCORRECT_METHOD__PREVIOUS = 4  # "PREVIOUS"

    # DCAM_IDPROP_HOTPIXELCORRECT_LEVEL
    DCAMPROP_HOTPIXELCORRECT_LEVEL__STANDARD = 1  # "STANDARD"
    DCAMPROP_HOTPIXELCORRECT_LEVEL__MINIMUM = 2  # "MINIMUM"
    DCAMPROP_HOTPIXELCORRECT_LEVEL__AGGRESSIVE = 3  # "AGGRESSIVE"

    # DCAM_IDPROP_DEVICEBUFFER_MODE
    DCAMPROP_DEVICEBUFFER_MODE__THRU = 1  # "THRU"
    DCAMPROP_DEVICEBUFFER_MODE__SNAPSHOT = 2  # "SNAPSHOT"

    # DCAM_IDPROP_SYSTEM_ALIVE
    DCAMPROP_SYSTEM_ALIVE__OFFLINE = 1  # "OFFLINE"
    DCAMPROP_SYSTEM_ALIVE__ONLINE = 2  # "ONLINE"
    DCAMPROP_SYSTEM_ALIVE__ERROR = 3  # "ERROR"

    # DCAM_IDPROP_TIMESTAMP_MODE
    DCAMPROP_TIMESTAMP_MODE__NONE = 1  # "NONE"
    DCAMPROP_TIMESTAMP_MODE__LINEBEFORELEFT = 2  # "LINE BEFORE LEFT"
    DCAMPROP_TIMESTAMP_MODE__LINEOVERWRITELEFT = 3  # "LINE OVERWRITE LEFT"
    DCAMPROP_TIMESTAMP_MODE__AREABEFORELEFT = 4  # "AREA BEFORE LEFT"
    DCAMPROP_TIMESTAMP_MODE__AREAOVERWRITELEFT = 5  # "AREA OVERWRITE LEFT"

    # DCAM_IDPROP_TIMING_EXPOSURE
    DCAMPROP_TIMING_EXPOSURE__AFTERREADOUT = 1  # "AFTER READOUT"
    DCAMPROP_TIMING_EXPOSURE__OVERLAPREADOUT = 2  # "OVERLAP READOUT"
    DCAMPROP_TIMING_EXPOSURE__ROLLING = 3  # "ROLLING"
    DCAMPROP_TIMING_EXPOSURE__ALWAYS = 4  # "ALWAYS"
    DCAMPROP_TIMING_EXPOSURE__TDI = 5  # "TDI"

    # DCAM_IDPROP_TIMESTAMP_PRODUCER
    DCAMPROP_TIMESTAMP_PRODUCER__NONE = 1  # "NONE"
    DCAMPROP_TIMESTAMP_PRODUCER__DCAMMODULE = 2  # "DCAM MODULE"
    DCAMPROP_TIMESTAMP_PRODUCER__KERNELDRIVER = 3  # "KERNEL DRIVER"
    DCAMPROP_TIMESTAMP_PRODUCER__CAPTUREDEVICE = 4  # "CAPTURE DEVICE"
    DCAMPROP_TIMESTAMP_PRODUCER__IMAGINGDEVICE = 5  # "IMAGING DEVICE"

    # DCAM_IDPROP_FRAMESTAMP_PRODUCER
    DCAMPROP_FRAMESTAMP_PRODUCER__NONE = 1  # "NONE"
    DCAMPROP_FRAMESTAMP_PRODUCER__DCAMMODULE = 2  # "DCAM MODULE"
    DCAMPROP_FRAMESTAMP_PRODUCER__KERNELDRIVER = 3  # "KERNEL DRIVER"
    DCAMPROP_FRAMESTAMP_PRODUCER__CAPTUREDEVICE = 4  # "CAPTURE DEVICE"
    DCAMPROP_FRAMESTAMP_PRODUCER__IMAGINGDEVICE = 5  # "IMAGING DEVICE"

    # DCAM_IDPROP_CAMERASTATUS_INTENSITY
    DCAMPROP_CAMERASTATUS_INTENSITY__GOOD = 1  # "GOOD"
    DCAMPROP_CAMERASTATUS_INTENSITY__TOODARK = 2  # "TOO DRAK"
    DCAMPROP_CAMERASTATUS_INTENSITY__TOOBRIGHT = 3  # "TOO BRIGHT"
    DCAMPROP_CAMERASTATUS_INTENSITY__UNCARE = 4  # "UNCARE"
    DCAMPROP_CAMERASTATUS_INTENSITY__EMGAIN_PROTECTION = 5  # "EMGAIN PROTECTION"
    DCAMPROP_CAMERASTATUS_INTENSITY__INCONSISTENT_OPTICS = 6  # "INCONSISTENT OPTICS"
    DCAMPROP_CAMERASTATUS_INTENSITY__NODATA = 7  # "NO DATA"

    # DCAM_IDPROP_CAMERASTATUS_INPUTTRIGGER
    DCAMPROP_CAMERASTATUS_INPUTTRIGGER__GOOD = 1  # "GOOD"
    DCAMPROP_CAMERASTATUS_INPUTTRIGGER__NONE = 2  # "NONE"
    DCAMPROP_CAMERASTATUS_INPUTTRIGGER__TOOFREQUENT = 3  # "TOO FREQUENT"

    # DCAM_IDPROP_CAMERASTATUS_CALIBRATION
    DCAMPROP_CAMERASTATUS_CALIBRATION__DONE = 1  # "DONE"
    DCAMPROP_CAMERASTATUS_CALIBRATION__NOTYET = 2  # "NOT YET"
    DCAMPROP_CAMERASTATUS_CALIBRATION__NOTRIGGER = 3  # "NO TRIGGER"
    DCAMPROP_CAMERASTATUS_CALIBRATION__TOOFREQUENTTRIGGER = 4  # "TOO FREQUENT TRIGGER"
    DCAMPROP_CAMERASTATUS_CALIBRATION__OUTOFADJUSTABLERANGE = 5  # "OUT OF ADJUSTABLE RANGE"
    DCAMPROP_CAMERASTATUS_CALIBRATION__UNSUITABLETABLE = 6  # "UNSUITABLE TABLE"
    DCAMPROP_CAMERASTATUS_CALIBRATION__TOODARK = 7  # "TOO DARK"
    DCAMPROP_CAMERASTATUS_CALIBRATION__TOOBRIGHT = 8  # "TOO BRIGHT"
    DCAMPROP_CAMERASTATUS_CALIBRATION__NOTDETECTOBJECT = 9  # "NOT DETECT OBJECT"

    # -- for general purpose --
    DCAMPROP_MODE__OFF = 1  # "OFF"
    DCAMPROP_MODE__ON = 2  # "ON"

    # -- options --

    # for backward compativilities

    DCAMPROP_SCAN_MODE__NORMAL = DCAMPROP_SENSORMODE__AREA
    DCAMPROP_SCAN_MODE__SLIT = DCAMPROP_SENSORMODE__SLIT

    DCAMPROP_SWITCHMODE_OFF = DCAMPROP_MODE__OFF  # "OFF"
    DCAMPROP_SWITCHMODE_ON = DCAMPROP_MODE__ON  # "ON"

    DCAMPROP_TRIGGERACTIVE__PULSE = DCAMPROP_TRIGGERACTIVE__SYNCREADOUT  # was "PULSE"

    DCAMPROP_READOUT_DIRECTION__NORMAL = DCAMPROP_READOUT_DIRECTION__FORWARD  # VALUETEXT was "NORMAL"
    DCAMPROP_READOUT_DIRECTION__REVERSE = DCAMPROP_READOUT_DIRECTION__BACKWARD  # VALUETEXT was "REVERSE"

    # -- miss spelling --
    DCAMPROP_TRIGGERSOURCE__EXERNAL = DCAMPROP_TRIGGERSOURCE__EXTERNAL
