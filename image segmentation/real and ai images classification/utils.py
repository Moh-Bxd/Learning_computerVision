import base64
import streamlit as st  
import numpy as np
from PIl import ImageOps, Image


def set_background(png_file):

    with open(png_file, "rb") as f:
        png_file = f.read()
        
    base64_image = base64.b64encode(png_file.decode())
    style = f"""
    <style>
    .reportview-container {{
        background: url(data:image/png;base64,{base64_image}) !important;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    
  
def classify(image,model, class_names):
    image = ImageOps.fit(image, (224, 224),Image.Resampling.LANCZOS)
    image_array = np.asarray(image)   
    
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
     
    # set the input 
    data = np.ndarray(shape =(1,224,224,3), dtype = np.float32)
    data[0] = normalized_image_array
    
    prediction = model.predict(data)
     
    index = np.argmax(prediction)
    
    class_name = class_names[index]
    conf_score = prediction[0][index]
    
    
    
    return "dammy", 0