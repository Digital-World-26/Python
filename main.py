import cv2
import pytesseract
import pandas as pd

# ⚠️ Agar Windows use kar rahe ho to path set karo
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Image load karo
image_path = "table.png"   # yaha apni image ka naam daalo
img = cv2.imread(image_path)

# Grayscale conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thoda cleaning (optional)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# OCR run karo
text = pytesseract.image_to_string(thresh)

print("Extracted Text:\n", text)

# 🔹 Text ko rows me todna
lines = text.split("\n")
data = []

for line in lines:
    if line.strip() != "":
        row = line.split()   # space ke basis par split
        data.append(row)

# 🔹 DataFrame banana
df = pd.DataFrame(data)

# Excel me save karna
df.to_excel("output.xlsx", index=False)

print("✅ Excel file ban gayi: output.xlsx")
