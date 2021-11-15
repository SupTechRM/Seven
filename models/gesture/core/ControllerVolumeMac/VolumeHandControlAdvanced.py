import cv2
import time
import numpy as np
import math
import HandTrackingModule as htm
import osascript


wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon = 0.7)

minVol = 0
maxVol = 100
vol = 0
volBar = 400
volPer = 0
area = 0

while True:
    # Find Hand
    success, img = cap.read()
    img = detector.findHands(img, draw=False)
    lmList, bbox = detector.findPosition(img, draw=False)
    if len(lmList) != 0:

        area = (bbox[2]-bbox[0]) * (bbox[3]-bbox[1])//100
        # print(area)
        if 250 < area < 1000:
            # print("Yes")
            length, img, lineInfo = detector.findDistance(4, 8, img, draw=False)
            # print(length)

            vol = np.interp(length, [50, 300], [minVol, maxVol])
            volPer = np.interp(length, [50, 300], [0, 100])

            smoothness = 10
            volPer = smoothness * (round(volPer/smoothness))

            fingers = detector.fingersUp()
            # print(fingers)
            if not fingers[4]:
                osascript.osascript("set volume output volume " + str(volPer))

    cVol = osascript.osascript("get output volume of (get volume settings)")
    cv2.putText(img, f'Volume: {int(cVol[1])} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 250, 0), 3)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)