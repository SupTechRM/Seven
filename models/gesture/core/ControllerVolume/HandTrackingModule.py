"""
Hand Tracking Module
"""

# Import Packages
import cv2
import mediapipe as mp
import time
import math

# Hand Detection Module Class
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionConfidence=0.5, trackConfidence=0.5):
        
        """ Define Variables"""
        
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionConfidence
        self.trackCon = trackConfidence
 
        # Initialize MediaPipe Hand Detector
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode = self.mode, max_num_hands=self.maxHands, min_detection_confidence = self.detectionCon, min_tracking_confidence = self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

        self.tipIds = [4, 8, 12, 16, 20]
 
    def findHands(self, img, draw=True):
        # Process RGB Image
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        # Check for Hand Results
        if self.results.multi_hand_landmarks:
            
            # Check for each hand
            for handLms in self.results.multi_hand_landmarks:
                
                # Draw connections between landmarks on hand position
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img
 
    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []

        # Make a list of hand landmarks
        self.lmList = []
        if self.results.multi_hand_landmarks:
            
            # Define hand by an id
            myHand = self.results.multi_hand_landmarks[handNo]
            
            # Check for each landmark
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                
                # Find Endpoints; Calculate Pixel Distance
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                xList.append(cx)
                yList.append(cy)

                # print(id, cx, cy)
                # Append Pixel Distance Data to lmList
                self.lmList.append([cx, cy])

                # Draw circle on Pixel Distance endpoint on hand landmarks
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 255, 255), cv2.FILLED)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax
            
            if draw:
                cv2.rectangle(img, (bbox[0]-20, bbox[1]-20), (bbox[2], bbox[3]), (0, 255, 0), 2)

        return self.lmList, bbox

    def fingersUp(self):
        fingers = []

        # Thumb
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        # Fingers
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][1] < self.lmList[self.tipIds[id] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        return fingers

    def findDistance(self, p1, p2, img, draw=True):
        x1 = self.lmList[p1][0]
        y1 = self.lmList[p1][1]
        x2, y2 = self.lmList[p2][0], self.lmList[p2][1]
       
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
        if draw: 
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)
        return length, img, [x1, y1, x2, y2, cx, cy]

# Test Case for Hand Tracking Module 
def main():

    # FPS Data Define
    pTime = 0
    cTime = 0

    # Take Webcam Input
    cap = cv2.VideoCapture(0)
    
    # Define Hand Module Class
    detector = handDetector()

    while True:

        # Define variable img to capture frame
        success, img = cap.read()

        # Recognize Hand Positions
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        # Calculate FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        
        # Render FPS On Screen
        cv2.putText(img, "FPS: " + str(round(fps, 1)), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
 
        cv2.imshow("Image", img)
        cv2.waitKey(1)
 
# Run main as an example when the module is run 
if __name__ == "__main__":
    main()
