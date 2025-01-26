# AI Model Interface Web App

This web application allows you to interact with the latest models from OpenAI and Anthropic by sending user inputs and system prompts, and selecting the desired AI model to get responses. This document will guide you through setting up and using the application.

## Features

- **Model Selection**: Toggle between various AI models from OpenAI and Anthropic.
- **User Interaction**: Enter a system prompt and user input to query the AI models.
- **Local Hosting**: The application is hosted locally at http://localhost:3000.

## Prerequisites

Before running the application, ensure you have the following installed:

- [Node.js](https://nodejs.org/) (which includes npm)
- Python 3.13.1

## Setup

To set up the application on your local machine, follow these steps:

1. **Clone the repository**

   - Clone this repository to your local machine using `git clone`, followed by the repository URL.

2. **Environment Variables**

   - Create a `.env` file in the backend directory of the project and add your OpenAI and Anthropic API keys:

     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ANTHROPIC_API_KEY=your_anthropic_api_key_here
     ```

3. **Set up a Python virtual environment**

   - Navigate to the backend directory of your project.
   - Create a virtual environment by running:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows, run:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS and Linux, run:
       ```bash
       source venv/bin/activate
       ```

4. **Install Dependencies**
   - While the virtual environment is activated, install the required Node.js and Python dependencies:
     ```bash
     cd backend
     npm install
     pip install -r requirements.txt
     ```

## Running the Application

To start the application, run the provided commands:

1. Start the backend server:

   ```bash
   python3 backend/app.py
   ```

2. Navigate to the frontend directory and start the frontend server:
   ```bash
   cd frontend
   npm start
   ```

This script starts both the backend server and the frontend development server. Once the servers are up and running, you can access the application by navigating to http://localhost:3000 in your web browser.

## Using the Application

- **Select a Model**: Use the dropdown menu to select one of the supported AI models.
- **Enter System Prompt**: Input a system prompt that guides the AI's response.
- **Enter User Input**: Type your query or statement for the AI to respond to.
- **Submit**: Click the submit button or press Enter to send your request to the AI model.
- **View Response**: The AI's response will be displayed below the input fields.

### Additional Notes

- **Deactivating the Virtual Environment**: To stop using the virtual environment and return to your global Python environment, you can deactivate it by simply running:
  ```bash
  deactivate
  ```
