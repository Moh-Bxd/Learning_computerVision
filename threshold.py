import os
import cv2


image_path = os.path.join('images', 'handwritten.png')
img = cv2.imread(image_path)
thresh = cv2.adaptiveThreshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
cv2.imwrite(os.path.join(os.getcwd(), 'images', 'handwritten_out.jpg'), thresh)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)