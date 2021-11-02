"""
Hand Tracking Module
"""

# Import Packages
import cv2
import mediapipe as mp
import time

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
        
        # Make a list of hand landmarks
        lmList = []
        if self.results.multi_hand_landmarks:
            
            # Define hand by an id
            myHand = self.results.multi_hand_landmarks[handNo]
            
            # Check for each landmark
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                
                # Find Endpoints; Calculate Pixel Distance
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                # print(id, cx, cy)
                # Append Pixel Distance Data to lmList
                lmList.append([cx, cy])

                # Draw circle on Pixel Distance endpoint on hand landmarks
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 255, 255), cv2.FILLED)
 
        return lmList
 
 
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
