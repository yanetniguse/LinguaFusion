from flask import Flask, request, jsonify, send_from_directory
import tensorflow as tf  # if using TensorFlow
# or import torch (for PyTorch)

# Load the model (assuming TensorFlow for this example)
model = tf.keras.models.load_model('translation_model.h5')

app = Flask(__name__, static_folder='static')  # Specify static folder for assets if needed

@app.route('/')
def home():
    # Serve the index.html from the root directory
    return send_from_directory('.', 'index.html')  # '.' refers to the root directory

@app.route('/translate', methods=['POST'])
def translate():
    text_to_translate = request.json.get('text')  # Using JSON instead of form-data for better API design
    
    # Translate the text using your model
    # Assuming your model has a `predict` method or similar for translation
    translated_text = model.translate(text_to_translate)  # Adjust based on your model's API

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
