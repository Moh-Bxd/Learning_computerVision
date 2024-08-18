import cv2
import numpy as np
import torch
from ultralytics import YOLO

# Load the model
model = YOLO("yolov8n-cls.pt")  # Load a pretrained model for classification

# Train the model
results = model.train(
    data="C:\\Users\\bahha\\Desktop\\ComputerVision\\Learning_OpenCV\\image segmentation\\yolov8\\data",  # Path to your dataset
    epochs=20,  # Number of epochs
    imgsz=64, 
# Increase image size for better learning
)

