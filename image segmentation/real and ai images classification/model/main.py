from ultralytics import YOLO 
import torch
import cv2
import numpy as np

model = YOLO("yolov8n-cls.pt")  # load a pretrained model (recommended for training)

results = model.train(data="C:\\Users\\bahha\\Desktop\\ComputerVision\\Learning_OpenCV\\image segmentation\\real and ai images classification\\model\\data", epochs=21, imgsz=64)
