import cv2
import os
import mediapipe as mp

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    
    H, W, _ = frame.shape
    
    mp_face_detection = mp.solutions.face_detection
    with mp_face_detection.FaceDetection(min_detection_confidence=0.95,model_selection = 0 ) as face_detection:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out = face_detection.process(rgb)
        if out.detections:
            for detection in out.detections:
                location = detection.location_data
                bbox = detection.location_data.relative_bounding_box
                x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
                x1, y1, w, h = int(x1*W), int(y1*H), int(w*W), int(h*H)
                cv2.rectangle(frame, (x1, y1), (x1+w, y1+h), (0, 255, 0), 2)  
                cv2.putText(frame, f'{int(detection.score[0]*100)}%', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                ## Anonymize the face
                frame[y1:y1+h, x1:x1+w, :]=cv2.blur(frame[y1:y1+h, x1:x1+w, :], (50, 50))
                
           
        pass
        
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()