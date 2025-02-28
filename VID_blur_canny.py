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
    edges = cv2.Canny(frame1, 100, 200)
    # Apply Gaussian blur
    blur = cv2.GaussianBlur(frame1, (15, 15), 2)
    # Display videos
    cv2.imshow('Original Video', frame1)
    cv2.imshow('Blue Video',blur)
    cv2.imshow('Canny Video',edges)
    # Exit on 'q' key press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cv2.destroyAllWindows()
