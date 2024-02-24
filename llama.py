import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



token = "" # REPLACE WITH HUGGINGFACE TOKEN FOR AUTH OR LOCAL AUTH USING huggingface-cli login command
# Loading the model




model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", token=token, device_map='auto')


tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf", token=token)


def llama2_response(prompt, max_tokens=20):
    inputs = tokenizer(prompt, return_tensors='pt').to(device)
    output = model.generate(**inputs, max_new_tokens=max_tokens)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response


prompt = "What is gradient decent?"
llama2_response(prompt)