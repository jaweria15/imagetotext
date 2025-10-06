from flask import Flask, render_template, jsonify
import cv2
from PIL import Image
import pytesseract
import os

app = Flask(__name__)


# optional: set path of tesseract.exe if needed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/capture')
def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        cap.release()
        return jsonify({'error': 'Camera not detected'})

    img_path = os.path.join('static', 'captured_image.jpg')
    cv2.imwrite(img_path, frame)
    cap.release()

    img = Image.open(img_path)
    text = pytesseract.image_to_string(img)
    return jsonify({'text': text})


if __name__ == '__main__':
    app.run(debug=True)
