import os
import cv2


path = os.path.join('images', 'me.jpg')
img = cv2.imread(path)
img_edged = cv2.Canny(img, 100, 200)
cv2.imshow('img', img)
cv2.imshow('img_edged', img_edged)
cv2.imwrite(os.path.join(os.getcwd(), 'images', 'me_edged.jpg'), img_edged)

cv2.waitKey(0)