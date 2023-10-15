from collections.abc import Callable, Iterable, Mapping
from typing import Any
from pyDCAM import *
import matplotlib.pyplot as plt
import time
import threading


def main(i_device = 0):
    print("PROGRAM START")

    with use_dcamapi:
        with HDCAM(i_device) as hdcam:

            # Use the software trigger. Alternatively, use DCAMPROP_TRIGGERSOURCE__EXTERNAL
            # to use the external trigger.
            hdcam.dcamprop_setvalue(DCAMIDPROP.DCAM_IDPROP_TRIGGERSOURCE,
                DCAMPROPMODEVALUE.DCAMPROP_TRIGGERSOURCE__SOFTWARE
            )
           
            delay = 5

            class FireSoftwareTrigger(threading.Thread):
                def run(self):
                    for i in range(delay, 0, -1):
                        print(i)
                        time.sleep(1)

                    print("Firing software trigger")
                    hdcam.dcamcap_firetrigger()
                

            hdcam.dcambuf_alloc(1)

            hwait = hdcam.dcamwait_open()

            hdcam.dcamcap_start()

            # Firing the software trigger from a separate thread
            FireSoftwareTrigger().start()

            # Blocking until the software trigger is fired
            hwait.dcamwait_start()

            array = hdcam.dcambuf_copyframe()

            hdcam.dcamcap_stop()
            hdcam.dcambuf_release()

            plt.imshow(array)
            plt.show()

    print("PROGRAM END")


if __name__ == '__main__':
    main()
