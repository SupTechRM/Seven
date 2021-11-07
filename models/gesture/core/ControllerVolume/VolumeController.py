from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math

wCam, hCam = 640, 480


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(3, hCam)

pTime = 0

detector = htm.handDetector(detectionConfidence=0.7, maxHands=1)

devices = AudioUtilities.GetSpeakers()
print(devices)
interface = devices.Activate(
	IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
area = 0
colorVol = (0, 0, 255)

while True:
	# Capture Frames
	success, img = cap.read()
	
	# Locate Hands in Frame
	img = detector.findHands(img, draw=False)
	
	# Find Position of Landmarks
	lmList, bbox = detector.findPosition(img, draw=True)
	if len(lmList) != 0:

		# Filter Based on Size
		area = (bbox[2]-bbox[0]) * (bbox[3] - bbox[1])//100
		print(area)
		# Find Position of Hand

		# Find distance between index and thumb
		length, img, lineInfo = detector.findDistance(4, 8, img)            
		print(length)

		# Convert Volume
		volBar = np.interp(length,[50, 200], [400, 150])
		volPer=np.interp(length, [50, 200], [0, 100])

		# Reduce Resolution
		smoothness = 10
		volPer = smoothness * round(volPer / smoothness)

		# Check Fingers Up
		fingers = detector.fingersUp()
		print(fingers)

		# If SetTarget is down set volume
		if not fingers[4]:
			volume.SetMasterVolumeLevelScalar(volPer/100, None)
			cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 0, 255), cv2.FILLED)
			colorVol = (0, 255, 0)
		else:
			colorVol = (0, 0, 255)

	# Drawings to Render on Indicator
	cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
	cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
	cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
				1, (255, 0, 0), 3)
	cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
	cv2.putText(img, f'Vol Set: {int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX,
				1, colorVol, 3)
	# Calculate FPS
	cTime = time.time()
	fps = 1 / (cTime - pTime)
	pTime = cTime

	# Render Data
	# Render FPS on Screen
	cv2.putText(img, f"FPS: {int(fps)}", (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
	cv2.imshow("Img", img)
	cv2.waitKey(1)
