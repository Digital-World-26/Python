import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from model import CustomImageClassifier
import os

# 1. Hyperparameters & Setup
EPOCHS = 10
BATCH_SIZE = 32
LEARNING_RATE = 0.001
DATA_DIR = "dataset"

# Hardware Acceleration check (GPU ya CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"🚀 Training on device: {device}")

# 2. Image Transformations (Resize, Convert to Tensor, Normalize)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 3. Load Dataset
train_data = datasets.ImageFolder(os.path.join(DATA_DIR, 'train'), transform=transform)
val_data = datasets.ImageFolder(os.path.join(DATA_DIR, 'val'), transform=transform)

train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_data, batch_size=BATCH_SIZE, shuffle=False)

num_classes = len(train_data.classes)
print(f"📊 Classes Found: {train_data.classes}")

# 4. Initialize Model, Loss Function, and Optimizer
model = CustomImageClassifier(num_classes=num_classes).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

# 5. Training Loop
for epoch in range(EPOCHS):
    model.train()
    running_loss = 0.0
    
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        
        optimizer.zero_grad()        # Reset gradients
        outputs = model(images)      # Forward pass
        loss = criterion(outputs, labels) # Calculate error
        loss.backward()              # Backward pass
        optimizer.step()             # Update weights
        
        running_loss += loss.item()
        
    print(f"Epoch [{epoch+1}/{EPOCHS}], Loss: {running_loss/len(train_loader):.4f}")

# 6. Save the trained model
torch.save(model.state_dict(), "custom_ai_model.pth")
print("✅ Training Complete! Model saved as 'custom_ai_model.pth'")

# Save class names for prediction
with open("classes.txt", "w") as f:
    f.write("\n".join(train_data.classes))
