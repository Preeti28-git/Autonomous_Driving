import cv2
import numpy as np

# Open video file
cap1 = cv2.VideoCapture("video/vid.mp4")  # Put your video path

if not cap1.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break  # Exit when video ends

    cropped = frame1[250:400, 150:300] #y_end > y_start and x_end > x_start
    # Display videos
    cv2.imshow('Original Video', frame1)
    cv2.imshow('cropped Video',cropped)
    # Exit on 'q' key press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cv2.destroyAllWindows()
