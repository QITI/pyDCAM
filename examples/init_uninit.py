from pyDCAM import *


def main():
    print("PROGRAM START")

    device_count = dcamapi_init()
    print("dcamapi_init() found {} device(s).".format(device_count))

    for i_device in range(device_count):
        with HDCAM(i_device) as hdcam:
            model = hdcam.dcamdev_getstring(DCAM_IDSTR.DCAM_IDSTR_MODEL)
            camera_id = hdcam.dcamdev_getstring(DCAM_IDSTR.DCAM_IDSTR_CAMERAID)
            bus = hdcam.dcamdev_getstring(DCAM_IDSTR.DCAM_IDSTR_BUS)

        print("{} ({}) on {}".format(model, camera_id, bus))

    dcamapi_uninit()

    print("PROGRAM END")


if __name__ == '__main__':
    main()
