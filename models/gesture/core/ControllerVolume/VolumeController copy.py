from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math

class VolumeController:
	def __init__(self):
		""" Define Webcam Height/Width"""
		self.wCam, self.hCam = 640, 480

		# Start Webcam Object
		self.cap = cv2.VideoCapture(0)
		self.cap.set(3, self.wCam)
		self.cap.set(3, self.hCam)

		# Define timer for FPS
		self.pTIme = 0

		""" Create the Detector Object """
		self.detector = htm.handDetector(detectionConfidence=0.7, maxHands=1)

		""" Speaker Activate"""
		self.devices = AudioUtilities.GetSpeakers()
		self.interface = self.devices.Activate(
			IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
		# Define Volume and Volume Range
		self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))
		self.volRange = self.volume.GetVolumeRange()

		""" Variable Define """
		# Define Min/Max Volume
		self.minVol = self.volRange[0]
		self.maxVol = self.volRange[1]
		
		# Define Volume Step
		self.vol = 0
		self.volBar = 400
		self.volPer = 0
		
		# Define Modular Area/Color
		self.area = 0
		self.colorVol = (0, 0, 255)

		###################################
		# Main Process
		###################################

		self.main()

	def main(self):
		# Capture Frames
		self.success, self.img = self.cap.read()

		# Locate Hands in Frame
		self.img = self.detector.findHands(self.img, draw=False)

		# Find Position of Landmarks
		lmList, bbox = self.detector.findPosition(self.img, draw=True)
		if len(lmList) != 0:

			# Filter Based on Size
			self.area = (bbox[2]-bbox[0]) * (bbox[3] - bbox[1])//100
			print(self.area)
			# Find Position of Hand

			# Find distance between index and thumb
			self.length, self.img, self.lineInfo = self.detector.findDistance(4, 8, self.img)
			# print(self.length)

			# Convert Volume
			volBar = np.interp(self.length, [50, 200], [400, 150])
			volPer = np.interp(self.length, [50, 200], [0, 100])

			# Reduce Resolution
			smoothness = 10
			volPer = smoothness * round(volPer / smoothness)

			# Check Fingers Up
			fingers = self.detector.fingersUp()
			print(fingers)

			# If SetTarget is down set self.volume
			if not fingers[4]:
				self.volume.SetMasterVolumeLevelScalar(volPer/100, None)
				cv2.circle(self.img, (self.lineInfo[4], self.lineInfo[5]), 15, (0, 0, 255), cv2.FILLED)
				colorVol = (0, 255, 0)
			else:
				colorVol = (0, 0, 255)
			thumbindex, self.img, soemthing = self.detector.findDistance(4, 8, self.img, draw=False)
			middleindex, self.img1, abc = self.detector.findDistance(12, 8, self.img, draw=False)
			ringindex, im2, dye = self.detector.findDistance(16, 8, self.img, draw=False)
			pinkyindex, im34, scd = self.detector.findDistance(20, 8, self.img, draw=False)

			if thumbindex < 60 and middleindex < 60 and ringindex < 60 and pinkyindex < 60:
				self.volume.SetMasterVolumeLevel(40, None)
				exit()

		# Drawings to Render on Indicator
		thumbindex = self.detector.findDistance(4, 8, self.img)
		middleindex = self.detector.findDistance(12, 8, self.img)
		ringindex = self.detector.findDistance(16, 8, self.img)
		pinkyindex = self.detector.findDistance(20, 8, self.img)

		if fingers[0] != 0 and fingers[1] != 0 and fingers[2] != 0 and fingers[3] != 0 and fingers[4] != 0:
			if thumbindex < 60 and middleindex < 60 and ringindex < 60 and pinkyindex < 60:
				exit()
		cv2.rectangle(self.img, (50, 150), (85, 400), (255, 0, 0), 3)
		cv2.rectangle(self.img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
		cv2.putText(self.img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
				1, (255, 0, 0), 3)
		cVol = int(self.volume.GetMasterVolumeLevelScalar() * 100)
		cv2.putText(self.img, f'Vol Set: {int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX,
				1, colorVol, 3)
		# Calculate FPS
		cTime = time.time()
		fps = 1 / (cTime - self.pTIme)
		self.pTIme = cTime

		# Render Data
		# Render FPS on Screen
		cv2.putText(self.img, f"FPS: {int(fps)}", (40, 50),
					cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
		cv2.imshow("Img", self.img)
		cv2.waitKey(1)

VolumeController()
