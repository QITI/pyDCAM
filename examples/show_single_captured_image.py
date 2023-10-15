from pyDCAM import *
import matplotlib.pyplot as plt


def main(i_device = 0):
    print("PROGRAM START")

    with use_dcamapi:
        with HDCAM(i_device) as hdcam:
            
            # Configure the readout speed. Use slowest option for the ultraquite mode
            hdcam.readout_speed = DCAMPROPMODEVALUE.DCAMPROP_READOUTSPEED__SLOWEST

            hdcam.dcambuf_alloc(1)

            hwait = hdcam.dcamwait_open()

            hdcam.dcamcap_start()

            hwait.dcamwait_start(timeout=1000) # 1000 millisec timeout
            array = hdcam.dcambuf_copyframe()

            hdcam.dcamcap_stop()
            hdcam.dcambuf_release()

            plt.imshow(array)
            plt.show()

    print("PROGRAM END")


if __name__ == '__main__':
    main()
