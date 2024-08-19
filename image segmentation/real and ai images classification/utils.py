import base64
import streamlit as st  


def set_background(png_file):
    with open(png_file, "rb") as f:
        png_file = f.read()

    base64_image = base64.b64encode(png_file).decode()
    style = f"""
    <style>
    .stApp {{
        background: url(data:image/png;base64,{base64_image}) no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)
    
    
  
def classify(image, model):
    # Resize and normalize the image

    # Perform inference using YOLOv8
    results = model(image)
    
    class_names = results[0].names
    class_index = results[0].probs.top1
    conf_score = results[0].probs.top1conf
    
    class_name = class_names[class_index]

    # Map specific class names to human-readable labels
    
    if class_name == "AiArtData":
        class_name = "this art was made by an AI"
    else:
        class_name = "This art was made by a human"
    
    return class_name  , conf_score