import cv2
import pytesseract
from PIL import Image

# Optional: if Tesseract is not in PATH, uncomment this
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

cap = cv2.VideoCapture(0)
print("Press 's' to scan image...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not detected!")
        break

    cv2.imshow("Camera", frame)

    # Step 2: 's' key press par image capture
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("captured_image.jpg", frame)
        print("Image captured successfully!")
        break

# Step 3: Camera band karo
cap.release()
cv2.destroyAllWindows()

# Step 4: OCR - Image se text extract karo
img = Image.open("captured_image.jpg")
text = pytesseract.image_to_string(img)

# Step 5: Output show karo
print("\n--- Extracted Text ---\n")
print(text)