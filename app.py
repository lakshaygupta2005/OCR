from flask import Flask, request, jsonify
from ocr_api import process_image

app = Flask(__name__)

@app.route('/')
def home():
    return 'OCR API is running!'

@app.route('/ocr', methods=['POST'])
def ocr():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Call the process_image function and pass the file
    result = process_image(file)
    
    # Return the OCR result as JSON
    return jsonify({'text': result})

if __name__ == '__main__':
    app.run(debug=True)s