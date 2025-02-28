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

    # Convert to grayscale
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Display videos
    cv2.imshow('Original Video', frame1)
    cv2.imshow('Equalized Video (Grayscale)', equalized)

    # Exit on 'q' key press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cv2.destroyAllWindows()
