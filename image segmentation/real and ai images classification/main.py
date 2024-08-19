import streamlit as st
from PIL import Image
from utils import set_background, classify
from ultralytics import YOLO

# Set the background image
set_background(r"C:/Users/bahha/Desktop/ComputerVision/Learning_OpenCV/image segmentation/real and ai images classification/background.png")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #ec4899, #8b5cf6, #6366f1);
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="stCard">', unsafe_allow_html=True)
# Your existing content here
st.markdown('</div>', unsafe_allow_html=True)

# Title
st.markdown('<h1 style="text-align: center; font-size: 2.5rem; font-weight: bold; color: #1f2937;">Real and AI Images Classification</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; font-size: 1.25rem; color: #4b5563; margin-bottom: 2rem;">Upload an image to classify it as real or AI generated</h2>', unsafe_allow_html=True)

# File uploader
st.markdown(
    """
    <style>
    .stFileUploader > div {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        padding: 1rem;
    }
    .stFileUploader > div:hover {
        border-color: #6366f1;
    }
    </style>
    """,
    unsafe_allow_html=True
)
file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg', 'webp', 'jfif', 'tiff', 'tif'])
# Load the YOLOv8 model
model = YOLO("C:\\Users\\bahha\\Desktop\\ComputerVision\\Learning_OpenCV\\image segmentation\\real and ai images classification\\model\\best.pt")

# Display the image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Classify the image
    class_name, conf_score = classify(image, model)
    
    st.markdown(f"""
    <div class="result-card">
        <h3>Classification Result</h3>
        <p>Prediction: {class_name}</p>
        <p>Confidence: {conf_score:.3f}</p>
    </div>
    """, unsafe_allow_html=True)
