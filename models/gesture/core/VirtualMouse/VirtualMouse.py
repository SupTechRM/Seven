import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
import os

wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 6

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

while True:
    try:
        success, img = cap.read(0)
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        # cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        if(len(lmList)) != 0:
            try:
                x1, y1 = lmList[8][1:]
                x2, y2 = lmList[12][1:]

                # print(x1, y1, x2, y2)

                fingers = detector.fingersUp()
                # print(fingers)

                if fingers[1] == 1 and fingers[2] == 0:
                    try:
                        x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
                        y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

                        clocX = plocX + (x3 - plocX) / smoothening
                        clocY = plocY + (y3 - plocY) / smoothening

                        autopy.mouse.move(wScr - clocX, clocY)
                        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

                        plocX, plocY = clocX, clocY
                    except Exception:
                        continue

                if fingers[1] == 1 and fingers[2] == 1:
                    length, img, lineInfo = detector.findDistance(8, 12, img)
                    if length < 80:
                        # cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)

                        autopy.mouse.click()
                thumbindex, img, soemthing = detector.findDistance(4, 8, img, draw=False)
                middleindex, img1, abc = detector.findDistance(12, 8, img, draw=False)
                ringindex, im2, dye = detector.findDistance(16, 8, img, draw=False)
                pinkyindex, im34, scd = detector.findDistance(20, 8, img, draw=False)

                if thumbindex < 30 and middleindex < 30 and ringindex < 30 and pinkyindex < 30:
                    exit()
            except Exception:
                continue


        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        # cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # cv2.imshow("Image", img)
        cv2.waitKey(1)
    except Exception:
        continue