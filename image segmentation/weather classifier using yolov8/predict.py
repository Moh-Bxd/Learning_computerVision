from ultralytics import YOLO

# Load the model
model = YOLO("C:\\Users\\bahha\\Desktop\\ComputerVision\\runs\\classify\\train\\weights\\last.pt")

# Perform inference on the image
results = model("C:\\Users\\bahha\\Desktop\\test\\5.jpg")

# Access the names of the classes
names = results[0].names

top5_indices = results[0].probs.top5
top5_confidences = results[0].probs.top5conf

# Print out the probabilities for the top-5 classes
for idx, conf in zip(top5_indices, top5_confidences):
    print(f"{names[idx]}: {conf.item()}")