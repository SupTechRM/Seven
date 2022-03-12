from sys import platform
import os


if platform == "darwin":
    os.system("python3 ../../../ControllerVolumeMac/VolumeHandControllerAdvanced.py")
elif platform == "win32":
    os.system("python3 Seven/models/core/ControllerVolume/VolumeController.py")
