import numpy as np
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM, QuantoConfig
import os
import time

gpu = True if torch.cuda.is_available() else False
device = torch.device("cuda" if (gpu == True) else "cpu")
token = os.getenv('TOKEN')  # Huggingface token


def min_max_scaling(data):
    if data:
        min_val = min(data)
        max_val = max(data)
        normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
        return normalized_data
    else:
        return []


def main():
    prompt = "Summarize the following text:\n In electrical engineering, a transformer is a passive component that transfers electrical energy from one electrical circuit to another circuit, or multiple circuits. A varying current in any coil of the transformer produces a varying magnetic flux in the transformer's core, which induces a varying electromotive force (EMF) across any other coils wound around the same core. Electrical energy can be transferred between separate coils without a metallic (conductive) connection between the two circuits. Faraday's law of induction, discovered in 1831, describes the induced voltage effect in any coil due to a changing magnetic flux encircled by the coil."

    settings = ["int8, int4, none"]
    speed_results = {}
    response_results = {}
    all_results = {}
    for setting in settings:
        print(f"Testing quantization setting {setting}")

        try:
            if setting == "none":
                quantization_config = None
            else:
                quantization_config = QuantoConfig(weights=setting)

            model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf", token=token,
                                                         quantization_config=quantization_config)
            model.to(device)
            tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf", token=token)
            # tokenizer.to(device)

            all_results[setting] = np.array([])
            for i in range(30):
                start_time = time.time()
                inputs = tokenizer(prompt, return_tensors='pt').to(device)
                output = model.generate(**inputs, max_new_tokens=50)
                response = tokenizer.decode(output[0], skip_special_tokens=True)
                end_time = time.time()
                execution_time = (end_time - start_time)
                print(execution_time)
                np.append(all_results[setting], execution_time)

            speed_results[setting] = np.average(all_results[setting])
            response_results[setting] = response

            print(f"Average Results: {speed_results[setting]}")
            print(f"Standard Deviation: {np.std(speed_results[setting])}")
            print(f"Quantization setting {setting} took {speed_results[setting]} seconds")
            print(f"Response: {response}")
        except Exception as e:
            print(f"An error occurred for quantization setting {setting}: {e.with_traceback()}")
    print("Results:")
    print(response_results)
    print(speed_results)
    # Normalize the results
    speed_results_normalized = min_max_scaling(list(speed_results.values()))
    print(f"Normalized results: {speed_results_normalized}")


main()
