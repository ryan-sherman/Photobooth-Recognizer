

import os
from time import sleep
from camera_integration import Capture


def running():
    print ("Parent runs the camera.")
    runner.runCam()


runner = Capture()
running()
