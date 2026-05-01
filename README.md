# Custom Image Classification AI 🧠

This project is a custom Image Processing and Classification AI built using **PyTorch**. It uses a Convolutional Neural Network (CNN) architecture to learn and classify images from your custom dataset.

## 🌟 Features
* **Custom CNN Architecture:** Built from scratch using PyTorch for high performance.
* **Easy Training:** Automated dataset loading and training loop.
* **Smart Prediction:** Test new images easily with confidence scores.
* **Scalable:** Works with any number of custom image classes.

## 📁 Project Structure

\`\`\`text
Custom_Image_AI/
│
├── requirements.txt         # Dependencies required for the project
├── README.md                # Project documentation
│
├── dataset/                 # Your image data goes here
│   ├── train/               # Training data (80% of images)
│   │   ├── class_A/
│   │   └── class_B/
│   └── val/                 # Validation data (20% of images)
│       ├── class_A/
│       └── class_B/
│
├── model.py                 # The CNN Neural Network architecture
├── train.py                 # Script to train the model on your dataset
└── predict.py               # Script to test the AI with a new image
\`\`\`

## 🛠️ Installation & Setup

**1. Clone the repository (or download the files):**
\`\`\`bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
\`\`\`

**2. Install required libraries:**
Make sure you have Python installed, then run:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## 🚀 How to Use

### Step 1: Prepare Your Data
Organize your images inside the `dataset/train` and `dataset/val` folders. Create a new folder for each category you want the AI to learn.
Example:
* `dataset/train/dogs/` (put training images of dogs here)
* `dataset/train/cats/` (put training images of cats here)

### Step 2: Train the AI Model
Run the training script to allow the AI to learn from your dataset.
\`\`\`bash
python train.py
\`\`\`
*Once training is complete, it will generate a `custom_ai_model.pth` file (the trained model) and a `classes.txt` file (list of categories).*

### Step 3: Test the AI (Prediction)
Want to check if the AI works? Pass a new image to the predict script!
\`\`\`bash
python predict.py path/to/your/test_image.jpg
\`\`\`
**Output Example:**
\`\`\`text
🧠 AI Prediction:
➔ Class: dogs
➔ Confidence: 98.45%
\`\`\`

## ⚙️ Built With
* [Python](https://www.python.org/)
* [PyTorch](https://pytorch.org/) - Deep Learning Framework
* [Torchvision](https://pytorch.org/vision/stable/index.html) - Image Data Processing

## 📜 License
This project is open-source and available under the [MIT License](LICENSE). Feel free to modify and use it for your own projects!
