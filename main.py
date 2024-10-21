from flask import Flask, request, jsonify
from flask_cors import CORS
from summarization import driver

app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    text = data['text']
    
    summary = driver(text)
    
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)