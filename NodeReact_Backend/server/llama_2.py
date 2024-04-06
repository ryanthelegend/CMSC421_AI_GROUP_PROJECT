import sys
import os 
import pip
import requests
import torch
import torch.nn as nn
import fitz

from flask_cors import CORS
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM
import subprocess



token = os.getenv('TOKEN')
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install('pymupdf')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

token = os.getenv('TOKEN')
# Loading the model

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf", token=token, device_map='auto')

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf", token=token)


def llama2_response(prompt, max_tokens=20):
    inputs = tokenizer(prompt, return_tensors='pt').to(device)
    output = model.generate(**inputs, max_new_tokens=max_tokens)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response


# test purpose
def prompt_response():
    user_input = input("Please enter your prompt: ")
    response = llama2_response(user_input)
    print("Your prompt: ", user_input)
    print()
    print("Response: ", response)


# pip install pymupdf


def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page in document:
        text += page.get_text()
    return text


# !pip install requests beautifulsoup4

# maybe need to tune when testing
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
]


def extract_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.find_all(text=True)

        output = ''
        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)

        return output
    else:
        raise HTTPError(f'Failed to retrieve content from {url}, Status code: {response.status_code}')


from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json

    if 'url' in data:
        prompt = extract_text_from_url(data['url'])
    elif 'pdf_path' in data:
        prompt = extract_text_from_pdf(data['pdf_path'])
    else:
        prompt = data['prompt']

    max_tokens = data.get('max_tokens', 20)
    max_tokens = max(10, min(max_tokens, 1000))  # some range of max_tokens

    response = llama2_response(prompt, max_tokens=max_tokens)

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(port=5002)
