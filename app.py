import os
from flask import Flask, render_template, request
import torch
from torchvision import transforms
from PIL import Image
from model import CustomImageClassifier # Aapke banaye hue model file se import

app = Flask(__name__)

# --- Model Loading Setup ---
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
classes = []
model = None

try:
    # Classes aur trained weights load karna
    with open("classes.txt", "r") as f:
        classes = f.read().splitlines()
    
    model = CustomImageClassifier(num_classes=len(classes)).to(device)
    model.load_state_dict(torch.load("custom_ai_model.pth", map_location=device))
    model.eval()
    print(f"✅ AI Model successfully loaded on {device}!")
except Exception as e:
    print(f"⚠️ Warning: Model loading failed. Pehle train.py run karein! Error: {e}")

# --- Prediction Function ---
def get_prediction(image_bytes):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    img = Image.open(image_bytes).convert('RGB')
    img_tensor = transform(img).unsqueeze(0).to(device)
    
    with torch.no_grad():
        output = model(img_tensor)
        _, predicted_idx = torch.max(output, 1)
        predicted_class = classes[predicted_idx.item()]
        
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        confidence = probabilities[predicted_idx.item()].item() * 100
        
    return predicted_class, round(confidence, 2)

# --- Routes (URLs) ---
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400
        
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
        
    if file:
        try:
            predicted_class, confidence = get_prediction(file)
            return render_template('index.html', prediction=predicted_class, confidence=confidence)
        except Exception as e:
            return f"Error processing image: {e}", 500

if __name__ == '__main__':
    print("🚀 Starting Web Server... Open http://127.0.0.1:5000 in your browser.")
    app.run(debug=True, port=5000)
