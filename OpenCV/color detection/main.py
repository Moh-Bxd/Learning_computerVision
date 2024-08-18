import cv2
from utils import get_limits
from PIL import Image



yellow = [0, 255, 255]



cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower, upper = get_limits(color=yellow)   
    
    mask = cv2.inRange(hsv, lower, upper)   
    
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()  
    if bbox:
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), yellow, 2)     
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()    