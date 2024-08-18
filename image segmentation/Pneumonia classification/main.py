import streamlit as st
from keras.models import load_model # type: ignore
import keras
from PIL import Image
from utils import set_background, classify

# title
st.title("Pneumonia Classification")
# header
st.header("Upload an X-ray chest image for classification")
# file uploader
file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])
# load the model
print(keras.__version__)
model = None

# model = load_model("C:\\Users\\bahha\\Desktop\\ComputerVision\\Learning_OpenCV\\image segmentation\\Pneumonia classification\\model\\pneumonia_classifier.h5", )
# class names
class_names = ["NORMAL", "PNEUMONIA"]
# display the image
if file is not None:
    image = Image.open(file).convert('RGB') 
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # classify the image
    class_name,conf_score = classify(image, model, class_names)    
    
    st.write(f"## Prediction: {class_name}")
    st.write(f"### Confidence: {conf_score}")
    