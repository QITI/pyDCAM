from pyDCAM import *
import matplotlib.pyplot as plt


def main(i_device = 0):
    print("PROGRAM START")

    with use_dcamapi:
        with HDCAM(i_device) as hdcam:

            # Configure the readout speed. Use slowest option for the ultraquite mode
            hdcam.readout_speed = DCAMPROPMODEVALUE.DCAMPROP_READOUTSPEED__SLOWEST

            hdcam.subarray_mode = True # Enable subarray mode
            hdcam.subarray_size = (100, 100) # 100x100 pixels
            hdcam.subarray_pos = (200, 200) # 200 pixels from the top-left corner

            hdcam.dcambuf_alloc(1)

            hwait = hdcam.dcamwait_open()

            hdcam.dcamcap_start()

            # Wait for the frame to be ready, it has a timeout of 1000 millisec
            hwait.dcamwait_start(timeout=1000)

            # Copy the frame from the internal buffer to create a numpy array
            array = hdcam.dcambuf_copyframe()

            # Stop the capture and release the buffer
            hdcam.dcamcap_stop()
            hdcam.dcambuf_release()

            # Display the image
            plt.imshow(array)
            plt.show()

    print("PROGRAM END")


if __name__ == '__main__':
    main()
