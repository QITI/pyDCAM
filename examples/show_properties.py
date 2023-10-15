from pyDCAM import *


def main(i_device = 0):
    print("PROGRAM START")

    with use_dcamapi:
        with HDCAM(i_device) as hdcam:
            for prop_id in hdcam.dcamprop_ids():
                name = hdcam.dcamprop_getname(prop_id)
                value = hdcam.dcamprop_getvalue(prop_id)

                print(name, value)

    print("PROGRAM END")


if __name__ == '__main__':
    main()
