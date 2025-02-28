import cv2
import numpy as np

# Open video file
cap1 = cv2.VideoCapture("video/video.mp4")  # Put your video path

if not cap1.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break  # Exit when video ends
    hsv_vid = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

    # Display original, hsv 
    cv2.imshow('Original Video', frame1)
    cv2.imshow('HSV Video', hsv_vid)

    # Exit on 'q' key press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cv2.destroyAllWindows()
