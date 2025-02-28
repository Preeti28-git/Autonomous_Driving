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

    kernel = np.ones((5,5), np.uint8)


    opening = cv2.morphologyEx(frame1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(frame1, cv2.MORPH_CLOSE, kernel)

    # Display videos
    cv2.imshow('Original Video', frame1)
    cv2.imshow('Opening (Noise Removal)', opening)
    cv2.imshow('Closing (Fill Gaps)', closing)

    # Exit on 'q' key press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cv2.destroyAllWindows()
