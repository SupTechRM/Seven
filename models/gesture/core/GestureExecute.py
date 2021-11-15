from sys import platform
import os 


if platform == "darwin":
    os.system("python ../../../ControllerVolumeMac/VolumeHandControllerAdvanced.py")
elif platform == "win32":
    os.system("python Seven/models/core/ControllerVolume/VolumeController.py")