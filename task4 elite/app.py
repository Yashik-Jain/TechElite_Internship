from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)
generator = pipeline("text-generation", model="gpt2")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data.get('prompt', '')
    generated = generator(prompt, max_length=150, num_return_sequences=1)
    return jsonify({'generated_text': generated[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)
