Custom_Image_AI/
│
├── requirements.txt         # Required libraries
├── README.md                # GitHub instructions
│
├── dataset/                 # Yahan aapki images hongi
│   ├── train/               # AI ko sikhane ke liye (80% images)
│   │   ├── class_A/
│   │   └── class_B/
│   └── val/                 # AI ka test lene ke liye (20% images)
│       ├── class_A/
│       └── class_B/
│
├── model.py                 # AI ka Brain (CNN Architecture)
├── train.py                 # AI ko sikhane (train) ka code
└── predict.py               # Nayi image ko test karne ka code
