import torch
from torchvision import transforms
from PIL import Image
import sys
from model import CustomImageClassifier

def predict_image(image_path):
    # 1. Load Classes
    try:
        with open("classes.txt", "r") as f:
            classes = f.read().splitlines()
    except FileNotFoundError:
        print("❌ classes.txt not found. Please train the model first.")
        return

    # 2. Setup Device and Load Model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = CustomImageClassifier(num_classes=len(classes)).to(device)
    
    try:
        model.load_state_dict(torch.load("custom_ai_model.pth", map_location=device))
        model.eval() # Set to evaluation mode
    except FileNotFoundError:
        print("❌ custom_ai_model.pth not found. Please train the model first.")
        return

    # 3. Process the Input Image
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    try:
        img = Image.open(image_path).convert('RGB')
        img_tensor = transform(img).unsqueeze(0).to(device) # Add batch dimension
    except Exception as e:
        print(f"❌ Error loading image: {e}")
        return

    # 4. Make Prediction
    with torch.no_grad():
        output = model(img_tensor)
        _, predicted_idx = torch.max(output, 1)
        predicted_class = classes[predicted_idx.item()]
        
        # Calculate Confidence
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        confidence = probabilities[predicted_idx.item()].item() * 100

    print(f"\n🧠 AI Prediction:")
    print(f"➔ Class: {predicted_class}")
    print(f"➔ Confidence: {confidence:.2f}%\n")

if __name__ == "__main__":
    # Example usage: python predict.py my_test_image.jpg
    if len(sys.argv) < 2:
        print("Usage: python predict.py <path_to_image>")
    else:
        predict_image(sys.argv[1])
