# Getting Started Guide

Welcome to our project! This guide will walk you through setting up the project on your local machine, from pulling the repository to running the client side. Let's dive in. Our code is designed to work primarily in linux and unix environments.

## Setting Up the Backend

1. **Pull the Repository**
   - Pull the repository from the GitHub repo onto your local machine.

2. **Open Terminal/Bash**
   - Navigate to the directory where the repository was stored.

3. **Navigate to Backend Directory**
   - Change into the backend directory.

4. **Create a Virtual Environment**
   - Use the following commands to set up a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

5. **Create a Hugging Face Account**
   - Request access for the default model: `meta-llama/Llama-2-7b-chat-hf`.

6. **API Key (Optional)**
   - If you prefer using an API key, create an OpenAI account and subscribe to one of the plans to receive an API key. Store this key in your environment.

7. **Generate a HuggingFace Token**
   - Store the token in your local variable using the command:
     ```bash
     export TOKEN="your huggingface token"
     ```

8. **Install Requirements**
   - In the backend directory, install the requirements. If you have access to a GPU install both the GPU and CPU requirements:
     ```bash
     pip install -r GPUrequirements.txt
     ```
   - Otherwise, install only the CPU requirements:
     ```bash
     pip install -r CPUrequirements.txt
     ```

9. **Run the Flask Server**
   - Start the server with the command:
     ```bash
     python llama2.py
     ```

10. **Testing**
    - Test your model using curl or Postman.

## Running the Client Side

1. **Open a New Terminal**
   - Navigate to the client directory.

2. **Check Node.js Installation**
   - Verify if Node.js is installed, or visit https://nodejs.org/en to install the LTS version 17.0.0.

3. **Install npm**
   - Run `npm install`. If you encounter errors, try reinstalling node with:
     ```bash
     npm install --legacy-peer-deps
     ```

4. **Start the Frontend**
   - Launch the frontend using:
     ```bash
     npm start
     ```

## Using the Application

- Experiment with different prompts in the chatbox and click submit to see the responses.

## Common FAQs

**Q: I am getting a proxy error. What should I do?**
A: This may be due to an older version of Node. Upgrade Node using:
```bash
brew install node
npm start --reset --cache
```

Q: The responses take too long. 
A: It is completely normal, especially if you do not have access to a GPU. We have quantized the models to have a right balance between speed and accuracy. 

Q: I am getting a react dom error. 
A: This is also due to not having the latest version of dom
```bash
npm install react@latest react-dom@latest
```







