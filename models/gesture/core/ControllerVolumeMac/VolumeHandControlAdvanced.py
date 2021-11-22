import cv2

cam = cv2.VideoCapture(0)
print(cam.isOpened())
cam.release()