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
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    
    # Apply threshold
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on a copy of the original frame
    contour_frame = frame1.copy()
    cv2.drawContours(contour_frame, contours, -1, (0, 255, 0), 2)
    
    # Display videos
    cv2.imshow('Original Video', frame1)
    cv2.imshow('Contours Video', contour_frame)
    
    # Exit on 'q' key press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cv2.destroyAllWindows()
