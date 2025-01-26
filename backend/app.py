from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import anthropic
import os

app = Flask(__name__)
CORS(app)

load_dotenv()  

openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

clientopenai = openai.OpenAI(api_key=openai_api_key)
clientanthropic = anthropic.Anthropic()

api_key = openai_api_key

# Map models to their respective clients
client_dispatch = {
    'gpt': clientopenai,  
    'chatgpt': clientopenai,  
    'o1': clientopenai,   
    'gpt-4-turbo': clientopenai,
    'claude': clientanthropic
}

# Return correct client for the given model type
def get_client(model_type):
    for prefix, client in client_dispatch.items():
        if model_type.startswith(prefix):
            return client
    return None

@app.route('/generate', methods=['POST'])
def generate_text():
    userInput = request.json.get('userInput')
    prompt = request.json.get('prompt')
    modelType = request.json.get('modelType')
    message_content = ''

    # Checks if userInput was provided
    if not userInput:
        return jsonify({"error": "No input provided"}), 400
    # Checks if api_key was provided properly
    if not api_key:
        return jsonify({"error": "API key not configured properly"}), 500
    
    # Provides a default prompt if none is specified
    if not prompt:
        prompt = "You are a helpful assistant."
    # Sets a default model type if none is specified
    if not modelType:
        modelType = "gpt-4o"

    # Retrieves the appropriate client for the specified model type
    client = get_client(modelType)
    if not client:
        return jsonify({"error": "Invalid model type or client not configured"}), 400

    try:
        # Checks if the model type belongs to the Anthropic API and makes the appropriate API call
        if modelType.startswith('claude'):
            response = clientanthropic.messages.create(
                model=modelType,
                max_tokens=1000,
                temperature=0,
                system=prompt,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": userInput
                            }
                        ]
                    }
                ]
            )
            message_content = response.content[0].text         
        else:
            # For OpenAI models, this executes the chat completion API call
            response = clientopenai.chat.completions.create(
                model=modelType,
                messages=[
                    {"role": "system", "content": prompt},
                    {
                        "role": "user",
                        "content": userInput
                    }
                ]
            )
            message_content = response.choices[0].message.content

        # Returns the message content and model type in the response after successful API call
        return jsonify({"response": message_content, "model": modelType}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
