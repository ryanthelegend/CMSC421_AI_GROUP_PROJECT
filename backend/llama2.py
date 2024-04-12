import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM
import fitz
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from flask import Flask, request, jsonify


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



token = "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" # REPLACE WITH HUGGINGFACE TOKEN FOR AUTH OR LOCAL AUTH USING huggingface-cli login command
# Loading the model


try:
    # Loading the model
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf", token=token, device_map='auto')

    # Loading the tokenizer
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf", token=token)

except Exception as e:
    print(f"An error occurred: {e}")

def llama2_response(prompt, max_tokens=20):
    inputs = tokenizer(prompt, return_tensors='pt').to(device)
    output = model.generate(**inputs, max_new_tokens=max_tokens)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response



def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page in document:
        text += page.get_text()
    return text



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


app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = "Summarize the following text:\n"

    if 'url' in data:
      prompt += extract_text_from_url(data['url'])
    elif 'pdf_path' in data:
      prompt += extract_text_from_pdf(data['pdf_path'])
    else:
      prompt += data['prompt']

    max_tokens = len(prompt)

    response = llama2_response(prompt, max_tokens=max_tokens)

    return jsonify({'response': response})
