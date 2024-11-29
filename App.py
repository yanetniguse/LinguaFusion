from flask import Flask, request, render_template, jsonify
from transformers import MarianMTModel, MarianTokenizer

# Flask app initialization
app = Flask(__name__)

# Path to the local trained model
model_path = "./trained_model"

# Load the pre-trained model and tokenizer
model = MarianMTModel.from_pretrained(model_path)
tokenizer = MarianTokenizer.from_pretrained(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text_to_translate = request.json.get("text")
    inputs = tokenizer(text_to_translate, return_tensors="pt", padding=True, truncation=True, max_length=512)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return jsonify({"translated_text": translated_text})

if __name__ == '__main__':
    app.run(debug=True)
