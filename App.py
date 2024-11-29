from flask import Flask, render_template, request, jsonify
import tensorflow as tf  # if using TensorFlow
# or import torch (for PyTorch)

# Load the model (assuming TensorFlow for this example)
model = tf.keras.models.load_model('translation_model.h5')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text_to_translate = request.form['text']  # Get the text from the form
    
    # Translate the text using your model
    translated_text = model.translate(text_to_translate)  # Adjust based on your model's API

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
