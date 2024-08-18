import os 
import cv2 
import numpy as np

def colorspaces():
    
    
    img = cv2.imread(os.path.join('images', 'flower.jpg'))
    img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    cv2.imshow('img',img)
    cv2.imshow('img_rgb',img_rgb)
    cv2.imshow('img_gray',img_gray)
    cv2.imshow('img_hsv',img_hsv)   
    cv2.waitKey(0)
    
    
def blurring():
    # we use blurring to reduce noise 
    # this is useful in many applications like edge detection and segmentation and object detection and tracking
    img = cv2.imread(os.path.join('images', 'flower.jpg'))
    img_blur = cv2.GaussianBlur(img,(5,5),0)
    img_blur2 = cv2.medianBlur(img,5)
    
    cv2.imshow('img',img)
    cv2.imshow('img_gaussian',img_blur)
    cv2.imshow('img_median',img_blur2)
    cv2.waitKey(0)     
    
    
while True:
    print("1. Colorspaces\n2. Blurring\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        colorspaces()
    elif choice == 2:
        blurring()
    else:
        break    