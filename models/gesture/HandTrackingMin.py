import cv2
import mediapipe as mp
import numpy
import os
import time

# Capture Image Data
cap = cv2.VideoCapture(0)

# Use MediaPipe's API to load the TFLite model and labels.
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
  success, img = cap.read()
  imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  results = hands.process(imgRGB)

  if results.multi_hand_landmarks:
    for handLms in results.multi_hand_landmarks:
      for id, lm in enumerate(handLms.landmark):
        h, w, c = img.shape

        cx, cy = int(lm.x * w), int(lm.y * h)
        #if id == 4:
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

      mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

  cTime = time.time()
  fps = 1/(cTime - pTime)
  pTime = cTime
  cv2.putText(img, "FPS: " + str(round(fps, 2)), (10, 30),
              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

  # Run the pipeline.
  cv2.imshow("Image", img)
  cv2.waitKey(1)
