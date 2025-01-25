from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os

load_dotenv() 

app = Flask(__name__)

@app.route('/api/interact', methods=['POST'])
def interact_with_model():
    data = request.json
    model_type = data['model_type']
    prompt = data['prompt']
    user_input = data['user_input']

    if model_type == 'openai':
        api_key = os.getenv('OPENAI_API_KEY')
        url = 'https://api.openai.com/v1/engines/davinci/completions'
    elif model_type == 'anthropic':
        api_key = os.getenv('ANTHROPIC_API_KEY')
        url = 'https://api.anthropic.com/v1/engines/claudia/completions'
    else:
        return jsonify({'error': 'Invalid model type'}), 400

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    response = requests.post(url, json={'prompt': f'{prompt} {user_input}'}, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
