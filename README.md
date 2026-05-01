# Custom Image Classification AI with Web UI 🧠🌐

This project is a complete Custom Image Classification AI built using **PyTorch** for the backend and **Flask** for a beautiful web interface. You can train the AI on your own images and test it directly in your browser!

## 🌟 Features
* **Custom CNN Architecture:** Built from scratch using PyTorch.
* **Easy Training:** Automated dataset loading and training loop.
* **Web Interface:** Beautiful, user-friendly UI built with Flask to test images directly from your browser.
* **Terminal Support:** You can also test images directly via the command line.

## 📁 Project Structure

\`\`\`text
Custom_Image_AI/
│
├── requirements.txt         # Required libraries (PyTorch, Flask, etc.)
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
├── predict.py               # Script to test the AI via Terminal/CMD
│
├── app.py                   # The Web Server (Flask)
└── templates/               
    └── index.html           # The frontend Website design
\`\`\`

## 🛠️ Installation & Setup

**1. Clone the repository (or set up the folder):**
\`\`\`bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
\`\`\`

**2. Install required libraries:**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## 🚀 How to Use

### Step 1: Prepare Your Data
Organize your images inside the `dataset/train` and `dataset/val` folders. Create a new folder for each category.
* Example: `dataset/train/dogs/` and `dataset/train/cats/`

### Step 2: Train the AI Model
Run the training script to allow the AI to learn from your images.
\`\`\`bash
python train.py
\`\`\`
*(This will generate a `custom_ai_model.pth` file and a `classes.txt` file.)*

### Step 3: Run the Web App (Recommended)
Start the Flask web server to use the AI via a clean UI.
\`\`\`bash
python app.py
\`\`\`
* Open your browser and go to: **http://127.0.0.1:5000/**
* Upload an image and see the prediction!

### Step 4: Test via Terminal (Alternative)
If you prefer the command line, you can test a new image like this:
\`\`\`bash
python predict.py path/to/your/test_image.jpg
\`\`\`

## ⚙️ Built With
* [Python](https://www.python.org/)
* [PyTorch](https://pytorch.org/) - Deep Learning Framework
* [Flask](https://flask.palletsprojects.com/) - Web Framework
* [HTML/CSS] - For the Frontend UI

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
