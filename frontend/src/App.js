import React, { useState } from "react";
import "./App.css";
import ReactMarkdown from "react-markdown";

function App() {
  const [userInput, setUserInput] = useState("");
  const [modelType, setModelType] = useState("");
  const [prompt, setPrompt] = useState("");
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  // Handles the form submission, triggers the API call, and processes the response.
  const handleSubmit = async (event) => {
    event.preventDefault(); // Prevents the default form submission behavior.
    setIsLoading(true); // Indicates the start of an API request.
    const newMessage = {
      user: userInput,
      id: messages.length,
    };

    try {
      // Asynchronous API request to the server with user's input and model specifications.
      const result = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ modelType, prompt, userInput }),
      });

      // Processes the JSON response from the API.
      const data = await result.json();
      if (result.ok) {
        newMessage.response = data.response; // Successful API response.
        newMessage.model = data.model; // Model type used for the response.
      } else {
        // Handling server-side errors by logging and displaying an error message.
        newMessage.response = "Failed to fetch response from server";
        console.error("Server response:", data);
      }
    } catch (error) {
      // Handling client-side errors by logging and setting an error message.
      console.error("Error:", error);
      newMessage.response = "Error sending data to the server";
    }
    // Updating the messages array to include the new message and resetting user input.
    setMessages([...messages, newMessage]);
    setUserInput("");
    setIsLoading(false); // Indicates the end of the API request.
  };

  return (
    <div className="App">
      {isLoading && <div className="loading">Loading...</div>}
      <div className="header">
        <label class="model-prompt">
          Model Type:
          <select
            value={modelType}
            onChange={(e) => setModelType(e.target.value)} // Updates the model type based on user selection.
          >
            <option value="gpt-4o">GPT-4o</option>
            <option value="chatgpt-4o-latest">ChatGPT-4o Latest</option>
            <option value="gpt-4o-mini">GPT-4o Mini</option>
            <option value="gpt-4-turbo">GPT-4 Turbo</option>
            <option value="claude-3-5-sonnet-20241022">
              Claude 3.5 Sonnet
            </option>
            <option value="claude-3-5-haiku-20241022">Claude 3.5 Haiku</option>
            <option value="claude-3-opus-20240229">Claude 3 Opus</option>
            <option value="claude-3-sonnet-20240229">Claude 3 Sonnet</option>
            <option value="claude-3-haiku-20240307">Claude 3 Haiku</option>
          </select>
        </label>
        <label className="label-prompt">
          Prompt:
          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)} // Updates the prompt based on user input.
          />
        </label>
      </div>
      <div className="messages">
        {messages.map((msg) => (
          <div key={msg.id} className="message">
            <div className="user-message">
              <b>You: {msg.user}</b>
            </div>
            <div className="response-message">
              {msg.model}: <ReactMarkdown>{msg.response}</ReactMarkdown>
            </div>
          </div>
        ))}
      </div>
      <div className="chat-interface">
        <textarea
          placeholder="Type your message..."
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)} // Updates the user input from the text area.
        />
        <button onClick={handleSubmit}>Submit</button>
      </div>
    </div>
  );
}

export default App;
