import cv2
import numpy as np

cap1 = cv2.VideoCapture("video/video.mp4")  # First video
cap2 = cv2.VideoCapture("video/vid.mp4")  # Second video

if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Could not videos.")
    exit()

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break

    # Resize both frames to have the same width & height
    frame1 = cv2.resize(frame1, (640, 360))
    frame2 = cv2.resize(frame2, (640, 360))

    h_concat = np.hstack((frame1, frame2))
    v_concat = np.vstack((frame1, frame2))
    cv2.imshow('Horizontal Concatenation', h_concat)
    cv2.imshow('Vertical Concatenation', v_concat)

    # Exit on 'q' key press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
