from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    input_text = data.get('inputText', '')
    translated_text = translate_text(input_text)
    return jsonify({"translatedText": translated_text})
