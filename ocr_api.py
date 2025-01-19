import pytesseract
from PIL import Image
from flask import request, jsonify
import io

def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files.get('file')

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Convert the file to a file-like object
        img = Image.open(io.BytesIO(file.read()))
        # Perform OCR on the image
        text = pytesseract.image_to_string(img)
        return jsonify({'text': text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500