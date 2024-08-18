import cv2
import os

path = os.path.join('images', 'white.jpg')
img = cv2.imread(path)
resized = cv2.resize(img, (800, 600))


cv2.line(resized, (100, 150), (400, 500), (0, 255, 0), 5)


cv2.rectangle(resized, (100, 150), (400, 500), (0, 255, 0), 5)
cv2.circle(resized, (250, 325), 50, (0, 255, 0), 5)

cv2.putText(resized, 'YO openCV here', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)


cv2.imshow('img', resized)
cv2.waitKey(0)
