import cv2
import numpy as np

# Open video file
cap1 = cv2.VideoCapture("video/video.mp4")  # Put your video path

if not cap1.isOpened():
    print("Error: Could not open video.")
    exit()

# Kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break  # Exit when video ends

    # Resize frame
    frame1 = cv2.resize(frame1, (640, 360))

    # Apply dilation and erosion
    dilation = cv2.dilate(frame1, kernel, iterations=1)
    erosion = cv2.erode(frame1, kernel, iterations=1)

    # Display original, dilated, and eroded frames
    cv2.imshow('Original Video', frame1)
    cv2.imshow('Dilated Video', dilation)
    cv2.imshow('Eroded Video', erosion)

    # Exit on 'q' key press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cv2.destroyAllWindows()
