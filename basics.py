import os 
import cv2

def image():
    ## read image

    image_path = os.path.join('images', 'flower.jpg')
    img = cv2.imread(image_path)

    ## write image

    cv2.imwrite(os.path.join(os.getcwd(), 'images', 'flower_outy.jpg'), img)

    cv2.imshow('image', img)
    cv2.waitKey(0)

def video():
    video_path = os.path.join('videos', 'video.mp4')
    video = cv2.VideoCapture(video_path)
    
    #visualize video
    ret = True
    while ret:
        ret, frame = video.read()
        cv2.imshow('video', frame)
        cv2.waitKey(1)
        
    video.release()
    cv2.destroyAllWindows()    
        
def webcam():
    webcam = cv2.VideoCapture(0)
    
    #visualize webcam
    while True:
        ret,f = webcam.read()
        cv2.imshow('webcam', f)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    webcam.release()
    cv2.destroyAllWindows()    
    
while True:
    print("1. Image\n2. Video\n3. Webcam\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        image()
    elif choice == 2:
        video()
    elif choice == 3:
        webcam()
    else:
        break