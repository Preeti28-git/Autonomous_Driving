import cv2


img = cv2.imread("park.jpg")
(h, w) = img.shape[:2]
center = (w // 2, h // 2)#centre = line

matrix = cv2.getRotationMatrix2D(center, 30, 1.0)#matrix = cv2.getRotationMatrix, angle of ration is 45 ,+ means anticlockwise ,-value clockwise ,1.0 is scale ,image is same size
rotated = cv2.warpAffine(img, matrix, (w, h))#applies rotion matrix 

cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()